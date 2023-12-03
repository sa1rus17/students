from tkinter import Tk, Canvas, ARC, W
 
 
class human():
    def __init__(self,canvas, name, x,y,gen):
        self.canvas=canvas
        self.name=name
        self.x=x
        self.y=y
        self.gen=gen
        
    def display(self):
        self.__drawName()
        self.__drawHead()
        self.__drawBody()
        self.__drawLegs()
        self.__drawHends()
        self.__drawEyes()
        
  
    def __drawName(self):
        self.canvas.create_text(self.x+25,self.y-220, text=self.name, anchor=W, font="Arial", fill="salmon")
        
    def __drawHead(self):
        self.canvas.create_oval(self.x+25, self.y-150, self.x+75, self.y-200, width=2)
        self.canvas.create_arc(self.x+40,self.y-155,self.x+60,self.y-175, start=0, extent=-180,style=ARC, outline="red", width=3)
        if self.gen=='м':
            self.canvas.create_line(self.x+35,self.y-200, self.x+30,self.y-210)
            self.canvas.create_line(self.x+50,self.y-200, self.x+50,self.y-215)
            self.canvas.create_line(self.x+65,self.y-200, self.x+70,self.y-210)
        else :
            self.canvas.create_line(self.x+25,self.y-175,self.x+10,self.y-150)
            self.canvas.create_line(self.x+75,self.y-175,self.x+90,self.y-150)
        
    def __drawBody(self):
        self.canvas.create_line(self.x+50, self.y-50, self.x+50, self.y-150, width=2)
    
    def __drawLegs(self):
        self.canvas.create_line(self.x,self.y, self.x+50,self.y-50,self.x+100,self.y, width=3)        
    def __drawHends(self):
        self.canvas.create_line(self.x,self.y-100, self.x+50, self.y-150,self.x+100,self.y-100, width=2)
        
    def __drawEyes(self):
        self.canvas.create_oval(self.x+40, self.y-180, self.x+40, self.y-180, width=2),
        self.canvas.create_oval(self.x+60, self.y-180, self.x+60, self.y-180, width=2)
       

