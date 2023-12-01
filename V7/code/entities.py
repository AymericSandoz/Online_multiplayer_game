from player import OtherPlayers
import pygame
from tool import Tool

players_start = [
    {"x": 50, "y": 50, "role": "cat", "name": "louis"},
    {"x": 50, "y": 50, "role": "mouse", "name": "luc"},
    {"x": 50, "y": 50, "role": "mouse", "name": "jerome"},
    {"x": 50, "y": 50, "role": "mouse", "name": "shlops"},
    {"x": 50, "y": 50, "role": "mouse", "name": "basile"},
    {"x": 50, "y": 50, "role": "mouse", "name": "sacha"},
    # {"x": 1500, "y": 350},
]

# Créez des instances de la classe Player à partir de la liste de dictionnaires
player_instances = []
for player_data in players_start:
    x = player_data["x"]
    y = player_data["y"]
    role = player_data["role"]
    name = player_data["name"]
    player_instance = OtherPlayers(
        x, y, direction="down", index_image=0, spritesheet_index="foot_red", current_map_name="paradis", role=role, name=name)
    player_instances.append(player_instance)

MAX_PLAYERS = len(player_instances)
