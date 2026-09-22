import pygame
import random

from circleshape import CircleShape
from typing import override
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    @override
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius ,LINE_WIDTH)

    @override
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt

    def split(self) -> None:
        self.kill()

        if self.radius < ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")

        new_angle = random.uniform(20, 50)

        asteroid_one_vector = self.velocity.rotate(new_angle)

        asteroid_two_vector = self.velocity.rotate(new_angle*-1)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_one.velocity = asteroid_one_vector * 1.2

        asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)

        asteroid_two.velocity = asteroid_two_vector * 1.2
        
