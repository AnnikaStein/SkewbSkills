import random
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QCheckBox, QPushButton, QLabel, QSlider, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QPoint

class StartWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Skewb Skills"
        self.top = 100
        self.left = 500
        self.width = 1000
        self.height = 750

        self.setWindowIcon(QtGui.QIcon("logoicon.png"))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)
        self.windowFLT = WindowFLT()
        self.windowL2LT = WindowL2LT()
        self.show()

    def CreateLayout(self):
        # starting to define the layout of the CentralWidget
        self.central.groupBox = QGroupBox("How do you want to practice?")
        self.central.groupBox.setFont(QtGui.QFont("Sansserif", 13))
        gridLayout = QGridLayout()

        # button to start the first layer trainer
        self.firstlayerbut = QPushButton("First Layer Trainer (or press F)", self)
        self.firstlayerbut.setMinimumHeight(80)
        self.firstlayerbut.setToolTip("Generates scrambles from 1 up to 7 moves and random "
                                          "colours to start the first layer with, if you wish.")
        self.firstlayerbut.clicked.connect(self.StartFirstLayerTrainer)
        self.firstlayerbut.setShortcut(QtGui.QKeySequence(Qt.Key_F))
        gridLayout.addWidget(self.firstlayerbut, 0, 0)

        # button to start the alg trainer
        self.algbut = QPushButton("Alg Trainer (or press A)", self)
        self.algbut.setMinimumHeight(80)
        self.algbut.setToolTip("Shows you L2L-cases (and corresponding algs if needed).\n"
                               "Follows a flashcard principle, define piles of cases you know "
                               "or want to work on.")
        self.algbut.clicked.connect(self.StartAlgTrainer)
        self.algbut.setShortcut(QtGui.QKeySequence(Qt.Key_A))
        gridLayout.addWidget(self.algbut, 0, 1)

        # button to start the comp sim
        self.compsimbut = QPushButton("Comp Sim (or press C)", self)
        self.compsimbut.setMinimumHeight(80)
        self.compsimbut.setToolTip("Starts the competition simulation in a new window.")
        self.compsimbut.clicked.connect(self.StartCompSim)
        self.compsimbut.setShortcut(QtGui.QKeySequence(Qt.Key_C))
        gridLayout.addWidget(self.compsimbut, 1, 0)

        # button to start the quiz
        self.firstlayerbut = QPushButton("Quiz (or press Q)", self)
        self.firstlayerbut.setMinimumHeight(80)
        self.firstlayerbut.setToolTip("Starts a new quiz window.")
        self.firstlayerbut.clicked.connect(self.StartQuiz)
        self.firstlayerbut.setShortcut(QtGui.QKeySequence(Qt.Key_Q))
        gridLayout.addWidget(self.firstlayerbut, 1, 1)

        # this label shows a picture
        self.scrpic = QLabel(self)
        self.scrpic.setMinimumHeight(50)
        self.scrpic.setPixmap(QtGui.QPixmap("logogreen").scaled(50, 50, Qt.KeepAspectRatio, Qt.FastTransformation))
        gridLayout.addWidget(self.scrpic, 2, 0)

        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        gridLayout.addWidget(self.creatorlabel, 2, 1)

        self.central.groupBox.setLayout(gridLayout)

        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def StartFirstLayerTrainer(self):
        self.close()
        self.windowFLT.show()

    def StartAlgTrainer(self):
        self.close()
        self.windowL2LT.show()

    def StartCompSim(self):
        pass

    def StartQuiz(self):
        pass

class WindowFLT(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Skewb Skills"
        self.top = 100
        self.left = 500
        self.width = 1000
        self.height = 750

        self.setWindowIcon(QtGui.QIcon("logoicon.png"))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.ReadAllScrambles()
        
        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)

    def ReadAllScrambles(self):
        # with a given file that consists of all scrambles to a given number of moves and
        # all possible starting colours, the next few lines of code generate a list of all lines
        # in the scrambles.txt-File and append groups of two elements of this list to the
        # final scramblelist
        self.scramble1list = []
        self.kombiscramblelist = []
        datei = open('scrambles1.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble1list.append(kombi)

        self.scramble2list = []
        self.kombiscramblelist = []
        datei = open('scrambles2.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble2list.append(kombi)

        self.scramble3list = []
        self.kombiscramblelist = []
        datei = open('scrambles3.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble3list.append(kombi)

        self.scramble4list = []
        self.kombiscramblelist = []
        datei = open('scrambles4.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble4list.append(kombi)

        self.scramble5list = []
        self.kombiscramblelist = []
        datei = open('scrambles5.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble5list.append(kombi)

        self.scramble6list = []
        self.kombiscramblelist = []
        datei = open('scrambles6.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble6list.append(kombi)

        self.scramble7list = []
        self.kombiscramblelist = []
        datei = open('scrambles7.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble7list.append(kombi)

        #### ONLY WHITE
        self.scramble1wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles1w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble1wlist.append(kombi)
        self.scramblelist = self.scramble1wlist.copy()

        self.scramble2wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles2w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble2wlist.append(kombi)

        self.scramble3wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles3w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble3wlist.append(kombi)

        self.scramble4wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles4w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble4wlist.append(kombi)

        self.scramble5wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles5w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble5wlist.append(kombi)

        self.scramble6wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles6w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble6wlist.append(kombi)

        self.scramble7wlist = []
        self.kombiscramblelist = []
        datei = open('scrambles7w.txt', 'r', encoding='utf-8')
        for line in datei:
            self.kombiscramblelist.append(line[:-1])
        for i in range(0, len(self.kombiscramblelist), 2):
            s = self.kombiscramblelist[i]
            c = self.kombiscramblelist[i + 1]
            kombi = [s, c]
            self.scramble7wlist.append(kombi)

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
        self.anycolourchecker.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.anycolourchecker, 0, 1)

        # slider to define the scramble length
        self.scrlenslider = QSlider(Qt.Horizontal)
        self.scrlenslider.setMinimum(1)
        self.scrlenslider.setMaximum(7)
        self.scrlenslider.setValue(1)
        self.scrlenslider.setTickPosition(QSlider.TicksBelow)
        self.scrlenslider.setTickInterval(1)
        self.scrlenslider.setToolTip("Change the scramble length from 1 on the left to 7 on the right.")
        self.gridLayout.addWidget(self.scrlenslider, 1, 0)
        self.scrlenslider.setMinimumWidth(70)
        self.scrlenslider.valueChanged.connect(self.changescrlen)

        # button to generate a scramble and a random colour to start the first layer with
        self.scramblegenbutton = QPushButton("Generate Scramble + Colour\n (or press Spacebar)", self)
        self.scramblegenbutton.setMinimumHeight(80)
        self.scramblegenbutton.setToolTip("Generates a scramble of the defined length and "
                                     "a random colour to start the first layer with.")
        self.scramblegenbutton.clicked.connect(self.ScramblePlusColour)
        self.scramblegenbutton.setShortcut(QtGui.QKeySequence(Qt.Key_Space))
        self.gridLayout.addWidget(self.scramblegenbutton, 1, 1)

        # this label shows the scramble
        self.scramblelabel = QLabel(self)
        self.scramblelabel.setMinimumHeight(50)
        self.scramblelabel.setText('')
        self.scramblelabel.setFont(QtGui.QFont("Monospace", 20))
        self.gridLayout.addWidget(self.scramblelabel, 2, 0)

        # this label shows the colour
        self.colourlabel = QLabel(self)
        self.colourlabel.setMinimumHeight(50)
        self.colourlabel.setStyleSheet('background-color : transparent')
        self.gridLayout.addWidget(self.colourlabel, 2, 1)
        '''
        # draws the scramble by drawing several polygongs corresponding to the scramble
        self.drawscrwidget = ScrambleDrawing()
        self.drawscrwidget.setMinimumHeight(120)
        gridLayout.addWidget(self.drawscrwidget, 3, 0)
        '''
        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        self.gridLayout.addWidget(self.creatorlabel, 3, 1)

        self.central.groupBox.setLayout(self.gridLayout)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def changescrlen(self):

        scrlen = self.scrlenslider.value()

        if scrlen == 1:
            if self.anycolourchecker.isChecked():
                self.auxscrl = self.scramble1list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscrl)
                    self.scramblelist = self.auxscrl
                else:
                    self.scramblelist = self.auxscrl
            else:
                self.auxscrl = self.scramble1wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscrl)
                    self.scramblelist = self.auxscrl
                else:
                    self.scramblelist = self.auxscrl
        elif scrlen == 2:
            if self.anycolourchecker.isChecked():
                self.auxscr2 = self.scramble2list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr2)
                    self.scramblelist = self.auxscr2
                else:
                    self.scramblelist = self.auxscr2
            else:
                self.auxscr2 = self.scramble2wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr2)
                    self.scramblelist = self.auxscr2
                else:
                    self.scramblelist = self.auxscr2
        elif scrlen == 3:
            if self.anycolourchecker.isChecked():
                self.auxscr3 = self.scramble3list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr3)
                    self.scramblelist = self.auxscr3
                else:
                    self.scramblelist = self.auxscr3
            else:
                self.auxscr3 = self.scramble3wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr3)
                    self.scramblelist = self.auxscr3
                else:
                    self.scramblelist = self.auxscr3
        elif scrlen == 4:
            if self.anycolourchecker.isChecked():
                self.auxscr4 = self.scramble4list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr4)
                    self.scramblelist = self.auxscr4
                else:
                    self.scramblelist = self.auxscr4
            else:
                self.auxscr4 = self.scramble4wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr4)
                    self.scramblelist = self.auxscr4
                else:
                    self.scramblelist = self.auxscr4
        elif scrlen == 5:
            if self.anycolourchecker.isChecked():
                self.auxscr5 = self.scramble5list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr5)
                    self.scramblelist = self.auxscr5
                else:
                    self.scramblelist = self.auxscr5
            else:
                self.auxscr5 = self.scramble5wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr5)
                    self.scramblelist = self.auxscr5
                else:
                    self.scramblelist = self.auxscr5
        elif scrlen == 6:
            if self.anycolourchecker.isChecked():
                self.auxscr6 = self.scramble6list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr6)
                    self.scramblelist = self.auxscr6
                else:
                    self.scramblelist = self.auxscr6
            else:
                self.auxscr6 = self.scramble6wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr6)
                    self.scramblelist = self.auxscr6
                else:
                    self.scramblelist = self.auxscr6
        else:
            if self.anycolourchecker.isChecked():
                self.auxscr7 = self.scramble7list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr7)
                    self.scramblelist = self.auxscr7
                else:
                    self.scramblelist = self.auxscr7
            else:
                self.auxscr7 = self.scramble7wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr7)
                    self.scramblelist = self.auxscr7
                else:
                    self.scramblelist = self.auxscr7

    def ScramblePlusColour(self):

        if len(self.scramblelist) == 0:
            self.changescrlen()

        scramblezumanzeigen = self.scramblelist[-1]
        self.scramblelist.pop()
        self.scramblelabel.setText(scramblezumanzeigen[0])

        # rufe hier nun die Funktion auf, die den ausgewählten Scramble zeichnet

        self.ShowScramble(scramblezumanzeigen[0])

        if scramblezumanzeigen[1] == "w":
            self.colourlabel.setStyleSheet('background-color : white')
        elif scramblezumanzeigen[1] == "y":
            self.colourlabel.setStyleSheet('background-color : yellow')
        elif scramblezumanzeigen[1] == "g":
            self.colourlabel.setStyleSheet('background-color : green')
        elif scramblezumanzeigen[1] == "r":
            self.colourlabel.setStyleSheet('background-color : red')
        elif scramblezumanzeigen[1] == "b":
            self.colourlabel.setStyleSheet('background-color : blue')
        else:
            self.colourlabel.setStyleSheet('background-color : orange')

    def ShowScramble(self, scramble):
        stickercol = ["o", "o", "o", "o", "o", "g", "g", "g", "g", "g", "y", "y", "y", "y", "y",
                      "w", "w", "w", "w", "w", "r", "r", "r", "r", "r", "b", "b", "b", "b", "b"]
        scrsplit = scramble.split()
        for i in scrsplit:
            if i == "R":
                #(4, 8, 17)(11, 21, 26)(12, 22, 28)(13, 23, 29)(14, 24, 30)
                #(3, 7, 16)(10, 20, 25)(11, 21, 27)(12, 22, 28)(13, 23, 29)
                threeswap(stickercol, 3, 7, 16)
                threeswap(stickercol, 10, 20, 25)
                threeswap(stickercol, 11, 21, 27)
                threeswap(stickercol, 12, 22, 28)
                threeswap(stickercol, 13, 23, 29)
            elif i == "R'":
                #
                #(16, 7, 3)(25, 20, 10)(27, 21, 11)(28, 22, 12)(29, 23, 13)
                threeswap(stickercol, 16, 7, 3)
                threeswap(stickercol, 25, 20, 10)
                threeswap(stickercol, 27, 21, 11)
                threeswap(stickercol, 28, 22, 12)
                threeswap(stickercol, 29, 23, 13)
            elif i == "L":
                #(1, 6, 11)(2, 8, 14)(3, 9, 15)(4, 10, 12)(19, 24, 28)
                #(0, 5, 10)(1, 7, 13)(2, 8, 14)(3, 9, 11)(18, 23, 27)
                threeswap(stickercol, 0, 5, 10)
                threeswap(stickercol, 1, 7, 13)
                threeswap(stickercol, 2, 8, 14)
                threeswap(stickercol, 3, 9, 11)
                threeswap(stickercol, 18, 23, 27)
            elif i == "L'":
                #
                #(10, 5, 0)(13, 7, 1)(14, 8, 2)(11, 9, 3)(27, 23, 18)
                threeswap(stickercol, 10, 5, 0)
                threeswap(stickercol, 13, 7, 1)
                threeswap(stickercol, 14, 8, 2)
                threeswap(stickercol, 11, 9, 3)
                threeswap(stickercol, 27, 23, 18)
            elif i == "U":
                #(1, 26, 16)(2, 28, 17)(4, 30, 19)(5, 27, 20)(10, 14, 22)
                #(0, 25, 15)(1, 27, 16)(3, 29, 18)(4, 26, 19)(9, 13, 21)
                threeswap(stickercol, 0, 25, 15)
                threeswap(stickercol, 1, 27, 16)
                threeswap(stickercol, 3, 29, 18)
                threeswap(stickercol, 4, 26, 19)
                threeswap(stickercol, 9, 13, 21)
            elif i == "U'":
                #
                #(15, 25, 0)(16, 27, 1)(18, 29, 3)(19, 26, 4)(21, 13, 9)
                threeswap(stickercol, 15, 25, 0)
                threeswap(stickercol, 16, 27, 1)
                threeswap(stickercol, 18, 29, 3)
                threeswap(stickercol, 19, 26, 4)
                threeswap(stickercol, 21, 13, 9)
            elif i == "B":
                #(1, 11, 26)(3, 13, 27)(4, 14, 28)(5, 15, 29)(9, 23, 20)
                #(0, 10, 25)(2, 12, 26)(3, 13, 27)(4, 14, 28)(8, 22, 19)
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
        self.drawscrwidget = ScrambleDrawing(stickercol)
        self.drawscrwidget.setMinimumHeight(430)
        self.gridLayout.addWidget(self.drawscrwidget, 3, 0)

class WindowL2LT(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Skewb Skills"
        self.top = 100
        self.left = 500
        self.width = 1000
        self.height = 750

        self.setWindowIcon(QtGui.QIcon("logoicon.png"))

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        #self.ReadAllScrambles()

        self.central = QWidget()
        self.CreateLayout()
        self.setCentralWidget(self.central)#

    def ReadAllScrambles(self):
        self.piswirl = []
        datei = open('piswirl.txt', 'r', encoding='utf-8')
        for line in datei:
            self.piswirl.append(line[:-1])

        self.piwat = []
        datei = open('piwat.txt', 'r', encoding='utf-8')
        for line in datei:
            self.piwat.append(line[:-1])

        self.pix = []
        datei = open('pix.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pix.append(line[:-1])

        self.pihu = []
        datei = open('pihu.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pihu.append(line[:-1])

        self.pivu = []
        datei = open('pivu.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pivu.append(line[:-1])

        self.pio = []
        datei = open('pio.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pio.append(line[:-1])

        self.pizconj = []
        datei = open('pizconj.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pizconj.append(line[:-1])

        self.pi3s = []
        datei = open('pi3z.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pi3s.append(line[:-1])

        self.pihz = []
        datei = open('pihz.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pihz.append(line[:-1])

        self.pswirl = []
        datei = open('pswirl.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pswirl.append(line[:-1])

        self.pwat = []
        datei = open('pwat.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pwat.append(line[:-1])

        self.px = []
        datei = open('px.txt', 'r', encoding='utf-8')
        for line in datei:
            self.px.append(line[:-1])

        self.phu = []
        datei = open('phu.txt', 'r', encoding='utf-8')
        for line in datei:
            self.phu.append(line[:-1])

        self.pvu = []
        datei = open('pvu.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pvu.append(line[:-1])

        self.po = []
        datei = open('po.txt', 'r', encoding='utf-8')
        for line in datei:
            self.po.append(line[:-1])

        self.pzconj = []
        datei = open('pzconj.txt', 'r', encoding='utf-8')
        for line in datei:
            self.pzconj.append(line[:-1])

        self.p3s = []
        datei = open('p3z.txt', 'r', encoding='utf-8')
        for line in datei:
            self.p3s.append(line[:-1])

        self.phzpure = []
        datei = open('phzpure.txt', 'r', encoding='utf-8')
        for line in datei:
            self.phzpure.append(line[:-1])

        self.l4c = []
        datei = open('l4c.txt', 'r', encoding='utf-8')
        for line in datei:
            self.l4c.append(line[:-1])

        self.l5c = []
        datei = open('l5c.txt', 'r', encoding='utf-8')
        for line in datei:
            self.l5c.append(line[:-1])


        self.scramblelist = self.l5c.copy()

    def CreateLayout(self):
        # starting to define the layout of the CentralWidget
        self.central.groupBox = QGroupBox("L2L Trainer")
        self.central.groupBox.setFont(QtGui.QFont("Sansserif", 13))
        self.gridLayout = QGridLayout()

        '''
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
        self.anycolourchecker.stateChanged.connect(self.changescrlen)
        self.gridLayout.addWidget(self.anycolourchecker, 0, 1)

        '''

        # button to generate a scramble and a random colour to start the first layer with
        self.scramblegenbutton = QPushButton("Generate L2L Case", self)
        self.scramblegenbutton.setMinimumHeight(80)
        self.scramblegenbutton.setToolTip("Generates a scramble to a L2L case of the defined type(s).")
        #self.scramblegenbutton.clicked.connect(self.ScramblePlusColour)
        self.scramblegenbutton.setShortcut(QtGui.QKeySequence(Qt.Key_Space))
        self.gridLayout.addWidget(self.scramblegenbutton, 1, 1)

        # this label shows the scramble
        self.scramblelabel = QLabel(self)
        self.scramblelabel.setMinimumHeight(50)
        self.scramblelabel.setText('')
        self.scramblelabel.setFont(QtGui.QFont("Monospace", 20))
        self.gridLayout.addWidget(self.scramblelabel, 2, 0)

        '''
        # this label shows the colour
        self.colourlabel = QLabel(self)
        self.colourlabel.setMinimumHeight(50)
        self.colourlabel.setStyleSheet('background-color : transparent')
        self.gridLayout.addWidget(self.colourlabel, 2, 1)
        
        # draws the scramble by drawing several polygongs corresponding to the scramble
        self.drawscrwidget = ScrambleDrawing()
        self.drawscrwidget.setMinimumHeight(120)
        gridLayout.addWidget(self.drawscrwidget, 3, 0)
        '''
        # this label shows some info about the creator
        self.creatorlabel = QLabel(self)
        self.creatorlabel.setText("© Annika Stein")
        self.creatorlabel.setMinimumHeight(50)
        self.gridLayout.addWidget(self.creatorlabel, 3, 1)

        self.central.groupBox.setLayout(self.gridLayout)

        vbox = QVBoxLayout()
        vbox.addWidget(self.central.groupBox)
        self.central.setLayout(vbox)

    def changescrlen(self):
        # andere Abfragen um zu prüfen, welche Cases verwendet werden sollen
        scrlen = self.scrlenslider.value()

        if scrlen == 1:
            if self.anycolourchecker.isChecked():
                self.auxscrl = self.scramble1list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscrl)
                    self.scramblelist = self.auxscrl
                else:
                    self.scramblelist = self.auxscrl
            else:
                self.auxscrl = self.scramble1wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscrl)
                    self.scramblelist = self.auxscrl
                else:
                    self.scramblelist = self.auxscrl
        elif scrlen == 2:
            if self.anycolourchecker.isChecked():
                self.auxscr2 = self.scramble2list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr2)
                    self.scramblelist = self.auxscr2
                else:
                    self.scramblelist = self.auxscr2
            else:
                self.auxscr2 = self.scramble2wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr2)
                    self.scramblelist = self.auxscr2
                else:
                    self.scramblelist = self.auxscr2
        elif scrlen == 3:
            if self.anycolourchecker.isChecked():
                self.auxscr3 = self.scramble3list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr3)
                    self.scramblelist = self.auxscr3
                else:
                    self.scramblelist = self.auxscr3
            else:
                self.auxscr3 = self.scramble3wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr3)
                    self.scramblelist = self.auxscr3
                else:
                    self.scramblelist = self.auxscr3
        elif scrlen == 4:
            if self.anycolourchecker.isChecked():
                self.auxscr4 = self.scramble4list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr4)
                    self.scramblelist = self.auxscr4
                else:
                    self.scramblelist = self.auxscr4
            else:
                self.auxscr4 = self.scramble4wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr4)
                    self.scramblelist = self.auxscr4
                else:
                    self.scramblelist = self.auxscr4
        elif scrlen == 5:
            if self.anycolourchecker.isChecked():
                self.auxscr5 = self.scramble5list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr5)
                    self.scramblelist = self.auxscr5
                else:
                    self.scramblelist = self.auxscr5
            else:
                self.auxscr5 = self.scramble5wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr5)
                    self.scramblelist = self.auxscr5
                else:
                    self.scramblelist = self.auxscr5
        elif scrlen == 6:
            if self.anycolourchecker.isChecked():
                self.auxscr6 = self.scramble6list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr6)
                    self.scramblelist = self.auxscr6
                else:
                    self.scramblelist = self.auxscr6
            else:
                self.auxscr6 = self.scramble6wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr6)
                    self.scramblelist = self.auxscr6
                else:
                    self.scramblelist = self.auxscr6
        else:
            if self.anycolourchecker.isChecked():
                self.auxscr7 = self.scramble7list.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr7)
                    self.scramblelist = self.auxscr7
                else:
                    self.scramblelist = self.auxscr7
            else:
                self.auxscr7 = self.scramble7wlist.copy()
                if self.shufflescrchecker.isChecked():
                    random.shuffle(self.auxscr7)
                    self.scramblelist = self.auxscr7
                else:
                    self.scramblelist = self.auxscr7

    def ScramblePlusColour(self):

        if len(self.scramblelist) == 0:
            self.changescrlen()

        scramblezumanzeigen = self.scramblelist[-1]
        self.scramblelist.pop()
        self.scramblelabel.setText(scramblezumanzeigen)

        # rufe hier nun die Funktion auf, die den ausgewählten Scramble zeichnet

        self.ShowScramble(scramblezumanzeigen)

    def ShowScramble(self, scramble):
        stickercol = ["o", "o", "o", "o", "o", "g", "g", "g", "g", "g", "y", "y", "y", "y", "y",
                      "w", "w", "w", "w", "w", "r", "r", "r", "r", "r", "b", "b", "b", "b", "b"]
        scrsplit = scramble.split()
        for i in scrsplit:
            if i ==  "x":
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
            elif i == "r":
                #(4, 8, 17)(11, 21, 26)(12, 22, 28)(13, 23, 29)(14, 24, 30)
                #(3, 7, 16)(10, 20, 25)(11, 21, 27)(12, 22, 28)(13, 23, 29)
                threeswap(stickercol, 3, 7, 16)
                threeswap(stickercol, 10, 20, 25)
                threeswap(stickercol, 11, 21, 27)
                threeswap(stickercol, 12, 22, 28)
                threeswap(stickercol, 13, 23, 29)
            elif i == "r'":
                #
                #(16, 7, 3)(25, 20, 10)(27, 21, 11)(28, 22, 12)(29, 23, 13)
                threeswap(stickercol, 16, 7, 3)
                threeswap(stickercol, 25, 20, 10)
                threeswap(stickercol, 27, 21, 11)
                threeswap(stickercol, 28, 22, 12)
                threeswap(stickercol, 29, 23, 13)
            elif i == "R":
                threeswap(stickercol, 15, 25, 20)
                threeswap(stickercol, 16, 29, 21)
                threeswap(stickercol, 17, 26, 22)
                threeswap(stickercol, 24, 19, 28)
                threeswap(stickercol, 6, 4, 12)
            elif i == "R'":
                threeswap(stickercol, 20, 25, 15)
                threeswap(stickercol, 21, 29, 16)
                threeswap(stickercol, 22, 26, 17)
                threeswap(stickercol, 28, 19, 24)
                threeswap(stickercol, 12, 4, 6)
            elif i == "l":
                #(1, 6, 11)(2, 8, 14)(3, 9, 15)(4, 10, 12)(19, 24, 28)
                #(0, 5, 10)(1, 7, 13)(2, 8, 14)(3, 9, 11)(18, 23, 27)
                threeswap(stickercol, 0, 5, 10)
                threeswap(stickercol, 1, 7, 13)
                threeswap(stickercol, 2, 8, 14)
                threeswap(stickercol, 3, 9, 11)
                threeswap(stickercol, 18, 23, 27)
            elif i == "l'":
                #
                #(10, 5, 0)(13, 7, 1)(14, 8, 2)(11, 9, 3)(27, 23, 18)
                threeswap(stickercol, 10, 5, 0)
                threeswap(stickercol, 13, 7, 1)
                threeswap(stickercol, 14, 8, 2)
                threeswap(stickercol, 11, 9, 3)
                threeswap(stickercol, 27, 23, 18)
            elif i == "f":
                threeswap(stickercol, 5, 20, 10)
                threeswap(stickercol, 7, 23, 11)
                threeswap(stickercol, 17, 28, 2)
                threeswap(stickercol, 24, 12, 8)
                threeswap(stickercol, 6, 22, 14)
            elif i == "f'":
                threeswap(stickercol, 10, 20, 5)
                threeswap(stickercol, 11, 23, 7)
                threeswap(stickercol, 2, 28, 17)
                threeswap(stickercol, 8, 12, 24)
                threeswap(stickercol, 14, 22, 6)
            elif i == "B":
                #(1, 26, 16)(2, 28, 17)(4, 30, 19)(5, 27, 20)(10, 14, 22)
                #(0, 25, 15)(1, 27, 16)(3, 29, 18)(4, 26, 19)(9, 13, 21)
                threeswap(stickercol, 0, 25, 15)
                threeswap(stickercol, 1, 27, 16)
                threeswap(stickercol, 3, 29, 18)
                threeswap(stickercol, 4, 26, 19)
                threeswap(stickercol, 9, 13, 21)
            elif i == "B'":
                #
                #(15, 25, 0)(16, 27, 1)(18, 29, 3)(19, 26, 4)(21, 13, 9)
                threeswap(stickercol, 15, 25, 0)
                threeswap(stickercol, 16, 27, 1)
                threeswap(stickercol, 18, 29, 3)
                threeswap(stickercol, 19, 26, 4)
                threeswap(stickercol, 21, 13, 9)
            elif i == "b":
                #(1, 11, 26)(3, 13, 27)(4, 14, 28)(5, 15, 29)(9, 23, 20)
                #(0, 10, 25)(2, 12, 26)(3, 13, 27)(4, 14, 28)(8, 22, 19)
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
        self.drawscrwidget = ScrambleDrawing(stickercol)
        self.drawscrwidget.setMinimumHeight(430)
        self.gridLayout.addWidget(self.drawscrwidget, 3, 0)

class ScrambleDrawing(QWidget):
    def __init__(self, stickers):
        super().__init__()
        self.stic = stickers

    def paintEvent(self, QPaintEvent):
        painter = QtGui.QPainter(self)
        self.drawScr(painter, self.stic)

    def drawScr(self, painter, s):
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
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]

def fourswap(listname,i,j,k,l):
    listname[k], listname[l] = listname[l], listname[k]
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]

def corrcol(list,i):
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
    App = QApplication(sys.argv)
    startwindow = StartWindow()
    sys.exit(App.exec())

