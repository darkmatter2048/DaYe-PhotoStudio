# Form implementation generated from reading ui file 'koutu.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon,QPixmap, QFont, QFontDatabase, QIcon, QColor
from PyQt6.QtWidgets import QApplication, QFileDialog, QColorDialog, QDialog, QVBoxLayout, QProgressBar, QPushButton, QProgressDialog
from PyQt6.QtCore import Qt, QTimer
import os
import glob
from rembg import new_session,remove
from PIL import Image
import pyautogui
import cv2
import subprocess
import shutil
import pygame


class Koutu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(512, 670)
        MainWindow.setStyleSheet("background-color: rgb(59,63,66);")
        MainWindow.setWindowIcon(QIcon("resource/logo.png"))
        self.sound_file = "tools/audio/audio.wav"

        # 获取用户目录路径
        user_dir = os.path.expanduser('~')

        # 判断用户目录下是否存在.u2net文件夹且为空
        u2net_dir = os.path.join(user_dir, '.u2net')
        if not os.path.exists(u2net_dir) or not os.listdir(u2net_dir):
            # 复制.u2net文件夹及其内容到用户目录
            current_dir = os.path.dirname(os.path.abspath(__file__))
            shutil.copytree(os.path.join(current_dir, '.u2net'), u2net_dir)

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

        # 加载字体文件
        font_id = QFontDatabase.addApplicationFont("font/DingTalk_JinBuTi_Regular.ttf")
        # 获取字体家族名称
        font_families = QFontDatabase.applicationFontFamilies(font_id)
        font_family = font_families[0]
        # 创建字体对象
        self.font = QFont(font_family)

        # 加载字体文件
        font_id1 = QFontDatabase.addApplicationFont("font/ZCOOL_KuHei_Regular.ttf")
        # 获取字体家族名称
        font_families1 = QFontDatabase.applicationFontFamilies(font_id1)
        font_family1 = font_families1[0]
        # 创建字体对象
        self.font1 = QFont(font_family1)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 95, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);\n"
"")
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 190, 461, 221))
        font = QtGui.QFont(self.font1)
        font.setPointSize(20)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.groupBox.setObjectName("groupBox")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 441, 181))
        font = QtGui.QFont(self.font)
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 430, 461, 42))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont(self.font)
        #font.setFamily("钉钉进步体")
        font.setPointSize(23)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont(self.font)
        #font.setFamily("钉钉进步体")
        font.setPointSize(13)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 140, 461, 40))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont(self.font)
        font.setPointSize(23)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget1)
        font = QtGui.QFont(self.font)
        font.setPointSize(13)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 530, 461, 26))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_6.setMinimumSize(QtCore.QSize(221, 0))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);\n"
"border: 1px solid rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        spacerItem = QtWidgets.QSpacerItem(51, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_19.setMinimumSize(QtCore.QSize(141, 0))
        font = QtGui.QFont(self.font)
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_19.setFont(font)
        self.pushButton_19.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_5.addWidget(self.pushButton_19)
        self.ChooseFolder_2 = QtWidgets.QPushButton(self.centralwidget)
        self.ChooseFolder_2.setGeometry(QtCore.QRect(350, 570, 121, 41))
        self.ChooseFolder_2.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont(self.font)
        #font.setFamily("钉钉进步体")
        font.setPointSize(20)
        font.setBold(False)
        self.ChooseFolder_2.setFont(font)
        self.ChooseFolder_2.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.ChooseFolder_2.setObjectName("ChooseFolder_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 30, 461, 43))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.SingleFile = QtWidgets.QPushButton(self.widget)
        self.SingleFile.setMinimumSize(QtCore.QSize(131, 41))
        font = QtGui.QFont(self.font)
        font.setPointSize(23)
        font.setBold(False)
        self.SingleFile.setFont(font)
        self.SingleFile.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.SingleFile.setObjectName("SingleFile")
        self.horizontalLayout.addWidget(self.SingleFile)
        spacerItem1 = QtWidgets.QSpacerItem(28, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.ChooseFiles = QtWidgets.QPushButton(self.widget)
        self.ChooseFiles.setMinimumSize(QtCore.QSize(124, 41))
        font = QtGui.QFont(self.font)
        font.setPointSize(23)
        font.setBold(False)
        self.ChooseFiles.setFont(font)
        self.ChooseFiles.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.ChooseFiles.setObjectName("ChooseFiles")
        self.horizontalLayout.addWidget(self.ChooseFiles)
        spacerItem2 = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.ChooseFolder = QtWidgets.QPushButton(self.widget)
        self.ChooseFolder.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont(self.font)
        font.setPointSize(23)
        font.setBold(False)
        self.ChooseFolder.setFont(font)
        self.ChooseFolder.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.ChooseFolder.setObjectName("ChooseFolder")
        self.horizontalLayout.addWidget(self.ChooseFolder)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 490, 461, 24))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.widget1)
        self.label_5.setMinimumSize(QtCore.QSize(221, 0))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(255,0,0)")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(51, 0, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.pushButton_18 = QtWidgets.QPushButton(self.widget1)
        self.pushButton_18.setMinimumSize(QtCore.QSize(141, 0))
        font = QtGui.QFont(self.font)
        font.setPointSize(13)
        font.setBold(True)
        self.pushButton_18.setFont(font)
        self.pushButton_18.setStyleSheet("QPushButton{\n"
"    background-color:rgba(0,0,0,50);\n"
"    color:rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgba(0, 0, 0,150);\n"
"}")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_4.addWidget(self.pushButton_18)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 512, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_18.hide()
        self.label_5.hide()
        self.label_6.hide()
        self.pushButton_19.hide()

        self.moshi = 0
        self.way = 0

        self.comboBox_2.currentIndexChanged.connect(self.showm)
        self.SingleFile.clicked.connect(self.choose_single_file)
        self.ChooseFiles.clicked.connect(self.choose_some_file)
        self.ChooseFolder.clicked.connect(self.choose_folder)
        self.ChooseFolder_2.clicked.connect(self.start_koutu)
        self.pushButton_18.clicked.connect(self.show_color_dialog)
        self.pushButton_19.clicked.connect(self.choose_background_image)

    def open_and_select_file(self, file_path):
        file_path = file_path.replace("/", "\\")
        # 将文件路径转换为绝对路径
        absolute_path = os.path.abspath(file_path)
        # 检查文件是否存在
        if not os.path.exists(absolute_path):
            print(f"文件 {file_path} 不存在")
            return
        # 检查文件是否是一个文件
        if not os.path.isfile(absolute_path):
            print(f"路径 {file_path} 不是一个文件")
            return
        # 获取文件所在的文件夹路径
        folder_path = os.path.dirname(absolute_path)
        # 打开文件夹并选中指定文件
        subprocess.Popen(f'explorer /select,"{absolute_path}"',
                         cwd=folder_path,
                         shell=True)

    def show_color_dialog(self):
        # 创建颜色对话框并获取所选颜色
        color = QColorDialog.getColor()

        if color.isValid():
            # 设置按钮的背景色为所选颜色
            self.label_5.setStyleSheet(f'background-color: {color.name()}')
            self.bgcolor = f"{color.red()},{color.green()},{color.blue()},{color.alpha()}"
            print(self.bgcolor)

    def showm(self, index):
        if index == 0:
                self.pushButton_18.hide()
                self.label_5.hide()
                self.pushButton_19.hide()
                self.label_6.hide()
                self.way = 0
        elif index == 1:
                self.pushButton_19.hide()
                self.label_6.hide()
                self.label_5.show()
                self.pushButton_18.show()
                self.way = 1
        elif index == 2:
                self.pushButton_18.hide()
                self.label_5.hide()
                self.label_6.show()
                self.pushButton_19.show()
                self.way = 2

    def choose_single_file(self):
        self.moshi = 0
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Image Files (*.jpg *.jpeg *.png *.gif *.bmp *.tif *.tiff)"])
        file_dialog.exec()

        selected_files = file_dialog.selectedFiles()
        if selected_files:
                image_file = selected_files[0]
                # 在这里可以处理选择的图像文件
                print("Selected image file:", image_file)
                self.label.setText(image_file)
                self.imgpath = image_file

    def choose_background_image(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilters(["Image Files (*.jpg *.jpeg *.png *.gif *.bmp *.tif *.tiff)"])
        file_dialog.exec()

        selected_files = file_dialog.selectedFiles()
        if selected_files:
                image_file = selected_files[0]
                # 在这里可以处理选择的图像文件
                print("Selected image file:", image_file)
                self.label_6.setText(image_file)
                self.backbgound_imgpath = image_file

    def choose_some_file(self):
        self.moshi = 1
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
        self.moshi = 1
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

    def exchange_bg(self, input_path,bg_path,output_path,model_name):
        # 打开原始图像和替换背景图像
        original_image = Image.open(input_path)
        background_image = Image.open(bg_path)
        # 调整替换背景图像的尺寸，使其与原始图像尺寸匹配
        background_image = background_image.resize(original_image.size)
        # 将原始图像和替换背景图像转换为RGBA模式
        original_image = original_image.convert("RGBA")
        background_image = background_image.convert("RGBA")
        # 使用rembg库对原始图像进行背景去除处理
        #session = new_session(model_name)
        bg_removed_image = remove(original_image, session=model_name)
        # 将去除背景的图像与调整后的替换背景图像进行合并
        merged_image = Image.alpha_composite(background_image, bg_removed_image)
        # 保存合并后的图像
        save_path = self.convert_slashes(output_path)
        merged_image.save(save_path)

    def play_sound(self, sound_file):
        pygame.mixer.init()
        pygame.mixer.music.load(sound_file)
        pygame.mixer.music.play()

    def start_koutu(self):
        #from rembg import new_session, remove
        if self.label.text() == "Path":
            pass
        elif self.way == 2 and self.label_6.text() == "Path":
            pass
        elif self.moshi == 0:
            folder_dialog = QFileDialog()
            folder_path = folder_dialog.getExistingDirectory(self, "请选择保存路径Please select a save path", "")
            # 获取保存文件路径
            #save_path, _ = QFileDialog.getSaveFileName(None, '保存文件', '', 'PNG 文件 (*.png)')
            #print(folder_path)
            if folder_path == "":
                pass
            else:
                self.hide()
                model_name = self.comboBox.currentText()
                session = new_session(model_name)
                #output = remove(input, session=session)
                input_path = self.imgpath
                output_path = folder_path + "/" + self.get_filename(input_path) + ".png"
                output_pil_path = self.convert_slashes(output_path)
                #print(output_path)

                #input = cv2.imread(input_path)
                #input = cv2.cvtColor(input, cv2.COLOR_BGR2RGB)
                input = Image.open(input_path)
                if self.way == 0:
                    output = remove(input, session=session)
                    #cv2.imwrite(output_path, output)
                    output.save(output_pil_path)
                    if self.ifaudio == "True":
                        self.play_sound(self.sound_file)
                    pyautogui.alert("已完成抠图\nThe cutout task has been completed")  # 提示音
                    self.open_and_select_file(output_path)
                elif self.way == 1:
                    string = self.bgcolor
                    tuple_values = tuple(map(int, string.split(",")))

                    output = remove(input, session=session,bgcolor=tuple_values)
                    #cv2.imwrite(output_path, output)
                    output.save(output_pil_path)
                    if self.ifaudio == "True":
                        self.play_sound(self.sound_file)
                    pyautogui.alert("已完成抠图\nThe cutout task has been completed")  # 提示音
                    self.open_and_select_file(output_path)

                elif self.way == 2:
                    print("wtf")

                    bgpath = self.backbgound_imgpath
                    save_path = folder_path + "/" + self.get_filename(input_path) + ".png"
                    #save_path = self.convert_slashes(save_path)
                    self.exchange_bg(input_path,bgpath,save_path,model_name=session)
                    if self.ifaudio == "True":
                        self.play_sound(self.sound_file)
                    pyautogui.alert("已完成抠图\nThe cutout task has been completed")  # 提示音
                    self.open_and_select_file(save_path)

        elif self.moshi == 1:

            folder_dialog = QFileDialog()
            folder_path = folder_dialog.getExistingDirectory(self, "请选择保存路径Please select a save path", "")
            if folder_path == "":
                pass
            else:
                self.hide()

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

                model_name = self.comboBox.currentText()
                session = new_session(model_name)
                files = self.somefiles

                count = len(files)
                value = 0

                for file in files:
                    value += (1/count)*100
                    # 更新进度条的值
                    progress_bar.setValue(value)
                    progress_dialog.setLabelText(file)
                    QApplication.processEvents()
                    # 如果用户点击了取消按钮，则停止循环
                    if progress_dialog.wasCanceled():
                        break

                    if self.way == 0:
                        input = Image.open(file)
                        output = remove(input, session=session)
                        output_path = folder_path + "/" + self.get_filename(file) + ".png"
                        output_pil_path = self.convert_slashes(output_path)
                        output.save(output_pil_path)
                    if self.way == 1:
                        input = Image.open(file)
                        string = self.bgcolor
                        tuple_values = tuple(map(int, string.split(",")))
                        output = remove(input, session=session, bgcolor=tuple_values)
                        output_path = folder_path + "/" + self.get_filename(file) + ".png"
                        output_pil_path = self.convert_slashes(output_path)
                        output.save(output_pil_path)
                    if self.way == 2:
                        bgpath = self.backbgound_imgpath
                        save_path = folder_path + "/" + self.get_filename(file) + ".png"
                        self.exchange_bg(file, bgpath, save_path, model_name=session)

                # 更新进度条的值
                progress_bar.setValue(100)
                QApplication.processEvents()
                progress_dialog.close()
                if self.ifaudio == "True":
                    self.play_sound(self.sound_file)
                pyautogui.alert("已完成抠图\nThe cutout task has been completed")  # 提示音
                os.startfile(folder_path)


    def get_filename(self, path):
        path = path.split("/")
        last_part = path[-1]
        last_part = last_part.split(".")
        last_name = last_part[0]
        return last_name




    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path"))
        self.groupBox.setTitle(_translate("MainWindow", self.lanpack[51]))
        self.label_3.setText(_translate("MainWindow", f"{self.lanpack[52]}\n"
f"{self.lanpack[53]}\n"
f"{self.lanpack[54]}\n"
f"{self.lanpack[55]}\n"
f"{self.lanpack[56]}\n"
f"{self.lanpack[57]}\n"
f"{self.lanpack[58]}\n"
f"{self.lanpack[59]}"))
        self.label_4.setText(_translate("MainWindow", self.lanpack[60]))
        self.comboBox_2.setItemText(0, _translate("MainWindow", self.lanpack[61]))
        self.comboBox_2.setItemText(1, _translate("MainWindow", self.lanpack[62]))
        self.comboBox_2.setItemText(2, _translate("MainWindow", self.lanpack[63]))
        self.label_2.setText(_translate("MainWindow", self.lanpack[50]))
        self.comboBox.setItemText(0, _translate("MainWindow", "u2net"))
        self.comboBox.setItemText(1, _translate("MainWindow", "u2netp"))
        self.comboBox.setItemText(2, _translate("MainWindow", "u2net_human_seg"))
        self.comboBox.setItemText(3, _translate("MainWindow", "u2net_cloth_seg_2"))
        self.comboBox.setItemText(4, _translate("MainWindow", "silueta"))
        self.comboBox.setItemText(5, _translate("MainWindow", "isnet-general-use_2"))
        self.comboBox.setItemText(6, _translate("MainWindow", "isnet-anime"))
        self.label_6.setText(_translate("MainWindow", "Path"))
        self.pushButton_19.setText(_translate("MainWindow", self.lanpack[65]))
        self.ChooseFolder_2.setText(_translate("MainWindow", self.lanpack[66]))
        self.SingleFile.setText(_translate("MainWindow", self.lanpack[47]))
        self.ChooseFiles.setText(_translate("MainWindow", self.lanpack[48]))
        self.ChooseFolder.setText(_translate("MainWindow", self.lanpack[49]))
        self.pushButton_18.setText(_translate("MainWindow", self.lanpack[64]))

