import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):
    def __init__(self, x, y, velocity):
        radius = SHOT_RADIUS
        super().__init__(x, y, radius)
        self.velocity = velocity
        pass
        
    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), self.position, self.radius, 2)

        return super().draw(screen)
    
    def update(self, delta_time):
        self.position += self.velocity*delta_time