import pygame
import pygame.locals
import numpy as np
from robGUI import ArmPart
import time

white = (255, 255, 255)
black = (0, 0, 0)
 
pygame.init()
 
width = 500
height = 500
display = pygame.display.set_mode((width, height))
fpsClock = pygame.time.Clock()

pic1 = ArmPart('C:\\Users\\First Place\\Documents\\GitHub\\ProjetoSemestralProg\\Repo_ProjetoSem\\Projeto_2sem\\pic1.png',scale=.7)
pic2 = ArmPart('C:\\Users\\First Place\\Documents\\GitHub\\ProjetoSemestralProg\\Repo_ProjetoSem\\Projeto_2sem\\pic2.png',scale=.7)

origin = (width / 2, height / 2)

while 1:
 
    display.fill(white)

    

    if(s==1):
        pic1_image, pic1_rect = pic1.rotate(.1)
        pic2_image, pic2_rect = pic2.rotate(-.03)
    elif(s==2):
        pic1_image, pic1_rect = pic1.rotate(-.1)
        pic2_image, pic2_rect = pic2.rotate(+.03)

    joints_x = np.cumsum([0, 
                          pic1.scale * np.cos(pic1.rotation),
                          pic2.scale * np.cos(pic2.rotation)]) + origin[0]
    joints_y = np.cumsum([0, 
                          pic1.scale * np.sin(pic1.rotation),
                          pic2.scale * np.sin(pic2.rotation)]) * -1 + origin[1]
    joints = [(int(x), int(y)) for x,y in zip(joints_x, joints_y)]

    def transform(rect, base, arm_part):
        rect.center += np.asarray(base)
        rect.center += np.array([np.cos(arm_part.rotation) * arm_part.offset,
                                -np.sin(arm_part.rotation) * arm_part.offset])
 
    transform(pic1_rect, joints[0], pic1)
    transform(pic2_rect, joints[1], pic2)

    display.blit(pic1_image, pic1_rect)
    display.blit(pic2_image, pic2_rect)

    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    fpsClock.tick(30)

