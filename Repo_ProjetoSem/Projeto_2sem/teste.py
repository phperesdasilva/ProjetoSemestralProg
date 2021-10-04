from robGUI import ArmPart
import pygame
import pygame.locals

white = (255, 255, 255)
 
pygame.init()
 
display = pygame.display.set_mode((300, 300))
fpsClock = pygame.time.Clock()

teste = ArmPart('C:\\Users\\First Place\\Documents\\GitHub\\ProjetoSemestralProg\\Repo_ProjetoSem\\Projeto_2sem\\pic.png',scale=.7)

while 1:
 
    display.fill(white)

    ua_image, ua_rect = teste.rotate(.01)

    display.blit(ua_image, ua_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            sys.exit()
 
    pygame.display.update()
    fpsClock.tick(30)

