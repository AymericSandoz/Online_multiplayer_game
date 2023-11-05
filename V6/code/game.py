import pygame
from keylistener import KeyListener
from map import Map
from screen import Screen
from player import Player, OtherPlayers
from screen import Screen
from network import Network
from entities import player_instances, initial_X_Position, initial_Y_Position


class Game:
    def __init__(self):
        self.running: bool = True
        self.screen: Screen = Screen()
        self.map: Map = Map(self.screen)
        self.keylistener: KeyListener = KeyListener()
        self.player: Player = Player(
            self.keylistener, self.screen, initial_X_Position, initial_Y_Position)
        self.players = []
        self.map.add_player(self.player)
        # self.map.add_squares(player_instances)
        self.map.add_characters(player_instances)

    def run(self):
        n = Network()
        p = n.getP()

        clock = pygame.time.Clock()

        while self.running:
            # self.map.test_print()
            clock.tick(60)
            # Envoyez une requête pour obtenir la liste des joueurs du serveur
            other_players = n.send(OtherPlayers(
                self.player.position.x, self.player.position.y, self.player.direction, self.player.index_image, self.player.spritesheet_index))

            self.handle_input()
            # self.map.move_squares(other_players)
            self.map.move_characters(other_players)
            self.map.update()
            self.screen.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.KEYDOWN:
                self.keylistener.add_key(event.key)
            elif event.type == pygame.KEYUP:
                self.keylistener.remove_key(event.key)
