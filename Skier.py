import pygame, sys, math

class Skier():
    def __init__(self, speed = [2,5], startPos=[0,0]):
        self.imagesFORWARD = [pygame.image.load ("Images/Skier/forward.png")]
        self.imagesBACKWARD = [pygame.image.load ("Images/Skier/sidewaysR.png"),
                               pygame.image.load ("Images/Skier/backward.png")]
        self.imagesREVERT = [pygame.image.load ("Images/Skier/sidewaysR.png"),
                               pygame.image.load ("Images/Skier/forward.png")]
        self.imagesLEFT = [pygame.image.load ("Images/Skier/sidewaysL.png")]
        self.imagesRIGHT = [pygame.image.load ("Images/Skier/sidewaysR.png")]
        self.imagesturnR = [pygame.image.load ("Images/Skier/turnR.png")]
        self.imagesturnL = [pygame.image.load ("Images/Skier/turnL.png")]
        self.imagesspinL = [pygame.image.load ("Images/Skier/sidewaysL.png"),
                            pygame.image.load ("Images/Skier/backward.png"),
                            pygame.image.load ("Images/Skier/sidewaysR.png"),
                            pygame.image.load ("Images/Skier/forward.png")]
        self.imagesspinR = [pygame.image.load ("Images/Skier/sidewaysR.png"),
                            pygame.image.load ("Images/Skier/backward.png"),
                            pygame.image.load ("Images/Skier/sidewaysL.png"),
                            pygame.image.load ("Images/Skier/forward.png")]
        self.images = self.imagesFORWARD
        self.frame = 0
        self.frameMax = len(self.images)-1
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = startPos)
        
        self.animationTimer = 0
        self.animationTimerMax = 60*.25
        
        self.didBounceX = False   
        self.didBounceY = False 
        
        self.maxSpeedx = speed[0]
        self.maxSpeedy = speed[1]
        self.kind = "skier"    
        
        self.speedx = 0
        self.speedy = 1
        self.speed = [self.speedx, 0]

    def goKEY(self, direction):
        if direction == "left":
            self.speedx = -self.maxSpeedx
            self.images = self.imagesturnL
        elif direction == "right":
            self.speedx = self.maxSpeedx
            self.images = self.imagesturnR
        elif direction == "up":
            self.images = self.imagesBACKWARD
            self.speedy -=1
            if self.speedy <1:
                self.speedy = 1
        elif direction == "down":
            self.speedy +=1
            if self.speedy > self.maxSpeedy:
                self.speedy = self.maxSpeedy
        if direction == "spinL":
            self.images = self.imagesspinL
        if direction == "spinR":
            self.images = self.imagesspinR
        elif direction == "sleft":
            self.speedx = 0
            self.images = self.imagesFORWARD
        elif direction == "sright":
            self.speedx = 0
            self.images = self.imagesFORWARD
        elif direction == "sup":
            self.images = self.imagesREVERT
        elif direction == "sspinL":
            self.speedx = 0
            self.images = self.imagesFORWARD
        elif direction == "sspinR":
            self.speedx = 0
            self.images = self.imagesFORWARD
         
            
        self.frameMax = len(self.images)-1
        self.frame=0
        self.image = self.images[self.frame]
        self.animationTimer += 1

    def update(self, size):
        self.move()
        
        self.didBounceX = False   
        self.didBounceY = False
        
        self.wallCollide(size)
        self.animate()
        
    def animate(self):
        if self.animationTimer > 0:
            self.animationTimer += 1
        if self.animationTimer >= self.animationTimerMax:
            self.animationTimer = 1
            if self.frame < self.frameMax:
                self.frame += 1
            else:
                self.animationTimer = 0
            self.image = self.images[self.frame]
    
    def move(self):
        self.speed = [self.speedx, 0]
        self.rect = self.rect.move(self.speed)
        
    def wallCollide(self, size):
        width = size[0]
        height = size[1]
        if not self.didBounceX:
            if self.rect.right> width:
                self.speedx=-self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True 
            if self.rect.left < 0:
                self.speedx=-self.speedx
                self.move()
                self.speedx = 0
                self.didBounceX = True 
