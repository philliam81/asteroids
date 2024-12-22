# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()


    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        Player.update(dt)
        # Fill the screen with black
        black = (0, 0, 0)  # RGB color for black
        screen.fill(black)

        pygame.display.flip()
        time =  clock.tick(60)
        dt = time / 1000



if __name__ == "__main__":
    main()