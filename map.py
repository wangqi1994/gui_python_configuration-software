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
        # 新建MyLabel的类
        self.map_position = MyLabel(self)
        self.map_position.setGeometry(QRect(20, 20, 800, 800))

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

        self.position.append([self.x0, self.y0, 0])
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