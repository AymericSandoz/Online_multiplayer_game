import socket
from _thread import *
from player import Player
import pickle
from entities import players_start

server = "192.168.1.75"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(10)
print("Waiting for a connection, Server Started")


players = [Player(player_data["x"], player_data["y"],player_data["width"], player_data["height"], player_data["color"], player_data["role"]) for player_data in players_start]


def threaded_client(conn, player):
    conn.send(pickle.dumps(players[player]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                reply = players[:player] + players[player+1:]


            conn.sendall(pickle.dumps(reply))  # replay jusqua présent mais marche aussi avec players
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
    print(currentPlayer)