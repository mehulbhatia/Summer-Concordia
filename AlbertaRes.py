# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'blah8.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import webbrowser as wb
from PyQt4.QtGui import QInputDialog
from input_dialog import Ui_Dialog
from graph_dialog_2 import Ui_Dialog_2


#path="D:\SUMMER INTERNSHIP CONCORDIA\Updated Work here" 


#globalpath="D:\SUMMER INTERNSHIP CONCORDIA\Updated Work here"

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

class Ui_MainWindow(object):
    def graphWindow(self):
        self.Dialog2=QtGui.QDialog()
        self.ui2=Ui_Dialog_2()
        self.ui2.setupUi(self.Dialog2)
        self.Dialog2.show()
    def dialogWindow(self):
        self.Dialog=QtGui.QDialog()
        self.ui= Ui_Dialog()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(880, 564)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.Oldman = QtGui.QRadioButton(self.centralwidget)
        self.Oldman.setObjectName(_fromUtf8("Oldman Reservoir"))
        self.gridLayout_2.addWidget(self.Oldman, 0, 0, 1, 1)
        self.Keho = QtGui.QRadioButton(self.centralwidget)
        self.Keho.setObjectName(_fromUtf8("Keho Lake"))
        self.gridLayout_2.addWidget(self.Keho, 0, 1, 1, 1)
        self.Badger = QtGui.QRadioButton(self.centralwidget)
        self.Badger.setObjectName(_fromUtf8("Badger Reservoir"))
        self.gridLayout_2.addWidget(self.Badger, 0, 2, 1, 1)
        self.TilleyB = QtGui.QRadioButton(self.centralwidget)
        self.TilleyB.setObjectName(_fromUtf8("TilleyB Reservoir"))
        self.gridLayout_2.addWidget(self.TilleyB, 0, 3, 1, 1)
        self.ChainLakes = QtGui.QRadioButton(self.centralwidget)
        self.ChainLakes.setObjectName(_fromUtf8("ChainLakes Reservoir"))
        self.gridLayout_2.addWidget(self.ChainLakes, 1, 0, 1, 1)
        self.McGregors = QtGui.QRadioButton(self.centralwidget)
        self.McGregors.setObjectName(_fromUtf8("McGregors Lake"))
        self.gridLayout_2.addWidget(self.McGregors, 1, 1, 1, 1)
        self.BuffaloLake = QtGui.QRadioButton(self.centralwidget)
        self.BuffaloLake.setObjectName(_fromUtf8("Buffalo Lake"))
        self.gridLayout_2.addWidget(self.BuffaloLake, 1, 2, 1, 1)
        self.Cowoki = QtGui.QRadioButton(self.centralwidget)
        self.Cowoki.setObjectName(_fromUtf8("Cowoki Lake"))
        self.gridLayout_2.addWidget(self.Cowoki, 1, 3, 1, 1)
        self.Travers = QtGui.QRadioButton(self.centralwidget)
        self.Travers.setObjectName(_fromUtf8("Travers Reservoir"))
        self.gridLayout_2.addWidget(self.Travers, 2, 0, 1, 1)
        self.Kitsim = QtGui.QRadioButton(self.centralwidget)
        self.Kitsim.setObjectName(_fromUtf8("Kitsim Reservoir"))
        self.gridLayout_2.addWidget(self.Kitsim, 2, 2, 2, 1)
        self.CrawlingValley = QtGui.QRadioButton(self.centralwidget)
        self.CrawlingValley.setObjectName(_fromUtf8("CrawlingValley Reservoir"))
        self.gridLayout_2.addWidget(self.CrawlingValley, 2, 3, 2, 1)
        self.PineCoulee = QtGui.QRadioButton(self.centralwidget)
        self.PineCoulee.setObjectName(_fromUtf8("PineCoulee Reservoir"))
        self.gridLayout_2.addWidget(self.PineCoulee, 3, 0, 2, 1)
        self.LittleBow = QtGui.QRadioButton(self.centralwidget)
        self.LittleBow.setObjectName(_fromUtf8("LittleBow Reservoir"))
        self.gridLayout_2.addWidget(self.LittleBow, 3, 1, 2, 1)
        self.LakeNewell = QtGui.QRadioButton(self.centralwidget)
        self.LakeNewell.setObjectName(_fromUtf8("Lake Newell"))
        self.gridLayout_2.addWidget(self.LakeNewell, 4, 2, 1, 1)
        self.BruceLake = QtGui.QRadioButton(self.centralwidget)
        self.BruceLake.setObjectName(_fromUtf8("Bruce Lake"))
        self.gridLayout_2.addWidget(self.BruceLake, 4, 3, 1, 1)
        self.Langdon = QtGui.QRadioButton(self.centralwidget)
        self.Langdon.setObjectName(_fromUtf8("Langdon Exp"))
        self.gridLayout_2.addWidget(self.Langdon, 5, 0, 1, 1)
        self.LostLake = QtGui.QRadioButton(self.centralwidget)
        self.LostLake.setObjectName(_fromUtf8("Los tLake"))
        self.gridLayout_2.addWidget(self.LostLake, 5, 1, 1, 1)
        self.Scope = QtGui.QRadioButton(self.centralwidget)
        self.Scope.setObjectName(_fromUtf8("Scope Reservoir"))
        self.gridLayout_2.addWidget(self.Scope, 5, 2, 1, 1)
        self.Chestermere = QtGui.QRadioButton(self.centralwidget)
        self.Chestermere.setObjectName(_fromUtf8("Chestermere Lake"))
        self.gridLayout_2.addWidget(self.Chestermere, 5, 3, 1, 1)
        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-129, -78, 2269, 977))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.gridLayout = QtGui.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.scrollAreaWidgetContents)
        self.label.setText(_fromUtf8(""))
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8("picture.PNG")))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 6, 0, 1, 6)
        self.Factsheet = QtGui.QPushButton(self.centralwidget)
        self.Factsheet.setObjectName(_fromUtf8("Factsheet"))
        self.gridLayout_2.addWidget(self.Factsheet, 2, 4, 1, 1)
        self.GlenniferLake = QtGui.QRadioButton(self.centralwidget)
        self.GlenniferLake.setObjectName(_fromUtf8("GlenniferLake"))
        self.gridLayout_2.addWidget(self.GlenniferLake, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 880, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuSelect_Reservoir_2 = QtGui.QMenu(self.menubar)
        self.menuSelect_Reservoir_2.setObjectName(_fromUtf8("menuSelect_Reservoir_2"))
        self.menuReservoir_Location = QtGui.QMenu(self.menuSelect_Reservoir_2)
        self.menuReservoir_Location.setObjectName(_fromUtf8("menuReservoir_Location"))
        self.menuInfo = QtGui.QMenu(self.menubar)
        self.menuInfo.setObjectName(_fromUtf8("menuInfo"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionCheck_License = QtGui.QAction(MainWindow)
        self.actionCheck_License.setCheckable(False)
        self.actionCheck_License.setObjectName(_fromUtf8("actionCheck_License"))
        self.actionClick_for_License = QtGui.QAction(MainWindow)
        self.actionClick_for_License.setObjectName(_fromUtf8("actionClick_for_License"))
        
        self.actionReservoir_Data = QtGui.QAction(MainWindow)
        self.actionReservoir_Data.setObjectName(_fromUtf8("actionReservoir_Data"))
        self.actionReservoir_Data.triggered.connect(self.dialogWindow)
        self.actionGraph_Plot = QtGui.QAction(MainWindow)
        self.actionGraph_Plot.setObjectName(_fromUtf8("actionGraph_Plot"))
        self.actionGraph_Plot.triggered.connect(self.graphWindow)
        self.actionOldman_Reservoir = QtGui.QAction(MainWindow)
        self.actionOldman_Reservoir.setObjectName(_fromUtf8("actionOldman_Reservoir"))
        self.actionOldman_Reservoir.triggered.connect(self.oldman_location)
        self.actionChain_Lakes_Reservoir = QtGui.QAction(MainWindow)
        self.actionChain_Lakes_Reservoir.setObjectName(_fromUtf8("actionChain_Lakes_Reservoir"))
        self.actionChain_Lakes_Reservoir.triggered.connect(self.chainlakes_location)
        self.actionTravers_Reservoir = QtGui.QAction(MainWindow)
        self.actionTravers_Reservoir.setObjectName(_fromUtf8("actionTravers_Reservoir"))
        self.actionTravers_Reservoir.triggered.connect(self.travers_location)
        self.actionPine_Coulee_Reservoir = QtGui.QAction(MainWindow)
        self.actionPine_Coulee_Reservoir.setObjectName(_fromUtf8("actionPine_Coulee_Reservoir"))
        self.actionPine_Coulee_Reservoir.triggered.connect(self.pineCoulee_location)
        self.actionLangdon_Exp = QtGui.QAction(MainWindow)
        self.actionLangdon_Exp.setObjectName(_fromUtf8("actionLangdon_Exp"))
        self.actionLangdon_Exp.triggered.connect(self.langdon_location)
        self.actionKeho_Lake = QtGui.QAction(MainWindow)
        self.actionKeho_Lake.setObjectName(_fromUtf8("actionKeho_Lake"))
        self.actionKeho_Lake.triggered.connect(self.keho_location)
        self.actionMcGregors_Lake = QtGui.QAction(MainWindow)
        self.actionMcGregors_Lake.setObjectName(_fromUtf8("actionMcGregors_Lake"))
        self.actionMcGregors_Lake.triggered.connect(self.mcgregors_location)
        self.actionGlennifer_Lake = QtGui.QAction(MainWindow)
        self.actionGlennifer_Lake.setObjectName(_fromUtf8("actionGlennifer_Lake"))
        self.actionGlennifer_Lake.triggered.connect(self.glennifer_location)
        self.actionLittle_Bow_Reservoir = QtGui.QAction(MainWindow)
        self.actionLittle_Bow_Reservoir.setObjectName(_fromUtf8("actionLittle_Bow_Reservoir"))
        self.actionLittle_Bow_Reservoir.triggered.connect(self.littleBow_location)
        self.actionLost_Lake_Reservoir = QtGui.QAction(MainWindow)
        self.actionLost_Lake_Reservoir.setObjectName(_fromUtf8("actionLost_Lake_Reservoir"))
        self.actionLost_Lake_Reservoir.triggered.connect(self.lostLake_location)
        self.actionBadger_Lake = QtGui.QAction(MainWindow)
        self.actionBadger_Lake.setObjectName(_fromUtf8("actionBadger_Lake"))
        self.actionBadger_Lake.triggered.connect(self.badger_location)
        self.actionBuffalo_Lake = QtGui.QAction(MainWindow)
        self.actionBuffalo_Lake.setObjectName(_fromUtf8("actionBuffalo_Lake"))
        self.actionBuffalo_Lake.triggered.connect(self.buffalo_location)
        self.actionKitsim_Reservoir = QtGui.QAction(MainWindow)
        self.actionKitsim_Reservoir.setObjectName(_fromUtf8("actionKitsim_Reservoir"))
        self.actionKitsim_Reservoir.triggered.connect(self.kitsim_location)
        self.actionLake_Newell = QtGui.QAction(MainWindow)
        self.actionLake_Newell.setObjectName(_fromUtf8("actionLake_Newell"))
        self.actionLake_Newell.triggered.connect(self.newell_location)
        self.actionScope_Reservoir = QtGui.QAction(MainWindow)
        self.actionScope_Reservoir.setObjectName(_fromUtf8("actionScope_Reservoir"))
        self.actionScope_Reservoir.triggered.connect(self.scope_location)
        self.actionTilley_B_Reservoir = QtGui.QAction(MainWindow)
        self.actionTilley_B_Reservoir.setObjectName(_fromUtf8("actionTilley_B_Reservoir"))
        self.actionTilley_B_Reservoir.triggered.connect(self.tilley_location)
        self.actionCowoki_Lake = QtGui.QAction(MainWindow)
        self.actionCowoki_Lake.setObjectName(_fromUtf8("actionCowoki_Lake"))
        self.actionCowoki_Lake.triggered.connect(self.cowoki_location)
        self.actionCrawling_Valley = QtGui.QAction(MainWindow)
        self.actionCrawling_Valley.setObjectName(_fromUtf8("actionCrawling_Valley"))
        self.actionCrawling_Valley.triggered.connect(self.crawling_location)
        self.actionBruce_Lake = QtGui.QAction(MainWindow)
        self.actionBruce_Lake.setObjectName(_fromUtf8("actionBruce_Lake"))
        self.actionBruce_Lake.triggered.connect(self.bruce_location)
        self.actionChestermere_Lake = QtGui.QAction(MainWindow)
        self.actionChestermere_Lake.setObjectName(_fromUtf8("actionChestermere_Lake"))
        self.actionChestermere_Lake.triggered.connect(self.chestermere_location)







        self.menuReservoir_SE = QtGui.QMenu(self.menuSelect_Reservoir_2)
        self.menuReservoir_SE.setObjectName(_fromUtf8("menuReservoir_SE"))
        self.actionOldman_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionOldman_Reservoir1.setObjectName(_fromUtf8("actionOldman_Reservoir1"))
        self.actionOldman_Reservoir1.triggered.connect(self.oldman_location1)
        self.actionChain_Lakes_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionChain_Lakes_Reservoir1.setObjectName(_fromUtf8("actionChain_Lakes_Reservoir1"))
        self.actionChain_Lakes_Reservoir1.triggered.connect(self.chainlakes_location1)
        self.actionTravers_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionTravers_Reservoir1.setObjectName(_fromUtf8("actionTravers_Reservoir1"))
        self.actionTravers_Reservoir1.triggered.connect(self.travers_location1)
        self.actionPine_Coulee_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionPine_Coulee_Reservoir1.setObjectName(_fromUtf8("actionPine_Coulee_Reservoir1"))
        self.actionPine_Coulee_Reservoir1.triggered.connect(self.pineCoulee_location1)
        self.actionLangdon_Exp1 = QtGui.QAction(MainWindow)
        self.actionLangdon_Exp1.setObjectName(_fromUtf8("actionLangdon_Exp1"))
        self.actionLangdon_Exp1.triggered.connect(self.langdon_location1)
        self.actionKeho_Lake1 = QtGui.QAction(MainWindow)
        self.actionKeho_Lake1.setObjectName(_fromUtf8("actionKeho_Lake1"))
        self.actionKeho_Lake1.triggered.connect(self.keho_location1)
        self.actionMcGregors_Lake1 = QtGui.QAction(MainWindow)
        self.actionMcGregors_Lake1.setObjectName(_fromUtf8("actionMcGregors_Lake1"))
        self.actionMcGregors_Lake1.triggered.connect(self.mcgregors_location1)
        self.actionGlennifer_Lake1 = QtGui.QAction(MainWindow)
        self.actionGlennifer_Lake1.setObjectName(_fromUtf8("actionGlennifer_Lake1"))
        self.actionGlennifer_Lake1.triggered.connect(self.glennifer_location1)
        self.actionLittle_Bow_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionLittle_Bow_Reservoir1.setObjectName(_fromUtf8("actionLittle_Bow_Reservoir1"))
        self.actionLittle_Bow_Reservoir1.triggered.connect(self.littleBow_location1)
        self.actionLost_Lake_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionLost_Lake_Reservoir1.setObjectName(_fromUtf8("actionLost_Lake_Reservoir1"))
        self.actionLost_Lake_Reservoir1.triggered.connect(self.lostLake_location1)
        self.actionBadger_Lake1 = QtGui.QAction(MainWindow)
        self.actionBadger_Lake1.setObjectName(_fromUtf8("actionBadger_Lake1"))
        self.actionBadger_Lake1.triggered.connect(self.badger_location1)
        self.actionBuffalo_Lake1 = QtGui.QAction(MainWindow)
        self.actionBuffalo_Lake1.setObjectName(_fromUtf8("actionBuffalo_Lake1"))
        self.actionBuffalo_Lake1.triggered.connect(self.buffalo_location1)
        self.actionKitsim_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionKitsim_Reservoir1.setObjectName(_fromUtf8("actionKitsim_Reservoir1"))
        self.actionKitsim_Reservoir1.triggered.connect(self.kitsim_location1)
        self.actionLake_Newell1 = QtGui.QAction(MainWindow)
        self.actionLake_Newell1.setObjectName(_fromUtf8("actionLake_Newell1"))
        self.actionLake_Newell1.triggered.connect(self.newell_location1)
        self.actionScope_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionScope_Reservoir1.setObjectName(_fromUtf8("actionScope_Reservoir1"))
        self.actionScope_Reservoir1.triggered.connect(self.scope_location1)
        self.actionTilley_B_Reservoir1 = QtGui.QAction(MainWindow)
        self.actionTilley_B_Reservoir1.setObjectName(_fromUtf8("actionTilley_B_Reservoir1"))
        self.actionTilley_B_Reservoir1.triggered.connect(self.tilley_location1)
        self.actionCowoki_Lake1 = QtGui.QAction(MainWindow)
        self.actionCowoki_Lake1.setObjectName(_fromUtf8("actionCowoki_Lake1"))
        self.actionCowoki_Lake1.triggered.connect(self.cowoki_location1)
        self.actionCrawling_Valley1 = QtGui.QAction(MainWindow)
        self.actionCrawling_Valley1.setObjectName(_fromUtf8("actionCrawling_Valley1"))
        self.actionCrawling_Valley1.triggered.connect(self.crawling_location1)
        self.actionBruce_Lake1 = QtGui.QAction(MainWindow)
        self.actionBruce_Lake1.setObjectName(_fromUtf8("actionBruce_Lake1"))
        self.actionBruce_Lake1.triggered.connect(self.bruce_location1)
        self.actionChestermere_Lake1 = QtGui.QAction(MainWindow)
        self.actionChestermere_Lake1.setObjectName(_fromUtf8("actionChestermere_Lake1"))
        self.actionChestermere_Lake1.triggered.connect(self.chestermere_location1)
        self.menuReservoir_SE.addAction(self.actionOldman_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionChain_Lakes_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionTravers_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionPine_Coulee_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionLangdon_Exp1)
        self.menuReservoir_SE.addAction(self.actionKeho_Lake1)
        self.menuReservoir_SE.addAction(self.actionMcGregors_Lake1)
        self.menuReservoir_SE.addAction(self.actionGlennifer_Lake1)
        self.menuReservoir_SE.addAction(self.actionLittle_Bow_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionLost_Lake_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionBadger_Lake1)
        self.menuReservoir_SE.addAction(self.actionBuffalo_Lake1)
        self.menuReservoir_SE.addAction(self.actionKitsim_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionLake_Newell1)
        self.menuReservoir_SE.addAction(self.actionScope_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionTilley_B_Reservoir1)
        self.menuReservoir_SE.addAction(self.actionCowoki_Lake1)
        self.menuReservoir_SE.addAction(self.actionCrawling_Valley1)
        self.menuReservoir_SE.addAction(self.actionBruce_Lake1)
        self.menuReservoir_SE.addAction(self.actionChestermere_Lake1)













        
        self.actionClick_for_License_2 = QtGui.QAction(MainWindow)
        self.actionClick_for_License_2.setObjectName(_fromUtf8("actionClick_for_License_2"))
        self.actionClick_for_License_2.triggered.connect(self.about)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionHelp.triggered.connect(self.s_elf)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        #self.actionQuit.triggered.connect(MainWindow.close)
        self.actionQuit.triggered.connect(self.on_pushButtonClose_clicked)
        
        self.menuReservoir_Location.addAction(self.actionOldman_Reservoir)
        self.menuReservoir_Location.addAction(self.actionChain_Lakes_Reservoir)
        self.menuReservoir_Location.addAction(self.actionTravers_Reservoir)
        self.menuReservoir_Location.addAction(self.actionPine_Coulee_Reservoir)
        self.menuReservoir_Location.addAction(self.actionLangdon_Exp)
        self.menuReservoir_Location.addAction(self.actionKeho_Lake)
        self.menuReservoir_Location.addAction(self.actionMcGregors_Lake)
        self.menuReservoir_Location.addAction(self.actionGlennifer_Lake)
        self.menuReservoir_Location.addAction(self.actionLittle_Bow_Reservoir)
        self.menuReservoir_Location.addAction(self.actionLost_Lake_Reservoir)
        self.menuReservoir_Location.addAction(self.actionBadger_Lake)
        self.menuReservoir_Location.addAction(self.actionBuffalo_Lake)
        self.menuReservoir_Location.addAction(self.actionKitsim_Reservoir)
        self.menuReservoir_Location.addAction(self.actionLake_Newell)
        self.menuReservoir_Location.addAction(self.actionScope_Reservoir)
        self.menuReservoir_Location.addAction(self.actionTilley_B_Reservoir)
        self.menuReservoir_Location.addAction(self.actionCowoki_Lake)
        self.menuReservoir_Location.addAction(self.actionCrawling_Valley)
        self.menuReservoir_Location.addAction(self.actionBruce_Lake)
        self.menuReservoir_Location.addAction(self.actionChestermere_Lake)
        self.menuSelect_Reservoir_2.addAction(self.actionReservoir_Data)
        self.menuSelect_Reservoir_2.addAction(self.actionGraph_Plot)
        self.menuSelect_Reservoir_2.addAction(self.menuReservoir_Location.menuAction())
        self.menuSelect_Reservoir_2.addAction(self.menuReservoir_SE.menuAction())
        self.menuInfo.addAction(self.actionClick_for_License_2)
        self.menuInfo.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuSelect_Reservoir_2.menuAction())
        self.menubar.addAction(self.menuInfo.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())

        

        self.Factsheet.clicked.connect(lambda: self.btn(self.Oldman.isChecked(), self.Keho.isChecked(), self.Badger.isChecked(), self.TilleyB.isChecked(),self.ChainLakes.isChecked(), self.McGregors.isChecked(), self.BuffaloLake.isChecked(), self.Cowoki.isChecked(),self.Travers.isChecked(), self.Kitsim.isChecked(),self.CrawlingValley.isChecked(), self.PineCoulee.isChecked(),self.LittleBow.isChecked(), self.LakeNewell.isChecked(), self.BruceLake.isChecked(), self.Langdon.isChecked(),self.LostLake.isChecked(), self.Scope.isChecked(), self.GlenniferLake.isChecked(), self.Chestermere.isChecked()))
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "AlbertaRes", None))
        self.Oldman.setText(_translate("MainWindow", "Oldman Reservoir", None))
        self.Keho.setText(_translate("MainWindow", "Keho Lake", None))
        self.Badger.setText(_translate("MainWindow", "Badger Lake", None))
        self.TilleyB.setText(_translate("MainWindow", "Tilley B Reservoir", None))
        self.ChainLakes.setText(_translate("MainWindow", "Chain Lakes Reservoir", None))
        self.McGregors.setText(_translate("MainWindow", "McGregors Lake", None))
        self.BuffaloLake.setText(_translate("MainWindow", "Buffalo Lake", None))
        self.Cowoki.setText(_translate("MainWindow", "Cowoki Lake", None))
        self.Travers.setText(_translate("MainWindow", "Travers Reservoir", None))
        self.Kitsim.setText(_translate("MainWindow", "Kitsim Reservoir", None))
        self.CrawlingValley.setText(_translate("MainWindow", "Crawling Valley Reservoir", None))
        self.PineCoulee.setText(_translate("MainWindow", "Pine Coulee Reservoir", None))
        self.LittleBow.setText(_translate("MainWindow", "Little Bow Reservoir", None))
        self.LakeNewell.setText(_translate("MainWindow", "Lake Newell", None))
        self.BruceLake.setText(_translate("MainWindow", "Bruce Lake", None))
        self.Langdon.setText(_translate("MainWindow", "Langdon Exp", None))
        self.LostLake.setText(_translate("MainWindow", "Lost Lake", None))
        self.Scope.setText(_translate("MainWindow", "Scope Reservoir", None))
        self.Chestermere.setText(_translate("MainWindow", "Chestermere Lake", None))
        self.Factsheet.setText(_translate("MainWindow", "Get Factsheet", None))
        self.GlenniferLake.setText(_translate("MainWindow", "Glennifer Lake", None))
        self.menuSelect_Reservoir_2.setTitle(_translate("MainWindow", "Reservoir Information", None))
        self.menuReservoir_Location.setTitle(_translate("MainWindow", "Reservoir Location", None))
        self.menuInfo.setTitle(_translate("MainWindow", "Info", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionCheck_License.setText(_translate("MainWindow", "Quit", None))
        self.actionClick_for_License.setText(_translate("MainWindow", "Quit", None))
        self.actionReservoir_Data.setText(_translate("MainWindow", "Reservoir Data", None))
        self.actionGraph_Plot.setText(_translate("MainWindow", "Graph Plot", None))
        self.actionOldman_Reservoir.setText(_translate("MainWindow", "Oldman Reservoir", None))
        self.actionChain_Lakes_Reservoir.setText(_translate("MainWindow", "Chain Lakes Reservoir", None))
        self.actionTravers_Reservoir.setText(_translate("MainWindow", "Travers Reservoir", None))
        self.actionPine_Coulee_Reservoir.setText(_translate("MainWindow", "Pine Coulee Reservoir", None))
        self.actionLangdon_Exp.setText(_translate("MainWindow", "Langdon Exp", None))
        self.actionKeho_Lake.setText(_translate("MainWindow", "Keho Lake", None))
        self.actionMcGregors_Lake.setText(_translate("MainWindow", "McGregors Lake", None))
        self.actionGlennifer_Lake.setText(_translate("MainWindow", "Glennifer Lake", None))
        self.actionLittle_Bow_Reservoir.setText(_translate("MainWindow", "Little Bow Reservoir", None))
        self.actionLost_Lake_Reservoir.setText(_translate("MainWindow", "Lost Lake Reservoir", None))
        self.actionBadger_Lake.setText(_translate("MainWindow", "Badger Lake", None))
        self.actionBuffalo_Lake.setText(_translate("MainWindow", "Buffalo Lake", None))
        self.actionKitsim_Reservoir.setText(_translate("MainWindow", "Kitsim Reservoir", None))
        self.actionLake_Newell.setText(_translate("MainWindow", "Lake Newell", None))
        self.actionScope_Reservoir.setText(_translate("MainWindow", "Scope Reservoir", None))
        self.actionTilley_B_Reservoir.setText(_translate("MainWindow", "Tilley B Reservoir", None))
        self.actionCowoki_Lake.setText(_translate("MainWindow", "Cowoki Lake", None))
        self.actionCrawling_Valley.setText(_translate("MainWindow", "Crawling Valley", None))
        self.actionBruce_Lake.setText(_translate("MainWindow", "Bruce Lake", None))
        self.actionChestermere_Lake.setText(_translate("MainWindow", "Chestermere Lake", None))





        self.menuReservoir_SE.setTitle(_translate("MainWindow", "Reservoir Characteristics", None))
        self.actionOldman_Reservoir1.setText(_translate("MainWindow", "Oldman Reservoir", None))
        self.actionChain_Lakes_Reservoir1.setText(_translate("MainWindow", "Chain Lakes Reservoir", None))
        self.actionTravers_Reservoir1.setText(_translate("MainWindow", "Travers Reservoir", None))
        self.actionPine_Coulee_Reservoir1.setText(_translate("MainWindow", "Pine Coulee Reservoir", None))
        self.actionLangdon_Exp1.setText(_translate("MainWindow", "Langdon Exp", None))
        self.actionKeho_Lake1.setText(_translate("MainWindow", "Keho Lake", None))
        self.actionMcGregors_Lake1.setText(_translate("MainWindow", "McGregors Lake", None))
        self.actionGlennifer_Lake1.setText(_translate("MainWindow", "Glennifer Lake", None))
        self.actionLittle_Bow_Reservoir1.setText(_translate("MainWindow", "Little Bow Reservoir", None))
        self.actionLost_Lake_Reservoir1.setText(_translate("MainWindow", "Lost Lake Reservoir", None))
        self.actionBadger_Lake1.setText(_translate("MainWindow", "Badger Lake", None))
        self.actionBuffalo_Lake1.setText(_translate("MainWindow", "Buffalo Lake", None))
        self.actionKitsim_Reservoir1.setText(_translate("MainWindow", "Kitsim Reservoir", None))
        self.actionLake_Newell1.setText(_translate("MainWindow", "Lake Newell", None))
        self.actionScope_Reservoir1.setText(_translate("MainWindow", "Scope Reservoir", None))
        self.actionTilley_B_Reservoir1.setText(_translate("MainWindow", "Tilley B Reservoir", None))
        self.actionCowoki_Lake1.setText(_translate("MainWindow", "Cowoki Lake", None))
        self.actionCrawling_Valley1.setText(_translate("MainWindow", "Crawling Valley", None))
        self.actionBruce_Lake1.setText(_translate("MainWindow", "Bruce Lake", None))
        self.actionChestermere_Lake1.setText(_translate("MainWindow", "Chestermere Lake", None))










        
        self.actionClick_for_License_2.setText(_translate("MainWindow", "About", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))


    def on_pushButtonClose_clicked(self):
        app = QtGui.QApplication.instance()
        app.closeAllWindows()
    def about(self):
        wb.open_new(r'About.txt')

    def s_elf(self):
        wb.open_new(r'Help.txt')
        
    def oldman_location(self):
        wb.open_new(r'Oldman Reservoir(Number 215)\Oldman Reservoir.kmz')
    def chainlakes_location(self):
        wb.open_new(r'Chain Lakes (Number 212)\Chain Lakes Reservoir.kmz')
    def travers_location(self):
        wb.open_new(r'Travers Reservoir(Number 203)\Travers Reservoir.kmz')
    def pineCoulee_location(self):
        wb.open_new(r'Pine Coulee Reservoir (Number 216)\Pine Coulee Reservoir.kmz')
    def langdon_location(self):
        wb.open_new(r'Langdon Exp (NUmber 59)\Langdon Exp.kmz')
    def keho_location(self):
        wb.open_new(r'Keho Lake (Number 205)\Keho Lake.kmz')
    def mcgregors_location(self):
        wb.open_new(r'McGregor_s Lake(Number 202)\McGregors Lake.kmz')
    def glennifer_location(self):
        wb.open_new(r'Glennifer Lake (number 200)\Glennifer Lake.kmz')
    def littleBow_location(self):
        wb.open_new(r'Little Bow Reservoir(Number 252)\Little Bow Reservoir.kmz')
    def lostLake_location(self):
        wb.open_new(r'Lost Lake(number 226)\Lost Lake.kmz')
    def badger_location(self):
        wb.open_new(r'Badger Reservoir(Number 204)\Badger Lake.kmz')
    def buffalo_location(self):
        wb.open_new(r'Buffalo Lake(number 266)\Buffalo Lake.kmz')
    def kitsim_location(self):
        wb.open_new(r'Kitsim Reservoir (Number 220)\Kitsim Reservoir.kmz')
    def newell_location(self):
        wb.open_new(r'Lake Newell (Number 221)\Lake Newell.kmz')
    def scope_location(self):
        wb.open_new(r'Scope Reservoir(Number 255)\Scope Reservoir.kmz')
    def tilley_location(self):
        wb.open_new(r'Tilley B Reservoir (Number 224)\Tilley B Reservoir.kmz')
    def cowoki_location(self):
        wb.open_new(r'Cowoki Lake (Number 223)\Cowoki Lake.kmz')
    def crawling_location(self):
        wb.open_new(r'Crawling Valley (Number 218)\Crawling Valley Reservoir.kmz')
    def bruce_location(self):
        wb.open_new(r'Bruce Reservoir(Number 57)\Bruce Lake.kmz')
    def chestermere_location(self):
        wb.open_new(r'Chestermere Lake (Number 225)\Chestermere Lake.kmz')


    def oldman_location1(self):
        wb.open_new(r'Oldman Reservoir(Number 215)\SE.xlsx')
    def chainlakes_location1(self):
        wb.open_new(r'Chain Lakes (Number 212)\SE.xlsx')
    def travers_location1(self):
        wb.open_new(r'Travers Reservoir(Number 203)\SE.xlsx')
    def pineCoulee_location1(self):
        wb.open_new(r'Pine Coulee Reservoir (Number 216)\SE.xlsx')
    def langdon_location1(self):
        wb.open_new(r'Langdon Exp (NUmber 59)\SE.xlsx')
    def keho_location1(self):
        wb.open_new(r'Keho Lake (Number 205)\SE.xlsx')
    def mcgregors_location1(self):
        wb.open_new(r'McGregor_s Lake(Number 202)\SE.xlsx')
    def glennifer_location1(self):
        wb.open_new(r'Glennifer Lake (number 200)\SE.xlsx')
    def littleBow_location1(self):
        wb.open_new(r'Little Bow Reservoir(Number 252)\SE.xlsx')
    def lostLake_location1(self):
        wb.open_new(r'Lost Lake(number 226)\SE.xlsx')
    def badger_location1(self):
        wb.open_new(r'Badger Reservoir(Number 204)\SE.xlsx')
    def buffalo_location1(self):
        wb.open_new(r'Buffalo Lake(number 266)\SE.xlsx')
    def kitsim_location1(self):
        wb.open_new(r'Kitsim Reservoir (Number 220)\SE.xlsx')
    def newell_location1(self):
        wb.open_new(r'Lake Newell (Number 221)\SE.xlsx')
    def scope_location1(self):
        wb.open_new(r'Scope Reservoir(Number 255)\SE.xlsx')
    def tilley_location1(self):
        wb.open_new(r'Tilley B Reservoir (Number 224)\SE.xlsx')
    def cowoki_location1(self):
        wb.open_new(r'Cowoki Lake (Number 223)\SE.xlsx')
    def crawling_location1(self):
        wb.open_new(r'Crawling Valley (Number 218)\SE.xlsx')
    def bruce_location1(self):
        wb.open_new(r'Bruce Reservoir(Number 57)\SE.xlsx')
    def chestermere_location1(self):
        wb.open_new(r'Chestermere Lake (Number 225)\SE.xlsx')


        

    def btn(self, chk1, chk2, chk3, chk4, chk5, chk6, chk7, chk8, chk9, chk10, chk11, chk12, chk14, chk15, chk16, chk17, chk18, chk19, chk20, chk21):
        if chk1:
            wb.open_new(r'Oldman Reservoir(Number 215)\Factsheet.pdf')
        if chk2:
            wb.open_new(r'Keho Lake (Number 205)\Factsheet.pdf')
        if chk3:
            wb.open_new(r'Badger Reservoir(Number 204)\Factsheet for Badger Reservoir.pdf')    
        if chk4:
            wb.open_new(r'Tilley B Reservoir (Number 224)\Factsheet.pdf')
        if chk5:
            wb.open_new(r'Chain Lakes (Number 212)\Factsheet for Chain Lakes.pdf')
        if chk6:
            wb.open_new(r"McGregor's Lake(Number 202)\Factsheet.pdf")
        if chk7:
            wb.open_new(r'Buffalo Lake(number 266)\Factsheet.pdf')
        if chk8:
            wb.open_new(r'Cowoki Lake (Number 223)\Factsheet.pdf')
        if chk9:
            wb.open_new(r'Travers Reservoir(Number 203)\Factsheet.pdf')
        if chk10:
            wb.open_new(r'Kitsim Reservoir (Number 220)\Factsheet.pdf')
        if chk11:
            wb.open_new(r'Crawling Valley (Number 218)\Factsheet.pdf')
        if chk12:
            wb.open_new(r'Pine Coulee Reservoir (Number 216)\Factsheet.pdf')
        if chk14:
            wb.open_new(r'Little Bow Reservoir(Number 252)\Factsheet.pdf')
        if chk15:
            wb.open_new(r'Lake Newell (Number 221)\Factsheet.pdf')
        if chk16:
            wb.open_new(r'Bruce Reservoir(Number 57)\Factsheet.pdf')
        if chk17:
            wb.open_new(r'Langdon Exp (NUmber 59)\Factsheet.pdf')
        if chk18:
            wb.open_new(r'Lost Lake(number 226)\Factsheet.pdf')
        if chk19:
            wb.open_new(r'Scope Reservoir(Number 255)\Factsheet.pdf')
        if chk20:
            wb.open_new(r'Glennifer Lake (number 200)\Factsheet.pdf')
        if chk21:
            wb.open_new(r'Chestermere Lake (Number 225)\Factsheet.pdf')


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

