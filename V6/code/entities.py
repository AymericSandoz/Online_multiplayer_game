from player import OtherPlayers
import pygame
from tool import Tool

players_start = [
    {"x": 550, "y": 300},
    {"x": 590, "y": 300},
    {"x": 450, "y": 300},
    {"x": 400, "y": 350},
    {"x": 500, "y": 300},
    {"x": 800, "y": 350},
    {"x": 1500, "y": 350},
]

# Créez des instances de la classe Player à partir de la liste de dictionnaires
player_instances = []
for player_data in players_start:
    x = player_data["x"]
    y = player_data["y"]
    player_instance = OtherPlayers(
        x, y, direction="down", index_image=0, spritesheet_index="foot_red")
    player_instances.append(player_instance)

MAX_PLAYERS = 10

initial_X_Position = 1500

initial_Y_Position = 300
