import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    AsteroidField.containers = updateable
    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        for x in updateable:
            x.update(dt)

        for x in asteroids:
            if x.collision(player):
                print("Game over!")
                sys.exit(0)

        for x in drawable:
            x.draw(screen)

        # player.update(dt)
        # player.draw(screen)
        pygame.display.flip()
        # limit the framerate to 60fps
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
