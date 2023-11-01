from player import OtherPlayers

players_start = [
    {"x": 100, "y": 100},
    {"x": 200, "y": 200},
    {"x": 300, "y": 300},
    {"x": 400, "y": 400},
    {"x": 500, "y": 500},
    {"x": 600, "y": 600},
    # {"x": 700, "y": 700},
    # {"x": 800, "y": 800},
    # {"x": 900, "y": 900},
    # {"x": 1000, "y": 1000}
]

# Créez des instances de la classe Player à partir de la liste de dictionnaires
player_instances = []
for player_data in players_start:
    x = player_data["x"]
    y = player_data["y"]
    player_instance = OtherPlayers(x, y)
    player_instances.append(player_instance)

for player in player_instances:
    print(player.x, player.y)

MAX_PLAYERS = 10

