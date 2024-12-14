from gui import *
from PyQt6.QtWidgets import *

from PyQt6 import QtCore
import csv

class Logic(QMainWindow, Ui_PolytopiaCompDatabase):
    def __init__(self)->None:
        """
        Method to define instance variables.
        Method checks for user input upon pressing buttons.
        """

        super().__init__()
        self.setupUi(self)

        self.buttonClearBoolean = True
        self.introOpen = True

        self.PointCOpen = True
        self.scoreCClose = 0
        self.scoreCHoldX = 501
        self.scoreCHoldY = 91
        self.scoreCX = 0
        self.scoreCY = 0

        self.text = ""

        self.addNameEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.addDataEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.addAddButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.addCancelButton.setGeometry(QtCore.QRect(0, 0, 0, 0))

        self.introButton.clicked.connect(lambda : self.intro())
        self.ScoreCButton.clicked.connect(lambda : self.submit())
        self.addButton.clicked.connect(lambda: self.entry_menu())
        self.addCancelButton.clicked.connect(lambda: self.button_clear())
        self.addAddButton.clicked.connect(lambda: self.add_entry())

        self.user_add_a = True
        self.user_add_b = True
        self.user_add_c = True
        self.user_add_d = True
        self.user_functions_check()

        self.user_buttons()

    def user_buttons(self)->None:
        """
        Method to hides user tabs if no data has been put in them
        """
        self.user_add_a = True
        self.user_add_b = True
        self.user_add_c = True
        self.user_add_d = True
        self.user_functions_check()
        if self.user_add_d:
            self.ScoreCButtonZZD.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ZZDTextEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))

        if self.user_add_c:
            self.ScoreCButtonZZC.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ZZCTextEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))

        if self.user_add_b:
            self.ScoreCButtonZZB.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ZZBTextEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))

        if self.user_add_a:
            self.ScoreCButtonZZA.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ZZATextEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))

    def entry_menu(self)->None:
        """
        Method hides original tabs to make way for user input on creating tabs
        Method sets Geometry for user input on creating tabs
        """
        self.introOpen = True
        self.PointCOpen = True
        self.intro()
        self.submit()
        self.button_clear()

        self.addNameEdit.setGeometry(QtCore.QRect(0, 70, 511, 22))
        self.addAddButton.setGeometry(QtCore.QRect(0, 220, 93, 28))
        self.addCancelButton.setGeometry(QtCore.QRect(100, 220, 93, 28))
        self.addDataEdit.setGeometry(QtCore.QRect(0, 100, 511, 111))

    def add_entry(self)->None:
        """
        Method checks if user has data.csv in the files, if not method creates them
        Method pulls user input into a string then into a csv file
        Method closes user input tab and brings back the initial tab
        """
        while True:
            try:

                with open("data.csv") as input_file:
                    break
            except FileNotFoundError:
                with open("data.csv", "w", newline="") as output_csv_file:
                    content = csv.writer(output_csv_file)
                    content.writerow(["Name", "Data"])

        name_str = self.addNameEdit.text()
        data_str = self.addDataEdit.text()
        with open("data.csv", "a", newline="") as output_csv_file:
            content = csv.writer(output_csv_file)
            content.writerow([name_str, data_str])

        self.user_buttons()
        self.button_clear()

    def user_functions_check(self)->None:
        """
        Method checks if user has data.csv in the files, if not method creates them
        Method reads csv file and puts contents within an array
        Method then creates user functions from input provided within array
        """
        while True:
            try:
                with open("data.csv") as input_file:
                    break
            except FileNotFoundError:
                with open("data.csv", "w", newline="") as output_csv_file:
                    content = csv.writer(output_csv_file)
                    content.writerow(["Name", "Data"])
        with open("data.csv", "r", newline="") as output_csv_file:
            content = csv.reader(output_csv_file)
            user_data_str = []
            for row in content:
                for item in row:
                    item_as_string = str(item)
                    user_data_str.append(item_as_string)

                    print(item_as_string)

            length = len(user_data_str)
            print(length)
            gate = True
            _translate = QtCore.QCoreApplication.translate
            while gate:
                if length > 2:
                    print(1)
                    self.ScoreCButtonZZA.setText(user_data_str[2])
                    self.ZZATextEdit.setPlainText(user_data_str[3])
                    self.user_add_a = False
                if length > 4:
                    print(1)
                    self.ScoreCButtonZZB.setText(user_data_str[4])
                    self.ZZBTextEdit.setPlainText(user_data_str[5])
                    self.user_add_b = False

                if length > 6:
                    print(1)
                    self.ScoreCButtonZZC.setText(user_data_str[6])
                    self.ZZCTextEdit.setPlainText(user_data_str[7])
                    self.user_add_c = False

                if length > 8:
                    print(1)
                    self.ScoreCButtonZZD.setText(user_data_str[8])
                    self.ZZDTextEdit.setPlainText(user_data_str[9])
                    self.user_add_d = False


                gate = False

    def button_clear(self)->None:
        """
        Method hides entry screen when called
        """
        if self.buttonClearBoolean:
            self.ScoreCButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.introButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.addButton.setGeometry(QtCore.QRect(0, 0, 0, 0))

            self.buttonClearBoolean = False
        else:
            self.ScoreCButton.setGeometry(QtCore.QRect(0, 180, 521, 28))
            self.introButton.setGeometry(QtCore.QRect(0, 70, 521, 28))
            self.addButton.setGeometry(QtCore.QRect(530, 70, 241, 28))

            self.order()
            self.addNameEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.addDataEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.addAddButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.addCancelButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.buttonClearBoolean = True

    def intro(self)->None:
        """
        Method hides/revels introduction data
        """
        if self.introOpen:
            self.introTextEdit.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.introOpen = False
            self.order()

        else:
            self.introTextEdit.setGeometry(QtCore.QRect(10, 100, 501, 71))
            self.introOpen = True
            self.order()

    def submit(self)->None:
        """
        Method hides/revels Score Counting data
        """

        if self.PointCOpen:

            self.scoreCX = self.scoreCClose
            self.scoreCY = self.scoreCClose
            ##self.ScoreCTextEdit_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.PointCOpen = False
            self.order()
        else:
            self.scoreCX = self.scoreCHoldX
            self.scoreCY = self.scoreCHoldY

            ##self.ScoreCTextEdit_2.setGeometry(QtCore.QRect(10, 100, 501, 71))
            self.PointCOpen = True
            self.order()




    def order(self)->None:
        """
        Method changes introduction and score counting locations on screen
        """
        if self.introOpen:
            self.ScoreCButton.setGeometry(QtCore.QRect(0, 180, 521, 28))
            self.ScoreCTextEdit.setGeometry(QtCore.QRect(10, 210, self.scoreCX , self.scoreCY))
        else:
            intro_gone: int = 80
            self.ScoreCButton.setGeometry(QtCore.QRect(0, 180 - intro_gone, 521, 28))
            self.ScoreCTextEdit.setGeometry(QtCore.QRect(10, 210- intro_gone, self.scoreCX , self.scoreCY))










