import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    timer = pygame.time.Clock()
    dt = 0.0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} \nScreen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(x, y)
    AsteroidField()

    while True:
        log_state()
        updatable.update(dt)
        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        screen.fill("black")
        for drawing in drawable:
            drawing.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = timer.tick(60) / 1000


if __name__ == "__main__":
    main()
