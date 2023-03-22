import pygame, sys, math, random

class Bump():
    def __init__(self, pos=[25,25]):
        n = random.randint(1,2,3,4)
        self.image = pygame.image.load("images/obstacles/bumps"+str(n)"+.png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "bump"

