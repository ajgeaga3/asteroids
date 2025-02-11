

import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from player import Player

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:",  SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    player = Player(x, y)
    asteroidfield = AsteroidField()  
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        screen.fill("black")
        for asteroid in asteroids:
            if asteroid.does_collide(player):
                print("Game over!")
                sys.exit()
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 
        
    
    
if __name__ == "__main__":
    main()