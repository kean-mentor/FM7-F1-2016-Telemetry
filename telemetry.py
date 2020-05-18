import csv
import socket

from f12016_data import F12016TelemetryData, teams, tracks
from fm7_data import FM7TelemetryData


def get_packet(address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    data, _ = sock.recvfrom(1024)
    #data, _ = sock.recvfrom(280)
    return FM7Telemetry.from_buffer_copy(data)
    #return TelemetryData.from_buffer_copy(data)


def get_telemetry(address, port):
    last_packet = None
    while True:
        packet = get_packet(address, port)
        if last_packet == None or packet.time > last_packet.time:
            yield packet
        last_packet = packet


if __name__ == "__main__":
    prev_lap_number = 0
    prev_lap = 0
    prev_best_lap = 86400
    for data in get_telemetry("", 20777):
        if data.is_race_on and data.lap_number != prev_lap_number:
            print(f"LAP: {data.lap_number}   POS: {data.race_position}")
            print(f"BEST: {round(data.best_lap, 3)}   LAST: {round(data.last_lap, 3)}")
            delta_best = round(data.last_lap - data.best_lap, 3)
            delta_prev = round(data.last_lap - prev_lap, 3)
            
            print(f"DELTA BEST: {delta_best}   DELTA PREV: {delta_prev}")
            prev_lap_number = data.lap_number
            prev_lap = data.last_lap
            if data.best_lap < prev_best_lap:
                if prev_best_lap != 86400:
                    delta_prev_best = round(prev_best_lap - data.best_lap, 3)
                    print(f"DELTA PREV BEST: {delta_prev_best}")
                else:
                    delta_prev_best = 0
                prev_best_lap = data.best_lap
            else:
                delta_prev_best = 0
