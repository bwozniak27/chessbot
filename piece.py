import pygame

class piece():
    def __init__(self, type, color, pos):
        self.type = type
        self.color = color
        self.pos = pos
        
        #fetch the image
        self.icon = pygame.image.load("piece_icons/" + self.type + "_" + self.color + ".svg")
        self.icon = pygame.transform.scale(self.icon, (80, 80))