import pygame

from game import Game
from entities import player_instances

pygame.init()

if __name__ == "__main__":
    game: Game = Game()
    game.run(player_instances)
