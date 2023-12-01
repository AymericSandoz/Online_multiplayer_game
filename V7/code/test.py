from PIL import Image
import os

def decouper_image():
    # Obtenez le chemin complet vers le fichier image dans le dossier de téléchargement
    chemin_image = os.path.join(os.path.expanduser("~"), "Downloads", "animals_sprites.png")

    # Vérifier si le fichier existe
    if not os.path.exists(chemin_image):
        print(f"Erreur : Le fichier {chemin_image} n'a pas été trouvé.")
        return

    # Charger l'image avec Pillow
    image = Image.open(chemin_image)

    # Convertir l'image en mode RGB (en supprimant le canal alpha)
    image = image.convert("RGB")

    # Obtenir les dimensions originales de l'image
    largeur, hauteur = image.size

    # Calculer les nouvelles dimensions pour découper l'image
    nouvelle_largeur = largeur // 4  # 1/3 de la largeur
    nouvelle_hauteur = hauteur // 2  # 1/2 de la hauteur

    # Découper l'image
    nouvelle_image = image.crop((0, 0, nouvelle_largeur, nouvelle_hauteur))

    # Enregistrer l'image découpée en tant que fichier JPEG
    nouvelle_image.save("image_decoupee.jpg")

    # Afficher l'image découpée
    nouvelle_image.show()

# Exemple d'utilisation
decouper_image()
