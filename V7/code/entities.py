from player import OtherPlayers
import pygame
from tool import Tool

players_start = [
    {"x": 380, "y": 640},
    {"x": 400, "y": 500},
    {"x": 450, "y": 300},
    {"x": 400, "y": 350},
    {"x": 500, "y": 300},
    {"x": 800, "y": 350},
    # {"x": 1500, "y": 350},
]

# Créez des instances de la classe Player à partir de la liste de dictionnaires
player_instances = []
for player_data in players_start:
    x = player_data["x"]
    y = player_data["y"]
    player_instance = OtherPlayers(
        x, y, direction="down", index_image=0, spritesheet_index="foot_red")
    player_instances.append(player_instance)

MAX_PLAYERS = len(player_instances)
