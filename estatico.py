import sys
import tkinter
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton ,QLabel,QLineEdit
from PyQt5 import QtGui
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk




class Janela(QMainWindow):#Janela principal
    def __init__(self):
     super().__init__()
     self.topo =100
     self.esquerda =100
     self.largura=750
     self.altura =600
     self.titulo="Calculadora Estatica"
     self.stile= 'QMainWindow {background-color:#c9d2d4}'
     #Botao Calcular
     botao1 = QPushButton('Calcular',self)
     botao1.move(630,500)
     botao1.resize(80,40)
     botao1.setStyleSheet('QPushButton {background-color:#ECE5C7;font:bold;font-size:15px}')
     botao1.clicked.connect(self.botao1_click)
     
     #Botao Reset
     botao2 = QPushButton('Reset',self)
     botao2.move(530,500)
     botao2.resize(80,40)
     botao2.setStyleSheet('QPushButton {background-color:#ECE5C7 ;font:bold;font-size:15px}')
     botao2.clicked.connect(self.botao2_click)

     #Botao DCL
     botao3 = QPushButton("DCL",self)
     botao3.move(590,225)
     botao3.resize(80,40)
     botao3.setStyleSheet('QPushButton {background-color:#C2DED1;font:bold;font-size:15px}')
     botao3.clicked.connect(self.botao3_click)

     #Botao Instruções
     botao4 = QPushButton("Instruções",self)
     botao4.move(590,50)
     botao4.resize(100,40)
     botao4.setStyleSheet('QPushButton {background-color:#81F495;font:bold;font-size:15px}')
     botao4.clicked.connect(self.botao4_click) 
     
     
    
     self.label_1 = QLabel(self)
     self.label_1.setText("Informe as forças  :")
     self.label_1.move(250,1)
     self.label_1.resize(250,200)
     self.label_1.setStyleSheet('QLabel {font:italic;font-size:25px}')
    
     #self.label_1.setAlignment(QtCore.Qt.AlignCenter)

     self.label_2 = QLabel(self)
     self.label_2.setText("Determinação das reações nos suportes A e B"+"\n"+"para que a viga fique em equilíbrio.")
     self.label_2.move(100,350)
     self.label_2.setStyleSheet('QLabel {font:bold;font-size:20px;color:#354259}')
     self.label_2.resize(700,150)

     #Imagem 
     pilar = QLabel(self)
     pilar.move(90,100)
     pilar.setPixmap(QtGui.QPixmap('pilar.png'))
     pilar.resize(500,300)

     
     #Força X                        
     self.forca1 = QLineEdit(self)
     self.forca1.move(147,165)
     self.forca1.resize(70,30)
    
     #Força Y
     self.forca2 = QLineEdit(self)
     self.forca2.move(455,134)
     self.forca2.resize(70,30)

    

     self.CarregarJanela()
           
     
    def CarregarJanela(self):#Carrega a janela Principal
     self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
     self.setWindowTitle(self.titulo)
     self.setStyleSheet(self.stile)
     self.show() 

    def botao1_click(self):#Da valor as variaveis X e Y e calcula as forças e reações
        x = float(self.forca1.text())
        y = float(self.forca2.text())

        l1= int(3)
        l2= int(4) 
       
        z =(y-x)
        F1 = ((z)*l1)/2
        F2 = (z)*l1
        F3 = x*l2
        Fr = F1+F2+F3
       
        d1=(2/3*l1) + l2
        d2=(l2+((1/2)*l1))
        d3 = l2/2
        db = l1 + l2

        Nb = (F1*d1+F2*d2+F3*d3)/db

        Nay =(Fr-Nb)


        self.label_2.setText("\n"+"Resultado:"+"\n"+"Força resultante = "+str(Fr)+"N"+"\n"+"Reação em B: "+
        str('{:.2f}'.format(Nb))+"N"+"\n"+"Reação em A: " +str('{:.2f}'.format(Nay))+"N") 
        self.label_2.setStyleSheet('QLabel {font:arial;font-size:25px;color:"red"}')
                
    def botao2_click(self):#Zera as variaves   
        self.label_2.setText("Determinação das reações nos suportes A e B"+"\n"+"para que a viga fique em equilíbrio.") 
        self.label_2.setStyleSheet('QLabel {font:bold;font-size:20px;color:#354259}') 
        self.forca1.setText("")
        self.forca2.setText("")

    def botao3_click(self):#Abre uma janela para mostrar a DLC
      root = Tk()  
      canvas = Canvas(root, width = 600, height = 400)  
      canvas.pack()  
      img = ImageTk.PhotoImage(Image.open("DCL.png"))   
      canvas.create_image(20, 20, anchor=NW, image=img) 
      root.mainloop() 

    def botao4_click(self):#Abre uma janela de aviso com as instruções
      top = tkinter.Tk()
      top.geometry("150x150")
      messagebox.showwarning('Modo de uso :', 
      '- Escreva as forças nas caixas da imagem'+"\n"+
      '- Clique no botao CALCULAR para ver o resultado '+"\n"+
      '- Clique no botao DLC para ver imagem com as forças '+"\n"+
      '- Para calcular de novo aperte o botao RESET'+"\n"+
      '- Aperte OK para abrir o Programa'+"\n"+
      '- Feche a guia em branco para não haver erros no programa ')
      top.mainloop()
      
      
aplicacao = QApplication(sys.argv)
j=Janela()
sys.exit(aplicacao.exec_())








