import pygame
from tool import Tool
from entity import Entity
from keylistener import KeyListener
from screen import Screen
from switch import Switch


class Player(Entity):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int):
        super().__init__(keylistener, screen, x, y)
        self.pokedollars: int = 0

        self.spritesheet_bike: pygame.image = pygame.image.load(
            "./assets/sprite/hero_01_red_m_cycle_roll.png")

        self.switchs: list[Switch] | None = None
        self.collisions: list[pygame.Rect] | None = None
        self.change_map: Switch | None = None

    def update(self) -> None:
        self.check_input()
        self.check_move()
        super().update()

    def check_move(self) -> None:
        if self.animation_walk is False:
            temp_hitbox = self.hitbox.copy()
            if self.keylistener.key_pressed(pygame.K_q):
                temp_hitbox.x -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_left()
                else:
                    self.direction = "left"
            elif self.keylistener.key_pressed(pygame.K_d):
                temp_hitbox.x += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_right()
                else:
                    self.direction = "right"
            elif self.keylistener.key_pressed(pygame.K_z):
                temp_hitbox.y -= 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_up()
                else:
                    self.direction = "up"
            elif self.keylistener.key_pressed(pygame.K_s):
                temp_hitbox.y += 16
                if not self.check_collisions(temp_hitbox):
                    self.check_collisions_switchs(temp_hitbox)
                    self.move_down()
                else:
                    self.direction = "down"

    def add_switchs(self, switchs: list[Switch]):
        self.switchs = switchs

    def check_collisions_switchs(self, temp_hitbox):
        if self.switchs:
            for switch in self.switchs:
                if switch.check_collision(temp_hitbox):
                    self.change_map = switch
        return None

    def add_collisions(self, collisions):
        self.collisions = collisions

    def check_collisions(self, temp_hitbox: pygame.Rect):
        for collision in self.collisions:
            if temp_hitbox.colliderect(collision):
                return True
        return False

    def check_input(self):
        if self.keylistener.key_pressed(pygame.K_b):
            self.switch_bike()

    def switch_bike(self, deactive=False):
        if self.speed == 1 and not deactive:
            self.speed = 2
            self.all_images = self.get_all_images(self.spritesheet_bike)
        else:
            self.speed = 1
            self.all_images = self.get_all_images(self.spritesheet)
        self.keylistener.remove_key(pygame.K_b)


class OtherPlayers():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __iter__(self):
        yield self.x
        yield self.y


class OtherPlayersVisualisation(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int):
        super().__init__()
        # OtherPlayers.__init__(self, x, y)
        # self.x = x
        # self.y = y
        self.spritesheet = pygame.image.load(
            "./assets/sprite/hero_01_red_m_walk.png")
        self.image = Tool.split_image(self.spritesheet, 0, 0, 24, 32)
        self.position = pygame.math.Vector2(x, y)
        self.rect = self.image.get_rect()
        self.all_images = self.get_all_images(self.spritesheet)
        self.index_image = 0
        self.image_part = 0
        self.reset_animation = False
        self.hitbox = pygame.Rect(0, 0, 16, 16)
        print(self.position)

        self.step: int = 0
        self.animation_walk: bool = False
        self.direction: str = "down"

        self.animtion_step_time: float = 0.0
        self.action_animation: int = 16

        self.speed: int = 1

        # self.rect = pygame.Rect(x, y, 20, 20)
        # self.image = pygame.Surface((20, 20))
        # self.image.fill("blue")

    def __iter__(self):
        yield self.x
        yield self.y

    def update(self) -> None:
        self.animation_sprite()
        # self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]

    def move_left(self) -> None:
        self.animation_walk = True
        self.direction = "left"

    def move_right(self) -> None:
        self.animation_walk = True
        self.direction = "right"

    def move_up(self) -> None:
        self.animation_walk = True
        self.direction = "up"

    def move_down(self) -> None:
        self.animation_walk = True
        self.direction = "down"

    def animation_sprite(self) -> None:
        if int(self.step // 8) + self.image_part >= 4:
            self.image_part = 0
            self.reset_animation = True
        self.index_image = int(self.step // 8) + self.image_part

    # def move(self) -> None:
    #     if self.animation_walk:
    #         self.animtion_step_time += self.screen.get_delta_time()
    #         if self.step < 16 and self.animtion_step_time >= self.action_animation:
    #             self.step += self.speed
    #             if self.direction == "left":
    #                 self.position.x -= self.speed
    #             elif self.direction == "right":
    #                 self.position.x += self.speed
    #             elif self.direction == "up":
    #                 self.position.y -= self.speed
    #             elif self.direction == "down":
    #                 self.position.y += self.speed
    #             self.animtion_step_time = 0
    #         elif self.step >= 16:
    #             self.step = 0
    #             self.animation_walk = False
    #             if self.reset_animation:
    #                 self.reset_animation = False
    #             else:
    #                 if self.image_part == 0:
    #                     self.image_part = 2
    #                 else:
    #                     self.image_part = 0

    def align_hitbox(self) -> None:
        self.position.x += 16
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.x % 16 != 0:
            self.rect.x -= 1
            self.hitbox.midbottom = self.rect.midbottom
        while self.hitbox.y % 16 != 0:
            self.rect.y -= 1
            self.hitbox.midbottom = self.rect.midbottom
        self.position = pygame.math.Vector2(self.rect.center)

    def get_all_images(self, spritesheet) -> dict[str, list[pygame.image]]:
        all_images = {
            "down": [],
            "left": [],
            "right": [],
            "up": []
        }

        width = spritesheet.get_width() // 4
        height = spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(
                    spritesheet, i * width, j * height, 24, 32))
        return all_images
