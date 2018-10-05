# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Input_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pandas as pd

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
        Dialog.resize(779, 550)
        self.start_line = QtGui.QLineEdit(Dialog)
        self.start_line.setGeometry(QtCore.QRect(440, 210, 113, 20))
        self.start_line.setObjectName(_fromUtf8("start_line"))
        self.end_line = QtGui.QLineEdit(Dialog)
        self.end_line.setGeometry(QtCore.QRect(440, 260, 113, 20))
        self.end_line.setObjectName(_fromUtf8("end_line"))
        self.inflow_line = QtGui.QLineEdit(Dialog)
        self.inflow_line.setGeometry(QtCore.QRect(440, 320, 113, 20))
        self.inflow_line.setObjectName(_fromUtf8("inflow_line"))
        self.weekly_line = QtGui.QLineEdit(Dialog)
        self.weekly_line.setGeometry(QtCore.QRect(440, 370, 113, 20))
        self.weekly_line.setObjectName(_fromUtf8("weekly_line"))
        self.start_label = QtGui.QLabel(Dialog)
        self.start_label.setGeometry(QtCore.QRect(280, 210, 81, 20))
        self.start_label.setObjectName(_fromUtf8("start_label"))
        self.end_label = QtGui.QLabel(Dialog)
        self.end_label.setGeometry(QtCore.QRect(300, 260, 91, 20))
        self.end_label.setObjectName(_fromUtf8("end_label"))
        self.inflow_label = QtGui.QLabel(Dialog)
        self.inflow_label.setGeometry(QtCore.QRect(160, 320, 281, 20))
        self.inflow_label.setObjectName(_fromUtf8("inflow_label"))
        self.weekly_label = QtGui.QLabel(Dialog)
        self.weekly_label.setGeometry(QtCore.QRect(250, 370, 170, 20))
        self.weekly_label.setObjectName(_fromUtf8("weekly_label"))
        self.heading = QtGui.QLabel(Dialog)
        self.heading.setGeometry(QtCore.QRect(290, 50, 261, 91))
        self.heading.setObjectName(_fromUtf8("heading"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(350, 450, 101, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.printInput)
        self.nameOFreservoir = QtGui.QLabel(Dialog)
        self.nameOFreservoir.setGeometry(QtCore.QRect(150, 170, 211, 20))
        self.nameOFreservoir.setObjectName(_fromUtf8("nameOFreservoir"))
        self.start_line_2 = QtGui.QLineEdit(Dialog)
        self.start_line_2.setGeometry(QtCore.QRect(440, 170, 113, 20))
        self.start_line_2.setObjectName(_fromUtf8("start_line_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        
    def reservoir_id(self,x,y,z,a,b):
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
        #df=df.reset_index(drop=True, inplace=True)

       # sys.__stdout__=sys.stdout
       # print(df.iloc[(52*(y-1928)):(52*(z-1928)),k])

        
        if a=='INFLOW' and b=='WEEKLY':
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),0:3]])
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),k+1]],axis=1)
            df_new=df_new.reset_index(drop=True)   
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")
            #df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
            #df_new.iloc[:,2:]=df.iloc[y:z,k]
            #print(df.iloc[y:z,k])
        elif a=='OUTFLOW' and b=='WEEKLY':
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),0:3]])
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),k+3]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+2]
        elif a=='ELEVATION' and b=='WEEKLY':
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),0:3]])
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),k+2]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+1]
        elif a=='RAW DATA' and b=='WEEKLY':
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),0:3]])
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),3:k+1]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,2:k]
        elif a=='ALL' and b=='WEEKLY':
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),0:3]])
            df_new=pd.concat([df_new,df.iloc[(52*(y-1928)):(52*(z-1927)),3:]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

            

        elif a=='INFLOW' and b=='MONTHLY':
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),0:2]])
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),k]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")
            #df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
            #df_new.iloc[:,2:]=df.iloc[y:z,k]
            #print(df.iloc[y:z,k])
        elif a=='OUTFLOW' and b=='MONTHLY':
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),0:2]])
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),k+2]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+2]
        elif a=='ELEVATION' and b=='MONTHLY':
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),0:2]])
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),k+1]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+1]
        elif a=='RAW DATA' and b=='MONTHLY':
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),0:2]])
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),2:k]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,2:k]
        elif a=='ALL' and b=='MONTHLY':
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),0:2]])
            df_new=pd.concat([df_new,df1.iloc[(12*(y-1928)):(12*(z-1927)),2:]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")



        elif a=='INFLOW' and b=='YEARLY':
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),0:1]])
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),k-1]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")
            #df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
            #df_new.iloc[:,2:]=df.iloc[y:z,k]
            #print(df.iloc[y:z,k])
        elif a=='OUTFLOW' and b=='YEARLY':
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),0:1]])
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),k+1]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+2]
        elif a=='ELEVATION' and b=='YEARLY':
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),0:1]])
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),k]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,k+1]
        elif a=='RAW DATA' and b=='YEARLY':
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),0:1]])
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),1:k-1]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,2:k]
        elif a=='ALL' and b=='YEARLY':
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),0:1]])
            df_new=pd.concat([df_new,df2.iloc[(1*(y-1928)):(1*(z-1927)),1:]],axis=1)
            df_new=df_new.reset_index(drop=True) 
            df_new.to_excel("OUTPUT_RESULT.xlsx")
            self.w2=QtGui.QWidget()
            self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

            

        else:
            self.w1=QtGui.QWidget()
            self.abc1=QtGui.QMessageBox.critical(self.w1, "Message", "Please Check your resposes and make sure OUTPUT_RESULT.xlsx is closed.")

           # df_new.iloc[:,0:1]=df.iloc[y:z,0:1]
           # df_new.iloc[:,2:]=df.iloc[y:z,:]

     #   print(df_new.head())
        #df_new=df_new.reset_index(drop=True)   
       # df_new.to_excel("OUTPUT_RESULT.xlsx")
       # self.w2=QtGui.QWidget()
       # self.abc2=QtGui.QMessageBox.information(self.w2, "Message", "Data has been successfully uploaded to OUTPUT_RESULT.xlsx ")

        
        #print(df.loc[y:z,:])
    
    def printInput(self):
        a=self.start_line_2.text()
        b=int(self.start_line.text())
        c=int(self.end_line.text())
        d=self.inflow_line.text()
        e=self.weekly_line.text()
        self.reservoir_id(a,b,c,d,e)
        

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.start_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">START YEAR</span></p></body></html>", None))
        self.end_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">END YEAR</span></p></body></html>", None))
        self.inflow_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">INFLOW/OUTFLOW/ELEVATION/RAW DATA/ALL</span></p></body></html>", None))
        self.weekly_label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">WEEKLY/MONTHLY/YEARLY</span></p></body></html>", None))
        self.heading.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600; font-style:italic; text-decoration: underline;\">DATA EXTRACTOR</span></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "OK", None))
        self.nameOFreservoir.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">SCF ID / NAME OF THE RESERVOIR</span></p></body></html>", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

