import pygame
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.height = random.randint(150, 400)

        self.gap = 80
        self.top_rect = self.image.get_rect()
        self.bottom_rect = self.image.get_rect()

        # Top pipe
        self.bottom_rect.topleft = (x, y + self.height)
        self.top_rect.topleft = (x, y + self.height - self.gap - self.top_rect.height)
        

    def draw(self, surface):
        surface.blit(self.image, self.bottom_rect)
        surface.blit(pygame.transform.flip(self.image, False, True), self.top_rect)
    

    def move(self):
        self.bottom_rect.left -= 1
        self.top_rect.left -= 1
        
        if self.bottom_rect.right <= 0 or self.bottom_rect.left <= -52:
            self.height = random.randint(150, 400)
            self.bottom_rect.topleft = (300, self.height)
            self.top_rect.topleft = (300, self.height - self.gap - self.top_rect.height)
    
    def restart(self):
        self.height = random.randint(150, 400)
        self.bottom_rect.topleft = (300, self.height)
        self.top_rect.topleft = (300, self.height - self.gap - self.top_rect.height)

            
