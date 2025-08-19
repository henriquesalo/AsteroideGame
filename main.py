import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fps = pygame.time.Clock()
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = updatable
    #criando um novo objeto
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collisions(player):
                print("Game Over!")
                sys.exit()

            for shot in shots:
                if asteroid.check_collisions(shot):
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for objects in drawable:
            objects.draw(screen)

        pygame.display.flip()
        #Limitando o fps para 60 frames por segundo
        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
