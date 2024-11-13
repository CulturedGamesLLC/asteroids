import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import *

def main ():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    pyClock = pygame.time.Clock()
    delta_time = 0
    screen = render_init()

    #Why did we remake delegates?
    updates = pygame.sprite.Group()
    draws = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updates, draws)
    Shot.containers = (shots, updates, draws)
    Asteroid.containers = (asteroids, updates, draws)
    AsteroidField.containers = (updates)


    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    running = True
    while running:
        if pygame:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
            
        pygame.display.flip()

        screen.fill((0,0,0))

        #This is poop
        for obj in draws:
            obj.draw(screen)

        #Buncha poop
        for obj in updates:
            obj.update(delta_time)

        #More diarrhea
        for obj in asteroids:
            for shot in shots:
                if shot.check_collision(obj):
                    shot.kill()
                    obj.split()
            for roid in asteroids:
                if roid != obj:
                    if roid.check_collision(obj):
                        roid.bounce(obj)
                        obj.bounce(roid)
            if obj.check_collision(player):
                print("Game over!")
                running = False
                pygame.quit()
                return

 
        delta_time = (pyClock.tick(60)/1000)


#Killing idea while I wait for the course to catch-up
#def render(surface):
#    pygame.display.update()

def render_init():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    return screen

if __name__ == "__main__":
    main()