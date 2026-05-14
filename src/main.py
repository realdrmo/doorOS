import importlib
import pygame

import os
import sys

from utils.engine import Engine

current_dir = os.getcwd()

if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

try:
    scenes = importlib.import_module("dooros-lock")
except ModuleNotFoundError:
    import sys

    print("[!] Please run 'py build.py' in order to build first")
    sys.exit()
    
pygame.init()

screen = pygame.display.set_mode((800, 400))

engine = Engine()

engine.add_error_scene(scenes.ErrorScene(screen))
engine.add_scene(scenes.Intro(screen))
engine.add_scene(scenes.MainScene(screen).on_error(lambda: setattr(engine, "is_error", True)))

engine.start()

