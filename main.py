import  sys
from numpy.polynomial import Polynomial
from sympy import *
import matplotlib.pyplot as plt
import numpy
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import  QIcon
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from ui import Ui_MainWindow

class Calk(QtWidgets.QMainWindow):
    def __init__(self):
        super(Calk, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
    def init_UI(self):
        self.setWindowTitle("Калькулятор ПВП и КВП")
        self.setWindowIcon(QIcon('ads.png'))
        self.ui.buttonKVP.clicked.connect(self.i2)
        self.ui.buttonKVP.clicked.connect(self.i1)
        self.ui.buttonKVP.clicked.connect(self.i3)
        self.ui.buttonKVP.clicked.connect(self.k)
        self.ui.buttonKVP.clicked.connect(self.type)
        self.ui.buttonKVP.clicked.connect(self.centr)
        self.ui.buttonKVP.clicked.connect(self.resh_KVP)
        self.ui.buttonPVP.clicked.connect(self.ii1)
        self.ui.buttonPVP.clicked.connect(self.ii2)
        self.ui.buttonPVP.clicked.connect(self.ii3)
        self.ui.buttonPVP.clicked.connect(self.ii4)
        self.ui.buttonPVP.clicked.connect(self.center)
        self.ui.buttonPVP.clicked.connect(self.typee)
        self.ui.buttonPVP.clicked.connect(self.resh_PVP)
        self.ui.buttonPVP.clicked.connect(self.k2k3)
        self.ui.buttonPVP.clicked.connect(self.graf)

    def i1(self):
        c=Calk()
        a1= float(self.ui.a1.text())
        a3 = float(self.ui.a3.text())
        i1_KVP=a1+a3
        self.ui.i1_KVP.setText(str(i1_KVP))
    def i2(self):
        c=Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        i2_KVP=round(a1*a3-a2*a2/4,2)
        self.ui.i2_KVP.setText(str(i2_KVP))
    def i3(self):
        c=Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        a4 = float(self.ui.a4.text())
        a5 = float(self.ui.a5.text())
        a6 = float(self.ui.a6.text())
        i3_KVP=round(a1*a3*a6+a2*a5*a4/4-a3*a4**2/4-a2**2*a6/4-a1*a5**2/4,2)
        self.ui.i3_KVP.setText(str(i3_KVP))

    def k(self):
        c = Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        a4 = float(self.ui.a4.text())
        a5 = float(self.ui.a5.text())
        a6 = float(self.ui.a6.text())
        k_KVP = a1*a6-a4*a4/4+a3*a6-a5*a5/4
        self.ui.k_KVP.setText(str(k_KVP))
    def type(self):
        c = Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        a4 = float(self.ui.a4.text())
        a5 = float(self.ui.a5.text())
        a6 = float(self.ui.a6.text())
        i1_KVP = a1+a3
        i2_KVP = a1 * a3 - a2 * a2 / 4
        i3_KVP = a1 * a3 * a6 + a2 * a5 * a4 / 4 - a3 * a4 ** 2 / 4 - a2 ** 2 * a6 / 4 - a1 * a5 ** 2 / 4
        k_KVP = a1 * a6 + a4 * a4 / 4 + a3 * a6 - a5 * a5 ** 2 / 4
        if i2_KVP!=0:
            if i2_KVP>0:
                if i1_KVP*i3_KVP>0:
                    self.ui.type_KVP.setText(str("Эллипс"))
                if i3_KVP==0:
                    self.ui.type_KVP.setText(str("Точка"))
                if i2_KVP*i3_KVP<0:
                    self.ui.type_KVP.setText(str("Эллипс"))

            if i2_KVP<0:
                if i3_KVP!=0:
                    self.ui.type_KVP.setText(str("Гиппербола"))
                else:
                    self.ui.type_KVP.setText(str("Пересек. прямые"))
        else:
            if i3_KVP!=0:
                self.ui.type_KVP.setText(str("Парабола"))
            else:
                if k_KVP>0:
                    self.ui.type_KVP.setText(str("Мним. парал. прямые"))
                if k_KVP<0:
                    self.ui.type_KVP.setText(str("Парал. прямые"))
                else:
                    self.ui.type_KVP.setText(str("Совпадающ. прямые"))

    def centr(self):
        c = Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        a4 = float(self.ui.a4.text())
        a5 = float(self.ui.a5.text())
        a6 = float(self.ui.a6.text())
        i2_KVP = a1 * a3 - a2 * a2 / 4
        if i2_KVP!=0:
            M1 = numpy.array([[a1, a2 / 2], [a2 / 2, a3]])
            V1 = numpy.array([a4 / 2, a5 / 2])
            centr_KVP = numpy.linalg.solve(M1, V1)
            for i in range(0, 2):
                centr_KVP[i] = round(centr_KVP[i], 2)
            self.ui.centr_KVP.setText(str(centr_KVP))
        else:
            self.ui.centr_KVP.setText(str('Центра нет'))
    def resh_KVP(self):
        c = Calk()
        a1 = float(self.ui.a1.text())
        a2 = float(self.ui.a2.text())
        a3 = float(self.ui.a3.text())
        a4 = float(self.ui.a4.text())
        a5 = float(self.ui.a5.text())
        a6 = float(self.ui.a6.text())
        i1_KVP = a1+a3
        i2_KVP = a1 * a3 - a2 * a2 / 4
        i3_KVP = a1 * a3 * a6 + a2 * a5 * a4 / 4 - a3 * a4 ** 2 / 4 - a2 ** 2 * a6 / 4 - a1 * a5 ** 2 / 4

        lam1=(i1_KVP-(i1_KVP**2-4*i2_KVP)**0.5)/2
        lam2 = (i1_KVP +(i1_KVP ** 2 - 4 * i2_KVP) ** 0.5) / 2
        if (lam1!=0 and lam2!=0):
            resh_KVP = str(numpy.round(lam1,2))+'*x^2+'+str(numpy.round(lam2,2))+"*y^2+"+str(numpy.round(i3_KVP/i2_KVP,2))+"=0"
            self.ui.resh_KVP.setText(str(resh_KVP))
            var('x y')
            plot_implicit(Eq(a1 * x ** 2 + a2 * x*y+a3*y**2+a4*x+a5*y+a6, 0),(x, -10, 10), (y, -10, 10))
        else:
            if lam1!=0:
                T=numpy.round((i3_KVP/-lam1)**0.5,1)
                resh_KVP=str(numpy.round(lam1,1))+"*y^2+"+str(2*T)+"*x=0"
                self.ui.resh_KVP.setText(str(resh_KVP))
                if i1_KVP ** 2 - 4 * i2_KVP > 0:
                    var('x y')
                    plot_implicit(Eq(a1 * x ** 2 + a2 * x*y+a3*y**2+a4*x+a5*y+a6, 0),(x, -10, 10), (y, -10, 10))
                else:
                    var('x y')
                    plot_implicit(Eq(x ** 2 + y ** 2, -2),(x, -10, 10), (y, -10, 10))
            if lam2!=0:
                T = numpy.round((i3_KVP / -lam2) ** 0.5,1)
                resh_KVP = str(numpy.round(lam2,1))+ "*y^2+" + str(2 * T) + "*x=0"
                self.ui.resh_KVP.setText(str(resh_KVP))
                if i1_KVP ** 2 - 4 * i2_KVP > 0:
                    var('x y')
                    plot_implicit(Eq(a1 * x ** 2 + a2 * x*y+a3*y**2+a4*x+a5*y+a6, 0),(x, -10, 10), (y, -10, 10))
                else:
                    var('x y')
                    plot_implicit(Eq(x ** 2 + y ** 2, -2),(x, -10, 10), (y, -10, 10))
            if lam1==lam2==0:
                resh_KVP =  str(a3) + "*y^2+" + str(a5) + "*x+"+str(a5) + "*y=" + str(-a5)
                self.ui.resh_KVP.setText(str(resh_KVP))
                var('x y')
                plot_implicit(Eq(a1 * x ** 2 + a2 * x*y+a3*y**2+a4*x+a5*y+a6, 0),(x, -10, 10), (y, -10, 10))

    def ii1(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        i1_PVP=round(a11+a12+a13,2)
        self.ui.i1_PVP.setText(str(i1_PVP))
    def ii2(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i2_PVP=a11*a12-a14**2/4+a11*a13-a15**2/4+a12*a13-a16**2/4
        i2_PVP=round(i2_PVP,2)
        self.ui.i2_PVP.setText(str(i2_PVP))

    def ii3(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i3_PVP = a11 * a12 *a13+a14*a16*a15/4-a15**2/4*a12-a14**2/4*a13-a16**2/4*a11
        i3_PVP = round(i3_PVP, 2)
        self.ui.i3_PVP.setText(str(i3_PVP))

    def ii4(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        A = np.array([[a11,a14/2,a15/2,a17/2],[a14/2,a12,a16/2,a18/2],[a15/2,a16/2,a13,a19/2],[a17/2,a18/2,a19/2,a20]])
        i4_PVP = round(np.linalg.det(A), 2)
        self.ui.i4_PVP.setText(str(i4_PVP))
    def center(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i1_PVP = a11 + a12 + a13
        i2_PVP = a11 * a12 - a14 ** 2 / 4 + a11 * a13 - a15 ** 2 / 4 + a12 * a13 - a16 ** 2 / 4
        i3_PVP = a11 * a12 * a13 + a14 * a16 * a15 / 4 - a15 ** 2 / 4 * a12 - a14 ** 2 / 4 * a13 - a16 ** 2 / 4 * a11
        A = np.array([[a11, a14 / 2, a15 / 2, a17 / 2], [a14 / 2, a12, a16 / 2, a18 / 2], [a15 / 2, a16 / 2, a13, a19 / 2],[a17 / 2, a18 / 2, a19 / 2, a20]])
        i4_PVP = np.linalg.det(A)
        if i3_PVP != 0:
            M1 = numpy.array([[a11, a14 / 2, a15 / 2], [a14 / 2, a12, a16 / 2], [a15 / 2, a16 / 2, a13]])
            V1 = numpy.array([a17 / 2, a18 / 2, a19 / 2])
            centr_PVP = numpy.linalg.solve(M1, V1)
            for i in range(0, 3):
                centr_PVP[i] = round(centr_PVP[i], 2)
            self.ui.centr_PVP.setText(str(centr_PVP))
        else:
            self.ui.centr_PVP.setText(str('Центра нет'))

    def typee(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i1_PVP = a11 + a12 + a13
        i2_PVP = a11 * a12 - a14 ** 2 / 4 + a11 * a13 - a15 ** 2 / 4 + a12 * a13 - a16 ** 2 / 4
        i3_PVP = a11 * a12 * a13 + a14 * a16 * a15 / 4 - a15 ** 2 / 4 * a12 - a14 ** 2 / 4 * a13 - a16 ** 2 / 4 * a11
        A = np.array([[a11, a14 / 2, a15 / 2, a17 / 2], [a14 / 2, a12, a16 / 2, a18 / 2], [a15 / 2, a16 / 2, a13, a19 / 2],[a17 / 2, a18 / 2, a19 / 2, a20]])
        i4_PVP = np.linalg.det(A)
        k4=i4_PVP
        k2=np.linalg.det(np.array([[a11,a17/2],[a17/2, a20]]))+np.linalg.det(np.array([[a12,a18/2],[a18/2, a20]]))+np.linalg.det(np.array([[a13,a19/2],[a19/2, a20]]))
        k3=np.linalg.det(np.array([[a11,a14/2,a17/2],[a14/2,a12,a18/2],[a17/2,a18/2,a20]]))+np.linalg.det(np.array([[a11,a15/2,a17/2],[a15/2,a13,a18/2],[a17/2,a19/2,a20]]))+np.linalg.det(np.array([[a12,a16/2,a18/2],[a16/2,a13,a19/2],[a18/2,a19/2,a20]]))
        a = 1
        b = -i1_PVP
        c = i2_PVP
        d = -i3_PVP
        x = Polynomial([d, c, b, a])
        if i3_PVP!=0:
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0):
                self.ui.type_PVP.setText(str("Эллипсоид"))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP>0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP<0):
                self.ui.type_PVP.setText(str("Мнимый эллипсоид"))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP == 0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP==0):
                self.ui.type_PVP.setText(str("Мнимый конус"))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP<0 or x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0 or x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP>0 or x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0 or x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0):
                self.ui.type_PVP.setText(str("Однополосный гиперболоид"))
            if (x.roots()[0]>0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP/i3_PVP>0 or x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP/i3_PVP>0 or x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]>0 and i4_PVP/i3_PVP>0 or x.roots()[0]<0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP/i3_PVP<0 or x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP/i3_PVP<0 or x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]<0 and i4_PVP/i3_PVP<0):
                self.ui.type_PVP.setText(str("Двуполосный гиперболоид"))
            if (x.roots()[0]>0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP==0 or x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP==0 or x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]>0 and i4_PVP==0 or x.roots()[0]<0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP==0 or x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP==0 or x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]<0 and i4_PVP==0):
                self.ui.type_PVP.setText(str("Конус"))
        if i3_PVP==0 and i2_PVP!=0 and i4_PVP!=0:
            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]>0 or x.roots()[1]==0 and x.roots()[0]*x.roots()[2]>0 or x.roots()[2]==0 and x.roots()[1]*x.roots()[0]>0):
                self.ui.type_PVP.setText(str("Эллептический параболоид"))
            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]<0 or x.roots()[1]==0 and x.roots()[0]*x.roots()[2]<0 or x.roots()[2]==0 and x.roots()[1]*x.roots()[0]<0):
                self.ui.type_PVP.setText(str("Гиперболический параболоид"))
        if i3_PVP==i4_PVP==0 and i2_PVP!=0:
            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]>0 and k3/i2_PVP<0 or x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]<0 and k3/i2_PVP>0 or x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]>0 and k3/i2_PVP<0 or x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]<0 and k3/i2_PVP>0 or x.roots()[2] == 0 and x.roots()[0] > 0 and x.roots()[1] > 0 and k3 / i2_PVP < 0 or x.roots()[2] == 0 and x.roots()[0] < 0 and x.roots()[1] < 0 and k3 / i2_PVP > 0):
                self.ui.type_PVP.setText(str("Эллиптический цилиндр"))
            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]>0 and k3/i2_PVP>0 or x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]<0 and k3/i2_PVP<0 or x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]>0 and k3/i2_PVP>0 or x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]<0 and k3/i2_PVP<0 or x.roots()[2] == 0 and x.roots()[0] > 0 and x.roots()[1] > 0 and k3 / i2_PVP > 0 or x.roots()[2] == 0 and x.roots()[0] < 0 and x.roots()[1] < 0 and k3 / i2_PVP < 0):
                self.ui.type_PVP.setText(str("Мнимый эллиптический цилиндр"))
            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]>0 and k3==0 or x.roots()[1]==0 and x.roots()[0]*x.roots()[2]>0 and k3==0 or x.roots()[2]==0 and x.roots()[1]*x.roots()[0]>0 and k3==0):
                self.ui.type_PVP.setText(str("Мнимые пересекающиеся пл-ти"))
            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]<0 and k3!=0 or x.roots()[1]==0 and x.roots()[0]*x.roots()[2]<0 and k3!=0 or x.roots()[2]==0 and x.roots()[1]*x.roots()[0]<0 and k3!=0):
                self.ui.type_PVP.setText(str("Гиперболический цилиндр"))
            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]<0 and k3==0 or x.roots()[1]==0 and x.roots()[0]*x.roots()[2]<0 and k3==0 or x.roots()[2]==0 and x.roots()[1]*x.roots()[0]<0 and k3==0):
                self.ui.type_PVP.setText(str("Пересекающиеся пл-ти"))
        if i3_PVP==i4_PVP==i2_PVP==0 and k3!=0:
            self.ui.type_PVP.setText(str("Параболический цилиндр"))
        if i3_PVP==i4_PVP==i2_PVP==k3==0:
            if k2<0:
                self.ui.type_PVP.setText(str("Параллельные пл-ти"))
            if k2>0:
                self.ui.type_PVP.setText(str("Мнимые параллельные пл-ти"))
            if k2==0:
                self.ui.type_PVP.setText(str("Совпадающие пл-ти"))
    def resh_PVP(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i1_PVP = a11 + a12 + a13
        i2_PVP = a11 * a12 - a14 ** 2 / 4 + a11 * a13 - a15 ** 2 / 4 + a12 * a13 - a16 ** 2 / 4
        i3_PVP = a11 * a12 * a13 + a14 * a16 * a15 / 4 - a15 ** 2 / 4 * a12 - a14 ** 2 / 4 * a13 - a16 ** 2 / 4 * a11
        A = np.array([[a11, a14 / 2, a15 / 2, a17 / 2], [a14 / 2, a12, a16 / 2, a18 / 2], [a15 / 2, a16 / 2, a13, a19 / 2],[a17 / 2, a18 / 2, a19 / 2, a20]])
        i4_PVP = np.linalg.det(A)
        k4 = i4_PVP
        k2 = np.linalg.det(np.array([[a11, a17 / 2], [a17 / 2, a20]])) + np.linalg.det(np.array([[a12, a18 / 2], [a18 / 2, a20]])) + np.linalg.det(np.array([[a13, a19 / 2], [a19 / 2, a20]]))
        k3 = np.linalg.det(np.array([[a11, a14 / 2, a17 / 2], [a14 / 2, a12, a18 / 2], [a17 / 2, a18 / 2, a20]])) + np.linalg.det(np.array([[a11, a15 / 2, a17 / 2], [a15 / 2, a13, a18 / 2], [a17 / 2, a19 / 2, a20]])) + np.linalg.det(np.array([[a12, a16 / 2, a18 / 2], [a16 / 2, a13, a19 / 2], [a18 / 2, a19 / 2, a20]]))
        a = 1
        b = -i1_PVP
        c = i2_PVP
        d = -i3_PVP
        x = Polynomial([d, c, b, a])

        if i3_PVP!=0:
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0):
                a=-x.roots()[0]*i3_PVP/i4_PVP
                b=-x.roots()[1]*i3_PVP/i4_PVP
                c=-x.roots()[2]*i3_PVP/i4_PVP
                resh_PVP = str(round(a,1))+"*x^2+" +str(round(b,1))+ "*y^2+" + str(round(c,1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP>0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP<0):
                a=x.roots()[0] * i3_PVP / i4_PVP
                b=x.roots()[1] * i3_PVP / i4_PVP
                c=x.roots()[2] * i3_PVP / i4_PVP
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2+" + str(round(c,1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP == 0 or x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP==0):
                a=abs(x.roots()[0])
                b=abs(x.roots()[1])
                c=abs(x.roots()[2])
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2+" + str(round(c,1)) + "*z^2 = 0"
                self.ui.type_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] > 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP<0 ):
                a = -x.roots()[0] * i3_PVP / i4_PVP
                b = -x.roots()[1] * i3_PVP / i4_PVP
                c = x.roots()[2] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0 ):
                a = -x.roots()[0] * i3_PVP / i4_PVP
                b = -x.roots()[2] * i3_PVP / i4_PVP
                c = x.roots()[1] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP<0):
                a = -x.roots()[1] * i3_PVP / i4_PVP
                b = -x.roots()[2] * i3_PVP / i4_PVP
                c = x.roots()[0] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP/i3_PVP>0):
                a = -x.roots()[0] * i3_PVP / i4_PVP
                b = -x.roots()[1] * i3_PVP / i4_PVP
                c = x.roots()[2] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0):
                a = -x.roots()[0] * i3_PVP / i4_PVP
                b = -x.roots()[2] * i3_PVP / i4_PVP
                c = x.roots()[1] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP/i3_PVP>0):
                a=-x.roots()[1] * i3_PVP / i4_PVP
                b=-x.roots()[2] * i3_PVP / i4_PVP
                c=x.roots()[0] * i3_PVP / i4_PVP
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2-" + str(round(c,1)) + "*z^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]>0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP/i3_PVP>0):
                a=-x.roots()[0] * i3_PVP / i4_PVP
                b=-x.roots()[1] * i3_PVP / i4_PVP
                c=x.roots()[2] * i3_PVP / i4_PVP
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2-" + str(round(c,1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP / i3_PVP > 0):
                a =-x.roots()[0] * i3_PVP / i4_PVP
                b =-x.roots()[2] * i3_PVP / i4_PVP
                c =x.roots()[1] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] > 0 and i4_PVP / i3_PVP > 0 ):
                a =-x.roots()[1] * i3_PVP / i4_PVP
                b =-x.roots()[2] * i3_PVP / i4_PVP
                c =x.roots()[0] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] < 0 and x.roots()[2] > 0 and i4_PVP / i3_PVP < 0 ):
                a =-x.roots()[0] * i3_PVP / i4_PVP
                b =-x.roots()[1] * i3_PVP / i4_PVP
                c =x.roots()[2] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] < 0 and x.roots()[1] > 0 and x.roots()[2] < 0 and i4_PVP / i3_PVP < 0):
                a =-x.roots()[0] * i3_PVP / i4_PVP
                b =-x.roots()[2] * i3_PVP / i4_PVP
                c =x.roots()[1] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] > 0 and x.roots()[1] < 0 and x.roots()[2] < 0 and i4_PVP / i3_PVP < 0):
                a =-x.roots()[1] * i3_PVP / i4_PVP
                b =-x.roots()[2] * i3_PVP / i4_PVP
                c =x.roots()[0] * i3_PVP / i4_PVP
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]>0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP==0):
                a =abs(x.roots()[0])
                b =abs(x.roots()[1])
                c =abs(x.roots()[2])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP==0 ):
                a =abs(x.roots()[0])
                b =abs(x.roots()[2])
                c =abs(x.roots()[1])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]>0 and i4_PVP==0 ):
                a =abs(x.roots()[1])
                b =abs(x.roots()[2])
                c =abs(x.roots()[0])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]<0 and x.roots()[1]<0 and x.roots()[2]>0 and i4_PVP==0 ):
                a =abs(x.roots()[0])
                b =abs(x.roots()[1])
                c =abs(x.roots()[2])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]<0 and x.roots()[1]>0 and x.roots()[2]<0 and i4_PVP==0):
                a =abs(x.roots()[0])
                b =abs(x.roots()[2])
                c =abs(x.roots()[1])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2-" + str(round(c, 1)) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]>0 and x.roots()[1]<0 and x.roots()[2]<0 and i4_PVP==0):
                a=abs(x.roots()[1])
                b=abs(x.roots()[2])
                c=abs(x.roots()[0])
                resh_PVP = str(abs(x.roots()[1])) + "*x^2+" + str(abs(x.roots()[2])) + "*y^2-" + str(abs(x.roots()[0])) + "*z^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))

        if i3_PVP==0 and i2_PVP!=0 and i4_PVP!=0:
            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]>0):
                a=-x.roots()[1]*sqrt(-i2_PVP/i4_PVP)
                b=-x.roots()[2]*sqrt(-i2_PVP/i4_PVP)
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0] == 0 and x.roots()[1] < 0 and x.roots()[2] < 0):
                a =x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                b =x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]>0):
                a =-x.roots()[0]*sqrt(-i2_PVP/i4_PVP)
                b =-x.roots()[2]*sqrt(-i2_PVP/i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1] == 0 and x.roots()[0] < 0 and x.roots()[2] < 0):
                a =x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                b =x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]>0 and x.roots()[0]>0):
                a =-x.roots()[1]*sqrt(-i2_PVP/i4_PVP)
                b =-x.roots()[0]*sqrt(-i2_PVP/i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2] == 0 and x.roots()[1] < 0 and x.roots()[0] < 0):
                a=x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                b=x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]<0):
                a =x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                b =x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]>0):
                a =x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]<0):
                a =x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]>0):
                a =x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]>0 and x.roots()[0]<0):
                a =x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]<0 and x.roots()[0]>0):
                a =x.roots()[0] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]<0):
                a =x.roots()[1] * sqrt(-i2_PVP / i4_PVP)
                b =-x.roots()[2] * sqrt(-i2_PVP / i4_PVP)
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 2z"
                resh_PVP = str(x.roots()[1] * sqrt(-i2_PVP / i4_PVP)) + "*x^2-" + str(-x.roots()[2] * sqrt(-i2_PVP / i4_PVP)) + "*y^2 = 2z"
                self.ui.resh_PVP.setText(str(resh_PVP))

        if i3_PVP==i4_PVP==0 and i2_PVP!=0:

            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]>0 and k3/i2_PVP<0):
                a =-x.roots()[1]*i2_PVP/k3
                b =-x.roots()[2]*i2_PVP/k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]<0 and k3/i2_PVP>0):
                a =-x.roots()[1]*i2_PVP/k3
                b =-x.roots()[2]*i2_PVP/k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]>0 and k3/i2_PVP<0):
                a =-x.roots()[0]*i2_PVP/k3
                b =-x.roots()[2]*i2_PVP/k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]<0 and k3/i2_PVP>0):
                a =-x.roots()[0]*i2_PVP/k3
                b =-x.roots()[2]*i2_PVP/k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2] == 0 and x.roots()[0] > 0 and x.roots()[1] > 0 and k3 / i2_PVP < 0):
                a =-x.roots()[0]*i2_PVP/k3
                b =-x.roots()[1]*i2_PVP/k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2] == 0 and x.roots()[0] < 0 and x.roots()[1] < 0 and k3 / i2_PVP > 0):
                a=-x.roots()[0]*i2_PVP/k3
                b=-x.roots()[1]*i2_PVP/k3
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2 = 1"
                self.ui.resh_PVP.setText(str(resh_PVP))

            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]>0 and k3/i2_PVP>0):
                a =x.roots()[1] * i2_PVP / k3
                b =x.roots()[2] * i2_PVP / k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]<0 and k3/i2_PVP<0):
                a =x.roots()[1] * i2_PVP / k3
                b =x.roots()[2] * i2_PVP / k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]>0 and k3/i2_PVP>0):
                a =x.roots()[0] * i2_PVP / k3
                b =x.roots()[2] * i2_PVP / k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]<0 and k3/i2_PVP<0):
                a =x.roots()[0] * i2_PVP / k3
                b =x.roots()[2] * i2_PVP / k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2] == 0 and x.roots()[0] > 0 and x.roots()[1] > 0 and k3 / i2_PVP > 0):
                a =x.roots()[0] * i2_PVP / k3
                b =x.roots()[1] * i2_PVP / k3
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2] == 0 and x.roots()[0] < 0 and x.roots()[1] < 0 and k3 / i2_PVP < 0):
                a=x.roots()[0] * i2_PVP / k3
                b=x.roots()[1] * i2_PVP / k3
                resh_PVP = str(round(a,1)) + "*x^2+" + str(round(b,1)) + "*y^2 = -1"
                self.ui.resh_PVP.setText(str(resh_PVP))

            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]>0 and k3==0):
                a=abs(x.roots()[1])
                b=abs(x.roots()[2])
                resh_PVP = str(round(a,1)) + "*x^2+" + str(abs(round(b,1))) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]*x.roots()[2]>0 and k3==0):
                a = abs(x.roots()[0])
                b = abs(x.roots()[2])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]*x.roots()[0]>0 and k3==0):
                a = abs(x.roots()[1])
                b = abs(x.roots()[0])
                resh_PVP = str(round(a, 1)) + "*x^2+" + str(abs(round(b, 1))) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))

            if (x.roots()[0]==0 and x.roots()[1]*x.roots()[2]<0 and k3!=0):
                if (x.roots()[1]*k3/i2_PVP<0):
                    a=-x.roots()[1] * i2_PVP / k3
                    b=x.roots()[2] * i2_PVP / k3
                    resh_PVP = str(round(a,1)) + "*x^2-" + str(round(b,1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))
                if (x.roots()[2]*k3/i2_PVP<0):
                    a=-x.roots()[2] * i2_PVP / k3
                    b=x.roots()[1] * i2_PVP / k3
                    resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]*x.roots()[2]<0 and k3!=0):
                if (x.roots()[0] * k3 / i2_PVP < 0):
                    a =-x.roots()[0] * i2_PVP / k3
                    b =x.roots()[2] * i2_PVP / k3
                    resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))
                if (x.roots()[2] * k3 / i2_PVP < 0):
                    a =-x.roots()[2] * i2_PVP / k3
                    b =x.roots()[0] * i2_PVP / k3
                    resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]*x.roots()[0]<0 and k3!=0):
                if (x.roots()[1] * k3 / i2_PVP < 0):
                    a =-x.roots()[1] * i2_PVP / k3
                    b =x.roots()[0] * i2_PVP / k3
                    resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))
                if (x.roots()[0] * k3 / i2_PVP < 0):
                    a =-x.roots()[0] * i2_PVP / k3
                    b =x.roots()[1] * i2_PVP / k3
                    resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 1"
                    self.ui.resh_PVP.setText(str(resh_PVP))

            if (x.roots()[0]==0 and x.roots()[1]>0 and x.roots()[2]<0 and k3==0):
                a=x.roots()[1]
                b=-x.roots()[2]
                resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[0]==0 and x.roots()[1]<0 and x.roots()[2]>0 and k3==0):
                a=x.roots()[2]
                b=-x.roots()[1]
                resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]>0 and x.roots()[2]<0 and k3==0):
                a=x.roots()[0]
                b=-x.roots()[2]
                resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[1]==0 and x.roots()[0]<0 and x.roots()[2]>0 and k3==0):
                a=x.roots()[2]
                b=-x.roots()[0]
                resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]>0 and x.roots()[0]<0 and k3==0):
                a=x.roots()[1]
                b=-x.roots()[0]
                resh_PVP = str(round(a, 1)) + "*x^2-" + str(round(b, 1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if (x.roots()[2]==0 and x.roots()[1]<0 and x.roots()[0]>0 and k3==0):
                a=x.roots()[0]
                b=-x.roots()[1]
                resh_PVP = str(round(a,1)) + "*x^2-" + str(round(b,1)) + "*y^2 = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))

        if i3_PVP==i4_PVP==i2_PVP==0 and k3!=0:
            b=sqrt(-k3/i3_PVP**3)
            resh_PVP = "x^2 = 2*"+str(round(b,1)) + "*y"
            self.ui.resh_PVP.setText(str(resh_PVP))
        if i3_PVP==i4_PVP==i2_PVP==k3==0:
            if k2<0:
                c=sqrt(-k2 / i1_PVP ** 2)
                resh_PVP = "x^2 = " + str(round(c,1))
                self.ui.resh_PVP.setText(str(resh_PVP))
            if k2>0:
                c=sqrt(k2 / i1_PVP ** 2)
                resh_PVP = "x^2 + " + str(round(c,1))+" = 0"
                self.ui.resh_PVP.setText(str(resh_PVP))
            if k2==0:
                resh_PVP = "x^2 = 0 " 
                self.ui.resh_PVP.setText(str(resh_PVP))

    def k2k3(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())
        i1_PVP = a11 + a12 + a13
        i2_PVP = a11 * a12 - a14 ** 2 / 4 + a11 * a13 - a15 ** 2 / 4 + a12 * a13 - a16 ** 2 / 4
        i3_PVP = a11 * a12 * a13 + a14 * a16 * a15 / 4 - a15 ** 2 / 4 * a12 - a14 ** 2 / 4 * a13 - a16 ** 2 / 4 * a11
        A = np.array([[a11, a14 / 2, a15 / 2, a17 / 2], [a14 / 2, a12, a16 / 2, a18 / 2], [a15 / 2, a16 / 2, a13, a19 / 2],[a17 / 2, a18 / 2, a19 / 2, a20]])
        i4_PVP = np.linalg.det(A)
        k4 = i4_PVP
        k2 = np.linalg.det(np.array([[a11, a17 / 2], [a17 / 2, a20]])) + np.linalg.det(np.array([[a12, a18 / 2], [a18 / 2, a20]])) + np.linalg.det(np.array([[a13, a19 / 2], [a19 / 2, a20]]))
        k3 = np.linalg.det(np.array([[a11, a14 / 2, a17 / 2], [a14 / 2, a12, a18 / 2], [a17 / 2, a18 / 2, a20]])) + np.linalg.det(np.array([[a11, a15 / 2, a17 / 2], [a15 / 2, a13, a18 / 2], [a17 / 2, a19 / 2, a20]])) + np.linalg.det(np.array([[a12, a16 / 2, a18 / 2], [a16 / 2, a13, a19 / 2], [a18 / 2, a19 / 2, a20]]))
        self.ui.k_PVP.setText(str(round(k2,1))+" , "+str(round(k3,1)))


    def graf(self):
        c = Calk()
        a11 = float(self.ui.a11.text())
        a12 = float(self.ui.a12.text())
        a13 = float(self.ui.a13.text())
        a14 = float(self.ui.a14.text())
        a15 = float(self.ui.a15.text())
        a16 = float(self.ui.a16.text())
        a17 = float(self.ui.a17.text())
        a18 = float(self.ui.a18.text())
        a19 = float(self.ui.a19.text())
        a20 = float(self.ui.a20.text())

        # Создание сетки точек
        x = np.linspace(-5, 5, 100)
        y = np.linspace(-5, 5, 100)
        X, Y = np.meshgrid(x, y)

        # Вычисление Z-координат по уравнению поверхности
        Z = (-a11 * X ** 2 - a12 * Y ** 2 - a13 * (a20 + a17 * X + a18 * Y) - a14 * X * Y - a15 * X * (
                    a20 + a19 * Y) - a16 * (a20 + a18 * Y) * Y - a19 * X) / a13

        # Построение графика
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='coolwarm')
        ax.set_xlabel('X Label')
        ax.set_ylabel('Y Label')
        ax.set_zlabel('Z Label')
        plt.title('Surface Plot', fontsize=14)
        plt.show()

app = QtWidgets.QApplication([])

application = Calk()

application.show()

sys.exit(app.exec())

