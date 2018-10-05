# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graph_plot_Dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(788, 424)
        self.Reserv_Name = QtGui.QLineEdit(Dialog)
        self.Reserv_Name.setGeometry(QtCore.QRect(400, 50, 231, 20))
        self.Reserv_Name.setObjectName(_fromUtf8("Reserv_Name"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 291, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.XAxis = QtGui.QLineEdit(Dialog)
        self.XAxis.setGeometry(QtCore.QRect(400, 190, 231, 20))
        self.XAxis.setObjectName(_fromUtf8("XAxis"))
        self.YAxis = QtGui.QLineEdit(Dialog)
        self.YAxis.setGeometry(QtCore.QRect(400, 250, 231, 20))
        self.YAxis.setObjectName(_fromUtf8("YAxis"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(180, 190, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(180, 250, 111, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(170, 320, 491, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(360, 360, 81, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(160, 90, 141, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(170, 140, 131, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.End_Year = QtGui.QLineEdit(Dialog)
        self.End_Year.setGeometry(QtCore.QRect(400, 140, 231, 20))
        self.End_Year.setObjectName(_fromUtf8("End_Year"))
        self.Start_Year = QtGui.QLineEdit(Dialog)
        self.Start_Year.setGeometry(QtCore.QRect(400, 90, 231, 20))
        self.Start_Year.setObjectName(_fromUtf8("Start_Year"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Reservoir Name/Reservoir SCF ID</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the X-Axis</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Y-Axis</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "Note: The available options for X and Y Axis are: Storage, Evaporation, Inflow and Outflow ", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Start Year</span></p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the End Year</span></p><p><br/></p></body></html>", None))

    def for_reservoir(self,x,y,z,a,b):
        import pandas as pd
        import numpy as np
        if x==204 or x=='Badger' or x=='badger' or x=='Badger Lake' or x=='Badger lake' or x=='badger lake' or x=='BADGER LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Badger Reservoir(Number 204)\\Book3_Final.xlsx")
            k=7
        if x==212 or x=='Chain Lakes' or x=='Chain' or x=='chain lakes' or x=='chain' or x=='Chain Lakes Reservoir' or x=='chain lakes reservoir' or x=='Chain lakes reservoir' or x=='CHAIN LAKES RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Chain Lakes (Number 212)\\Book3_Final.xlsx")
            k=6
        if x==225 or x=='Chestermere Lake' or x=='Chestermere' or x=='chestermere lake' or x=='chestermere' or x=='CHESTERMERE LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Chestermere Lake (Number 225)\\Book3_Final.xlsx")
            k=8
        if x==223 or x=='Cowoki Lake' or x=='cowoki' or x=='Cowoki' or x=='cowoki lake' or x=='COWOKI LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Cowoki Lake (Number 223)\\Book3_Final.xlsx")
            k=6
        if x==218 or x=='Crawling Valley' or x=='crawling valley' or x=='Crawling Valley Reservoir' or x=='crawling valley reservoir' or x=='Crawling valley reservoir' or x=='CRAWLING VALLEY RESERVOIR' or x=='CRAWLING VALLEY':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Crawling Valley (Number 218)\\Book3_Final.xlsx")
            k=6
        if x==215 or x=='Oldman Reservoir' or x=='Oldman reservoir' or x=='oldman reservoir' or x=='oldman' or x=='OLDMAN RESERVOIR' or x=='OLDMAN':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Oldman Reservoir(Number 215)\\Book3_Final.xlsx")
            k=10
        #if x==227 or x=='Duchess':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Duchess Reservoir( Number 227)\\Book3_Final.xlsx")
        if x==205 or x=='Keho Lake' or x=='keho lake' or x=='Keho' or x=='keho' or x=='Keho lake' or x=='KEHO' or x=='KEHO LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Keho Lake (Number 205)\\Book3_Final.xlsx")
            k=5
        if x==220 or x=='Kitsim' or x=='kitsim' or x=='Kitsim reservoir' or x=='kitsim reservoir' or x=='Kitsim Reservoir' or x=='KITSIM' or x=='KITSIM RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Kitsim Reservoir (Number 220)\\Book3_Final.xlsx")
            k=7
        if x==221 or x=='Newell' or x=='newell' or x=='Lake Newell' or x=='lake newell' or x=='newell lake' or x=='Lake newell' or x=='Newell Lake' or x=='Newell lake' or x=='NEWELL' or x=='NEWELL LAKE' or x=='LAKE NEWELL':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Lake Newell (Number 221)\\Book3_Final.xlsx")
            k=10
        if x==59 or x=='Langdon' or x=='langdon' or x=='Langdon Exp' or x=='Langdon exp' or x=='langdon exp' or x=='LANGDON' or x=='LANGDON EXP':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Langdon Exp (NUmber 59)\\Book3_Final.xlsx")
            k=7
        if x==252 or x=='Little Bow' or x=='Little bow' or x=='little bow' or x=='Little Bow Reservoir' or x=='little bow reservoir' or x=='Little Bow reservoir' or x=='Little bow  reservoir' or x=='LITTLE BOW RESERVOIR' or x=='LITTLE BOW':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Little Bow Reservoir(Number 252)\\Book3_Final.xlsx")
            k=6
        if x==226 or x=='Lost Lake' or x=='lost lake' or x=='Lost lake' or x=='lost' or x=='Lost' or x=='LOST LAKE' or x=='LOST':
            k=7
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Lost Lake(number 226)\\Book3_Final.xlsx") 
        if x==202 or x=="Mcgregor's Lake" or x=="McGregor's lake" or x=="Mcgregor's lake" or x=="mcgregor's lake" or x=="McGregor's" or x=="Mcgregor's"  or x=='McGregors Lake' or x=='McGregors lake' or x=='Mcgregors lake' or x=='mcgregors lake' or x=='mcgregors' or x=='Mcgregors' or x=='McGregors' or x=='MCGREGOR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\McGregor's Lake(Number 202)\\Book3_Final.xlsx")
            k=7
        if x==216 or x=='Pine Coulee' or x=='Pine coulee' or x=='pine coulee' or x=='Pine Coulee Reservoir' or x=='Pine Coulee reservoir' or x=='Pine coulee reservoir' or x=='pine coulee reservoir' or x=='PINE COULEE' or x=='PINE COULEE RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Pine Coulee Reservoir (Number 216)\\Book3_Final.xlsx")
            k=8
        #if x==219 or x=='Rock Lake' or x=='Rock lake' or x=='rock lake' or x=='Rock' or x=='rock':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Rock Lake (Number 219)\\Book3_Final.xlsx")
        if x==225 or x=='Scope Reservoir' or x=='Scope reservoir' or x=='scope reservoir' or x=='scope' or x=='Scope' or x=='SCOPE' or x=='SCOPE RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Scope Reservoir(Number 255)\\Book3_Final.xlsx")
            k=6
        #if x==222 or x=='Snake Lake' or x=='Snake lake' or x=='snake lake' or x=='Snake' or x=='snake':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Snake Lake(Number 222)\\Book3_Final.xlsx")
        if x==224 or x=='Tilley B' or x=='Tilley b reservoir' or x=='Tilley B Reservoir' or x=='Tilley B reservoir' or x=='tilley b reservoir' or x=='Tilley b' or x=='tilley b' or x=='TILLEY B' or x=='TILLEY B RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Tilley B Reservoir (Number 224)\\Book3_Final.xlsx")
            k=7
        if x==203 or x=='Travers' or x=='travers' or x=='Travers Reservoir' or x=='Travers reservoir' or x=='travers reservoir' or x=='TRAVERS' or x=='TRAVERS RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Travers Reservoir(Number 203)\\Book3_Final.xlsx")
            k=8
        if x==266 or x=='Buffalo' or x=='buffalo' or x=='Buffalo Lake' or x=='Buffalo lake' or x=='buffalo lake' or x=='BUFFALO' or x=='BUFFALO LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Buffalo Lake(number 266)\\Book3_Final.xlsx")
            k=6
        if x==57 or x=='Bruce' or x=='bruce' or x=='Bruce Reservoir' or x=='Bruce reservoir' or x=='bruce reservoir' or x=='BRUCE' or x=='BRUCE RESERVOIR':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Bruce Reservoir(Number 57)\\Book3_Final.xlsx")
            k=7
        if x==266 or x=='Glennifer Lake' or x=='Glennifer lake' or x=='glennifer lake' or x=='Glennifer' or x=='glennifer' or x=='GLENNIFER' or x=='GLENNIFER LAKE':
            df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Buffalo Lake(number 266)\\Book3_Final.xlsx")
            k=6

        
        if a=='Inflow':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k]].values
        if a=='Outflow':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k+2]].values
        if a=='Storage':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k+1]].values
        if a=='Evaporation':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k-1]].values

        if b=='Inflow':
            array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k]].values
        if b=='Outflow':
            array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k+2]].values
        if b=='Storage':
            array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k+1]].values
        if b=='Evaporation':
            array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k-1]].values

        app= QtGui.QApplication(sys.argv)
        widget=pg.PlotWidget(title='Graph Plot')
        widget.setWindowTitle("Plotting Window")
        widget.plotItem.plot(a,b)
        widget.show()

        sys.exit(app.exec_())

    def graph_plot(self):
        a=self.Reserv_Name.text()
        b=int(self.Start_Year.text())
        c=int(self.end_line.text())
        d=self.inflow_line.text()
        e=self.weekly_line.text()
        self.reservoir_id(a,b,c,d,e)
        
        
            
            

        



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

