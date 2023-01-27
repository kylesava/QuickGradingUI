import pygame as p
  
p.init()  
programIcon = p.image.load('assets/icon.png')

p.display.set_caption('QuickGrader')  
p.display.set_icon(programIcon)
screenX = 1500
screenY = 900
screen = p.display.set_mode((screenX,screenY))  


############################### Graphics Functions ###############################
def template():
    screen.fill(0x000000)
    mediaBg = p.image.load('assets/mediaBackground.png')
    mediaBg = p.transform.scale(mediaBg, (screenY,screenY))
    screen.blit(mediaBg,(0,0))
    gradeBg = p.image.load('assets/gradingBackground.png')
    gradeBg = p.transform.scale(gradeBg, (int(2*screenY/3),screenY))
    screen.blit(gradeBg,(screenY+1,0))
    #p.draw.rect(screen,0xaaaaaa,(0,0,int(screenX*2/3),screenY))
##################################################################################

done = False  
template()
while not done:  
    for event in p.event.get():  
        if event.type == p.QUIT:  
            done = True  
        elif event.type == p.MOUSEBUTTONDOWN:
            position=event.pos
            p.draw.rect(screen,(255,255,255),(position[0],position[1],20,20))
    p.display.flip()  