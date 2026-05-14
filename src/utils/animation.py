import pygame
import math

class AnimationQuery:
    def __init__(self, **query):
        self.opacity = query.get("opacity", 0)
        self.position = query.get("position")
        
class Animation:
    def __init__(self, _from: AnimationQuery, to: AnimationQuery):
        self.query = to
        self.start = _from

        self.is_finished = False
        
        self.draw_per_frame = 1
    def set_duration(self, duration):
        self.draw_per_frame = 60 * duration/1000
    def animate(self, surface: pygame.Surface, rect: pygame.Rect =None):
        step = 0.01
        if self.query.opacity >= 0:
            if abs(self.query.opacity - self.start.opacity) <= step:
                self.is_finished = True
                return
            
            
            if self.query.opacity > self.start.opacity: 
                self.start.opacity += self.draw_per_frame/100
            elif self.query.opacity < self.start.opacity:
                self.start.opacity -= self.draw_per_frame/100
            
            print(f"Alpha: {self.start.opacity}")
            surface.set_alpha(self.start.opacity * 255)
            
        if self.query.position:
            if self.query.position.get("x", 0) == rect.centerx or \
               self.query.position.get("y", 0) == rect.centery:
                self.is_finished = True
                return
            position = self.query.position
            
            if position.get("x", 0) > rect.centerx:
                rect.centerx += self.draw_per_frame
            elif position.get("x", 0) < rect.centerx:
                rect.centerx -= self.draw_per_frame
            
            if position.get("y", 0) > rect.centery:
                rect.centery += self.draw_per_frame
            elif position.get("y", 0) < rect.centery:
                rect.centery -= self.draw_per_frame
            

class AnimationSequence:
    def __init__(self):
        self.sequence: list[Animation] = []

        self.current_index = 0
        
        self.isloop = False
        self.is_finished = False
    def get_next(self):
        for x in range(len(self.sequence)):
            if self[x].is_finished: 
                continue

            self.current_index = x
            return self[x]
        
        if self.isloop:
            for x in range(len(self.sequence)):
                self[x].is_finished = True
            
            return self.sequence[0]
        else:
            
            self.is_finished = True
    def add_animation(self, animation):
        self.sequence.append(animation)
    def __getitem__(self, key):
        return self.sequence[key]