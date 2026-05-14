import pygame

class InteractiveScene:
    def __init__(self, screen: pygame.Surface):
        self.is_finished = False
        self.is_running = False

        self.error_func = None

    def on_error(self, func):
        self.error_func = func

        return self
    def update(self):
        raise NotImplemented()
    def run(self) -> bool:
        raise NotImplemented()
    