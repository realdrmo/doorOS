import pygame

from utils.scene import InteractiveScene
from utils.animation import *

class Intro(InteractiveScene):
    def __init__(self, screen):
        super().__init__(screen)

        screen_size = screen.get_size() 
        
        self.screen = screen

        self._logo = pygame.image.load("media/drmo.png").convert_alpha()

        self._logo_rect = self._logo.get_rect(center=(screen_size[0]//2, screen_size[1]//2))

        self._logo_animation = AnimationSequence()

        self._logo_animation.add_animation(
            Animation(
                AnimationQuery(opacity=0),
                AnimationQuery(opacity=1)
            )
        )
        self._logo_animation.add_animation(
            Animation(
                AnimationQuery(opacity=1),
                AnimationQuery(opacity=0)
            )
        )
    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        return True
    def run(self) -> bool:

        if not self.update(): return False

        self.screen.fill("black")

        animation = self._logo_animation.get_next()

        if self._logo_animation.is_finished:
            self.is_finished = True

        else:
            animation.set_duration(10)
            animation.animate(self._logo)
        
        self.screen.blit(self._logo, self._logo_rect)

        pygame.display.flip()

        return True
