import pygame, sys, math, random
from Skier import*
from Hud import*
pygame.init()

Clock = pygame.time.Clock();

size= [700, 900]
screen = pygame.display.set_mode(size)

player = Skier([2,5], [size[0]/2,100])
score = Hud("Score: ",[0,0])
timer = Hud("Time: ",[700-200,0])

time = 0
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKEY("left")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKEY("right")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKEY("up")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKEY("down")
            elif event.key == pygame.K_e:
                player.goKEY("spinR")
            elif event.key == pygame.K_q:
                player.goKEY("spinL")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                player.goKEY("sleft")
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                player.goKEY("sright")
            elif event.key == pygame.K_w or event.key == pygame.K_UP:
                player.goKEY("sup")
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                player.goKEY("sdown")
            elif event.key == pygame.K_e:
                player.goKEY("sspinR")
            elif event.key == pygame.K_q:
                player.goKEY("sspinL")
                 
    time += 1/60
    
    player.update(size)
    timer.update(int(time))
    score.update(0)
                
    screen.fill((255, 255, 255))
    screen.blit(player.image, player.rect)
    screen.blit(score.image, score.rect)
    screen.blit(timer.image, timer.rect)
    pygame.display.flip()
    Clock.tick(60)

