import pygame, sys, math,

class Bump():
    def __init__(self, pos=[25,25]):
        self.image = pygame.image.load("images/obstacles/jump.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "jump"
