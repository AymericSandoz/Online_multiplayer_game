import pyscroll
import pytmx
from player import Player
from screen import Screen
import pygame
from pygame.locals import Color
from square import Square
from entities import initial_X_Position, initial_Y_Position


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
        self.map_layer = pyscroll.BufferedRenderer(
            map_data, self.screen.get_size())
        self.map_layer.zoom = 1
        self.group = pyscroll.PyscrollGroup(
            map_layer=self.map_layer, default_layer=7)

    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()

    def add_players(self, other_players) -> None:
        self.players = other_players


    def add_squares(self, other_players, width=20, height=20, color="red"):
        screen_width, screen_heigth = self.screen.get_size()
        screen_width = screen_width / self.map_layer.zoom
        screen_heigth = screen_heigth / self.map_layer.zoom
        screen_topleft_coordinates_x, screen_topleft_coordinates_y = self.group.view.topleft
        map_width, map_heigth = self.map_layer.map_rect.size
        center_x, center_y = self.group.view.center
        # # Calculez camera_x et appliquez les limites
        # camera_x = initial_X_Position - (self.player.rect.x - screen_width / 2)
        # camera_x = max(0, min(camera_x, 2048))

        # # Calculez camera_y et appliquez les limites
        # camera_y = initial_Y_Position - \
        #     (self.player.rect.y - screen_heigth / 2)
        # camera_y = max(0, min(camera_y, 736))

        camera_x = self.player.rect.x - (screen_width / 2)
        camera_y = self.player.rect.y - (screen_heigth / 2)

        # Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
        camera_x = max(0, min(camera_x, map_width - screen_width))
        camera_y = max(0, min(camera_y, map_heigth - screen_heigth))

        for player in other_players:
            screen_x = (player.x - camera_x) * self.map_layer.zoom
            screen_y = (player.y - camera_y) * self.map_layer.zoom
            square = Square(screen_x, screen_y, width, height, color)
            self.squares.add(square)

    def test_print(self):
        print("self.tmx_data.width,self.tmx_data.height",
              self.tmx_data.width, self.tmx_data.height)
        print(self.screen.get_size())  # 426 240
        print(self.group.view.topright)  # (1622, 496)
        visible_rect = self.map_layer.map_rect
        visible_width, visible_height = visible_rect.size
        print(visible_width, visible_height)

        # 240

    def move_squares(self, other_players):
        for square, player in zip(self.squares, other_players):
            square.rect.x = player.x
            square.rect.y = player.y

    def update(self) -> None:
        self.group.update()
        self.squares.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
        self.squares.draw(self.screen.get_display())
