import pygame
import sys
from constants import *
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable, updatable, shots)

    player = Player(x = SCREEN_WIDTH / 2, y  = SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)
        screen.fill("black")
        for item in drawable:
            item.draw(screen)

        for object in asteroids:
            if(object.collides_with(player)):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                if(shot.collides_with(asteroid)):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000

    print(dt)
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}, Screen width: {SCREEN_WIDTH} Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
