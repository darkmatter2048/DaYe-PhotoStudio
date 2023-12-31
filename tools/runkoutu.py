
#ui转换为py后运行会报错，不要修改，直接调用即可（当然，图片路径要改一下）

import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from koutu import Koutu

class MyForm(QMainWindow, Koutu):
    def __init__(self):
        super().__init__()
        # 创建UI对象
        self.ui = Koutu()
        # 设置UI
        self.ui.setupUi(self)
        self.setWindowTitle("DaYe PhotoStudio")
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyForm()
    #form.show()
    sys.exit(app.exec())
