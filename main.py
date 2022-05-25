import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from menu import Ui_Menu
from lesson import Ui_Lesson
app = QtWidgets.QApplication(sys.argv)
Menu = QtWidgets.QMainWindow()
ui = Ui_Menu()
ui.setupUi(Menu)
Menu.show()

def open1():
    global Lesson
    global page
    page = "1"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open2():
    global Lesson
    global page
    page = "2"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open3():
    global Lesson
    global page
    page = "3"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open4():
    global Lesson
    global page
    page = "4"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open5():
    global Lesson
    global page
    page = "5"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open6():
    global Lesson
    global page
    page = "6"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open7():
    global Lesson
    global page
    page = "7"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open8():
    global Lesson
    global page
    page = "8"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open9():
    global Lesson
    global page
    page = "9"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()

def open10():
    global Lesson
    global page
    page = "10"
    Lesson = QtWidgets.QDialog()
    ui = Ui_Lesson()
    ui.setupUi(Lesson)
    ui.label.setPixmap(QtGui.QPixmap(f"{page}.PNG"))
    Lesson.show()


ui.Button1.clicked.connect(open1)
ui.Button2.clicked.connect(open2)
ui.Button3.clicked.connect(open3)
ui.Button4.clicked.connect(open4)
ui.Button5.clicked.connect(open5)
ui.Button6.clicked.connect(open6)
ui.Button7.clicked.connect(open7)
ui.Button8.clicked.connect(open8)
ui.pushButton_9.clicked.connect(open9)
ui.Button10.clicked.connect(open10)
sys.exit(app.exec_())