import pygame as p
import random
screenX = 1500
screenY = 900
class File:
    def __init__(self, media, name, type, grade=0, reviewed=False):
        if media.get_width() >= media.get_height():
            self.media = p.transform.scale(media, (int(8*screenY/9),int(media.get_height()*((8*screenY/9)/media.get_width()))))   
        else:
            self.media = p.transform.scale(media, (int(media.get_width()*((8*screenY/9)/media.get_height())),int(8*screenY/9)))
        self.name = name
        self.type = type
        self.grade = random.randint(0,10)
        self.reviewed = reviewed
    
    def changegrade(self,grade):
        self.grade=grade
        self.reviewed=True


class Student:
    def __init__(self, number=0, fname="", lname=""):
        self.fname = fname
        self.lname = lname
        self.number = number
        self.files=[]
    def addfile(self,file):
        self.files.append(file)
    def getfiles(self):
        return self.files
    
 