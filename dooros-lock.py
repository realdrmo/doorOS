from utils.scene import InteractiveScene

from ui.grid import GridLayout

import threading

from ui.icon import Icon

import pygame

from utils.animation import *


class ErrorScene(InteractiveScene):

    def __init__(self, screen):
        super().__init__(screen)
        screen_size = screen.get_size()
        self.screen = screen
        font_type = pygame.font.SysFont(None, 30)
        error_msg = 'FATAL: SIGSEGV (Segmentation Fault) at address 0x00000000'
        self.error_text = font_type.render(error_msg, False, 'black')
        self.error_text_rect = self.error_text.get_rect(center=(screen_size
            [0] // 2, screen_size[1] // 2))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def run(self) ->bool:
        if not self.update():
            return False
        self.screen.fill('blue')
        self.screen.blit(self.error_text, self.error_text_rect)
        pygame.display.flip()
        return True


class Intro(InteractiveScene):

    def __init__(self, screen):
        super().__init__(screen)
        screen_size = screen.get_size()
        self.screen = screen
        self._logo = pygame.image.load('media/drmo.png').convert_alpha()
        self._logo_rect = self._logo.get_rect(center=(screen_size[0] // 2, 
            screen_size[1] // 2))
        self._logo_animation = AnimationSequence()
        self._logo_animation.add_animation(Animation(AnimationQuery(opacity
            =0), AnimationQuery(opacity=1)))
        self._logo_animation.add_animation(Animation(AnimationQuery(opacity
            =1), AnimationQuery(opacity=0)))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        return True

    def run(self) ->bool:
        if not self.update():
            return False
        self.screen.fill('black')
        animation = self._logo_animation.get_next()
        if self._logo_animation.is_finished:
            self.is_finished = True
        else:
            animation.set_duration(10)
            animation.animate(self._logo)
        self.screen.blit(self._logo, self._logo_rect)
        pygame.display.flip()
        return True


class MainScene(InteractiveScene):

    def __init__(self, screen):
        super().__init__(screen)
        screen_size = screen.get_size()
        self.screen = screen
        self.grid = GridLayout(screen_size[0], screen_size[1] - 100, 100)
        self.grid[1].add(Icon('media/trash.svg'))
        self.grid[2].add(Icon('media/math-50-50.png'))
        self.current = None
        self.game_over = False
        self.has_started = False
        self.points = 0
        self.font = pygame.font.SysFont(None, 30)

    def _generate_apps(self):
        self.has_started = True
        while not self.game_over:
            pygame.time.wait(10000 // (self.points + 1))
            count = 0
            for x in range(len(self.grid.cells)):
                if not self.grid[x].current:
                    self.grid[x].add(Icon('media/math-50-50.png'))
                    break
                else:
                    count += 1
            if count == len(self.grid.cells):
                self.game_over = True

    def update(self) ->bool:
        mouse = pygame.mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    for x in range(len(self.grid.cells)):
                        if self.grid[x].current and not self.current:
                            if self.grid[x].current.rect.collidepoint(mouse
                                .get_pos()):
                                self.current = self.grid[x].current.copy()
                                self.grid[x].current = None
                                self.grid[x].clear()
            elif event.type == pygame.MOUSEBUTTONUP:
                for x in range(len(self.grid.cells)):
                    if self.grid[x].rect.collidepoint(mouse.get_pos()):
                        if not self.grid[x].current and self.current:
                            self.grid[x].current = self.current.copy()
                            self.current = None
                            self.grid[x].clear()
                        elif self.grid[x].current and self.current:
                            if self.grid[x
                                ].current.image_url == 'media/trash.svg':
                                self.points += 1
                                self.current = None
        if self.game_over:
            self.error_func()
        if not self.has_started:
            threading.Thread(target=self._generate_apps).start()
        return True

    def run(self) ->bool:
        mouse = pygame.mouse
        if not self.update():
            return False
        self.screen.fill('black')
        self.grid.draw(self.screen)
        if self.current:
            self.current.rect.center = mouse.get_pos()
            self.screen.blit(self.current.surface, self.current.rect)
        height = self.screen.get_height()
        width = self.screen.get_width()
        self.screen.blit(self.font.render(str(self.points), False, 'white'),
            (width // 2, height - 50))
        pygame.display.flip()
        return True


