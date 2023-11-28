import pygame
from keylistener import KeyListener
from screen import Screen
from tool import Tool


class Entity(pygame.sprite.Sprite):
    def __init__(self, keylistener: KeyListener, screen: Screen, x: int, y: int, role: int, name: int):
        super().__init__()
        self.screen: Screen = screen
        self.keylistener: KeyListener = keylistener
        self.role = role
        self.name = name
        self.init_spritesheet()
        self.image: pygame.image = Tool.split_image(
            self.spritesheet, 0, 0, 24, 32)
        self.position: pygame.math.Vector2 = pygame.math.Vector2(x, y)
        self.rect: pygame.Rect = self.image.get_rect()
        self.all_images: dict[str, list[pygame.image]
                              ] = self.get_all_images(self.spritesheet)
        self.index_image: int = 0
        self.image_part: int = 0
        self.reset_animation: bool = False
        self.hitbox: pygame.Rect = pygame.Rect(0, 0, 16, 16)

        self.step: int = 0
        self.animation_walk: bool = False
        self.direction: str = "down"

        self.animtion_step_time: float = 0.0
        self.action_animation: int = 16

        self.speed: int = 1

    def init_spritesheet(self) -> None:
        if self.role == "cat":
            self.spritesheet: pygame.image = pygame.image.load(
                "./assets/sprite/hero_01_white_f_run.png")
            self.spritesheet_index = "cat_red"
        else:
            self.spritesheet: pygame.image = pygame.image.load(
                f"./assets/sprite/{self.name}_walk.png")
            self.spritesheet_index = "foot_red"

    def update(self) -> None:
        self.animation_sprite()
        self.move()
        self.rect.center = self.position
        self.hitbox.midbottom = self.rect.midbottom
        self.image = self.all_images[self.direction][self.index_image]
        if self.role == "ghost":
            self.image.set_alpha(150)

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

    def move(self) -> None:
        if self.animation_walk:
            self.animtion_step_time += self.screen.get_delta_time()
            if self.step < 16 and self.animtion_step_time >= self.action_animation:
                self.step += self.speed
                if self.direction == "left":
                    self.position.x -= self.speed
                elif self.direction == "right":
                    self.position.x += self.speed
                elif self.direction == "up":
                    self.position.y -= self.speed
                elif self.direction == "down":
                    self.position.y += self.speed
                self.animtion_step_time = 0
            elif self.step >= 16:
                self.step = 0
                self.animation_walk = False
                if self.reset_animation:
                    self.reset_animation = False
                else:
                    if self.image_part == 0:
                        self.image_part = 2
                    else:
                        self.image_part = 0

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

        width: int = spritesheet.get_width() // 4
        height: int = spritesheet.get_height() // 4

        for i in range(4):
            for j, key in enumerate(all_images.keys()):
                all_images[key].append(Tool.split_image(
                    spritesheet, i * width, j * height, 24, 32))
        return all_images
