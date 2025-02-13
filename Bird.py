import pygame
import numpy as np
from NeuralNetwork import NeuralNetwork

class Bird(pygame.sprite.Sprite):   
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.gravity = 0.25
        self.jump_force = -4
        self.velocity = 0
        
        self.survival_time = 0
        self.isDead = False
        self.brain = NeuralNetwork(3, 5, 1)  

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def drop(self):
        if not self.isDead:
            self.velocity += self.gravity
            self.rect.y += self.velocity

    def jump_up(self):
        if not self.isDead:
            self.velocity = self.jump_force
            self.rect.y += self.velocity

    def think(self, pipe):
        distance_to_pipe = self.get_distance_to_pipe(pipe)
        height_difference = self.get_height_difference(pipe)
        velocity = self.velocity
        
        input_data = np.array([
            distance_to_pipe ,  
            height_difference,
            velocity
        ]).reshape(3, 1)

        output = self.brain.feedforward(input_data)
        if output.item() > 0.5:
            self.jump_up()

    def update_survival_time(self):
        if not self.isDead:
            self.survival_time += 0.5

    def restart(self):
        self.rect.topleft = (50, 144)
        self.velocity = 0
        self.isDead = False
        self.survival_time = 0

    def get_brain(self):
        return self.brain

    def get_height_difference(self, pipe):
        gap_center = (pipe.top_rect.bottom + pipe.bottom_rect.top) / 2
        return self.rect.centery - gap_center

    def get_distance_to_pipe(self, pipe):
        return max(0, pipe.top_rect.left - self.rect.right)
