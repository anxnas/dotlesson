# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\liceu\menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Menu(object):
    def setupUi(self, Menu):
        Menu.setObjectName("Menu")
        Menu.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Menu)
        self.centralwidget.setObjectName("centralwidget")
        self.picture = QtWidgets.QLabel(self.centralwidget)
        self.picture.setGeometry(QtCore.QRect(240, 0, 241, 161))
        self.picture.setText("")
        self.picture.setPixmap(QtGui.QPixmap("C:/Users/vladh/Downloads/Логотип_Ликино-Дулёвского_лицея-removebg-preview.png"))
        self.picture.setObjectName("picture")
        self.temalabel = QtWidgets.QLabel(self.centralwidget)
        self.temalabel.setGeometry(QtCore.QRect(210, 140, 391, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.temalabel.setFont(font)
        self.temalabel.setObjectName("temalabel")
        self.Button1 = QtWidgets.QPushButton(self.centralwidget)
        self.Button1.setGeometry(QtCore.QRect(20, 250, 311, 23))
        self.Button1.setObjectName("Button1")
        self.Button2 = QtWidgets.QPushButton(self.centralwidget)
        self.Button2.setGeometry(QtCore.QRect(20, 280, 311, 23))
        self.Button2.setObjectName("Button2")
        self.Button3 = QtWidgets.QPushButton(self.centralwidget)
        self.Button3.setGeometry(QtCore.QRect(20, 310, 311, 23))
        self.Button3.setObjectName("Button3")
        self.Button4 = QtWidgets.QPushButton(self.centralwidget)
        self.Button4.setGeometry(QtCore.QRect(20, 340, 311, 23))
        self.Button4.setObjectName("Button4")
        self.Button5 = QtWidgets.QPushButton(self.centralwidget)
        self.Button5.setGeometry(QtCore.QRect(20, 370, 311, 23))
        self.Button5.setObjectName("Button5")
        self.Button6 = QtWidgets.QPushButton(self.centralwidget)
        self.Button6.setGeometry(QtCore.QRect(460, 250, 311, 23))
        self.Button6.setObjectName("Button6")
        self.Button7 = QtWidgets.QPushButton(self.centralwidget)
        self.Button7.setGeometry(QtCore.QRect(460, 280, 311, 23))
        self.Button7.setObjectName("Button7")
        self.Button8 = QtWidgets.QPushButton(self.centralwidget)
        self.Button8.setGeometry(QtCore.QRect(460, 310, 311, 23))
        self.Button8.setObjectName("Button8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(460, 340, 311, 23))
        self.pushButton_9.setObjectName("pushButton_9")
        self.Button10 = QtWidgets.QPushButton(self.centralwidget)
        self.Button10.setGeometry(QtCore.QRect(460, 370, 311, 23))
        self.Button10.setObjectName("Button10")
        Menu.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Menu)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Menu.setMenuBar(self.menubar)

        self.retranslateUi(Menu)
        QtCore.QMetaObject.connectSlotsByName(Menu)

    def retranslateUi(self, Menu):
        _translate = QtCore.QCoreApplication.translate
        Menu.setWindowTitle(_translate("Menu", "Menu"))
        self.temalabel.setText(_translate("Menu", "Точечный урок"))
        self.Button1.setText(_translate("Menu", "Урок 1 .Как удалить задний фон любой фотографии"))
        self.Button2.setText(_translate("Menu", "Урок 2.Как создать Google-аккаунт"))
        self.Button3.setText(_translate("Menu", "Урок 3.Как создать Google-документ"))
        self.Button4.setText(_translate("Menu", "Урок 4.Как работать с Google-Forms"))
        self.Button5.setText(_translate("Menu", "Урок 5.Настройки доступа Google-документа "))
        self.Button6.setText(_translate("Menu", "Урок 6.Создание почты @mail.ru"))
        self.Button7.setText(_translate("Menu", "Урок 7.Создание чата в Viber"))
        self.Button8.setText(_translate("Menu", "Урок  8.Создание опроса в Viber"))
        self.pushButton_9.setText(_translate("Menu", "Урок  9.Настройка профиля WhatsApp"))
        self.Button10.setText(_translate("Menu", "Урок 10.Сохранение в документа из Office в формате .pdf"))
