from graphics import *
import random

class MainWindow:
    
    def __init__(self,W,H):
        Win = GraphWin("Game Of Life", W*7, H*7)
        Win.setCoords(0,0,W+1,H+3)
        self.width = W
        self.height = H
        self.window = Win
        self.colors = [color_rgb(0,0,0),color_rgb(0,255,0)]
        self.debug = color_rgb(0,0,255)
        self.Rounds = 0
        Win.getMouse()
        

    def drawGrid(self,val):
        W = self.width
        H = self.height
        self.GridArray = []
        self.OldArray = []
        self.cellsAlive = 1
        for i in range(W):
            a = []
            for x in range(H):
                life = random.randint(0,val)
                if life == 1:
                    Rect = Rectangle(Point(x+1,i+1),Point(x+2,i))
                    Rect.setFill(self.colors[1])
                    Rect.draw(self.window)
                    a.append([i,x,1,Rect])
                else:
                    Rect = Rectangle(Point(x+1,i+1),Point(x+2,i))
                    Rect.setFill(self.colors[0])
                    Rect.draw(self.window)
                    a.append([i,x,0,Rect])
                    
            self.GridArray.append(a)
        self.T1 = Text(Point(self.width/2,self.height+1),"Simulations rounds run: " + str(self.Rounds) + " | Cells alive: " + str(self.cellsAlive))
        self.T1.draw(self.window) 
    
    
    def check(self,a,old):
        for i in range(len(a)):
            Count = 0
            Obj = a[i]
            VRow = a[i][0]
            HRow = a[i][1]
            #print VRow,HRow
            for w in range(-1,2):
                for h in range(-1,2):
                    if not VRow+w < 0 and not VRow+w > self.height-1 and not HRow+h < 0 and not HRow+h > self.width-1:
                        C = self.OldArray[VRow+w][HRow+h]
                        if Obj[3] != C[3]:
                            if C[2] == 1:
                                Count = Count+1
                            

            Alive = old[i][2]
            if Alive == 1:
                if Count < 2 or Count > 3:
                    Obj[3].setFill(self.colors[0])
                    Obj[2] = 0
                else:
                    if Count == 2 or Count == 3:
                        Obj[3].setFill(self.colors[1])
                        Obj[2] = 1

            if Alive == 0:
                if Count == 3:
                    Obj[3].setFill(self.colors[1])
                    Obj[2] = 1
                    
    def isAlive(self):
        CountA = 0
        for i in range(len(self.GridArray)):
            for x in range(len(self.GridArray[i])):
                CountA = CountA+self.GridArray[i][x][2]

        self.cellsAlive = CountA                    
    
    def startSim(self):
        self.Rounds = 0
        while self.cellsAlive > 0:
            self.T1.setText("Simulations rounds run: " + str(self.Rounds) + " | Cells alive: " + str(self.cellsAlive))
            self.isAlive()
            self.OldArray = self.GridArray
            self.Rounds = self.Rounds + 1
            for i in range(len(self.GridArray)):
                self.check(self.GridArray[i],self.OldArray[i])



Start = input("Please state start value")
Window = MainWindow(80,80)
Window.drawGrid(Start)
Window.startSim()

