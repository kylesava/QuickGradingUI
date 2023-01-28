import pygame as p
from studentobj import Student,File
  
p.init()  
programIcon = p.image.load('assets/icon.png')

p.display.set_caption('QuickGrader')  
p.display.set_icon(programIcon)
screenX = 1500
screenY = 900
screen = p.display.set_mode((screenX,screenY))  


############################### Graphics Functions ###############################
def template(mode=6):
    if mode%2==0:
        mediaBg = p.image.load('assets/mediaBackground.png')
        mediaBg = p.transform.scale(mediaBg, (screenY,screenY))
        screen.blit(mediaBg,(0,0))
    if mode%3==0:
        gradeBg = p.image.load('assets/gradingBackground.png')
        gradeBg = p.transform.scale(gradeBg, (int(2*screenY/3),screenY))
        screen.blit(gradeBg,(screenY+1,0))
    #p.draw.rect(screen,0xaaaaaa,(0,0,int(screenX*2/3),screenY))

def displayMedia(student, fileno):
    template(2)
    media = student.files[fileno].media
    screen.blit(media,(int(screenY/2-(media.get_width()/2)), int(screenY/2-(media.get_height()/2))))

def displayFiles(student, fileno):
    template(3)
    for i in range(len(student.files)):
        introtext = p.font.Font('Fonts\KOMIKAX_.ttf', 15)
        if i==fileno:
            print("fart")
            
##################################################################################
########Test students
student1 = Student(4002,"Kyle","Sava")
fileimg = p.image.load('assets/runmean.png')
file1 = File(fileimg,"Runmean","fig")
student1.addfile(file1)
print(student1)
########
done = False  
template()
displayMedia(student1,0)
while not done:  
    for event in p.event.get():  
        if event.type == p.QUIT:  
            done = True  
        elif event.type == p.MOUSEMOTION:
            position=event.pos
            p.draw.rect(screen,(255,255,255),(position[0],position[1],20,20))
    p.display.flip()  