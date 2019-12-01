import random
import sys
import os
from PyQt5.QtWidgets import QLCDNumber, QAction, QApplication, QWidget,\
    QMainWindow, QStackedWidget, QCheckBox, QPushButton, QLabel, QSlider, QGroupBox, QVBoxLayout, QGridLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint, QTimer, pyqtSlot

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Skewb Skills"
        self.top = 100
        self.left = 500
        self.width = 1000
        self.height = 750

        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Icons/logoicon.png")))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.mainMenu = self.menuBar()
        self.generalMenu = self.mainMenu.addMenu('General Functions')
        self.funcMenu = self.mainMenu.addMenu('Practice Mode')
        #fileMenu = mainMenu.addMenu('File')
        #editMenu = mainMenu.addMenu('Edit')
        #viewMenu = mainMenu.addMenu('View')
        #searchMenu = mainMenu.addMenu('Search')
        #toolsMenu = mainMenu.addMenu('Tools')
        self.helpMenu = self.mainMenu.addMenu('Help')

        self.closeButton = QAction('Close Window', self)
        self.closeButton.setShortcut(Qt.Key_Escape)
        self.closeButton.triggered.connect(self.close)
        self.generalMenu.addAction(self.closeButton)

        self.fltButton = QAction('First Layer Trainer', self)
        self.fltButton.setShortcut('F')
        self.fltButton.triggered.connect(self.StartFirstLayerTrainer)
        self.funcMenu.addAction(self.fltButton)

        self.l2ltButton = QAction('Last 2 Layer Alg Trainer', self)
        self.l2ltButton.setShortcut('A')
        self.l2ltButton.triggered.connect(self.StartAlgTrainer)
        self.funcMenu.addAction(self.l2ltButton)

        self.helpbut = QAction('How to use it?', self)
        self.helpbut.setShortcut('H')
        self.helpbut.triggered.connect(self.do_h)
        self.helpMenu.addAction(self.helpbut)

        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)
        self.windowFLT = WindowFLT()
        self.windowL2LT = WindowL2LT()
        self.show()

    def do_h(self):
        self.helpwindow = Help()
        self.helpwindow.show()

    def CreateLayout(self):
        # starting to define the layout of the CentralWidget
        self.central.groupBox = QGroupBox("How do you want to practice?")
        self.central.groupBox.setFont(QtGui.QFont("Sansserif", 13))
        gridLayout = QGridLayout()

        # button to start the first layer trainer
        self.firstlayerbut = QPushButton("First Layer Trainer (or press F)", self)
        self.firstlayerbut.setMinimumHeight(80)
        self.firstlayerbut.setToolTip("Generates scrambles from 1 up to 7 moves. They either"
                                      " appear shuffled or ordered (depending on your choice).\n"
                                      "You will either see only white or random starting colours.\n"
                                      "With stopwatch to time your solutions.")
        self.firstlayerbut.clicked.connect(self.StartFirstLayerTrainer)
        gridLayout.addWidget(self.firstlayerbut, 0, 0)

        # button to start the alg trainer
        self.algbut = QPushButton("Last 2 Layer Alg Trainer (or press A)", self)
        self.algbut.setMinimumHeight(80)
        self.algbut.setToolTip("Shows you L2L-cases (scramble + drawing) to the sets you choose.\n"
                               "With stopwatch to time your solutions.")
        self.algbut.clicked.connect(self.StartAlgTrainer)
        gridLayout.addWidget(self.algbut, 0, 1)

        # ToDo:
        '''
        # button to start the comp sim
        self.compsimbut = QPushButton("Comp Sim (or press C)", self)
        self.compsimbut.setMinimumHeight(80)
        self.compsimbut.setToolTip("Starts the competition simulation in a new window.")
        self.compsimbut.clicked.connect(self.StartCompSim)
        gridLayout.addWidget(self.compsimbut, 1, 0)
                
        # button to start the quiz
        self.quizbut = QPushButton("Quiz (or press Q)", self)
        self.quizbut.setMinimumHeight(80)
        self.quizbut.setToolTip("Starts a new quiz window.")
        self.quizbut.clicked.connect(self.StartQuiz)
        gridLayout.addWidget(self.quizbut, 1, 1)
        '''

        # this label shows a picture
        self.scrpic = QLabel(self)
        self.scrpic.setMinimumHeight(50)
        self.scrpic.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "Icons/logogreen")).scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation))
        gridLayout.addWidget(self.scrpic, 2, 0)

        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© 2019, Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        gridLayout.addWidget(self.creatorlabel, 2, 1)

        self.central.groupBox.setLayout(gridLayout)

        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def StartFirstLayerTrainer(self):
        self.close()
        self.windowFLT.showMaximized()

    def StartAlgTrainer(self):
        self.close()
        self.windowL2LT.showMaximized()
    # ToDo:
    '''
    def StartCompSim(self):
        pass

    def StartQuiz(self):
        pass
    '''
class WindowFLT(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.title = "Skewb Skills: First Layer Trainer"
        self.top = 100
        self.left = 500
        self.width = 1000
        self.height = 750

        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Icons/logoicon.png")))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ReadAllScrambles()

        self.mainMenu = self.menuBar()
        self.generalMenu = self.mainMenu.addMenu('General Functions')
        self.funcMenu = self.mainMenu.addMenu('Practice Mode')
        self.fltMenu = self.mainMenu.addMenu('FLT Functions')
        # editMenu = mainMenu.addMenu('Edit')
        # viewMenu = mainMenu.addMenu('View')
        # searchMenu = mainMenu.addMenu('Search')
        # toolsMenu = mainMenu.addMenu('Tools')
        self.helpMenu = self.mainMenu.addMenu('Help')

        self.closeButton = QAction('Close Window', self)
        self.closeButton.setShortcut(Qt.Key_Escape)
        self.closeButton.triggered.connect(self.close)
        self.generalMenu.addAction(self.closeButton)

        self.fltButton = QAction('First Layer Trainer', self)
        self.fltButton.setShortcut('F')
        self.fltButton.setStatusTip('First Layer Trainer')
        self.fltButton.triggered.connect(self.StartFirstLayerTrainer)
        self.funcMenu.addAction(self.fltButton)

        self.l2ltButton = QAction('Last 2 Layer Alg Trainer', self)
        self.l2ltButton.setShortcut('A')
        self.l2ltButton.setStatusTip('Last 2 Layer Alg Trainer')
        self.l2ltButton.triggered.connect(self.StartAlgTrainer)
        self.funcMenu.addAction(self.l2ltButton)

        self.fltEnterButton = QAction('Generate Scramble + Colour', self)
        self.fltEnterButton.setShortcut(Qt.Key_Return)
        self.fltEnterButton.triggered.connect(self.ScramblePlusColour)
        self.fltMenu.addAction(self.fltEnterButton)

        self.fltSpaceBut = QAction('Start / Pause Timer', self)
        self.fltSpaceBut.setShortcut(Qt.Key_Space)
        self.fltSpaceBut.triggered.connect(self.whattodowithspace)
        self.fltMenu.addAction(self.fltSpaceBut)

        self.fltButR = QAction('Reset Timer', self)
        self.fltButR.setShortcut('R')
        self.fltButR.triggered.connect(self.do_reset)
        self.fltMenu.addAction(self.fltButR)

        self.fltBut1 = QAction('Scramble Length: 1', self)
        self.fltBut1.setShortcut('1')
        self.fltBut1.triggered.connect(self.do_1)
        self.fltMenu.addAction(self.fltBut1)
        self.fltBut2 = QAction('Scramble Length: 2', self)
        self.fltBut2.setShortcut('2')
        self.fltBut2.triggered.connect(self.do_2)
        self.fltMenu.addAction(self.fltBut2)
        self.fltBut3 = QAction('Scramble Length: 3', self)
        self.fltBut3.setShortcut('3')
        self.fltBut3.triggered.connect(self.do_3)
        self.fltMenu.addAction(self.fltBut3)
        self.fltBut4 = QAction('Scramble Length: 4', self)
        self.fltBut4.setShortcut('4')
        self.fltBut4.triggered.connect(self.do_4)
        self.fltMenu.addAction(self.fltBut4)
        self.fltBut5 = QAction('Scramble Length: 5', self)
        self.fltBut5.setShortcut('5')
        self.fltBut5.triggered.connect(self.do_5)
        self.fltMenu.addAction(self.fltBut5)
        self.fltBut6 = QAction('Scramble Length: 6', self)
        self.fltBut6.setShortcut('6')
        self.fltBut6.triggered.connect(self.do_6)
        self.fltMenu.addAction(self.fltBut6)
        self.fltBut7 = QAction('Scramble Length: 7', self)
        self.fltBut7.setShortcut('7')
        self.fltBut7.triggered.connect(self.do_7)
        self.fltMenu.addAction(self.fltBut7)

        self.fltButS = QAction('Shuffle Scrambles', self)
        self.fltButS.setShortcut('S')
        self.fltButS.triggered.connect(self.do_s)
        self.fltMenu.addAction(self.fltButS)
        self.fltButC = QAction('Use all colours', self)
        self.fltButC.setShortcut('C')
        self.fltButC.triggered.connect(self.do_c)
        self.fltMenu.addAction(self.fltButC)

        self.helpbut = QAction('How to use it?', self)
        self.helpbut.setShortcut('H')
        self.helpbut.triggered.connect(self.do_h)
        self.helpMenu.addAction(self.helpbut)

        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)

    def do_h(self):
        self.helpwindow = Help()
        self.helpwindow.show()

    def do_1(self):
        self.scrlenslider.setValue(1)

    def do_2(self):
        self.scrlenslider.setValue(2)

    def do_3(self):
        self.scrlenslider.setValue(3)

    def do_4(self):
        self.scrlenslider.setValue(4)

    def do_5(self):
        self.scrlenslider.setValue(5)

    def do_6(self):
        self.scrlenslider.setValue(6)

    def do_7(self):
        self.scrlenslider.setValue(7)

    def do_s(self):
        if self.shufflescrchecker.isChecked():
            self.shufflescrchecker.setChecked(False)
        else:
            self.shufflescrchecker.setChecked(True)

    def do_c(self):
        if self.anycolourchecker.isChecked():
            self.anycolourchecker.setChecked(False)
        else:
            self.anycolourchecker.setChecked(True)

    def whattodowithspace(self):
        if self.start.text() == "Start (SPACE)":
            self.do_start()
        else:
            self.do_pause()

    def ReadAllScrambles(self):
        # with a given file that consists of all scrambles to a given number of moves and
        # all possible starting colours, the next few lines of code generate a list of all lines
        # in the scrambles.txt-File and append groups of two elements of this list to the
        # final scramblelist

        self.newscramble1list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles1.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble1list.append(line[:-1])
        self.scramblelist = self.newscramble1list.copy()

        self.newscramble2list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles2.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble2list.append(line[:-1])

        self.newscramble3list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles3.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble3list.append(line[:-1])

        self.newscramble4list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles4.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble4list.append(line[:-1])

        self.newscramble5list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles5.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble5list.append(line[:-1])

        self.newscramble6list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles6.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble6list.append(line[:-1])

        self.newscramble7list = []
        datei = open(os.path.join(os.path.dirname(__file__), "FirstLayerScrambles/newscrambles7.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.newscramble7list.append(line[:-1])

    def CreateLayout(self):
        # starting to define the layout of the CentralWidget
        self.central.groupBox = QGroupBox("First Layer Trainer")
        self.central.groupBox.setFont(QtGui.QFont("Sansserif", 13))
        self.gridLayout = QGridLayout()

        # checkbox: shuffle scrambles or not
        self.shufflescrchecker = QCheckBox("Shuffle scrambles", self)
        self.shufflescrchecker.setMaximumHeight(50)
        self.shufflescrchecker.setToolTip("If enabled, the upcoming scrambles will be "
                                          "in random order. Otherwise, you will receive "
                                          "an ordered list of scrambles.\nRecommendation for "
                                          "learning purposes: do not enable this checkbox.\n"
                                          "If you feel ready, select this checkbox to shuffle "
                                          "your scramble list.\nShuffling might take some time.")
        self.shufflescrchecker.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.shufflescrchecker, 0, 0)

        # checkbox: use all colours or not
        self.anycolourchecker = QCheckBox("Use all colours", self)
        self.anycolourchecker.setMaximumHeight(50)
        self.anycolourchecker.setToolTip("If enabled, the upcoming scrambles will use all "
                                         "colours.\nIf you only want to practice on a single "
                                         "colour (e.g. white), do not activate this checkbox.")
        self.gridLayout.addWidget(self.anycolourchecker, 0, 2)

        # slider to define the scramble length
        self.scrlenslider = QSlider(Qt.Horizontal)
        self.scrlenslider.setMinimum(1)
        self.scrlenslider.setMaximum(7)
        self.scrlenslider.setValue(1)
        self.scrlenslider.setTickPosition(QSlider.TicksBelow)
        self.scrlenslider.setTickInterval(1)
        self.scrlenslider.setToolTip("Change the scramble length from 1 on the left to 7 on the right.")
        self.gridLayout.addWidget(self.scrlenslider, 0, 1)
        self.scrlenslider.setMinimumWidth(70)
        self.scrlenslider.valueChanged.connect(self.changescrlen)

        # button to generate a scramble and a random colour to start the first layer with
        self.scramblegenbutton = QPushButton("Generate Scramble + Colour\n(RETURN)", self)
        self.scramblegenbutton.setMinimumHeight(80)
        self.scramblegenbutton.setToolTip("Generates a scramble of the defined length and "
                                     "a random colour to start the first layer with.")
        self.scramblegenbutton.clicked.connect(self.ScramblePlusColour)
        self.gridLayout.addWidget(self.scramblegenbutton, 1, 0)

        # this label shows the scramble
        self.scramblelabel = QLabel(self)
        self.scramblelabel.setMinimumHeight(50)
        self.scramblelabel.setText('')
        self.scramblelabel.setFont(QtGui.QFont("Monospace", 20))
        self.gridLayout.addWidget(self.scramblelabel, 1, 1)

        # this label shows the colour
        self.colourlabel = QLabel(self)
        self.colourlabel.setMinimumHeight(50)
        self.colourlabel.setStyleSheet('background-color : transparent')
        self.gridLayout.addWidget(self.colourlabel, 1, 2)

        self.scrpic = QLabel(self)
        self.scrpic.setMinimumHeight(50)
        self.scrpic.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "Icons/logogreen")).scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.gridLayout.addWidget(self.scrpic, 4, 0)

        self.start = QPushButton("Start (SPACE)", self)
        self.start.setMinimumHeight(50)
        self.start.setToolTip("Starts (or stops) the timer.")
        self.start.clicked.connect(self.do_start)
        self.gridLayout.addWidget(self.start, 3, 0)

        self.reset = QPushButton("Reset (R)", self)
        self.reset.setMinimumHeight(50)
        self.reset.setToolTip("Resets the timer.")
        self.reset.clicked.connect(self.do_reset)
        self.gridLayout.addWidget(self.reset, 3, 2)

        self.lcd = QLCDNumber(self)
        self.lcd.setSmallDecimalPoint(True)
        self.lcd.setDigitCount(10)
        self.gridLayout.addWidget(self.lcd, 3, 1)
        self.timer = QTimer()
        self.timer.setInterval(2 ** 0)
        self.timer.timeout.connect(self.tick)

        self.do_reset()

        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© 2019, Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        self.gridLayout.addWidget(self.creatorlabel, 4, 2)

        self.central.groupBox.setLayout(self.gridLayout)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def changescrlen(self):
        scrlen = self.scrlenslider.value()

        if scrlen == 1:
            self.auxscr1 = self.newscramble1list[:]
            if self.shufflescrchecker.isChecked():
                random.shuffle(self.auxscr1)
                self.scramblelist = self.auxscr1
            else:
                self.scramblelist = self.auxscr1

        elif scrlen == 2:
            self.auxscr2 = self.newscramble2list[:]
            if self.shufflescrchecker.isChecked():
                random.shuffle(self.auxscr2)
                self.scramblelist = self.auxscr2
            else:
                self.scramblelist = self.auxscr2

        elif scrlen == 3:
            self.auxscr3 = self.newscramble3list[:]
            if self.shufflescrchecker.isChecked():
                random.shuffle(self.auxscr3)
                self.scramblelist = self.auxscr3
            else:
                self.scramblelist = self.auxscr3

        elif scrlen == 4:
            self.auxscr4 = self.newscramble4list[:]
            if self.shufflescrchecker.isChecked():
                random.shuffle(self.auxscr4)
                self.scramblelist = self.auxscr4
            else:
                self.scramblelist = self.auxscr4

        elif scrlen == 5:
            self.auxscr5 = self.newscramble5list[:]
            if self.shufflescrchecker.isChecked():
                random.shuffle(self.auxscr5)
                self.scramblelist = self.auxscr5
            else:
                self.scramblelist = self.auxscr5

        elif scrlen == 6:
            if self.shufflescrchecker.isChecked():
                self.scramblelist = random.sample(self.newscramble6list,len(self.newscramble6list))
            else:
                self.scramblelist = self.newscramble6list[:]

        else:
            if self.shufflescrchecker.isChecked():
                self.scramblelist = random.sample(self.newscramble7list,len(self.newscramble7list))
            else:
                self.scramblelist = self.newscramble7list[:]

    def ScramblePlusColour(self):

        if len(self.scramblelist) == 0:
            self.changescrlen()

        scramblezumanzeigen = self.scramblelist[-1]
        self.scramblelist.pop()
        self.scramblelabel.setText(scramblezumanzeigen)

        # generate scramble drawing

        self.ShowScramble(scramblezumanzeigen)

        # decide which colour one has to use as the starting colour

        if self.anycolourchecker.isChecked():
            cl = random.choice(["w", "y", "g", "r", "b", "o"])
            if cl == "w":
                self.colourlabel.setStyleSheet('background-color : white')
            elif cl == "y":
                self.colourlabel.setStyleSheet('background-color : yellow')
            elif cl == "g":
                self.colourlabel.setStyleSheet('background-color : green')
            elif cl == "r":
                self.colourlabel.setStyleSheet('background-color : red')
            elif cl == "b":
                self.colourlabel.setStyleSheet('background-color : blue')
            else:
                self.colourlabel.setStyleSheet('background-color : orange')
        else:
            self.colourlabel.setStyleSheet('background-color : white')


    def ShowScramble(self, scramble):
        stickercol = ["o", "o", "o", "o", "o", "g", "g", "g", "g", "g", "y", "y", "y", "y", "y",
                      "w", "w", "w", "w", "w", "r", "r", "r", "r", "r", "b", "b", "b", "b", "b"]
        scrsplit = scramble.split()
        for i in scrsplit:
            if i == "R":
                threeswap(stickercol, 3, 7, 16)
                threeswap(stickercol, 10, 20, 25)
                threeswap(stickercol, 11, 21, 27)
                threeswap(stickercol, 12, 22, 28)
                threeswap(stickercol, 13, 23, 29)
            elif i == "R'":
                threeswap(stickercol, 16, 7, 3)
                threeswap(stickercol, 25, 20, 10)
                threeswap(stickercol, 27, 21, 11)
                threeswap(stickercol, 28, 22, 12)
                threeswap(stickercol, 29, 23, 13)
            elif i == "L":
                threeswap(stickercol, 0, 5, 10)
                threeswap(stickercol, 1, 7, 13)
                threeswap(stickercol, 2, 8, 14)
                threeswap(stickercol, 3, 9, 11)
                threeswap(stickercol, 18, 23, 27)
            elif i == "L'":
                threeswap(stickercol, 10, 5, 0)
                threeswap(stickercol, 13, 7, 1)
                threeswap(stickercol, 14, 8, 2)
                threeswap(stickercol, 11, 9, 3)
                threeswap(stickercol, 27, 23, 18)
            elif i == "U":
                threeswap(stickercol, 0, 25, 15)
                threeswap(stickercol, 1, 27, 16)
                threeswap(stickercol, 3, 29, 18)
                threeswap(stickercol, 4, 26, 19)
                threeswap(stickercol, 9, 13, 21)
            elif i == "U'":
                threeswap(stickercol, 15, 25, 0)
                threeswap(stickercol, 16, 27, 1)
                threeswap(stickercol, 18, 29, 3)
                threeswap(stickercol, 19, 26, 4)
                threeswap(stickercol, 21, 13, 9)
            elif i == "B":
                threeswap(stickercol, 0, 10, 25)
                threeswap(stickercol, 2, 12, 26)
                threeswap(stickercol, 3, 13, 27)
                threeswap(stickercol, 4, 14, 28)
                threeswap(stickercol, 8, 22, 19)
            else:
                threeswap(stickercol, 25, 10, 0)
                threeswap(stickercol, 26, 12, 2)
                threeswap(stickercol, 27, 13, 3)
                threeswap(stickercol, 28, 14, 4)
                threeswap(stickercol, 19, 22, 8)

        # draws the scramble by drawing several polygons corresponding to the scramble
        self.drawscrwidget = ScrambleDrawing(stickercol)
        self.drawscrwidget.setMinimumHeight(430)
        self.drawscrwidget.setMinimumWidth(500)
        self.gridLayout.addWidget(self.drawscrwidget, 2, 1)

    def display(self):
        # shows the current time (since zero / or zero itself) on the lcd
        self.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))

    @pyqtSlot()
    def tick(self):
        # currently update the time, every 2**0/1000 ms, show it on the lcd
        self.time += 2**0/1000
        self.display()

    @pyqtSlot()
    def do_start(self):
        self.timer.start()
        self.start.setText("Pause (SPACE)")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_pause)

    @pyqtSlot()
    def do_pause(self):
        self.timer.stop()
        self.start.setText("Start (SPACE)")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_start)

    @pyqtSlot()
    def do_reset(self):
        # set time of the stopwatch back to zero, show the current time on the lcd
        self.time = 0
        self.display()

    def StartFirstLayerTrainer(self):
        self.close()
        self.windowFLT = WindowFLT()
        self.windowFLT.showMaximized()

    def StartAlgTrainer(self):
        self.close()
        self.windowL2LT = WindowL2LT()
        self.windowL2LT.showMaximized()
    # ToDo: other practicing modes
    '''
    def StartCompSim(self):
        pass

    def StartQuiz(self):
        pass
    '''

class WindowL2LT(QMainWindow):
    def __init__(self, parent=None):
        super(WindowL2LT, self).__init__(parent=parent)

        self.title = "Skewb Skills: Last 2 Layer Alg Trainer"
        self.top = 50
        self.left = 50
        self.width = 1600
        self.height = 800

        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Icons/logoicon.png")))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)


        self.ReadAllScrambles()

        self.mainMenu = self.menuBar()
        self.generalMenu = self.mainMenu.addMenu('General Functions')
        self.funcMenu = self.mainMenu.addMenu('Practice Mode')
        self.l2lMenu = self.mainMenu.addMenu('Alg Trainer Functions')
        self.helpMenu = self.mainMenu.addMenu('Help')

        self.closeButton = QAction('Close Window', self)
        self.closeButton.setShortcut(Qt.Key_Escape)
        self.closeButton.triggered.connect(self.close)
        self.generalMenu.addAction(self.closeButton)

        self.fltButton = QAction('First Layer Trainer', self)
        self.fltButton.setShortcut('F')
        self.fltButton.triggered.connect(self.StartFirstLayerTrainer)
        self.funcMenu.addAction(self.fltButton)

        self.l2ltButton = QAction('Last 2 Layer Alg Trainer', self)
        self.l2ltButton.setShortcut('A')
        self.l2ltButton.triggered.connect(self.StartAlgTrainer)
        self.funcMenu.addAction(self.l2ltButton)

        self.l2ltEnterButton = QAction('Generate Scramble', self)
        self.l2ltEnterButton.setShortcut(Qt.Key_Return)
        self.l2ltEnterButton.triggered.connect(self.ScramblePlusColour)
        self.l2lMenu.addAction(self.l2ltEnterButton)

        self.l2ltSpaceBut = QAction('Start / Pause Timer', self)
        self.l2ltSpaceBut.setShortcut(Qt.Key_Space)
        self.l2ltSpaceBut.triggered.connect(self.whattodowithspace)
        self.l2lMenu.addAction(self.l2ltSpaceBut)

        self.l2ltRBut = QAction('Reset Timer', self)
        self.l2ltRBut.setShortcut('R')
        self.l2ltRBut.triggered.connect(self.do_reset)
        self.l2lMenu.addAction(self.l2ltRBut)

        self.l2ltall = QAction('Select / Unselect all Cases', self)
        self.l2ltall.setShortcut(Qt.Key_T)
        self.l2ltall.triggered.connect(self.whattodowitht)
        self.l2lMenu.addAction(self.l2ltall)

        self.l2ltallPI = QAction('Select / Unselect all Pi Cases', self)
        self.l2ltallPI.setShortcut('I')
        self.l2ltallPI.triggered.connect(self.whattodowithi)
        self.l2lMenu.addAction(self.l2ltallPI)

        self.l2ltallPEANUT = QAction('Select / Unselect all Peanut Cases', self)
        self.l2ltallPEANUT.setShortcut('U')
        self.l2ltallPEANUT.triggered.connect(self.whattodowithu)
        self.l2lMenu.addAction(self.l2ltallPEANUT)

        self.l2ltallL45 = QAction('Select / Unselect all L4C / L5C Cases', self)
        self.l2ltallL45.setShortcut('L')
        self.l2ltallL45.triggered.connect(self.whattodowithl)
        self.l2lMenu.addAction(self.l2ltallL45)

        self.helpbut = QAction('How to use it?', self)
        self.helpbut.setShortcut('H')
        self.helpbut.triggered.connect(self.do_h)
        self.helpMenu.addAction(self.helpbut)

        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)

    def do_h(self):
        self.helpwind = Help()
        self.helpwind.show()

    def whattodowitht(self):
        if self.pi3s.isChecked() == False or \
                self.pihu.isChecked() == False or self.pihz.isChecked() == False or \
                self.pio.isChecked() == False or self.piswirl.isChecked() == False or \
                self.pivu.isChecked() == False or self.piwat.isChecked() == False or \
                self.pix.isChecked() == False or self.pizconj.isChecked() == False or\
                self.p3s.isChecked() == False or \
                self.phu.isChecked() == False or self.phzpure.isChecked() == False or \
                self.po.isChecked() == False or self.pswirl.isChecked() == False or \
                self.pvu.isChecked() == False or self.pwat.isChecked() == False or \
                self.px.isChecked() == False or self.pzconj.isChecked() == False or \
                self.l4c.isChecked() == False or self.l5c.isChecked() == False:
            self.pi3s.setChecked(True)
            self.pihu.setChecked(True)
            self.pihz.setChecked(True)
            self.pio.setChecked(True)
            self.piswirl.setChecked(True)
            self.pivu.setChecked(True)
            self.piwat.setChecked(True)
            self.pix.setChecked(True)
            self.pizconj.setChecked(True)
            self.p3s.setChecked(True)
            self.phu.setChecked(True)
            self.phzpure.setChecked(True)
            self.po.setChecked(True)
            self.pswirl.setChecked(True)
            self.pvu.setChecked(True)
            self.pwat.setChecked(True)
            self.px.setChecked(True)
            self.pzconj.setChecked(True)
            self.l4c.setChecked(True)
            self.l5c.setChecked(True)
        else:
            self.pi3s.setChecked(False)
            self.pihu.setChecked(False)
            self.pihz.setChecked(False)
            self.pio.setChecked(False)
            self.piswirl.setChecked(False)
            self.pivu.setChecked(False)
            self.piwat.setChecked(False)
            self.pix.setChecked(False)
            self.pizconj.setChecked(False)
            self.p3s.setChecked(False)
            self.phu.setChecked(False)
            self.phzpure.setChecked(False)
            self.po.setChecked(False)
            self.pswirl.setChecked(False)
            self.pvu.setChecked(False)
            self.pwat.setChecked(False)
            self.px.setChecked(False)
            self.pzconj.setChecked(False)
            self.l4c.setChecked(False)
            self.l5c.setChecked(False)

    def whattodowithi(self):
        if self.pi3s.isChecked() == False or \
                self.pihu.isChecked() == False or self.pihz.isChecked() == False or \
                self.pio.isChecked() == False or self.piswirl.isChecked() == False or \
                self.pivu.isChecked() == False or self.piwat.isChecked() == False or \
                self.pix.isChecked() == False or self.pizconj.isChecked() == False:
            self.pi3s.setChecked(True)
            self.pihu.setChecked(True)
            self.pihz.setChecked(True)
            self.pio.setChecked(True)
            self.piswirl.setChecked(True)
            self.pivu.setChecked(True)
            self.piwat.setChecked(True)
            self.pix.setChecked(True)
            self.pizconj.setChecked(True)
        else:
            self.pi3s.setChecked(False)
            self.pihu.setChecked(False)
            self.pihz.setChecked(False)
            self.pio.setChecked(False)
            self.piswirl.setChecked(False)
            self.pivu.setChecked(False)
            self.piwat.setChecked(False)
            self.pix.setChecked(False)
            self.pizconj.setChecked(False)

    def whattodowithu(self):
        if self.p3s.isChecked() == False or \
                self.phu.isChecked() == False or self.phzpure.isChecked() == False or \
                self.po.isChecked() == False or self.pswirl.isChecked() == False or \
                self.pvu.isChecked() == False or self.pwat.isChecked() == False or \
                self.px.isChecked() == False or self.pzconj.isChecked() == False:
            self.p3s.setChecked(True)
            self.phu.setChecked(True)
            self.phzpure.setChecked(True)
            self.po.setChecked(True)
            self.pswirl.setChecked(True)
            self.pvu.setChecked(True)
            self.pwat.setChecked(True)
            self.px.setChecked(True)
            self.pzconj.setChecked(True)
        else:
            self.p3s.setChecked(False)
            self.phu.setChecked(False)
            self.phzpure.setChecked(False)
            self.po.setChecked(False)
            self.pswirl.setChecked(False)
            self.pvu.setChecked(False)
            self.pwat.setChecked(False)
            self.px.setChecked(False)
            self.pzconj.setChecked(False)

    def whattodowithl(self):
        if self.l4c.isChecked() == False or self.l5c.isChecked() == False:
            self.l4c.setChecked(True)
            self.l5c.setChecked(True)
        else:
            self.l4c.setChecked(False)
            self.l5c.setChecked(False)

    def whattodowithspace(self):
        if self.start.text() == "Start (SPACE)":
            self.do_start()
        else:
            self.do_pause()

    def ReadAllScrambles(self):
        self.scrpiswirl = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/piswirl.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpiswirl.append(line[:-1])

        self.scrpiwat = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/piwat.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpiwat.append(line[:-1])

        self.scrpix = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pix.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpix.append(line[:-1])

        self.scrpihu = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pihu.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpihu.append(line[:-1])

        self.scrpivu = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pivu.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpivu.append(line[:-1])

        self.scrpio = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pio.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpio.append(line[:-1])

        self.scrpizconj = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pizconj.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpizconj.append(line[:-1])

        self.scrpi3s = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pi3s.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpi3s.append(line[:-1])

        self.scrpihz = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pihz.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpihz.append(line[:-1])

        self.scrpswirl = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pswirl.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpswirl.append(line[:-1])

        self.scrpwat = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pwat.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpwat.append(line[:-1])

        self.scrpx = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/px.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpx.append(line[:-1])

        self.scrphu = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/phu.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrphu.append(line[:-1])

        self.scrpvu = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pvu.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpvu.append(line[:-1])

        self.scrpo = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/po.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpo.append(line[:-1])

        self.scrpzconj = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/pzconj.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrpzconj.append(line[:-1])

        self.scrp3s = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/p3s.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrp3s.append(line[:-1])

        self.scrphzpure = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/phzpure.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrphzpure.append(line[:-1])

        self.scrl4c = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/l4c.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrl4c.append(line[:-1])

        self.scrl5c = []
        datei = open(os.path.join(os.path.dirname(__file__), "Last2LayerScrambles/l5c.txt"), 'r', encoding='utf-8')
        for line in datei:
            self.scrl5c.append(line[:-1])


        self.scramblelist = ["R R'"]

    def CreateLayout(self):
        # starting to define the layout of the CentralWidget
        self.central.groupBox = QGroupBox("L2L Trainer")
        self.central.groupBox.setFont(QtGui.QFont("Sansserif", 12))
        self.gridLayout = QGridLayout()


        # checkbox: l4c
        self.l4c = QCheckBox("L4C", self)
        self.l4c.setMaximumHeight(50)
        self.l4c.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.l4c, 0, 2)

        # checkbox: l5c
        self.l5c = QCheckBox("L5C", self)
        self.l5c.setMaximumHeight(50)
        self.l5c.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.l5c, 1, 2)

        # checkbox: pswirl
        self.pswirl = QCheckBox("Peanut + Swirl Perm", self)
        self.pswirl.setMaximumHeight(50)
        self.pswirl.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pswirl, 0, 1)

        # checkbox: pwat
        self.pwat = QCheckBox("Peanut + Wat Perm", self)
        self.pwat.setMaximumHeight(50)
        self.pwat.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pwat, 1, 1)

        # checkbox: px
        self.px = QCheckBox("Peanut + X Perm", self)
        self.px.setMaximumHeight(50)
        self.px.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.px, 2, 1)

        # checkbox: phu
        self.phu = QCheckBox("Peanut + Horizontal U Perm", self)
        self.phu.setMaximumHeight(50)
        self.phu.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.phu, 3, 1)

        # checkbox: pvu
        self.pvu = QCheckBox("Peanut + Vertical U Perm", self)
        self.pvu.setMaximumHeight(50)
        self.pvu.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pvu, 4, 1)

        # checkbox: po
        self.po = QCheckBox("Peanut + O Perm", self)
        self.po.setMaximumHeight(50)
        self.po.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.po, 5, 1)

        # checkbox: pzconj
        self.pzconj = QCheckBox("Peanut + Z Perm Conjugates", self)
        self.pzconj.setMaximumHeight(50)
        self.pzconj.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pzconj, 6, 1)

        # checkbox: p3s
        self.p3s = QCheckBox("Peanut + Triple Sledge", self)
        self.p3s.setMaximumHeight(50)
        self.p3s.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.p3s, 7, 1)

        # checkbox: phzpure
        self.phzpure = QCheckBox("Peanut + H or Z Perm and Pure Peanut", self)
        self.phzpure.setMaximumHeight(50)
        self.phzpure.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.phzpure, 8, 1)

        # checkbox: piswirl
        self.piswirl = QCheckBox("Pi + Swirl Perm", self)
        self.piswirl.setMaximumHeight(50)
        self.piswirl.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.piswirl, 0, 0)

        # checkbox: piwat
        self.piwat = QCheckBox("Pi + Wat Perm", self)
        self.piwat.setMaximumHeight(50)
        self.piwat.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.piwat, 1, 0)

        # checkbox: px
        self.pix = QCheckBox("Pi + X Perm", self)
        self.pix.setMaximumHeight(50)
        self.pix.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pix, 2, 0)

        # checkbox: pihu
        self.pihu = QCheckBox("Pi + Horizontal U Perm", self)
        self.pihu.setMaximumHeight(50)
        self.pihu.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pihu, 3, 0)

        # checkbox: pivu
        self.pivu = QCheckBox("Pi + Vertical U Perm", self)
        self.pivu.setMaximumHeight(50)
        self.pivu.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pivu, 4, 0)

        # checkbox: pio
        self.pio = QCheckBox("Pi + O Perm", self)
        self.pio.setMaximumHeight(50)
        self.pio.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pio, 5, 0)

        # checkbox: pizconj
        self.pizconj = QCheckBox("Pi + Z Perm Conjugates", self)
        self.pizconj.setMaximumHeight(50)
        self.pizconj.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pizconj, 6, 0)

        # checkbox: pi3s
        self.pi3s = QCheckBox("Pi + Triple Sledge", self)
        self.pi3s.setMaximumHeight(50)
        self.pi3s.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pi3s, 7, 0)

        # checkbox: phz
        self.pihz = QCheckBox("Pi + H or Z Perm", self)
        self.pihz.setMaximumHeight(50)
        self.pihz.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.pihz, 8, 0)

        # checkbox: showscramble
        self.showscr = QCheckBox("Show Scramble (from next time on)", self)
        self.showscr.setMaximumHeight(50)
        self.gridLayout.addWidget(self.showscr, 8, 2)

        # button to generate a scramble
        self.scramblegenbutton = QPushButton("Generate L2L Case (RETURN)", self)
        self.scramblegenbutton.setMinimumHeight(50)
        self.scramblegenbutton.setFocusPolicy(Qt.StrongFocus)
        self.scramblegenbutton.setToolTip("Generates a scramble to a L2L case of the defined type(s).")
        self.scramblegenbutton.clicked.connect(self.ScramblePlusColour)
        self.gridLayout.addWidget(self.scramblegenbutton, 9, 0)

        # this label shows the scramble
        self.scramblelabel = QLabel(self)
        self.scramblelabel.setMinimumHeight(50)
        self.scramblelabel.setText('')
        self.scramblelabel.setFont(QtGui.QFont("Monospace", 18))
        self.gridLayout.addWidget(self.scramblelabel, 9, 1)

        self.start = QPushButton("Start (SPACE)", self)
        self.start.setMinimumHeight(50)
        self.start.setToolTip("Starts (or stops) the timer.")
        self.start.clicked.connect(self.do_start)
        self.gridLayout.addWidget(self.start, 10, 0)

        self.reset = QPushButton("Reset (R)", self)
        self.reset.setMinimumHeight(50)
        self.reset.setToolTip("Resets the timer.")
        self.reset.clicked.connect(self.do_reset)
        self.gridLayout.addWidget(self.reset, 10, 2)

        self.lcd = QLCDNumber(self)
        self.lcd.setSmallDecimalPoint(True)
        self.lcd.setDigitCount(10)
        self.gridLayout.addWidget(self.lcd, 10, 1)
        self.timer = QTimer()
        self.timer.setInterval(2**0)
        self.timer.timeout.connect(self.tick)

        self.do_reset()

        self.scrpic = QLabel(self)
        self.scrpic.setMinimumHeight(50)
        self.scrpic.setPixmap(QtGui.QPixmap(os.path.join(os.path.dirname(__file__), "Icons/logogreen")).scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.gridLayout.addWidget(self.scrpic, 11, 0)

        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© 2019, Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        self.gridLayout.addWidget(self.creatorlabel, 11, 2)

        self.central.groupBox.setLayout(self.gridLayout)

        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def changescrlen(self):
        # find all corresponding sets of scrambles by using if-clauses to identify them
        # to store them, a new auxiliary list is used
        # if no checkbox is checked, just do nothing (rotate, rotate back)
        self.auxscrl = []
        if self.l4c.isChecked() == False and self.l5c.isChecked() == False and \
            self.p3s.isChecked() == False and self.phu.isChecked() == False and \
            self.phzpure.isChecked() == False and self.pi3s.isChecked() == False and \
            self.pihu.isChecked() == False and self.pihz.isChecked() == False and \
            self.pio.isChecked() == False and self.piswirl.isChecked() == False and \
            self.pivu.isChecked() == False and self.piwat.isChecked() == False and \
            self.pix.isChecked() == False and self.pizconj.isChecked() == False and \
            self.po.isChecked() == False and self.pswirl.isChecked() == False and \
            self.pvu.isChecked() == False and self.pwat.isChecked() == False and \
            self.px.isChecked() == False and self.pzconj.isChecked() == False:
            self.auxscrl.append("R R'")
        if self.l4c.isChecked():
            for i in range(len(self.scrl4c)):
                self.auxscrl.append(self.scrl4c.copy()[i])
        if self.l5c.isChecked():
            for i in range(len(self.scrl5c)):
                self.auxscrl.append(self.scrl5c.copy()[i])
        if self.p3s.isChecked():
            for i in range(len(self.scrp3s)):
                self.auxscrl.append(self.scrp3s.copy()[i])
        if self.phu.isChecked():
            for i in range(len(self.scrphu)):
                self.auxscrl.append(self.scrphu.copy()[i])
        if self.phzpure.isChecked():
            for i in range(len(self.scrphzpure)):
                self.auxscrl.append(self.scrphzpure.copy()[i])
        if self.pi3s.isChecked():
            for i in range(len(self.scrpi3s)):
                self.auxscrl.append(self.scrpi3s.copy()[i])
        if self.pihu.isChecked():
            for i in range(len(self.scrpihu)):
                self.auxscrl.append(self.scrpihu.copy()[i])
        if self.pihz.isChecked():
            for i in range(len(self.scrpihz)):
                self.auxscrl.append(self.scrpihz.copy()[i])
        if self.pio.isChecked():
            for i in range(len(self.scrpio)):
                self.auxscrl.append(self.scrpio.copy()[i])
        if self.piswirl.isChecked():
            for i in range(len(self.scrpiswirl)):
                self.auxscrl.append(self.scrpiswirl.copy()[i])
        if self.pivu.isChecked():
            for i in range(len(self.scrpivu)):
                self.auxscrl.append(self.scrpivu.copy()[i])
        if self.piwat.isChecked():
            for i in range(len(self.scrpiwat)):
                self.auxscrl.append(self.scrpiwat.copy()[i])
        if self.pix.isChecked():
            for i in range(len(self.scrpix)):
                self.auxscrl.append(self.scrpix.copy()[i])
        if self.pizconj.isChecked():
            for i in range(len(self.scrpizconj)):
                self.auxscrl.append(self.scrpizconj.copy()[i])
        if self.po.isChecked():
            for i in range(len(self.scrpo)):
                self.auxscrl.append(self.scrpo.copy()[i])
        if self.pswirl.isChecked():
            for i in range(len(self.scrpswirl)):
                self.auxscrl.append(self.scrpswirl.copy()[i])
        if self.pvu.isChecked():
            for i in range(len(self.scrpvu)):
                self.auxscrl.append(self.scrpvu.copy()[i])
        if self.pwat.isChecked():
            for i in range(len(self.scrpwat)):
                self.auxscrl.append(self.scrpwat.copy()[i])
        if self.px.isChecked():
            for i in range(len(self.scrpx)):
                self.auxscrl.append(self.scrpx.copy()[i])
        if self.pzconj.isChecked():
            for i in range(len(self.scrpzconj)):
                self.auxscrl.append(self.scrpzconj.copy()[i])
        # shuffle the scrambles and use the shuffled set
        random.shuffle(self.auxscrl)
        self.scramblelist = self.auxscrl

    def ScramblePlusColour(self):
        # if the scramblelist is empty, generate a new one
        if len(self.scramblelist) == 0:
            self.changescrlen()

        # take the last scramble in the list, use it, delete the last scramble on the list
        scramblezumanzeigen = self.scramblelist[-1]
        self.scramblelist.pop()
        self.scramblelabel.setText(scramblezumanzeigen)

        self.ShowScramble(scramblezumanzeigen)

        if self.showscr.isChecked():
            self.stack.setCurrentIndex(0)
        else:
            self.stack.setCurrentIndex(1)

    def display(self):
        # shows the current time (since zero / or zero itself) on the lcd
        self.lcd.display("%d:%05.2f" % (self.time // 60, self.time % 60))

    @pyqtSlot()
    def tick(self):
        # currently update the time, every 2**6/1000 ms, show it on the lcd
        self.time += 2**0/1000
        self.display()

    @pyqtSlot()
    def do_start(self):
        self.timer.start()
        self.start.setText("Pause (SPACE)")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_pause)

    @pyqtSlot()
    def do_pause(self):
        self.timer.stop()
        self.start.setText("Start (SPACE)")
        self.start.clicked.disconnect()
        self.start.clicked.connect(self.do_start)

    @pyqtSlot()
    def do_reset(self):
        # set time of the stopwatch back to zero, show the current time on the lcd
        self.time = 0
        self.display()

    def ShowScramble(self, scramble):
        # initial state of the stickers (ordered) and initial colors assigned to the stickers
        # (abbreviations)
        stickercol = ["o", "o", "o", "o", "o", "g", "g", "g", "g", "g", "y", "y", "y", "y", "y",
                      "w", "w", "w", "w", "w", "r", "r", "r", "r", "r", "b", "b", "b", "b", "b"]
        # take the scramble (type: string) and split it into single moves (split at every space)
        scrsplit = scramble.split()
        # perform three- or fourswaps with the stickers, corresponding to the given move
        # each line represents one orbit of stickers where the cycle happens
        # upper- and lowercase characters are supported, as well as rotations and double moves
        for i in scrsplit:
            if i == "x":
                fourswap(stickercol, 15, 25, 10, 5)
                fourswap(stickercol, 24, 21, 22, 23)
                fourswap(stickercol, 2, 1, 4, 3)
                fourswap(stickercol, 17, 29, 12, 7)
                fourswap(stickercol, 6, 16, 28, 11)
                fourswap(stickercol, 9, 19, 27, 14)
                fourswap(stickercol, 18, 26, 13, 8)
            elif i == "x'":
                fourswap(stickercol, 5, 10, 25, 15)
                fourswap(stickercol, 23, 22, 21, 24)
                fourswap(stickercol, 3, 4, 1, 2)
                fourswap(stickercol, 7, 12, 29, 17)
                fourswap(stickercol, 11, 28, 16, 6)
                fourswap(stickercol, 14, 27, 19, 9)
                fourswap(stickercol, 8, 13, 26, 18)
            elif i == "x2":
                fourswap(stickercol, 5, 10, 25, 15)
                fourswap(stickercol, 23, 22, 21, 24)
                fourswap(stickercol, 3, 4, 1, 2)
                fourswap(stickercol, 7, 12, 29, 17)
                fourswap(stickercol, 11, 28, 16, 6)
                fourswap(stickercol, 14, 27, 19, 9)
                fourswap(stickercol, 8, 13, 26, 18)
                fourswap(stickercol, 5, 10, 25, 15)
                fourswap(stickercol, 23, 22, 21, 24)
                fourswap(stickercol, 3, 4, 1, 2)
                fourswap(stickercol, 7, 12, 29, 17)
                fourswap(stickercol, 11, 28, 16, 6)
                fourswap(stickercol, 14, 27, 19, 9)
                fourswap(stickercol, 8, 13, 26, 18)
            elif i == "y":
                fourswap(stickercol, 19, 16, 17, 18)
                fourswap(stickercol, 14, 13, 12, 11)
                fourswap(stickercol, 25, 20, 5, 0)
                fourswap(stickercol, 21, 6, 1, 26)
                fourswap(stickercol, 29, 24, 9, 4)
                fourswap(stickercol, 23, 8, 3, 28)
                fourswap(stickercol, 27, 22, 7, 2)
            elif i == "y'":
                fourswap(stickercol, 18, 17, 16, 19)
                fourswap(stickercol, 11, 12, 13, 14)
                fourswap(stickercol, 0, 5, 20, 25)
                fourswap(stickercol, 26, 1, 6, 21)
                fourswap(stickercol, 4, 9, 24, 29)
                fourswap(stickercol, 28, 3, 8, 23)
                fourswap(stickercol, 2, 7, 22, 27)
            elif i == "y'":
                fourswap(stickercol, 18, 17, 16, 19)
                fourswap(stickercol, 11, 12, 13, 14)
                fourswap(stickercol, 0, 5, 20, 25)
                fourswap(stickercol, 26, 1, 6, 21)
                fourswap(stickercol, 4, 9, 24, 29)
                fourswap(stickercol, 28, 3, 8, 23)
                fourswap(stickercol, 2, 7, 22, 27)
                fourswap(stickercol, 18, 17, 16, 19)
                fourswap(stickercol, 11, 12, 13, 14)
                fourswap(stickercol, 0, 5, 20, 25)
                fourswap(stickercol, 26, 1, 6, 21)
                fourswap(stickercol, 4, 9, 24, 29)
                fourswap(stickercol, 28, 3, 8, 23)
                fourswap(stickercol, 2, 7, 22, 27)
            elif i == "z":
                fourswap(stickercol, 15, 20, 10, 0)
                fourswap(stickercol, 9, 6, 7, 8)
                fourswap(stickercol, 29, 28, 27, 26)
                fourswap(stickercol, 18, 24, 11, 2)
                fourswap(stickercol, 17, 23, 14, 1)
                fourswap(stickercol, 19, 21, 12, 3)
                fourswap(stickercol, 16, 22, 13, 4)
            elif i == "z'":
                fourswap(stickercol, 0, 10, 20, 15)
                fourswap(stickercol, 8, 7, 6, 9)
                fourswap(stickercol, 26, 27, 28, 29)
                fourswap(stickercol, 2, 11, 24, 18)
                fourswap(stickercol, 1, 14, 23, 17)
                fourswap(stickercol, 3, 12, 21, 19)
                fourswap(stickercol, 4, 13, 22, 16)
            elif i == "z2":
                fourswap(stickercol, 0, 10, 20, 15)
                fourswap(stickercol, 8, 7, 6, 9)
                fourswap(stickercol, 26, 27, 28, 29)
                fourswap(stickercol, 2, 11, 24, 18)
                fourswap(stickercol, 1, 14, 23, 17)
                fourswap(stickercol, 3, 12, 21, 19)
                fourswap(stickercol, 4, 13, 22, 16)
                fourswap(stickercol, 0, 10, 20, 15)
                fourswap(stickercol, 8, 7, 6, 9)
                fourswap(stickercol, 26, 27, 28, 29)
                fourswap(stickercol, 2, 11, 24, 18)
                fourswap(stickercol, 1, 14, 23, 17)
                fourswap(stickercol, 3, 12, 21, 19)
                fourswap(stickercol, 4, 13, 22, 16)
            elif i == "r" or i == "r'2":
                threeswap(stickercol, 3, 7, 16)
                threeswap(stickercol, 10, 20, 25)
                threeswap(stickercol, 11, 21, 27)
                threeswap(stickercol, 12, 22, 28)
                threeswap(stickercol, 13, 23, 29)
            elif i == "r'" or i == "r2":
                threeswap(stickercol, 16, 7, 3)
                threeswap(stickercol, 25, 20, 10)
                threeswap(stickercol, 27, 21, 11)
                threeswap(stickercol, 28, 22, 12)
                threeswap(stickercol, 29, 23, 13)
            elif i == "R" or i == "R'2":
                threeswap(stickercol, 15, 25, 20)
                threeswap(stickercol, 16, 29, 21)
                threeswap(stickercol, 17, 26, 22)
                threeswap(stickercol, 24, 19, 28)
                threeswap(stickercol, 6, 4, 12)
            elif i == "R'" or i == "R2":
                threeswap(stickercol, 20, 25, 15)
                threeswap(stickercol, 21, 29, 16)
                threeswap(stickercol, 22, 26, 17)
                threeswap(stickercol, 28, 19, 24)
                threeswap(stickercol, 12, 4, 6)
            elif i == "l" or i == "L" or i == "l'2" or i == "L'2":
                threeswap(stickercol, 0, 5, 10)
                threeswap(stickercol, 1, 7, 13)
                threeswap(stickercol, 2, 8, 14)
                threeswap(stickercol, 3, 9, 11)
                threeswap(stickercol, 18, 23, 27)
            elif i == "l'" or i == "L'" or i == "l2" or i == "L2":
                threeswap(stickercol, 10, 5, 0)
                threeswap(stickercol, 13, 7, 1)
                threeswap(stickercol, 14, 8, 2)
                threeswap(stickercol, 11, 9, 3)
                threeswap(stickercol, 27, 23, 18)
            elif i == "f" or i == "f'2":
                threeswap(stickercol, 5, 20, 10)
                threeswap(stickercol, 7, 23, 11)
                threeswap(stickercol, 17, 28, 2)
                threeswap(stickercol, 24, 12, 8)
                threeswap(stickercol, 6, 22, 14)
            elif i == "f'" or i == "f2":
                threeswap(stickercol, 10, 20, 5)
                threeswap(stickercol, 11, 23, 7)
                threeswap(stickercol, 2, 28, 17)
                threeswap(stickercol, 8, 12, 24)
                threeswap(stickercol, 14, 22, 6)
            elif i == "B" or i == "U" or i == "B'2" or i == "U'2":
                threeswap(stickercol, 0, 25, 15)
                threeswap(stickercol, 1, 27, 16)
                threeswap(stickercol, 3, 29, 18)
                threeswap(stickercol, 4, 26, 19)
                threeswap(stickercol, 9, 13, 21)
            elif i == "B'" or i == "U'" or i == "B2" or i == "U2":
                threeswap(stickercol, 15, 25, 0)
                threeswap(stickercol, 16, 27, 1)
                threeswap(stickercol, 18, 29, 3)
                threeswap(stickercol, 19, 26, 4)
                threeswap(stickercol, 21, 13, 9)
            elif i == "b" or i == "b'2":
                threeswap(stickercol, 0, 10, 25)
                threeswap(stickercol, 2, 12, 26)
                threeswap(stickercol, 3, 13, 27)
                threeswap(stickercol, 4, 14, 28)
                threeswap(stickercol, 8, 22, 19)
            else:
                #
                #(25, 10, 0)(26, 12, 2)(27, 13, 3)(28, 14, 4)(19, 22, 8)
                threeswap(stickercol, 25, 10, 0)
                threeswap(stickercol, 26, 12, 2)
                threeswap(stickercol, 27, 13, 3)
                threeswap(stickercol, 28, 14, 4)
                threeswap(stickercol, 19, 22, 8)

        # draws the scramble by drawing several polygons corresponding to the scramble
        # generate object of class ScrambleDrawing with the current state of scrambled stickers
        # (using variable stickercol)
        # define geometry, placement inside Layout
        self.drawscrwidget = ScrambleDrawing(stickercol)


        self.alternativepic = QLabel(" ")
        self.alternativepic.setAutoFillBackground(True)

        # stacked widget: switch between scramble image
        # and no image is made possible
        self.stack = QStackedWidget()
        self.stack.setFixedHeight(430)
        self.stack.setFixedWidth(500)
        self.stack.addWidget(self.drawscrwidget)
        self.stack.addWidget(self.alternativepic)
        self.stack.setCurrentIndex(0)
        self.gridLayout.addWidget(self.stack, 9, 2)

    def StartFirstLayerTrainer(self):
        # close the current window and open the one requested
        self.close()
        self.windowFLT = WindowFLT()
        self.windowFLT.showMaximized()

    def StartAlgTrainer(self):
        # close the current window and open the one requested
        self.close()
        self.windowL2LT = WindowL2LT()
        self.windowL2LT.showMaximized()
    '''
    def StartCompSim(self):
        # ToDo
        pass

    def StartQuiz(self):
        # ToDo
        pass
    '''

class Help(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Skewb Skills: Help"
        self.top = 50
        self.left = 50
        self.width = 1000
        self.height = 800

        self.setWindowIcon(QtGui.QIcon(os.path.join(os.path.dirname(__file__), "Icons/logoicon.png")))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.mainMenu = self.menuBar()
        self.generalMenu = self.mainMenu.addMenu('General Functions')

        self.helpbut = QAction('Close Help Window', self)
        self.helpbut.setShortcut(Qt.Key_Escape)
        self.helpbut.triggered.connect(self.close)
        self.generalMenu.addAction(self.helpbut)

        self.central2 = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central2)

    def CreateLayout(self):
        self.central2.groupBox2 = QGroupBox("Help")
        self.central2.groupBox2.setFont(QtGui.QFont("Sansserif", 13))
        self.gridLayout2 = QGridLayout()

        self.textlabel = QLabel(self)
        self.textlabel.setFont(QtGui.QFont("Sansserif", 12))
        self.textlabel.setText("How to use SkewbSkills?")
        self.gridLayout2.addWidget(self.textlabel, 0, 0)

        self.textlabel2 = QLabel(self)
        self.textlabel2.setFont(QtGui.QFont("Sansserif", 11))
        self.textlabel2.setText("Choose one of the practicing modes by pressing the "
                               "corresponding button in the starting window\nor by choosing "
                               "the corresponding keys: press 'F' to start the "
                               "First Layer Trainer,\nor press 'A' to start the L2L Alg Trainer.")
        self.gridLayout2.addWidget(self.textlabel2, 1, 0)

        self.textlabel3 = QLabel(self)
        self.textlabel3.setFont(QtGui.QFont("Sansserif", 12))
        self.textlabel3.setText("How to use the First Layer Trainer?")
        self.gridLayout2.addWidget(self.textlabel3, 2, 0)

        self.textlabel4 = QLabel(self)
        self.textlabel4.setFont(QtGui.QFont("Sansserif", 11))
        self.textlabel4.setText("Choose whether you want to receive a shuffled set of scrambles "
                                "by (un-)selecting the checkbox. This feature can also be toggled"
                                " with the 'S' key.\n"
                                "Decide if you want to use all six colours as your starting "
                                "colour. Because the colours are attached onto the scrambles list,"
                                " you need to shuffle the scrambles to use this feature.\n"
                                "Use the slider or one of the keys between '1' and '7' to choose"
                                " the scramble length.\n"
                                "Press RETURN or click the button 'Generate Scramble + Colour',"
                                " and a new scramble appears. You then have the option to time"
                                " yourself by pressing the 'Start' button (or use the spacebar).\n"
                                "If you need to reset the timer, use the 'Reset' button or"
                                " the 'R' key on yout keyboard.")
        self.gridLayout2.addWidget(self.textlabel4, 3, 0)

        self.textlabel5 = QLabel(self)
        self.textlabel5.setFont(QtGui.QFont("Sansserif", 12))
        self.textlabel5.setText("How to use the Alg Trainer?")
        self.gridLayout2.addWidget(self.textlabel5, 4, 0)

        self.textlabel6 = QLabel(self)
        self.textlabel6.setFont(QtGui.QFont("Sansserif", 11))
        self.textlabel6.setText("Choose which alg sets you want to practice "
                                "by (un-)selecting the checkboxes.\n"
                                "There are several options to choose, but if you want to quickly"
                                " (un-)select several alg sets, you can press 'T' to toggle all"
                                " alg sets.\n"
                                "Pressing 'U' toggles all Peanut cases, 'I' toggles all Pi cases"
                                " and 'L' toggles L4C / L5C cases.\n"
                                "Press RETURN or click the button 'Generate L2L Case',"
                                " and a new scramble appears. You then have the option to time"
                                " yourself by pressing the 'Start' button (or use the spacebar).\n"
                                "If you need to reset the timer, use the 'Reset' button or"
                                " the 'R' key on yout keyboard.")
        self.gridLayout2.addWidget(self.textlabel6, 5, 0)

        self.central2.groupBox2.setLayout(self.gridLayout2)

        vbox = QVBoxLayout()
        vbox.addWidget(self.central2.groupBox2)
        self.central2.setLayout(vbox)

class ScrambleDrawing(QWidget):
    def __init__(self, stickers):
        # each scrambledrawing needs a list containing each sticker, the entries are the
        # abbreviations of the colors
        super().__init__()
        self.stic = stickers

    def paintEvent(self, QPaintEvent):
        # overload and start the drawScr-function each time sth has to be drawn / painted
        painter = QtGui.QPainter(self)
        self.drawScr(painter, self.stic)

    def drawScr(self, painter, s):
        # set a polygon for each sticker and paint it with the color that's mentioned in the list
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s,0), Qt.SolidPattern))
        painter.drawPolygon(QPoint(0, 75), QPoint(60, 30), QPoint(120, 135), QPoint(60, 180))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 1), Qt.SolidPattern))
        painter.drawPolygon(QPoint(60, 30), QPoint(120, 135), QPoint(120, 60))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 2), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 135), QPoint(120, 210), QPoint(60, 180))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 3), Qt.SolidPattern))
        painter.drawPolygon(QPoint(0, 75), QPoint(60, 180), QPoint(0, 150))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 4), Qt.SolidPattern))
        painter.drawPolygon(QPoint(0, 0), QPoint(60, 30), QPoint(0, 75))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 5), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 135), QPoint(180, 90), QPoint(240, 195), QPoint(180, 240))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 6), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 90), QPoint(240, 120), QPoint(240, 195))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 7), Qt.SolidPattern))
        painter.drawPolygon(QPoint(240, 195), QPoint(240, 270), QPoint(180, 240))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 8), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 135), QPoint(180, 240), QPoint(120, 210))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 9), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 60), QPoint(180, 90), QPoint(120, 135))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 10), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 240), QPoint(240, 345), QPoint(180, 390), QPoint(120, 285))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 11), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 240), QPoint(240, 270), QPoint(240, 345))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 12), Qt.SolidPattern))
        painter.drawPolygon(QPoint(240, 345), QPoint(240, 420), QPoint(180, 390))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 13), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 285), QPoint(180, 390), QPoint(120, 360))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 14), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 210), QPoint(180, 240), QPoint(120, 285))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 15), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 90), QPoint(180, 30), QPoint(300, 30), QPoint(300, 90))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 16), Qt.SolidPattern))
        painter.drawPolygon(QPoint(300, 30), QPoint(360, 60), QPoint(300, 90))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 17), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 90), QPoint(300, 90), QPoint(240, 120))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 18), Qt.SolidPattern))
        painter.drawPolygon(QPoint(120, 60), QPoint(180, 30), QPoint(180, 90))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 19), Qt.SolidPattern))
        painter.drawPolygon(QPoint(180, 30), QPoint(240, 0), QPoint(300, 30))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 20), Qt.SolidPattern))
        painter.drawPolygon(QPoint(240, 195), QPoint(300, 90), QPoint(360, 135), QPoint(300, 240))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 21), Qt.SolidPattern))
        painter.drawPolygon(QPoint(300, 90), QPoint(360, 60), QPoint(360, 135))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 22), Qt.SolidPattern))
        painter.drawPolygon(QPoint(300, 240), QPoint(360, 135), QPoint(360, 210))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 23), Qt.SolidPattern))
        painter.drawPolygon(QPoint(240, 195), QPoint(300, 240), QPoint(240, 270))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 24), Qt.SolidPattern))
        painter.drawPolygon(QPoint(240, 120), QPoint(300, 90), QPoint(240, 195))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 25), Qt.SolidPattern))
        painter.drawPolygon(QPoint(360, 135), QPoint(420, 30), QPoint(480, 75), QPoint(420, 180))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 26), Qt.SolidPattern))
        painter.drawPolygon(QPoint(420, 30), QPoint(480, 0), QPoint(480, 75))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 27), Qt.SolidPattern))
        painter.drawPolygon(QPoint(420, 180), QPoint(480, 75), QPoint(480, 150))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 28), Qt.SolidPattern))
        painter.drawPolygon(QPoint(360, 135), QPoint(420, 180), QPoint(360, 210))
        painter.setPen(QtGui.QPen(Qt.black, 3, Qt.SolidLine))
        painter.setBrush(QtGui.QBrush(corrcol(s, 29), Qt.SolidPattern))
        painter.drawPolygon(QPoint(360, 60), QPoint(420, 30), QPoint(360, 135))

def threeswap(listname,i,j,k):
    # cycles three elements i,j,k of a given list by performing two transpositions
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]

def fourswap(listname,i,j,k,l):
    # same as threeswap, but cycles four elements i,j,k,l, which needs three transpositions
    listname[k], listname[l] = listname[l], listname[k]
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]

def corrcol(list,i):
    # returns the correct color for each possible entry of the list containing all stickers in
    # the correct order (therefore we also need the index i)
    # no orange predefined in PyQt --> choose RGB codes
    if list[i] == "o":
        return QtGui.QColor( 0xFF, 0x68, 0x00 )
    elif list[i] == "g":
        return Qt.green
    elif list[i] == "r":
        return Qt.red
    elif list[i] == "b":
        return Qt.blue
    elif list[i] == "w":
        return Qt.white
    else:
        return Qt.yellow

if __name__ == "__main__":
    # to be executed if this module has been started directly, not through another module
    App = QApplication(sys.argv)
    startwindow = StartWindow()
    sys.exit(App.exec())

