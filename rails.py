import pygame, sys, math, random

class Rail():
    def __init__(self, pos=[25,25]):
        n = random.randint(1,2)
        self.image = pygame.image.load("images/obstacles/rail"+str(n)+".png")
        self.rect = self.image.get_rect(center = pos)
        self.kind = "rail"
