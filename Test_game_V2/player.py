import pygame

class Player():
    def __init__(self, x, y, width, height, color, role):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.role = role
        self.rect = (x,y,width,height)
        self.vel = 3
        self.eliminated = False
        self.print_init()

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.x -= self.vel

        if keys[pygame.K_RIGHT]:
            self.x += self.vel

        if keys[pygame.K_UP]:
            self.y -= self.vel

        if keys[pygame.K_DOWN]:
            self.y += self.vel

        self.update()

    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)

    def collide(self, other_player):
    # Vérifiez si le joueur actuel (self) et l'autre joueur (other_player) se chevauchent
        if self.x < other_player.x + other_player.width and \
        self.x + self.width > other_player.x and \
        self.y < other_player.y + other_player.height and \
        self.y + self.height > other_player.y:
            print("yes")
            return True  # Il y a une collision
        else:
            return False  # Pas de collision

    def eliminate(self):
        print("self.color start", self.color)
        self.color = (110, 110, 110)
        self.eliminated = True
        print("self.color end", self.color)

    def print_init(self):
        print("player", self.color, self.eliminated)