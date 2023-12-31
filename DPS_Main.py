import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from test import Ui_MainWindow
from PyQt6.QtCore import Qt,QUrl,QPoint,QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QMouseEvent, QColor
import time
import os
from tools.koutu import Koutu  #类名
from tools.zip_image import Zip_image
from tools.imgtoscan import Imgtoscan
from tools2.recform import Rec_form
from tools2.reccha import Rec_cha
from tools2.clearbimg import CBIX2 #clear bigger images x2
from tools2.ctsvg import CTSvg
from tools2.resize import ReSize
from tools2.drename import DRename
from tools2.dreform import DReformate
from tools2.icomaker import ICOMaker
from tools2.gifdevider import GIFDevider
from tools2.gifmaker import GIFMaker
from tools2.svgpro import SVGPro
from tools2.plusimg import PLUSImg
from tools2.turnimg import TURNImg
from tools2.aipainter import AIPainter
from tools2.ccutimg import CCUTImg
from tools2.videodevider import VIDEODevider
from tools2.videomaker import VIDEOMaker
from tools2.imgtopdf import IMGtoPDF
from tools2.pdftoimg import PDFtoIMG
from tools2.pdftodocx import PDFtoDOCX
from tools2.printpdf import PDFPrinter
from tools2.turnpdf import TURNPdf
from tools2.pdfdevider import PDFDevider
from tools2.pdfpluser import PDFPluser
from tools2.pdfnumpluser import PDFNumAdder

class SKoutu(QMainWindow, Koutu): #Koutu类名
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class SRemwatermark_img(QMainWindow, Zip_image):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class ImgToScan(QMainWindow, Imgtoscan):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class RecForm(QMainWindow, Rec_form):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class RecCha(QMainWindow, Rec_cha):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class CBIx2(QMainWindow, CBIX2):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class ToSvg(QMainWindow, CTSvg):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class Resize(QMainWindow, ReSize):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class DReName(QMainWindow, DRename):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class DReForm(QMainWindow, DReformate):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class ICOMAKER(QMainWindow, ICOMaker):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class GIFDEVIDER(QMainWindow, GIFDevider):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class GIFMAKER(QMainWindow, GIFMaker):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class SVGPRO(QMainWindow, SVGPro):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PLUSIMG(QMainWindow, PLUSImg):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class TURNIMG(QMainWindow, TURNImg):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class AIPAINTER(QMainWindow, AIPainter):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class CCUTIMG(QMainWindow, CCUTImg):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class VIDEODEVIDER(QMainWindow, VIDEODevider):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class VIDEOMAKER(QMainWindow, VIDEOMaker):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class IMGTOPDF(QMainWindow, IMGtoPDF):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFTOIMG(QMainWindow, PDFtoIMG):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFTODOCX(QMainWindow, PDFtoDOCX):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFPRINTER(QMainWindow, PDFPrinter):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class TURNPDF(QMainWindow, TURNPdf):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFDEVIDER(QMainWindow, PDFDevider):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFPLUSER(QMainWindow, PDFPluser):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

class PDFNUMADDER(QMainWindow, PDFNumAdder):
    def __init__(self):
        super().__init__()

        self.setupUi(self)


class MyForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        # 创建UI对象
        self.ui = Ui_MainWindow()
        # 设置UI
        self.ui.setupUi(self)
        self.setWindowFlag(Qt.WindowType.FramelessWindowHint, True)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        #self.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
        self.setMouseTracking(True)
        self.draggable = False
        self.offset = QPoint()
        self.animation = QPropertyAnimation(self, b"windowOpacity")
        self.animation.setDuration(1000)  # 动画时长为1秒
        self.animation.setStartValue(float(self.ui.config[3]))  # 开始时的透明度
        self.animation.setEndValue(0.0)  # 结束时的透明度为0
        self.animation.setEasingCurve(QEasingCurve.Type.OutQuad)  # 设置缓动曲线
        self.setWindowTitle("DaYe PhotoStudio")

        self.skoutu = None
        self.sremwatermark_img = None
        self.imgtoscan = None
        self.recform = None
        self.reccha = None
        self.cbix2 = None
        self.tosvg = None
        self.run_resize = None
        self.drename = None
        self.drform = None
        self.icocreater = None
        self.devidegif = None
        self.makegif = None
        self.runsvgpro = None
        self.plusimages = None
        self.runturnimg = None
        self.runaipainter = None
        self.runccutimg = None
        self.runvideodevider = None
        self.runvideomaker = None
        self.runimgtopdf = None
        self.runpdftoimg = None
        self.runpdftodocx = None
        self.runpdfprinter = None
        self.turnpdf = None
        self.runpdfdevider = None
        self.runpdfpluser = None
        self.runpdfnumadder = None

        self.ui.coutu.clicked.connect(self.koutu)
        self.ui.windowbutoumingdu.valueChanged.connect(self.changewindowo)
        self.ui.completesettings.clicked.connect(self.finishisetup)
        self.ui.quit.clicked.connect(self.closewindow)
        self.ui.choosebg_btn.clicked.connect(self.choosebg)
        self.ui.deletebg_btn.clicked.connect(self.deletebg)
        self.ui.hidewindow.clicked.connect(self.showMinimized)
        self.ui.qushuiyin.clicked.connect(self.remwatermark_img)
        self.ui.linkwebsite.clicked.connect(self.visitwebsite)
        self.ui.scanfile.clicked.connect(self.run_imgtoscan)
        self.ui.shibieexcel.clicked.connect(self.run_recform)
        self.ui.wenzishibie.clicked.connect(self.run_reccha)
        self.ui.qingxifanda.clicked.connect(self.run_cbix2)
        self.ui.weitu_shiliang.clicked.connect(self.run_tosvg)
        self.ui.resize.clicked.connect(self.run_resizef)
        self.ui.rename.clicked.connect(self.run_rename)
        self.ui.changeformat.clicked.connect(self.run_reform)
        self.ui.makeico.clicked.connect(self.run_icomaker)
        self.ui.devidegif.clicked.connect(self.run_gifdevider)
        self.ui.addgif.clicked.connect(self.run_gifmaker)
        self.ui.pushButton_13.clicked.connect(self.run_svgpro)
        self.ui.addphotos.clicked.connect(self.run_plusimg)
        self.ui.turnphotos.clicked.connect(self.run_turnimg)
        self.ui.cleancharacter.clicked.connect(self.run_aipainter)
        self.ui.findxiangsitu.clicked.connect(self.run_ccutimg)
        self.ui.daochuzhen.clicked.connect(self.run_videodevider)
        self.ui.shipinhecheng.clicked.connect(self.run_videomaker)
        self.ui.photo_pdf.clicked.connect(self.run_imgtopdf)
        self.ui.pdf_photo.clicked.connect(self.run_pdftoimg)
        self.ui.pdf_word.clicked.connect(self.run_pdftodocx)
        self.ui.word_pdf.clicked.connect(self.run_pdfprinter)
        self.ui.pdfwenben.clicked.connect(self.run_pdfturner)
        self.ui.pdfprinter.clicked.connect(self.run_pdfdevider)
        self.ui.pdfreader.clicked.connect(self.run_pdfpluser)
        self.ui.pdfaddyema.clicked.connect(self.run_pdfnumadder)

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = True
            self.offset = event.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.draggable:
            self.move(self.mapToGlobal(event.pos() - self.offset))

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.draggable = False

    def closewindow(self):
        if self.ui.config[4] == "True":
            self.animation.start()  # 启动动画
            # 动画结束后关闭窗口
            self.animation.finished.connect(self.close)
        else:
            self.close()

    def koutu(self):
        print("抠图")
        if not self.skoutu:
            self.skoutu = SKoutu()
            #self.skoutu.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.skoutu.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[5]}")
        self.skoutu.show()

    def remwatermark_img(self):
        print("图片压缩")
        if not self.sremwatermark_img:
            self.sremwatermark_img = SRemwatermark_img()
            #self.skoutu.setWindowFlag(Qt.WindowType.WindowStaysOnTopHint, True)
            self.sremwatermark_img.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[6]}")
        self.sremwatermark_img.show()

    def run_imgtoscan(self):
        print("文档扫描")
        if not self.imgtoscan:
            self.simgtoscan = ImgToScan()
            self.simgtoscan.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[7]}*")
        self.simgtoscan.show()

    def run_recform(self):
        print("表格识别")
        if not self.recform:
            self.recform = RecForm()
            self.recform.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[8]}*")
        self.recform.show()

    def run_reccha(self):
        print("文字识别")
        if not self.reccha:
            self.reccha = RecCha()
            self.reccha.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[9]}")
        self.reccha.show()

    def run_cbix2(self):
        print("清晰放大")
        if not self.cbix2:
            self.cbix2 = CBIx2()
            self.cbix2.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[10]}")
        self.cbix2.show()

    def run_tosvg(self):
        print("位图转矢量")
        if not self.tosvg:
            self.tosvg = ToSvg()
            self.tosvg.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[11]}")
        self.tosvg.show()

    def run_resizef(self):
        print("修改尺寸")
        if not self.run_resize:
            self.run_resize = Resize()
            self.run_resize.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[12]}")
        self.run_resize.show()

    def run_rename(self):
        print("批量重命名")
        if not self.drename:
            self.drename = DReName()
            self.drename.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[13]}")
        self.drename.show()

    def run_reform(self):
        print("格式转换")
        if not self.drform:
            self.drform = DReForm()
            self.drform.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[14]}")
        self.drform.show()

    def run_icomaker(self):
        print("ICO制作")
        if not self.icocreater:
            self.icocreater = ICOMAKER()
            self.icocreater.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[15]}")
        self.icocreater.show()

    def run_gifdevider(self):
        print("GIF拆分")
        if not self.devidegif:
            self.devidegif = GIFDEVIDER()
            self.devidegif.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[16]}")
        self.devidegif.show()

    def run_gifmaker(self):
        print("GIF合成")
        if not self.makegif:
            self.makegif = GIFMAKER()
            self.makegif.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[17]}")
        self.makegif.show()

    def run_svgpro(self):
        print("批量打印")
        if not self.runsvgpro:
            self.runsvgpro = SVGPRO()
            self.runsvgpro.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[18]}")
        self.runsvgpro.show()

    def run_plusimg(self):
        print("图像拼接")
        if not self.plusimages:
            self.plusimages = PLUSIMG()
            self.plusimages.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[19]}")
        self.plusimages.show()

    def run_turnimg(self):
        print("图像旋转")
        if not self.runturnimg:
            self.runturnimg = TURNIMG()
            self.runturnimg.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[20]}")
        self.runturnimg.show()

    def run_aipainter(self):
        print("AI绘画")
        if not self.runaipainter:
            self.runaipainter = AIPAINTER()
            self.runaipainter.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[21]}")
        self.runaipainter.show()

    def run_ccutimg(self):
        print("圆角裁剪")
        if not self.runccutimg:
            self.runccutimg = CCUTIMG()
            self.runccutimg.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[22]}")
        self.runccutimg.show()

    def run_videodevider(self):
        print("视频导出帧")
        if not self.runvideodevider:
            self.runvideodevider = VIDEODEVIDER()
            self.runvideodevider.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[24]}*")
        self.runvideodevider.show()

    def run_videomaker(self):
        print("视频合成")
        if not self.runvideomaker:
            self.runvideomaker = VIDEOMAKER()
            self.runvideomaker.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[25]}*")
        self.runvideomaker.show()

    def run_imgtopdf(self):
        print("图片转PDF")
        if not self.runimgtopdf:
            self.runimgtopdf = IMGTOPDF()
            self.runimgtopdf.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[27]}")
        self.runimgtopdf.show()

    def run_pdftoimg(self):
        print("PDF转图片")
        if not self.runpdftoimg:
            self.runpdftoimg = PDFTOIMG()
            self.runpdftoimg.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[28]}")
        self.runpdftoimg.show()

    def run_pdftodocx(self):
        print("PDF转Word")
        if not self.runpdftodocx:
            self.runpdftodocx = PDFTODOCX()
            self.runpdftodocx.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[29]}")
        self.runpdftodocx.show()

    def run_pdfprinter(self):
        print("PDF打印")
        if not self.runpdfprinter:
            self.runpdfprinter = PDFPRINTER()
            self.runpdfprinter.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[30]}")
        self.runpdfprinter.show()

    def run_pdfturner(self):
        print("PDF旋转")
        if not self.turnpdf:
            self.turnpdf = TURNPDF()
            self.turnpdf.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[31]}")
        self.turnpdf.show()

    def run_pdfdevider(self):
        print("PDF拆分")
        if not self.runpdfdevider:
            self.runpdfdevider = PDFDEVIDER()
            self.runpdfdevider.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[32]}")
        self.runpdfdevider.show()

    def run_pdfpluser(self):
        print("PDF合并")
        if not self.runpdfpluser:
            self.runpdfpluser = PDFPLUSER()
            self.runpdfpluser.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[33]}")
        self.runpdfpluser.show()

    def run_pdfnumadder(self):
        print("PDF添加页码")
        if not self.runpdfnumadder:
            self.runpdfnumadder = PDFNUMADDER()
            self.runpdfnumadder.setWindowTitle(f"DaYe PhotoStudio-{self.ui.lanpack[34]}")
        self.runpdfnumadder.show()


    def changewindowo(self, value):
        self.sopacity = value / 100
        #print(self.sopacity)
        self.ui.label_10.setText("{}%".format(value))
        self.setWindowOpacity(self.sopacity)  #self就是MainWindow

    def finishisetup(self):
        lanpack = self.ui.language.currentText()
        theme = self.ui.theme.currentText()
        if theme == "Dark" or theme == "暗色主题":
            theme = 0
        elif theme == "Light" or theme == "亮色主题":
            theme = 1
        elif theme == "Follow the system" or theme == "跟随系统":
            theme = 2
        bgpath = self.ui.label_6.text()
        sopacity = self.ui.windowbutoumingdu.value() / 100
        ifjianyin = self.ui.jianyindonghua.isChecked()
        iffinishiaudio = self.ui.finishiaudio.isChecked()
        config = []
        config.append(lanpack)
        config.append(f"{theme}")
        config.append(bgpath)
        config.append(f"{sopacity}")
        config.append(f"{ifjianyin}")
        config.append(f"{iffinishiaudio}")
        config.append(f"{self.ui.config[6]}")
        print(config)
        with open('config.txt', 'w', encoding='utf-8') as file:
            for item in config:
                file.write(item + '\n')

    def choosebg(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Image Files (*.png *.jpg *.bmp *.gif)")

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            selected_files = file_dialog.selectedFiles()
            if len(selected_files) > 0:
                self.file_path = selected_files[0]
                self.ui.label_6.setText(self.file_path)
                print("Selected file:", self.file_path)
        else:
            self.file_path = ""

    def deletebg(self):
        self.ui.label_6.setText("")

    def visitwebsite(self):
        os.popen(f"start {self.ui.config[6]}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    #form.setWindowOpacity(0.5)
    form.show()
    sys.exit(app.exec())
