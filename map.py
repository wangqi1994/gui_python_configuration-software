# -*- coding: utf-8 -*-

import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPen, QPainter
from PyQt5.QtCore import QRect, Qt, QLine, QPoint

from ditu import *


# 创建map类并传入Ui_map
class map(QWidget, Ui_map):
    """地图操作窗口"""
    def __init__(self, parent=None):
        super(map, self).__init__(parent)
        self.setupUi(self)

        # self.scrollArea = QtWidgets.QScrollArea()
        # self.scrollArea.setGeometry(QtCore.QRect(0, 0, 800, 800))
        # self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        # self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        # self.scrollArea.setWidgetResizable(False)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1024, 1024))
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.scrollAreaWidgetContents.sizePolicy().hasHeightForWidth())
        # self.scrollAreaWidgetContents.setSizePolicy(sizePolicy)
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")


        # 新建MyLabel的类
        self.map_position = MyLabel(self.scrollAreaWidgetContents)

        self.map_position.setGeometry(QRect(0, 0, 730, 924))
        print(self.map_position.width(), self.map_position.height())

        img = cv2.imread('map.png')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(QImg)

        self.map_position.setPixmap(self.pixmap)

        self.map_position.setCursor(Qt.CrossCursor)

        self.show()

# 重写新的Qlabel类
class MyLabel(QLabel):
    def __init__(self, parent=map):
        super(MyLabel, self).__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.flag = False
        self.position = []
        self.begin_point = QPoint()
        self.end_point = QPoint()

    def mousePressEvent(self, event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        self.update()

    def mouseReleaseEvent(self, event):
        self.flag = False
        self.end_point = event.pos()
        if not self.begin_point:
            self.begin_point = self.end_point

        self.position.append([(self.x0-self.width()/2)*0.05, (self.height()/2-self.y0)*0.05, 0])
        print(self.height(), self.width())
        # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
        print(self.position)
        print(self.begin_point)
        print(self.end_point)
        self.update()



    def paintEvent(self, event):
        super().paintEvent(event)
        # 实例化QPainter
        painter = QPainter(self.pixmap())
        # 设置线颜色（蓝）粗细形式
        painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        # 开始绘画
        painter.begin(self)
        # 画线
        painter.drawLine(self.begin_point, self.end_point)
        # 将前一个点赋值给起点，保证连续画线
        self.begin_point = self.end_point
        # 结束绘画
        painter.end()

        painter_p = QPainter(self.pixmap())
        # 设置线颜色（蓝）粗细形式
        painter_p.setPen(QPen(Qt.red, 10))
        # 开始绘画
        painter_p.begin(self)
        # 画点
        painter_p.drawPoint(self.begin_point)
        painter_p.drawPoint(self.end_point)
        # 将前一个点赋值给起点，保证连续画线
        self.begin_point = self.end_point
        # 结束绘画
        painter_p.end()

        # 实现双缓冲
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pixmap())


def main():
    app = QApplication(sys.argv)
    map_w = map()
    map_w.show()
    sys.exit(app.exec_())





if __name__ =='__main__':
    main()