from utils.scene import InteractiveScene
import pygame

class ErrorScene(InteractiveScene):
    def __init__(self, screen):
        super().__init__(screen)

        screen_size = screen.get_size()

        self.screen = screen

        font_type = pygame.font.SysFont(None, 30)
        error_msg = "FATAL: SIGSEGV (Segmentation Fault) at address 0x00000000"

        self.error_text = font_type.render(error_msg, False, "black")
        self.error_text_rect = self.error_text.get_rect(center=(screen_size[0]//2, screen_size[1]//2))

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        return True
    def run(self) -> bool:

        if not self.update():
            return False
        self.screen.fill("blue")

        self.screen.blit(self.error_text, self.error_text_rect)

        pygame.display.flip()

        return True