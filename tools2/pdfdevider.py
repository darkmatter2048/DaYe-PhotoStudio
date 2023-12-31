# Form implementation generated from reading ui file 'gifdevider_ui.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QDialog, QVBoxLayout, QProgressBar, QPushButton, QProgressDialog
import os
import glob
import pyautogui
import pygame
from PIL import Image, ImageSequence
#import paddlehub as hub
import shutil
import PyPDF2


class PDFDevider(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 250)
        MainWindow.setStyleSheet("background-color: rgb(59,63,66);")
        MainWindow.setWindowIcon(QIcon("resource/logo.png"))

        # Read ConfigInfo
        with open("config.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        self.config = [line.strip() for line in lines]
        print(self.config)
        lanpath = "language\\" + self.config[0]
        with open(lanpath + ".txt", 'r', encoding='utf-8') as ff:
            liness = ff.readlines()

        self.lanpack = [lines.strip() for lines in liness]
        self.ifaudio = self.config[5]
        print(self.ifaudio)
        print(self.lanpack)
        self.sound_file = "tools/audio/audio.wav"

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setMinimumSize(QtCore.QSize(121, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(301, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem5 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(111, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 5, 0, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.openFileDialog)
        self.pushButton_3.clicked.connect(self.start_working)


    def openFileDialog(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "选择GIF文件", "", "PDF Files (*.pdf)")
        if fileName:
            print(f"选择的文件名为: {fileName}")
            self.label.setText(fileName)
            self.filename = fileName

    def convert_slashes(self, string):
        converted_string = string.replace("/", "\\")
        return converted_string

    def get_filename(self, path):
        path = path.split("/")
        last_part = path[-1]
        last_part = last_part.split(".")
        last_name = last_part[0]
        return last_name

    def play_sound(self, sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def run_main(self, file_path, output_folder):
        # 打开要拆分的PDF文件
        input_pdf = open(file_path, 'rb')
        pdf_reader = PyPDF2.PdfReader(input_pdf)

        # 遍历PDF页面并拆分
        for page in range(len(pdf_reader.pages)):
            output = PyPDF2.PdfWriter()
            output.add_page(pdf_reader.pages[page])
            with open(f'{output_folder}/output_page_{page + 1}.pdf', 'wb') as output_pdf:
                output.write(output_pdf)

        input_pdf.close()

    def start_working(self):
        if self.label.text() != "Path":
            folder_dialog = QFileDialog()
            folder_path = folder_dialog.getExistingDirectory(self, "请选择保存路径Please select a save path", "")
            if folder_path == "":
                pass
            else:
                #处理
                self.hide()
                input_path = self.convert_slashes(self.filename)
                self.run_main(self.filename, folder_path)

                if self.ifaudio == "True":
                    self.play_sound(self.sound_file)
                pyautogui.alert("已完成PDF拆分\nThe Splitting PDF task has been completed")  # 提示音
                os.startfile(folder_path)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DaYe PhotoStudio"))
        self.pushButton.setText(_translate("MainWindow", f"{self.lanpack[47]}"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.pushButton_3.setText(_translate("MainWindow", f"{self.lanpack[66]}"))