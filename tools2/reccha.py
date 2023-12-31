# Form implementation generated from reading ui file 'remwatermark_img.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QFileDialog, QDialog, QVBoxLayout, QProgressBar, QPushButton, QProgressDialog
import os
import glob
import pyautogui
import pygame
from PIL import Image
#from paddleocr import PaddleOCR
import shutil

class Rec_cha(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(447, 250)
        MainWindow.setStyleSheet("background-color: rgb(59,63,66);")
        MainWindow.setWindowIcon(QIcon("resource/logo.png"))

        # 获取用户目录路径
        user_dir = os.path.expanduser('~')

        # 判断用户目录下是否存在.u2net文件夹且为空
        u2net_dir = os.path.join(user_dir, '.paddleocr')
        if not os.path.exists(u2net_dir) or not os.listdir(u2net_dir):
            # 复制.u2net文件夹及其内容到用户目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            shutil.copytree(os.path.join(current_dir, '.paddleocr'), u2net_dir)

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

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(141, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem4, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(301, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 3, 0, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 6, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem5, 4, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem6)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
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
        spacerItem7 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.gridLayout.addItem(spacerItem7, 6, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 447, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.choose_some_file)
        self.pushButton_2.clicked.connect(self.choose_folder)
        self.pushButton_3.clicked.connect(self.start_working)

    def choose_some_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilters([
            "JPEG (*.jpg *.jpeg)",
            "PNG (*.png)",
            "GIF (*.gif)",
            "BMP (*.bmp)",
            "TIFF (*.tif *.tiff)"
        ])

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            selected_files = file_dialog.selectedFiles()
            print(selected_files)
            self.somefiles = selected_files
            self.label.setText(selected_files[0] + "...")

    def choose_folder(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.Directory)
        file_dialog.setNameFilter(
            "Images (*.jpg *.jpeg *.png *.gif *.bmp *.tif *.tiff)"
        )

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            selected_directory = file_dialog.selectedUrls()[0].toLocalFile()
            print("Selected Directory:", selected_directory)
            self.label.setText(selected_directory)
            directory = selected_directory
            extensions = ["*.jpg", "*.jpeg", "*.png", "*.gif", "*.bmp", "*.tif", "*.tiff"]
            choosed = []
            for extension in extensions:
                files = glob.glob(os.path.join(directory, extension))
                #print(files)
                for file in files:
                    file_name = os.path.basename(file)
                    #print("Selected File:", file_name)
                    choosed_file = selected_directory + "/" + file_name
                    choosed.append(choosed_file)
            print(choosed)
            self.somefiles = choosed

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

    def start_working(self):
        from paddleocr import PaddleOCR
        if self.label.text() != "Path":
            folder_dialog = QFileDialog()
            folder_path = folder_dialog.getExistingDirectory(self, "请选择保存路径Please select a save path", "")
            # 创建进度条
            progress_bar = QProgressBar()
            progress_bar.setMaximum(100)
            progress_bar.setTextVisible(True)

            # 创建进度对话框
            progress_dialog = QProgressDialog(self)
            progress_dialog.setWindowTitle("Progress")
            progress_dialog.setFixedSize(600, 100)  # 设置窗口宽度为400，高度为200
            progress_dialog.setLabelText("Running...")
            progress_dialog.setAutoClose(False)
            progress_dialog.setAutoReset(False)
            progress_dialog.setBar(progress_bar)
            if folder_path == "":
                progress_dialog.close()
                pass
            else:
                self.hide()
                ocr = PaddleOCR()

                count = len(self.somefiles)
                value = 0

                for file in self.somefiles:
                    #处理
                    file_name = self.get_filename(file)
                    result = ocr.ocr(file)

                    with open(f"{folder_path}/{file_name}.txt", 'a', encoding='utf-8') as sfile:
                        for line in result:
                            for word in line:
                                text_line = word[-1]
                                text = text_line[0]
                                print("text:", text)
                                sfile.write(text + "\n")

                    value += (1 / count) * 100
                    # 更新进度条的值
                    progress_bar.setValue(value)
                    progress_dialog.setLabelText(file)
                    progress_dialog.setWindowTitle(f"{value}%")
                    QApplication.processEvents()
                    # 如果用户点击了取消按钮，则停止循环
                    if progress_dialog.wasCanceled():
                        break

                # 更新进度条的值
                progress_bar.setValue(100)
                QApplication.processEvents()
                progress_dialog.close()
                if self.ifaudio == "True":
                    self.play_sound(self.sound_file)
                pyautogui.alert("已完成文字识别\nThe Text recognition task has been completed")  # 提示音
                os.startfile(folder_path)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DaYe PhotoStudio"))
        self.pushButton.setText(_translate("MainWindow", self.lanpack[67]))
        self.pushButton_2.setText(_translate("MainWindow", self.lanpack[68]))
        self.label.setText(_translate("MainWindow", "Path"))
        self.pushButton_3.setText(_translate("MainWindow", self.lanpack[66]))


