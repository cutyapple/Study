# CutyApple's PyQT5 Study.
# https://blog.naver.com/smilewhj/221044277007를 참고하였습니다.

import sys
from PyQt5.QtWidgets import QApplication, QWidget

# 함수를 이용하여 기본창을 띄우는 방법

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#
#     w = QWidget()
#     w.resize(250, 150)
#     w.move(300, 300)
#     w.setWindowTitle('Hello PyQT5!')
#     w.show()
#
#     w.resize(500, 500)
#
#     sys.exit(app.exec_())

# class를 이용하여 기본창을 띄우는 방법

# class basic_window(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Hello PyQT5!')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     basic_window = basic_window()
#     sys.exit(app.exec_())