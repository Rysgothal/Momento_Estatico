import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QPushButton , QToolTip , QLabel,QLineEdit
from PyQt5 import QtGui


class Janela(QMainWindow):
    def __init__(self):
     super().__init__()
     self.topo =100
     self.esquerda =100
     self.largura=800
     self.altura =600
     self.titulo="Calculadora Estatica"

     botao1 = QPushButton('Calcular',self)
     botao1.move(630,500)
     botao1.resize(80,40)
     botao1.setStyleSheet('QPushButton {background-color:#ECE5C7;font:bold;font-size:15px}')
     botao1.clicked.connect(self.botao1_click)
     

     botao2 = QPushButton('Reset',self)
     botao2.move(530,500)
     botao2.resize(80,40)
     botao2.setStyleSheet('QPushButton {background-color:#ECE5C7 ;font:bold;font-size:15px}')
     botao2.clicked.connect(self.botao2_click)

     botao3 = QPushButton("DCL",self)
     botao3.move(630,300)
     botao3.resize(80,40)
     botao3.setStyleSheet('QPushButton {background-color:#C2DED1;font:bold;font-size:15px}')
     
     
    
    # self.label_1 = QLabel(self)
     #self.label_1.setText("Bem Vindo!")
     #self.label_1.move(250,1)
     #self.label_1.resize(250,200)
     #self.label_1.setStyleSheet('QLabel {font:arial;font-size:20px}')
    
     #self.label_1.setAlignment(QtCore.Qt.AlignCenter)

     self.label_2 = QLabel(self)
     self.label_2.setText("Determinação das reações nos suportes A e B"+"\n"+"para que a viga fique em equilíbrio.")
     self.label_2.move(80,350)
     self.label_2.setStyleSheet('QLabel {font:bold;font-size:20px;color:#354259}')
     self.label_2.resize(700,150)

     pilar = QLabel(self)
     pilar.move(200,100)
     pilar.setPixmap(QtGui.QPixmap('pilar2.png'))
     pilar.resize(400,300)

     
                             
     '''self.forca1 = QLineEdit(self)
     self.forca1.move(100,175)
    


     self.forca2 = QLineEdit(self)
     self.forca2.move(590,150)
     '''

     self.CarregarJanela()
    
   

       

    def CarregarJanela(self):
     self.setGeometry(self.esquerda,self.topo,self.largura,self.altura)
     self.setWindowTitle(self.titulo)
     self.show() 

    

    def botao1_click(self):
        x = int(400)
        y = int(200)
        l1= int(3)
        l2= int(4) 
        #x = self.forca1.text()
        #y= self.forca2.text()

        F1 = ((x-y)*l1)/2
        F2 = (x-y)*l1
        F3 = y*l2
        Fr = F1+F2+F3

        d1=(2/3*l1) + l2
        d2=(l2+((1/2)*l1))
        d3 = l2/2
        db = l1 + l2

        Nb = (F1*d1+F2*d2+F3*d3)/db

        Nay =(Fr-Nb)

        self.label_2.setText("Resultado:"+"\n"+"Força resultante = "+str(Fr)+"N"+"\n"+"Reação em B: "+
        str('{:.2f}'.format(Nb))+"N"+"\n"+"Reação em A: " +str('{:.2f}'.format(Nay))+"N") 
        self.label_2.setStyleSheet('QLabel {font:arial;font-size:25px;color:"red"}')  


    def botao2_click(self):   
        self.label_2.setText("Determinação das reações nos suportes A e B"+"\n"+" para que a viga fique em equilíbrio.") 
        self.label_2.setStyleSheet('QLabel {font:bold;font-size:20px;color:#354259}') 
    
    






aplicacao = QApplication(sys.argv)
j=Janela()
sys.exit(aplicacao.exec_())








