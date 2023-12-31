# Form implementation generated from reading ui file 'aipainter.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


#from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QVBoxLayout, QProgressBar, QPushButton, QProgressDialog
import os
import glob
import pyautogui
import pygame
from PIL import Image
#import paddlehub as hub
import shutil
import datetime


class AIPainter(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(770, 554)
        MainWindow.setMinimumSize(QtCore.QSize(770, 554))
        MainWindow.setStyleSheet("background-color: rgb(59,63,66);")
        MainWindow.setWindowIcon(QIcon("resource/logo.png"))

        # 获取用户目录路径
        user_dir = os.path.expanduser('~')

        # 判断用户目录下是否存在.u2net文件夹且为空
        u2net_dir = os.path.join(user_dir, '.paddlehub')
        if not os.path.exists(u2net_dir) or not os.listdir(u2net_dir):
            # 复制.u2net文件夹及其内容到用户目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            shutil.copytree(os.path.join(current_dir, '.paddlehub'), u2net_dir)

        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Franklin Gothic Medium")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(301, 0))
        self.label.setMaximumSize(QtCore.QSize(16777215, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.toolButton = QtWidgets.QToolButton(parent=self.centralwidget)
        self.toolButton.setStyleSheet("color: rgb(255, 255, 255);")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(681, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.textEdit = QtWidgets.QTextEdit(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(158, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 770, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.toolButton.clicked.connect(self.choose_save_path)
        self.pushButton_3.clicked.connect(self.start_painting)

    def convert_slashes(self, string):
        converted_string = string.replace("/", "\\")
        return converted_string

    def name_creater(self):
        current_time = datetime.datetime.now()
        filename = current_time.strftime("%Y_%m_%d_%H_%M_%S") + ".png"
        return filename

    def choose_save_path(self):
        folder_dialog = QFileDialog()
        self.folder_path = folder_dialog.getExistingDirectory(self, "请选择保存路径Please select a save path", "")
        self.label.setText(self.folder_path)
        #self.folder_path = self.convert_slashes(self.folder_path)

    def start_painting(self):
        if self.label.text() != "" and self.textEdit.toPlainText() != "":
            self.setDisabled(True)
            import paddlehub as hub
            # 导入模型
            module = hub.Module(name='stable_diffusion')
            # 生成图像
            result = module.generate_image(
                text_prompts=f"{self.textEdit.toPlainText()}",
                output_dir=f'{self.folder_path}')
            # 保存最终生成的图像
            os.startfile(self.folder_path)
            #output_file = f'{self.folder_path}/{self.name_creater()}'
            #result[0].save(output_file)
            #self.setDisabled(False)
            #os.startfile(output_file)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DaYe PhotoStudio"))
        self.label_3.setText(_translate("MainWindow", "Stable Diffusion"))
        self.label.setText(_translate("MainWindow", ""))
        self.toolButton.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "此程序100%本地运行，因此运行速度完全取决于您的硬件条件。\n"
"This program runs 100% natively, so the speed at which it runs \n"
"depends entirely on your hardware conditions."))
        self.textEdit.setPlaceholderText(_translate("MainWindow", "Please enter the prompts"))
        self.pushButton_3.setText(_translate("MainWindow", "OK"))
