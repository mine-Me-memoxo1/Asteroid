import pygame
from constants import *
from player import *
def main():
    print("Starting Asteroids!")
    print("Screen width: {}\nScreen height: {}".format(SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    while 1:
        screen.fill('black')
        player.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
