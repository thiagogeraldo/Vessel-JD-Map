from flask import Flask, render_template, render_template_string, request, redirect, url_for, session
from flask_socketio import SocketIO, emit
from geopy.distance import geodesic
from time import sleep, time
from calc_route import add_route
from trilateration import trilateration

app = Flask(__name__)
app.secret_key = 'senha_secreta'
socketio = SocketIO(app)

requesters = []
requester = None
data_list = []
last_update_time = time()
location = ()
weight = []
path = []

@app.route('/')
def home():
    if 'logged_in' in session and session['logged_in']:
        user_id = session.get('user_id')
        if user_id == 'Vitor':
            return redirect(url_for('transportation', user_id=user_id))
        else:
            return redirect(url_for('requests', user_id=user_id))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form['username']
        password = request.form['password']
        if user_id == 'Thiago' and password == 'password':
            session['logged_in'] = True
            session['user_id'] = user_id
            return redirect(url_for('requests', user_id=user_id))
        elif user_id == 'Vitor' and password == 'password':
            session['logged_in'] = True
            session['user_id'] = user_id
            return redirect(url_for('transportation', user_id=user_id))
        return 'Credenciais inválidas!', 401
    return render_template('login.html', title='Login')

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/update', methods=['POST'])
def update():
    global data_list, last_update_time, location, destination, weight

    try:
        data_list = request.form['data']
        last_update_time = time()
        
        destination = tuple(map(float, data_list.split(',')[:2]))
        weight = list(map(int, data_list[2:6]))
        location = trilateration(data_list[6:])
        path = add_route(location, destination)

        socketio.emit('update_status', {'lista_dados_length': len(data_list)})
        socketio.emit('update_location', {'location': location, 'path': path, 'weight': weight})
        
        if location:
            return "Dados recebidos com sucesso"
        else:
            return "Dados insuficientes para calcular a localização"
    except Exception as e:
        return f"Erro ao processar dados: {str(e)}"

@app.route('/requests/<user_id>', methods=['GET', 'POST'])
def requests(user_id):
    requester = next((c for c in requesters if c['id'] == user_id), None)
    
    if request.method == 'POST' and not requester:
        obs = request.form['obs']
        pedido = request.form['pedido']
        requester = {'id': user_id, 'obs': obs, 'pedido': pedido}
        requesters.append(requester)
        socketio.emit('update_carrier', {'requesters': requesters})
        return redirect(url_for('requests', user_id=user_id))
    
    return render_template('requests.html', user_id=user_id, requester=requester)

@app.route('/transportation/<user_id>', methods=['GET', 'POST'])
@app.route('/transportation/<user_id>/<requester_id>', methods=['GET', 'POST'])
def transportation(user_id, requester_id=None):
    global requesters, requester
    
    if request.method == 'POST':
        requester_id = request.form['requester_id']
        requesters = [r for r in requesters if r['id'] != requester_id]
        socketio.emit('update_carrier', {'requesters': requesters})
        socketio.emit('pedido_deletado', {'requester_id': requester_id})
        return redirect(url_for('transportation', user_id=user_id))
    
    requester = None
    if requester_id:
        requester = next((r for r in requesters if r['id'] == requester_id), None)
    
    return render_template('transportation.html', user_id=user_id, requesters=requesters, requester=requester)


@socketio.on('connect')
def handle_connect():
    emit('update_carrier', {'requesters': requesters})
    emit('update_status', {'lista_dados_length': len(data_list)})

def check_esp32_connection():
    global last_update_time
    while True:
        sleep(5)
        if time() - last_update_time > 10:
            socketio.emit('update_status', {'lista_dados_length': 0})

if __name__ == '__main__':
    socketio.start_background_task(check_esp32_connection)
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)