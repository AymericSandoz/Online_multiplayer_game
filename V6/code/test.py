class Character:
    def __init__(self):
        # Utilisation d'un dictionnaire pour simuler character.rect
        self.rect = {'x': 100, 'y': 100}


# Initialisation des paramètres
screen_width = 1280
screen_height = 720
map_width = 2048
map_height = 736

# Position initiale du joueur
x = 100
y = 100

# Initialisation de la caméra
camera_x = x - (screen_width / 2)
camera_y = y - (screen_height / 2)

# Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
camera_x = max(0, min(camera_x, map_width - screen_width))
camera_y = max(0, min(camera_y, map_height - screen_height))

# Création d'un personnage
character = Character()

# Simulation d'une évolution de x et y
for step in range(50):
    x += 16  # Augmentez x pour simuler le mouvement du joueur
    y += 0  # Augmentez y pour simuler le mouvement du joueur

    # Mise à jour de la caméra
    camera_x = x - (screen_width / 2)
    camera_y = y - (screen_height / 2)

    # Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
    camera_x = max(0, min(camera_x, map_width - screen_width))
    camera_y = max(0, min(camera_y, map_height - screen_height))

    # Mise à jour des positions du personnage en fonction de la caméra
    # Utilisation de valeurs de zoom arbitraires
    character.rect['x'] = (x - camera_x - 20 / 2) * 2
    # Utilisation de valeurs de zoom arbitraires
    character.rect['y'] = (y - camera_y - 20 / 2) * 2

    # Affichage des résultats
    print(
        f"Step {x}: Character - X: {character.rect['x']}, Y: {character.rect['y']}")
