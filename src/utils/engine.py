import pygame
import sys

class Engine:
    def __init__(self):
        self.scenes = []
        self.error_scene = None

        self.is_error = False
    
    def add_error_scene(self, scene):
        self.error_scene = scene
    def add_scene(self, scene):
        self.scenes.append(scene)
    def start(self):
        print("[+] Starting the engine")

        clock = pygame.time.Clock()

        running = True
        count = 0

        is_current = False
        while running:
            if self.is_error:
                if not self.error_scene.run():
                    running = False
                    sys.exit()
            else:                
                for scene in self.scenes:
                    if not scene.is_finished:
                        if scene.is_running:
                            if not scene.run():
                                running = False
                                sys.exit()
                        else:
                            if not is_current: 
                                scene.is_running = True
                                is_current = True

                    else:
                        if scene.is_running: 
                            scene.is_running = False
                            is_current = False

                            count += 1
            
            clock.tick(60)
            
            if count == len(self.scenes):
                running = False
            