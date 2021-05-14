# # import sys
# # from PyQt5.QtWidgets import *
# #
# #
# # class MainWindow(QMainWindow):
# #     def __init__(self, ):
# #         super(QMainWindow, self).__init__()
# #         self.number = 0
# #
# #         w = QWidget()
# #         self.setCentralWidget(w)
# #
# #         self.topFiller = QWidget()
# #         self.topFiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
# #         for filename in range(20):
# #             self.MapButton = QPushButton(self.topFiller)
# #             self.MapButton.setText(str(filename))
# #             self.MapButton.move(10, filename * 40)
# #
# #           ##创建一个滚动条
# #         self.scroll = QScrollArea()
# #         self.scroll.setWidget(self.topFiller)
# #
# #         self.vbox = QVBoxLayout()
# #         self.vbox.addWidget(self.scroll)
# #         w.setLayout(self.vbox)
# #
# #         self.statusBar().showMessage("底部信息栏")
# #         self.resize(300, 500)
# #
# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     mainwindow = MainWindow()
# #     mainwindow.show()
# #     sys.exit(app.exec_())
#
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
#
# class ListWidgetDemo(QWidget):
#     def __init__(self):
#         super(ListWidgetDemo, self).__init__()
#         self.initUI()
#
#
#     def initUI(self):
#         self.setWindowTitle("QTableWidget演示")
#         self.resize(500, 300)
#         layout = QHBoxLayout()
#         tablewidget = QTableWidget()
#         # 设置行数与列数
#         tablewidget.setRowCount(4)
#         tablewidget.setColumnCount(3)
#         # 设置标签行
#         tablewidget.setHorizontalHeaderLabels(['姓名', '年龄', '籍贯'])
#
#         nameItem = QTableWidgetItem("小明")
#         tablewidget.setItem(0, 0, nameItem)
#
#
#         ageItem = QTableWidgetItem("24")
#         tablewidget.setItem(0, 1, ageItem)
#
#         homeItem = QTableWidgetItem("北京")
#         tablewidget.setItem(0, 2, homeItem)
#
#         layout.addWidget(tablewidget)
#         self.setLayout(layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     main = ListWidgetDemo()
#     main.show()
#     sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self, ):
        super(QMainWindow, self).__init__()
        self.number = 0

        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(250, 2000)  #######设置滚动条的尺寸
        for filename in range(50):
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText(str(filename))
            self.MapButton.move(10, filename * 40)

          ##创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)

        self.statusBar().showMessage("底部信息栏")
        self.resize(300, 500)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())