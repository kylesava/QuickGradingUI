import pygame as p
import math
from studentobj import Student,File
  
p.init()  
programIcon = p.image.load('assets/icon.png')

p.display.set_caption('QuickGrader')  
p.display.set_icon(programIcon)
screenY = 1200
screenX = int(screenY*5/3)
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
    introtext = p.font.Font('assets\Paul.ttf', int(7*screenY/180))
    for i in range(len(student.files)):
        color = (255,255,255)
        if i==fileno:
            color= (40,255,100)
        screen.blit(introtext.render(student.files[i].name,True,color),(int((920/1500)*screenX),int((64/900)*screenY)+int(7*screenY/180)*i))

def displayStudents(studentlist, stuno):
    for i in range(len(studentlist)):
        introtext = p.font.Font('assets\Paul.ttf', int(screenY/30))
        color = (255,255,255)
        if i==stuno:
            color= (40,255,100)
        screen.blit(introtext.render(studentlist[i].fname+ " "+studentlist[i].lname+", "+str(studentlist[i].number),True,color),(int((1257/1500)*screenX),int((42/900)*screenY)+int(screenY/30)*i))
        
            
##################################################################################
########Test students
student1 = Student(4002,"Kyle","Sava")
fileimg = p.image.load('assets/runmean.png')
file1 = File(fileimg,"Runmean.png","fig")
file2img = p.image.load('assets/lab06_slope.png')
file2 = File(file2img,"Slope.png","fig")
student1.addfile(file1)
student1.addfile(file2)
########
done = False  
template()

studentlist=[]
studentlist.append(student1)
studentlist.append(student1)
activestudent=0
displayMedia(student1,0)
displayFiles(student1, 0)
displayStudents(studentlist,activestudent)
while not done:  
    for event in p.event.get():  
        if event.type == p.QUIT:  
            done = True  
        elif event.type == p.MOUSEBUTTONDOWN:
            position=event.pos
            if position[0]<(1215/1500)*screenX and position[0]>screenY and position[1]>(64/900)*screenY and position[1]<(320/900)*screenY:
                if math.floor((position[1]-int((64/900)*screenY))/(7*screenY/180))<len(studentlist[activestudent].files):
                    displayFiles(studentlist[activestudent],math.floor((position[1]-int((64/900)*screenY))/(7*screenY/180)))
                    displayMedia(studentlist[activestudent],math.floor((position[1]-int((64/900)*screenY))/(7*screenY/180)))
                    displayStudents(studentlist,activestudent)
    p.display.flip()  