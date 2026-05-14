import pygame

class Cell:
    def __init__(self, width, height, pos):
        self.surface = pygame.Surface(
            (width, height)
        )
        self.surface.fill("white")
        self.rect = self.surface.get_rect()
        self.rect.bottomleft = pos

        self.border_width = 2

        self.border_surface = pygame.Surface(
            (width - self.border_width, height - self.border_width)
        )
        self.border_rect = self.border_surface.get_rect()

        self.border_rect.center = (width//2, height//2)

        self.current = None
    
    def add(self, app):
        self.current = app
    def clear(self):
        self.border_surface.fill((0, 0, 0, 0))
    def draw(self, screen: pygame.Surface):

        self.surface.blit(self.border_surface, self.border_rect)
        screen.blit(self.surface, self.rect)

        if self.current:
            self.current.rect.center = self.rect.center

            self.current.draw(screen)

class GridLayout:
    def __init__(self, width, height, ratio):
        self.cells: list[Cell] = []
        self.ratio = ratio

        for x in range(0, width + 1, ratio):
            for y in range(0, height + 1, ratio):
                cell = Cell(ratio, ratio, (x, y))
                self.cells.append(cell)
        
        self.surface = pygame.Surface((width, height))
        self.rect = self.surface.get_rect()

        self.enable_highlight = False
    def __getitem__(self, key) -> Cell:
        return self.cells[key]
    def draw(self, screen: pygame.Surface):
        screen.blit(self.surface, self.rect)
        for cell in self.cells:
            cell.draw(self.surface)