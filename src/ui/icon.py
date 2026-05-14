import pygame
import os

class Icon:
    def __init__(self, image_url):
        print(os.path.exists(image_url))

        self.image_url = image_url
        self.surface = pygame.image.load(image_url).convert_alpha()
        self.rect = self.surface.get_rect()
    
    def copy(self):
        return Icon(self.image_url)
    def __eq__(self, value):
        if isinstance(value, Icon):
            if self.image_url == value.image_url:
                return True
    def draw(self, screen):  
        
        screen.blit(self.surface, self.rect)