

import sys
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
from player import Player
from shot import Shot


def main():
    score = 0
    lives = 3
    pygame.font.init()
    pygame.init()
    font = pygame.font.SysFont("Arial", 36)
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:",  SCREEN_HEIGHT)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    right_edge = SCREEN_WIDTH
    left_edge = 0
    top_edge = 0
    bottom_edge = SCREEN_HEIGHT
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (updatables, drawables, shots)
    player = Player(x, y)
    
    asteroidfield = AsteroidField()  
    while(True):
        text_surface = font.render("Score: " + str(score) , True, (255, 255, 255))
        lives_text_surface = font.render("Lives: " + str(lives) , True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        screen.fill("black")
        screen.blit(text_surface, (10, 10))
        screen.blit(lives_text_surface, (10, 50))
        if player.position.x > right_edge:
            player.position.x = left_edge
        elif player.position.x < left_edge:
            player.position.x = right_edge
        elif player.position.y > bottom_edge:
            player.position.y = top_edge
        elif player.position.y < top_edge:
            player.position.y = bottom_edge
        for asteroid in asteroids:
            if asteroid.does_collide(player):
                player.position.x = SCREEN_WIDTH / 2
                player.position.y = SCREEN_HEIGHT / 2
                lives -= 1
                if lives == 0:
                    print("Game over!")
                    print(score)
                    sys.exit()
            for bullet in shots:
                if asteroid.does_collide(bullet):
                    asteroid.split()
                    bullet.kill()
                    score += 1
        
        for obj in drawables:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000 
    
        
    
    
if __name__ == "__main__":
    main()