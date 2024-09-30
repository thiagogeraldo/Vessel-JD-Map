def calculate_distance(rssi):
    tx_power = -59  # Potência de transmissão em dBm
    n = 2  # Fator de propagação
    return 10 ** ((tx_power - rssi) / (10 * n))

def trilateration(data):
    access_points = {
        # 'SSID1': (x, y),
        # 'SSID2': (x, y),
        # 'SSID3': (x, y)
    }
 
    distances = []
    for ssid, rssi in data:
        if ssid in access_points:
            print(ssid, calculate_distance(rssi))
            distances.append((access_points[ssid], calculate_distance(rssi)))
    
    if len(distances) >= 3:
        (x1, y1), d1 = distances[0]
        (x2, y2), d2 = distances[1]
        (x3, y3), d3 = distances[2]

        A = 2 * (x2 - x1)
        B = 2 * (y2 - y1)
        C = d1**2 - d2**2 - x1**2 + x2**2 - y1**2 + y2**2
        D = 2 * (x3 - x2)
        E = 2 * (y3 - y2)
        F = d2**2 - d3**2 - x2**2 + x3**2 - y2**2 + y3**2

        if (E * A - B * D) * (B * D - A * E) != 0:
            x = (C * E - F * B) / (E * A - B * D)
            y = (C * D - A * F) / (B * D - A * E)
            return (x, y)
        else:
            return 'Pontos de acesso muito próximos!'
    else:
        return None