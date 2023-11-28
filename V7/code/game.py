import pygame
from keylistener import KeyListener
from map import Map
from screen import Screen
from player import Player, OtherPlayers
from screen import Screen
from network import Network


class Game:
    def __init__(self):
        self.running: bool = True
        self.screen: Screen = Screen()
        self.map: Map = Map(self.screen)
        self.keylistener: KeyListener = KeyListener()
        self.player: Player = None

    def run(self, player_instances):
        n = Network()
        p = n.getP()
        self.player = Player(
            self.keylistener, self.screen, p.x, p.y, p.role, p.name)
        self.map.add_player(self.player)

        # intéressant si je laisse juste players instances il y a u bonhomme en haut à gauche
        filtered_instances = [
            player for player in player_instances if player.name != self.player.name]
        self.map.add_characters(filtered_instances)
        # self.map.add_characters(player_instances[0:(len(player_instances)-1)])
        clock = pygame.time.Clock()

        while self.running:
            clock.tick(60)
            # Envoyez une requête pour obtenir la liste des joueurs du serveur
            other_players = n.send(OtherPlayers(
                self.player.position.x, self.player.position.y, self.player.direction, self.player.index_image, self.player.spritesheet_index, self.map.current_map.name, self.player.role, self.player.name))
            self.handle_input()
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
