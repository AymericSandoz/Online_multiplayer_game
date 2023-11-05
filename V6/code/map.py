import pygame
import pyscroll
import pytmx

from player import Player, OtherPlayers, OtherPlayersVisualisation
from screen import Screen
from switch import Switch

from square import Square


class Map:
    def __init__(self, screen: Screen):
        self.screen: Screen = screen
        self.tmx_data: pytmx.TiledMap | None = None
        self.map_layer: pyscroll.BufferedRenderer | None = None
        self.group: pyscroll.PyscrollGroup | None = None

        self.player: Player | None = None
        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None

        self.squares = pygame.sprite.Group()
        self.character_sprites = pygame.sprite.Group()

        self.current_map: Switch = Switch(
            "switch", "map_0", pygame.Rect(0, 0, 0, 0), 0)

        self.switch_map(self.current_map)

    def switch_map(self, switch: Switch) -> None:
        self.tmx_data = pytmx.load_pygame(
            f"./assets/map/{switch.name}.tmx")
        map_data = pyscroll.data.TiledMapData(self.tmx_data)
        self.map_layer = pyscroll.BufferedRenderer(
            map_data, self.screen.get_size())
        self.group = pyscroll.PyscrollGroup(
            map_layer=self.map_layer, default_layer=7)

        if switch.name.split("_")[0] == "map":
            self.map_layer.zoom = 1
        else:
            self.map_layer.zoom = 3.75

        self.switchs = []
        self.collisions = []

        for obj in self.tmx_data.objects:
            if obj.name == "collision":
                self.collisions.append(pygame.Rect(
                    obj.x, obj.y, obj.width, obj.height))
            type = obj.name.split(" ")[0]
            if type == "switch":
                self.switchs.append(Switch(
                    type, obj.name.split(" ")[1], pygame.Rect(
                        obj.x, obj.y, obj.width, obj.height),
                    int(obj.name.split(" ")[-1])
                ))

        if self.player:
            self.pose_player(switch)
            self.player.align_hitbox()
            self.player.step = 16
            self.player.add_switchs(self.switchs)
            self.player.add_collisions(self.collisions)
            self.group.add(self.player)
            if switch.name.split("_")[0] != "map":
                self.player.switch_bike(True)

        self.current_map = switch

    def add_player(self, player) -> None:
        self.group.add(player)
        self.player = player
        self.player.align_hitbox()
        self.player.add_switchs(self.switchs)
        self.player.add_collisions(self.collisions)

    def add_players(self, other_players) -> None:
        self.players = other_players

    def add_squares(self, other_players, width=20, height=20, color="red"):
        screen_width, screen_heigth = self.screen.get_size()
        screen_width = screen_width / self.map_layer.zoom
        screen_heigth = screen_heigth / self.map_layer.zoom
        # screen_topleft_coordinates_x, screen_topleft_coordinates_y = self.group.view.topleft
        map_width, map_heigth = self.map_layer.map_rect.size
        # center_x, center_y = self.group.view.center
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

    def move_squares(self, other_players):
        screen_width, screen_heigth = self.screen.get_size()
        screen_width = screen_width / self.map_layer.zoom
        screen_heigth = screen_heigth / self.map_layer.zoom
        # screen_topleft_coordinates_x, screen_topleft_coordinates_y = self.group.view.topleft
        map_width, map_heigth = self.map_layer.map_rect.size
        # center_x, center_y = self.group.view.center
        camera_x = self.player.rect.x - (screen_width / 2)
        camera_y = self.player.rect.y - (screen_heigth / 2)

        # Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
        camera_x = max(0, min(camera_x, map_width - screen_width))
        camera_y = max(0, min(camera_y, map_heigth - screen_heigth))
        for square, player in zip(self.squares, other_players):
            square.rect.x = (player.x - camera_x) * self.map_layer.zoom
            square.rect.y = (player.y - camera_y) * self.map_layer.zoom

    def add_characters(self, character_data):
        screen_width, screen_heigth = self.screen.get_size()
        screen_width = screen_width / self.map_layer.zoom
        screen_heigth = screen_heigth / self.map_layer.zoom
        map_width, map_heigth = self.map_layer.map_rect.size
        camera_x = self.player.rect.x - (screen_width / 2)
        camera_y = self.player.rect.y - (screen_heigth / 2)

        # Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
        camera_x = max(0, min(camera_x, map_width - screen_width))
        camera_y = max(0, min(camera_y, map_heigth - screen_heigth))
        for data in character_data:
            screen_x = (data.x - camera_x) * self.map_layer.zoom
            screen_y = (data.y - camera_y) * self.map_layer.zoom
            character = OtherPlayersVisualisation(
                screen_x, screen_y,  data.direction, data.index_image, data.spritesheet_index)
            self.character_sprites.add(character)

    def move_characters(self, character_data):
        screen_width, screen_heigth = self.screen.get_size()
        screen_width = screen_width / self.map_layer.zoom
        screen_heigth = screen_heigth / self.map_layer.zoom
        map_width, map_heigth = self.map_layer.map_rect.size
        camera_x = self.player.rect.x - (screen_width / 2)
        camera_y = self.player.rect.y - (screen_heigth / 2)

        # Limitez les coordonnées de la caméra pour qu'elles restent dans les limites de la carte
        camera_x = max(0, min(camera_x, map_width - screen_width))
        camera_y = max(0, min(camera_y, map_heigth - screen_heigth))

        for character, data in zip(self.character_sprites, character_data):
            character.rect.x = (data.x - camera_x) * self.map_layer.zoom
            character.rect.y = (data.y - camera_y) * self.map_layer.zoom
            character.direction = data.direction
            character.index_image = data.index_image
            character.spritesheet_index = data.spritesheet_index

    def update(self) -> None:
        if self.player:
            if self.player.change_map and self.player.step >= 8:
                self.switch_map(self.player.change_map)
                self.player.change_map = None
        self.group.update()
        self.group.center(self.player.rect.center)
        self.group.draw(self.screen.get_display())
        # self.squares.draw(self.screen.get_display())
        self.character_sprites.update()
        self.character_sprites.draw(self.screen.get_display())

    def pose_player(self, switch: Switch):
        position = self.tmx_data.get_object_by_name(
            "spawn " + self.current_map.name + " " + str(switch.port))
        self.player.position = pygame.math.Vector2(position.x, position.y)
