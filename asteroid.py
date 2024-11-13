import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pass

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

        return super().draw(screen)
    
    def update(self, delta_time):
        self.position += self.velocity*delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        rangle = random.uniform(20,50)
        ast1_vel = self.velocity.rotate(rangle)*1.2
        ast2_vel = self.velocity.rotate(-rangle)*1.2
        newrad = self.radius - ASTEROID_MIN_RADIUS
        
        ast1 = Asteroid(self.position.x, self.position.y, newrad)
        ast1.velocity = ast1_vel
        ast2 = Asteroid(self.position.x, self.position.y, newrad)
        ast2.velocity = ast2_vel
            


