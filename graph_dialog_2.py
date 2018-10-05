# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Graph_plot_Dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
import numpy as np

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

class Ui_Dialog_2(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(788, 424)
        self.Reserv_Name = QtGui.QLineEdit(Dialog)
        self.Reserv_Name.setGeometry(QtCore.QRect(400, 50, 231, 20))
        self.Reserv_Name.setObjectName(_fromUtf8("Reserv_Name"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 50, 291, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.Time = QtGui.QLineEdit(Dialog)
        self.Time.setGeometry(QtCore.QRect(400, 190, 231, 20))
        self.Time.setObjectName(_fromUtf8("XAxis"))
        self.YAxis = QtGui.QLineEdit(Dialog)
        self.YAxis.setGeometry(QtCore.QRect(400, 250, 231, 20))
        self.YAxis.setObjectName(_fromUtf8("YAxis"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(120, 190, 211, 21))
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
        self.pushButton.clicked.connect(self.graph_plot)
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

    def for_reservoir(self,x,y,z,a,b):
        import pandas as pd
        import numpy as np
        if x==204 or x=='Badger' or x=='badger' or x=='Badger Lake' or x=='Badger lake' or x=='badger lake' or x=='BADGER LAKE' or x=='BADGER':
            df=pd.read_excel("Badger Reservoir(Number 204)\\Book3_Final.xlsx")
            df1=pd.read_excel("Badger Reservoir(Number 204)\\Book4_Final.xlsx")
            df2=pd.read_excel("Badger Reservoir(Number 204)\\Book5_Final.xlsx")
            k=7
        elif x==212 or x=='Chain Lakes' or x=='Chain' or x=='chain lakes' or x=='chain' or x=='Chain Lakes Reservoir' or x=='chain lakes reservoir' or x=='Chain lakes reservoir' or x=='CHAIN LAKES RESERVOIR' or x=='CHAIN LAKES':
            df=pd.read_excel("Chain Lakes (Number 212)\\Book3_Final.xlsx")
            df1=pd.read_excel("Chain Lakes (Number 212)\\Book4_Final.xlsx")
            df2=pd.read_excel("Chain Lakes (Number 212)\\Book5_Final.xlsx")
            k=6
        elif x==225 or x=='Chestermere Lake' or x=='Chestermere' or x=='chestermere lake' or x=='chestermere' or x=='CHESTERMERE LAKE' or x=='CHESTERMERE':
            df=pd.read_excel("Chestermere Lake (Number 225)\\Book3_Final.xlsx")
            df1=pd.read_excel("Chestermere Lake (Number 225)\\Book4_Final.xlsx")
            df2=pd.read_excel("Chestermere Lake (Number 225)\\Book5_Final.xlsx")
            k=8
        elif x==223 or x=='Cowoki Lake' or x=='cowoki' or x=='Cowoki' or x=='cowoki lake' or x=='COWOKI LAKE' or x=='COWOKI':
            df=pd.read_excel("Cowoki Lake (Number 223)\\Book3_Final.xlsx")
            df1=pd.read_excel("Cowoki Lake (Number 223)\\Book4_Final.xlsx")
            df2=pd.read_excel("Cowoki Lake (Number 223)\\Book5_Final.xlsx")
            k=6
        elif x==218 or x=='Crawling Valley' or x=='crawling valley' or x=='Crawling Valley Reservoir' or x=='crawling valley reservoir' or x=='Crawling valley reservoir' or x=='CRAWLING VALLEY RESERVOIR' or x=='CRAWLING VALLEY':
            df=pd.read_excel("Crawling Valley (Number 218)\\Book3_Final.xlsx")
            df1=pd.read_excel("Crawling Valley (Number 218)\\Book4_Final.xlsx")
            df2=pd.read_excel("Crawling Valley (Number 218)\\Book5_Final.xlsx")
            k=6
        elif x==215 or x=='Oldman Reservoir' or x=='Oldman reservoir' or x=='oldman reservoir' or x=='oldman' or x=='OLDMAN RESERVOIR' or x=='OLDMAN' or x=='Oldman':
            df=pd.read_excel("Oldman Reservoir(Number 215)\\Book3_Final.xlsx")
            df1=pd.read_excel("Oldman Reservoir(Number 215)\\Book4_Final.xlsx")
            df2=pd.read_excel("Oldman Reservoir(Number 215)\\Book5_Final.xlsx")
            k=10
        #if x==227 or x=='Duchess':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Duchess Reservoir( Number 227)\\Book3_Final.xlsx")
        elif x==205 or x=='Keho Lake' or x=='keho lake' or x=='Keho' or x=='keho' or x=='Keho lake' or x=='KEHO' or x=='KEHO LAKE':
            df=pd.read_excel("Keho Lake (Number 205)\\Book3_Final.xlsx")
            df1=pd.read_excel("Keho Lake (Number 205)\\Book4_Final.xlsx")
            df2=pd.read_excel("Keho Lake (Number 205)\\Book5_Final.xlsx")
            k=6
        elif x==220 or x=='Kitsim' or x=='kitsim' or x=='Kitsim reservoir' or x=='kitsim reservoir' or x=='Kitsim Reservoir' or x=='KITSIM' or x=='KITSIM RESERVOIR':
            df=pd.read_excel("Kitsim Reservoir (Number 220)\\Book3_Final.xlsx")
            df1=pd.read_excel("Kitsim Reservoir (Number 220)\\Book4_Final.xlsx")
            df2=pd.read_excel("Kitsim Reservoir (Number 220)\\Book5_Final.xlsx")
            k=7
        elif x==221 or x=='Newell' or x=='newell' or x=='Lake Newell' or x=='lake newell' or x=='newell lake' or x=='Lake newell' or x=='Newell Lake' or x=='Newell lake' or x=='NEWELL' or x=='NEWELL LAKE' or x=='LAKE NEWELL':
            df=pd.read_excel("Lake Newell (Number 221)\\Book3_Final.xlsx")
            df1=pd.read_excel("Lake Newell (Number 221)\\Book4_Final.xlsx")
            df2=pd.read_excel("Lake Newell (Number 221)\\Book5_Final.xlsx")
            k=10
        elif x==59 or x=='Langdon' or x=='langdon' or x=='Langdon Exp' or x=='Langdon exp' or x=='langdon exp' or x=='LANGDON' or x=='LANGDON EXP':
            df=pd.read_excel("Langdon Exp (NUmber 59)\\Book3_Final.xlsx")
            df1=pd.read_excel("Langdon Exp (NUmber 59)\\Book4_Final.xlsx")
            df2=pd.read_excel("Langdon Exp (NUmber 59)\\Book5_Final.xlsx")
            k=7
        elif x==252 or x=='Little Bow' or x=='Little bow' or x=='little bow' or x=='Little Bow Reservoir' or x=='little bow reservoir' or x=='Little Bow reservoir' or x=='Little bow  reservoir' or x=='LITTLE BOW RESERVOIR' or x=='LITTLE BOW':
            df=pd.read_excel("Little Bow Reservoir(Number 252)\\Book3_Final.xlsx")
            df1=pd.read_excel("Little Bow Reservoir(Number 252)\\Book4_Final.xlsx")
            df2=pd.read_excel("Little Bow Reservoir(Number 252)\\Book5_Final.xlsx")
            k=6
        elif x==226 or x=='Lost Lake' or x=='lost lake' or x=='Lost lake' or x=='lost' or x=='Lost' or x=='LOST LAKE' or x=='LOST':
            k=7
            df=pd.read_excel("Lost Lake(number 226)\\Book3_Final.xlsx")
            df1=pd.read_excel("Lost Lake(number 226)\\Book4_Final.xlsx")
            df2=pd.read_excel("Lost Lake(number 226)\\Book5_Final.xlsx")

        elif x==202 or x=="Mcgregor's Lake" or x=="McGregor's lake" or x=="Mcgregor's lake" or x=="mcgregor's lake" or x=="McGregor's" or x=="Mcgregor's"  or x=='McGregors Lake' or x=='McGregors lake' or x=='Mcgregors lake' or x=='mcgregors lake' or x=='mcgregors' or x=='Mcgregors' or x=='McGregors' or x=='MCGREGOR' or x=="McGregor's Lake" or x=='MCGREGORS LAKE' or x=="MCGREGOR'S LAKE" or x=='McGREGORS LAKE' or x=="McGREGOR'S LAKE" or x=="McGREGOR'S" or x=='MCGREGOR' or x=="MCGREGOR'S":
            df=pd.read_excel("McGregor's Lake(Number 202)\\Book3_Final.xlsx")
            df1=pd.read_excel("McGregor's Lake(Number 202)\\Book4_Final.xlsx")
            df2=pd.read_excel("McGregor's Lake(Number 202)\\Book5_Final.xlsx")
            k=7
        elif x==216 or x=='Pine Coulee' or x=='Pine coulee' or x=='pine coulee' or x=='Pine Coulee Reservoir' or x=='Pine Coulee reservoir' or x=='Pine coulee reservoir' or x=='pine coulee reservoir' or x=='PINE COULEE' or x=='PINE COULEE RESERVOIR':
            df=pd.read_excel("Pine Coulee Reservoir (Number 216)\\Book3_Final.xlsx")
            df1=pd.read_excel("Pine Coulee Reservoir (Number 216)\\Book4_Final.xlsx")
            df2=pd.read_excel("Pine Coulee Reservoir (Number 216)\\Book5_Final.xlsx")
            k=8
        #if x==219 or x=='Rock Lake' or x=='Rock lake' or x=='rock lake' or x=='Rock' or x=='rock':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Rock Lake (Number 219)\\Book3_Final.xlsx")
        elif x==225 or x=='Scope Reservoir' or x=='Scope reservoir' or x=='scope reservoir' or x=='scope' or x=='Scope' or x=='SCOPE' or x=='SCOPE RESERVOIR':
            df=pd.read_excel("Scope Reservoir(Number 255)\\Book3_Final.xlsx")
            df1=pd.read_excel("Scope Reservoir(Number 255)\\Book4_Final.xlsx")
            df2=pd.read_excel("Scope Reservoir(Number 255)\\Book5_Final.xlsx")
            k=6
        #if x==222 or x=='Snake Lake' or x=='Snake lake' or x=='snake lake' or x=='Snake' or x=='snake':
            #df=pd.read_excel("D:\\SUMMER INTERNSHIP CONCORDIA\\Updated Work here\\Snake Lake(Number 222)\\Book3_Final.xlsx")
        elif x==224 or x=='Tilley B' or x=='Tilley b reservoir' or x=='Tilley B Reservoir' or x=='Tilley B reservoir' or x=='tilley b reservoir' or x=='Tilley b' or x=='tilley b' or x=='TILLEY B' or x=='TILLEY B RESERVOIR':
            df=pd.read_excel("Tilley B Reservoir (Number 224)\\Book3_Final.xlsx")
            df1=pd.read_excel("Tilley B Reservoir (Number 224)\\Book4_Final.xlsx")
            df2=pd.read_excel("Tilley B Reservoir (Number 224)\\Book5_Final.xlsx")
            k=6
        elif x==203 or x=='Travers' or x=='travers' or x=='Travers Reservoir' or x=='Travers reservoir' or x=='travers reservoir' or x=='TRAVERS' or x=='TRAVERS RESERVOIR':
            df=pd.read_excel("Travers Reservoir(Number 203)\\Book3_Final.xlsx")
            df1=pd.read_excel("Travers Reservoir(Number 203)\\Book4_Final.xlsx")
            df2=pd.read_excel("Travers Reservoir(Number 203)\\Book5_Final.xlsx")
            k=8
            
        elif x==266 or x=='Buffalo' or x=='buffalo' or x=='Buffalo Lake' or x=='Buffalo lake' or x=='buffalo lake' or x=='BUFFALO' or x=='BUFFALO LAKE':
            df=pd.read_excel("Buffalo Lake(number 266)\\Book3_Final.xlsx")
            df1=pd.read_excel("Buffalo Lake(number 266)\\Book4_Final.xlsx")
            df2=pd.read_excel("Buffalo Lake(number 266)\\Book5_Final.xlsx")
            k=6
        elif x==57 or x=='Bruce' or x=='bruce' or x=='Bruce Reservoir' or x=='Bruce reservoir' or x=='bruce reservoir' or x=='BRUCE' or x=='BRUCE RESERVOIR' or x=='BRUCE LAKE' or x=='Bruce Lake' or x=='bruce lake':
            df=pd.read_excel("Bruce Reservoir(Number 57)\\Book3_Final.xlsx")
            df1=pd.read_excel("Bruce Reservoir(Number 57)\\Book4_Final.xlsx")
            df2=pd.read_excel("Bruce Reservoir(Number 57)\\Book5_Final.xlsx")
            k=7
        elif x==266 or x=='Glennifer Lake' or x=='Glennifer lake' or x=='glennifer lake' or x=='Glennifer' or x=='glennifer' or x=='GLENNIFER' or x=='GLENNIFER LAKE':
            df=pd.read_excel("Buffalo Lake(number 266)\\Book3_Final.xlsx")
            df1=pd.read_excel("Buffalo Lake(number 266)\\Book4_Final.xlsx")
            df2=pd.read_excel("Buffalo Lake(number 266)\\Book5_Final.xlsx")
            k=6
        else:
            self.w=QtGui.QWidget()
            self.abc=QtGui.QMessageBox.critical(self.w, "Message", "Please Enter a valid Reservoir Name/ID")


        df_new=pd.DataFrame()
        
        if b=='INFLOW' and a=='WEEKLY':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k+1].values
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            #df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            df_new.columns=['Year','Month','Day']
            df_new=df_new.assign(Date=pd.to_datetime(df_new))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='OUTFLOW' and a=='WEEKLY':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k+3].values
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            #df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            df_new.columns=['Year','Month','Day']
            df_new=df_new.assign(Date=pd.to_datetime(df_new))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='ELEVATION' and a=='WEEKLY':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k+2].values
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            #df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            df_new.columns=['Year','Month','Day']
            df_new=df_new.assign(Date=pd.to_datetime(df_new))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='EVAPORATION' and a=='WEEKLY':
            array1=df.iloc[(52*(y-1928)):(52*(z-1928)),k].values
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            #df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1928)),0:3]])
            df_new.columns=['Year','Month','Day']
            df_new=df_new.assign(Date=pd.to_datetime(df_new))
            df4=np.asarray(df_new.Date.apply(str))
            

        elif b=='INFLOW' and a=='MONTHLY':
            array1=df1.iloc[(12*(y-1928)):(12*(z-1928)),k].values
            df_new2=pd.DataFrame()
            df_new2=pd.concat([df_new2,df1.iloc[(12*(y-1928)):(12*(z-1928)),0:2]])
            df_new2.columns=['Year','Month']
            df_new = df_new.assign(Date=pd.to_datetime(df_new2[['Year', 'Month']].assign(day=1)))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='OUTFLOW' and a=='MONTHLY':
            array1=df1.iloc[(12*(y-1928)):(12*(z-1928)),k+2].values
            df_new2=pd.DataFrame()
            df_new2=pd.concat([df_new2,df1.iloc[(12*(y-1928)):(12*(z-1928)),0:2]])
            df_new2.columns=['Year','Month']
            df_new = df_new.assign(Date=pd.to_datetime(df_new2[['Year', 'Month']].assign(day=1)))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='ELEVATION' and a=='MONTHLY':
            array1=df1.iloc[(12*(y-1928)):(12*(z-1928)),k+1].values
            df_new2=pd.DataFrame()
            df_new2=pd.concat([df_new2,df1.iloc[(12*(y-1928)):(12*(z-1928)),0:2]])
            df_new2.columns=['Year','Month']
            df_new = df_new.assign(Date=pd.to_datetime(df_new2[['Year', 'Month']].assign(day=1)))
            df4=np.asarray(df_new.Date.apply(str))
        elif b=='EVAPORATION' and a=='MONTHLY':
            array1=df1.iloc[(12*(y-1928)):(12*(z-1928)),k-1].values
            df_new2=pd.DataFrame()
            df_new2=pd.concat([df_new2,df1.iloc[(12*(y-1928)):(12*(z-1928)),0:2]])
            df_new2.columns=['Year','Month']
            df_new = df_new.assign(Date=pd.to_datetime(df_new2[['Year', 'Month']].assign(day=1)))
            df4=np.asarray(df_new.Date.apply(str))

        elif b=='INFLOW' and a=='YEARLY':
            array1=df2.iloc[(1*(y-1928)):(1*(z-1928)),k-1].values
            df_new=df2.iloc[(1*(y-1928)):(1*(z-1928)),0].values
            df4=df_new.copy()
        elif b=='OUTFLOW' and a=='YEARLY':
            array1=df2.iloc[(1*(y-1928)):(1*(z-1928)),k+1].values
            df_new=df2.iloc[(1*(y-1928)):(1*(z-1928)),0].values
            df4=df_new.copy()
        
        elif b=='ELEVATION' and a=='YEARLY':
            array1=df2.iloc[(1*(y-1928)):(1*(z-1928)),k].values
            df_new=df2.iloc[(1*(y-1928)):(1*(z-1928)),0].values
            df4=df_new.copy()
        
        elif b=='EVAPORATION' and a=='YEARLY' :
            array1=df2.iloc[(1*(y-1928)):(1*(z-1928)),k-2].values
            df_new=df2.iloc[(1*(y-1928)):(1*(z-1928)),0].values
            df4=df_new.copy()

        else:
            self.w1=QtGui.QWidget()
            self.abc1=QtGui.QMessageBox.critical(self.w1, "Message", "Please Check your response for Response Blocks 4 & 5. Also make sure your entries are in Capital Letters. ")

        

       # if b=='Inflow':
         #   array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k].values
      #  if b=='Outflow':
     #       array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k+2].values
     #   if b=='Storage':
     #       array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k+1].values
     #   if b=='Evaporation':
     #       array2=df.iloc[(52*(y-1928)):(52*(z-1928)),k-1].values

        #print(type(array1))
       # print(type(array2))
        #print(array1)

      # df1=pd.DataFrame[df.iloc[:,0],df.iloc[:,1],df.iloc[:,2]]

        #app= QtGui.QApplication(sys.argv)
        df4dict=dict(enumerate(df4))
        self.win = pg.GraphicsWindow()
        self.stringaxis = pg.AxisItem(orientation='bottom')
        self.stringaxis.setTicks([df4dict.items()])
        self.plot = self.win.addPlot(axisItems={'bottom': self.stringaxis})
        self.curve = self.plot.plot(list(df4dict.keys()),array1)


        if b=='INFLOW':# and a=='WEEKLY':
            self.plot.setLabel('left', "Inflow (in m3/sec)")# units='A')
        #self.plotwin.setLabel('bottom', "Northing")
        elif b=='OUTFLOW':# and a=='WEEKLY':
            self.plot.setLabel('left', "Outflow (in m3/sec)")# units='A')
        #self.plotwin.setLabel('bottom', "Northing")
            
        elif b=='ELEVATION':# and a=='WEEKLY':
            self.plot.setLabel('left', "Elevation (in m)")
            
        elif b=='EVAPORATION':# and a=='WEEKLY':
            self.plot.setLabel('left', "Evaporation (in m3/sec)")
            
    

        
            

        #self.widget=pg.PlotWidget(title='Graph Plot')
        #self.widget.setWindowTitle("Plotting Window")
        #self.widget.plotItem.plot(array1,df_new3)
        #self.widget.show()

        #sys.exit(app.exec_())

    def graph_plot(self):
        a=self.Reserv_Name.text()
        b=int(self.Start_Year.text())
        c=int(self.End_Year.text())
        d=self.Time.text()
        e=self.YAxis.text()
        self.for_reservoir(a,b,c,d,e)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Reservoir Name/Reservoir SCF ID</span></p></body></html>", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">WEEKLY/MONTHLY/YEARLY</span></p></body></html>", None))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Y-Axis</span></p><p><br/></p></body></html>", None))
        self.label_4.setText(_translate("Dialog", "Note: The available options for Y Axis are: ELEVATION, EVAPORATION, INFLOW and OUTFLOW ", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.label_5.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the Start Year</span></p></body></html>", None))
        self.label_6.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600;\">Enter the End Year</span></p><p><br/></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog_2()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

