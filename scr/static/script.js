var user_id = "{{ user_id }}";

let map = L.map('map', {
    center: [25.1, 32.5],
    zoom: 3.27,
    minZoom: 3.27,
    maxZoom: 3.27,
    zoomControl: false,
    dragging: false,
    scrollWheelZoom: false,
    doubleClickZoom: false,
    boxZoom: false,
    keyboard: false,
    tap: false,
    touchZoom: false,
    attributionControl: false
});

L.tileLayer('').addTo(map);
L.imageOverlay(local_map, [[0, 0], [46, 65]]).addTo(map);

let polyline = L.polyline([], {color: 'yellow'}).addTo(map);
let stMarker = null;
let endMarker = null;

function getDirectionIcon(prev, next) {
    const directions = [
        { condition: next[0] > prev[0], icon: location_arrow1}, // Norte
        { condition: next[1] > prev[1], icon: location_arrow2}, // Leste
        { condition: next[0] < prev[0], icon: location_arrow3}, // Sul
        { condition: next[1] < prev[1], icon: location_arrow4}  // Oeste
    ];
    return directions.find(dir => dir.condition).icon;
}

const socket = io.connect();
socket.on('update_status', function(data) {
    var statusMessage = document.getElementById('status-message');
    if (data.lista_dados_length > 0) {
        statusMessage.style.color = 'green';
        statusMessage.textContent = 'ESP32 conectado';
    } else {
        statusMessage.style.color = 'red';
        statusMessage.textContent = '⚠ Conecte o ESP32';
    }
});

socket.on('update_location', function(data) {
    const { location, path = [], weight } = data;
    const destination = path.length ? path[path.length - 1] : null;

    images.forEach((imgId, index) => {
        const imgElement = document.getElementById(imgId);
        if (imgElement && weight[index] !== undefined) {
            imgElement.src = `{{ url_for('static', filename='img/' + imageSources[weight[index].toString()]) }}`;
        }
    });

    if (path.length) {
        if (stMarker) {
            if (path.length > 1) {
                stMarker.setIcon(L.icon({iconUrl: getDirectionIcon(path[0], path[1]), iconSize: [25, 25], iconAnchor: [12, 12], popupAnchor: [1, -25], shadowSize: [25, 25]}));
            }
            stMarker.setLatLng(location).openPopup();
        } else {
            stMarker = L.marker(location, {icon: L.icon({iconUrl: location_arrow1, iconSize: [25, 25], iconAnchor: [12, 12], popupAnchor: [1, -25], shadowSize: [25, 25]})}).addTo(map);
        }
        if (endMarker) {
            endMarker.setLatLng(destination).openPopup();
        } else {
            endMarker = L.marker(destination).addTo(map);
        }
        polyline.setLatLngs(path);
    } else {
        if (stMarker) {
            stMarker.setIcon(L.icon({iconUrl: tugger, iconSize: [40, 40], iconAnchor: [12, 12], popupAnchor: [1, -25], shadowSize: [25, 25]}));
            stMarker.setLatLng(location).openPopup();
        } else {
            stMarker = L.marker(location, {icon: L.icon({iconUrl: tugger, iconSize: [40, 40], iconAnchor: [12, 12], popupAnchor: [1, -25], shadowSize: [25, 25]})}).addTo(map);
        }
        if (endMarker) {
            map.removeLayer(endMarker);
            endMarker = null;
        }
        if (polyline) {
            map.removeLayer(polyline);
            polyline = L.polyline([], {color: 'yellow'}).addTo(map);
        }
    }
});

socket.on('update_carrier', function(data) {
    var lista = document.getElementById('requesters');
    lista.innerHTML = '';
    if (data.requesters.length > 0) {
        data.requesters.forEach(function(requester) {
            var item = document.createElement('li');
            item.innerHTML = `<a href="/transportation/${user_id}/${requester.id}">${requester.id}</a>`;
            lista.appendChild(item);
        });
    } else {
        var mensagem = document.createElement('p');
        mensagem.style.color = 'gray';
        mensagem.textContent = 'Não há pedidos no momento.';
        lista.appendChild(mensagem);
    }
});
