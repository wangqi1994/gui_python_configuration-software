# -*- coding: utf-8 -*-

import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPen, QPainter, QGuiApplication
from PyQt5.QtCore import QRect, Qt, QLine, QPoint

from ditu import *


# 创建map类并传入Ui_map
class map(QWidget, Ui_map):
    """主窗口类"""
    def __init__(self, parent=None):
        super(map, self).__init__(parent)
        self.setupUi(self)
        #
        # self.x0 = 0
        # self.y0 = 0
        # x1 = 0
        # y1 = 0
        # self.flag = False
        # sss = []
        # self.begin_point = QPoint()
        # self.end_point = QPoint()

        self.lb = MyLabel(self)
        self.lb.setGeometry(QRect(20, 20, 800, 800))



        img = cv2.imread('map.png')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(QImg)

        self.lb.setPixmap(self.pixmap)

        self.lb.setCursor(Qt.CrossCursor)

        self.show()


    #     self.pix = QPixmap(800, 800)
    #     self.pix.fill(Qt.white)
    #
    #
    #
    #
    # def mousePressEvent(self, event):
    #     self.flag = True
    #     self.x0 = event.x()
    #     self.y0 = event.y()
    #
    #     # self.begin_point = self.end_point
    #     print(self.begin_point)
    #     self.update()
    #
    # def mouseReleaseEvent(self, event):
    #     self.flag = False
    #     self.end_point = event.pos()
    #     if not self.begin_point:
    #         self.begin_point = self.end_point
    #     print(self.end_point)
    #     self.update()
    #
    # def paintEvent(self, event):
    #     super().paintEvent(event)
    #     painter = QPainter(self.pix)
    #     # painter.setBackgroundMode(Qt.OpaqueMode)
    #     # painter.setBackground(self.pixmap)
    #     painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
    #
    #     painter.begin(self)
    #
    #     painter.drawLine(self.begin_point, self.end_point)
    #     self.begin_point = self.end_point
    #     painter.end()
    #     painter2 = QPainter(self)
    #     painter2.drawPixmap(0, 0, self.pix)


class MyLabel(QLabel):
    def __init__(self, parent=map):
        super(MyLabel, self).__init__(parent)
        self.setWindowTitle("绘图例子")

        self.x0 = 0
        self.y0 = 0
        x1 = 0
        y1 = 0
        self.flag = False
        sss = []
        self.begin_point = QPoint()
        self.end_point = QPoint()
        #
    #
    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()

        # self.begin_point = self.end_point
        # print(self.begin_point)
        self.update()


    def mouseReleaseEvent(self, event):
        self.flag = False
        self.end_point = event.pos()
        if not self.begin_point:
            self.begin_point = self.end_point
        print(self.begin_point)
        print(self.end_point)
        self.update()


    def paintEvent(self, event):
        super().paintEvent(event)

        painter = QPainter(self.pixmap())

        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))

        painter.begin(self)

        painter.drawLine(self.begin_point, self.end_point)
        self.begin_point = self.end_point
        painter.end()
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pixmap())








def main():
    app = QApplication(sys.argv)
    map_w = map()
    map_w.show()
    sys.exit(app.exec_())





if __name__ =='__main__':
    main()