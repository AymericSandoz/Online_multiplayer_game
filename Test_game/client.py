import pygame
from network import Network
from player import Player

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")


def redrawWindow(win,player, other_players):
    win.fill((255,255,255))
    for other_player in other_players:
        other_player.draw(win)
    player.draw(win)
    pygame.display.update()


def main():
    run = True
    n = Network()
    p = n.getP()

    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        other_players = n.send(p)  # Envoyez une requête pour obtenir la liste des joueurs du serveur

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

        # # eliminiation si collision avec un joueur (n'importe lequel)
        # for player in other_players:
        #     if not player.eliminated:
        #         if p.collide(player):
        #             p.eliminate()

        # si je suis un chat
        for player in other_players:
            if p.role == "chat" and not player.eliminated and player.role == "souris":
                if p.collide(player):
                    player.eliminate()


        # si je suis une souris
        for player in other_players:
            if p.role == "souris" and player.role == "chat":
                if p.collide(player):
                    p.eliminate()

        for player in other_players:
            player.move()

        p.move()
        redrawWindow(win, p, other_players)


main()