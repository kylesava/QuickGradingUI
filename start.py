import pygame
  
pygame.init()  
programIcon = pygame.image.load('assets/icon.png')

pygame.display.set_caption('QuickGrader')  
pygame.display.set_icon(programIcon)
screen = pygame.display.set_mode((600,600))  
done = False  
  
while not done:  
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            done = True  
    pygame.display.flip()  