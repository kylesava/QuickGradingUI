import pygame as p
import math
from studentobj import Student,File
  
p.init()  
programIcon = p.image.load('assets/icon.png')

p.display.set_caption('QuickGrader')  
p.display.set_icon(programIcon)
screenY = 900
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
    media = student.files[fileno].media
    screen.blit(media,(int(screenY/2-(media.get_width()/2)), int(screenY/2-(media.get_height()/2))))

def displayFiles(student, fileno):
    introtext = p.font.Font('assets\Paul.ttf', int(7*screenY/180))
    for i in range(len(student.files)):
        color = (255,255,255)
        if i==fileno:
            color= (40,255,100)
        screen.blit(introtext.render(student.files[i].name,True,color),(int((920/1500)*screenX),int((64/900)*screenY)+int(7*screenY/180)*i))
        if student.files[i].reviewed:
            screen.blit(introtext.render("D",True,(100,255,110)),(int((1190/1500)*screenX),int((64/900)*screenY)+int(7*screenY/180)*i))

def displayStudents(studentlist, stuno):
    for i in range(len(studentlist)):
        introtext = p.font.Font('assets\Paul.ttf', int(screenY/30))
        color = (255,255,255)
        if i==stuno:
            color= (40,255,100)
        screen.blit(introtext.render(studentlist[i].fname+ " "+studentlist[i].lname+", "+str(studentlist[i].number),True,color),(int((1257/1500)*screenX),int((42/900)*screenY)+int(screenY/30)*i))

def displayGrade(student, fileno):
    introtext = p.font.Font('assets\Paul.ttf', int(screenY/5))
    gradecols=[(242,15,15),(219,60,24),(219,86,24),(219,128,24),(219,174,24),(219,219,24),(197,219,24),(177,219,24),(148,219,24),(89,219,24),(0,255,0)]
    color = gradecols[student.files[fileno].grade]
    screen.blit(introtext.render(str(student.files[fileno].grade),True,color),(int(screenX*1332/1500),int(screenY*334/900)))


def fullUpdate(stulist, stunum, filenum):
    template(6)
    displayFiles(stulist[stunum],filenum)
    displayMedia(stulist[stunum],filenum)
    displayStudents(stulist,stunum)
    displayGrade(stulist[stunum],filenum)
##################################################################################
########Test students
student1 = Student(4002,"Kyle","Sava")
fileimg = p.image.load('assets/runmean.png')
file1 = File(fileimg,"Runmean.png","fig")
file2img = p.image.load('assets/lab06_slope.png')
file2 = File(file2img,"Slope.png","fig")
student1.addfile(file1)
student1.addfile(file2)

student2 = Student(8293,"Francis","Doe")
file2img = p.image.load('assets/fig1.png')
file12 = File(file2img,"Speeds.png","fig")
file2img2 = p.image.load('assets/fig2.png')
file22 = File(file2img2,"FlyBy.png","fig")
file2img3 = p.image.load('assets/fig3.png')
file32 = File(file2img3,"Crash.png","fig")
student2.addfile(file12)
student2.addfile(file22)
student2.addfile(file32)
########
done = False  
template()

studentlist=[]
studentlist.append(student1)
studentlist.append(student2)
activestudent=0
currentfile=0
while not done:  
    for event in p.event.get():  
        if event.type == p.QUIT:  
            done = True  
        elif event.type == p.MOUSEBUTTONDOWN:
            position=event.pos
            if position[0]<(1215/1500)*screenX and position[0]>screenY and position[1]>(64/900)*screenY and position[1]<(320/900)*screenY:
                if math.floor((position[1]-int((64/900)*screenY))/(7*screenY/180))<len(studentlist[activestudent].files):
                    currentfile = math.floor((position[1]-int((64/900)*screenY))/(7*screenY/180))
            elif  position[0]>(1237/1500)*screenX and position[1]>(42/900)*screenY and position[1]<(270/900)*screenY:
                if math.floor((position[1]-int((42/900)*screenY))/(screenY/30))<len(studentlist):
                    activestudent=math.floor((position[1]-int((42/900)*screenY))/(screenY/30))
                    currentfile=0
            elif position[0]>(975/1500)*screenX and position[0]<(1427/1500)*screenX and position[1]>(582/900)*screenY and position[1]<(691/900)*screenY:
                studentlist[activestudent].files[currentfile].reviewed = True
                if currentfile < len(studentlist[activestudent].files)-1:
                    currentfile+=1
            elif position[0]>(975/1500)*screenX and position[0]<(1427/1500)*screenX and position[1]>(720/900)*screenY and position[1]<(828/900)*screenY:
                studentlist[activestudent].files[currentfile].grade = 10
                studentlist[activestudent].files[currentfile].reviewed = True
                if currentfile < len(studentlist[activestudent].files)-1:
                    currentfile+=1
            print(position)
    fullUpdate(studentlist, activestudent, currentfile)
    p.display.flip()  