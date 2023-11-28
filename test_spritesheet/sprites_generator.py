from PIL import Image

# Nom de l'image
nom_image = "./test_spritesheet/ghost_spritesheet.jpg"

# Charger l'image depuis le même répertoire que le script
original_image = Image.open(nom_image)

# Taille des images de sortie
nouvelle_largeur = 100
nouvelle_hauteur = 128

# Nombre de lignes et de colonnes pour la découpe
colonnes = 4  # 8 images de largeur
lignes = 2     # 4 images de hauteur

# Découper l'image
for i in range(lignes):
    for j in range(colonnes):
        # Coordonnées du coin supérieur gauche de la région à découper
        gauche = j * nouvelle_largeur
        haut = i * nouvelle_hauteur

        # Coordonnées du coin inférieur droit de la région à découper
        droite = gauche + nouvelle_largeur
        bas = haut + nouvelle_hauteur

        # Découper l'image
        region = original_image.crop((gauche, haut, droite, bas))

        # Sauvegarder la région découpée
        nom_fichier = f"image_decoupee_{i}_{j}.png"
        region.save(nom_fichier)

# Fermer l'image originale
original_image.close()
