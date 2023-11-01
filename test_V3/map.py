import pyscroll
import pytmx
from player import Player
from screen import Screen
import pygame
from pygame.locals import Color
from square import Square


class Map:
    def __init__(self, screen: Screen):
        self.screen: Screen = screen
        self.tmx_data: pytmx.TiledMap | None = None
        self.map_layer: pyscroll.BufferedRenderer | None = None
        self.group: pyscroll.PyscrollGroup | None = None
        self.squares = pygame.sprite.Group()

        self.switch_map("map_0")
        self.player: Player | None = None

    def switch_map(self, map: str) -> None:
        self.tmx_data = pytmx.load_pygame(f"./assets/map/{map}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(map_data, self.screen.get_size())
        self.map_layer.zoom = 3
        self.group = pyscroll.PyscrollGroup(map_layer=self.map_layer, default_layer=7)


    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()

    def add_players(self, other_players)-> None:
        self.players = other_players

    def add_squares(self, other_players, width=20, height=20, color="red"):
        for player in other_players:
            print("player", player)
            square = Square(player.x, player.y, width, height, color)
            self.squares.add(square)


    def move_squares(self, other_players):
        for square, player in zip(self.squares, other_players):
            square.rect.x = player.x
            square.rect.y = player.y
  # Efface tous les carrés

    # def update_other_players(self, other_players):

    #     for player in other_players:
    #         x = player.x  # Remplacez par l'attribut correct contenant la position X
    #         y = player.y  # Remplacez par l'attribut correct contenant la position Y
    #         square = pygame.Rect(x, y, 32, 32)  # Crée un carré de 32x32 pixels à la position (x, y)
    #         pygame.draw.rect(self.screen.get_display(), pygame.Color(255, 0, 0), square)

    def update(self) -> None:
        self.group.update()
        self.squares.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
        self.squares.draw(self.screen.get_display())

