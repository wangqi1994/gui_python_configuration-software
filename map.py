# -*- coding: utf-8 -*-

import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPen, QPainter, QGuiApplication
from PyQt5.QtCore import QRect, Qt, QLine, QPoint

from ditu import *


# 创建map类并传入Ui_map
class map(QMainWindow, Ui_map):
    """主窗口类"""
    def __init__(self, parent=None):
        super(map, self).__init__(parent)
        self.setupUi(self)



        self.lb = myLabel(self)
        self.lb.setGeometry(QRect(20, 20, 800, 800))
        # self.lb.setAttribute(Qt.WA_OpaquePaintEvent)

        img = cv2.imread('map.png')
        height, width, bytesPerComponent = img.shape
        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(QImg)

        self.lb.setPixmap(self.pixmap)

        self.lb.setCursor(Qt.CrossCursor)

        self.show()

    # 打开文件夹选择页面，选择生成文件保存路径
    def openFile(self):
        global get_directory_path
        # 获取选择的文件路径
        get_directory_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹", "C:/")


class myLabel(QLabel):

    x0 = 0
    y0 = 0
    x1 = 0
    y1 = 0
    flag = False
    sss=[]
    begin_point = QPoint()
    end_point = QPoint()

    # def mousePressEvent(self,event):
    #     self.flag = True
    #     self.x0 = event.x()
    #     self.y0 = event.y()
    #     self.begin_point = event.pos()
    #     self.end_point = self.begin_point
    #     self.update()
    # def mouseReleaseEvent(self,event):
    #     self.flag = False
    #     self.end_point = event.pos()
    #     self.update()
    # def paintEvent(self, event):  # 2
    #     painter = QPainter(self)
    #     painter.drawLine(self.begin_point, self.end_point)
    #     self.begin_point = self.end_point


#
    def mousePressEvent(self,event):
        self.flag = True
        self.x0 = event.x()
        self.y0 = event.y()
        # self.lastPoint = event.pos()
        # self.endPoint = self.lastPoint
        self.begin_point = event.pos()
        self.end_point = self.begin_point
        self.update()
    def mouseReleaseEvent(self,event):
        self.flag = False
        # self.lastPoint = event.pos()
        # self.endPoint = self.lastPoint
        self.end_point = event.pos()
        self.update()
    def paintEvent(self, QPaintEvent):
        painter = QPainter(self)
        painter.drawLine(self.begin_point, self.end_point)
        self.begin_point = self.end_point
        self.sss.append([self.x0, self.y0])
        print(self.sss)
#         if len(self.sss)> 2:
#             a, b = self.sss[0]
#             c, d = self.sss[1]
#             print(a,b,c,d)
#             aaa=QLine(a,b,c,d)
#             print(aaa)
#             # lin = QLine(QPoint(self.sss[0]), QPoint(self.sss[1]))
#             # print(lin)
#             painter = QPainter(self)
#             painter.begin(self)
#             painter.drawLine(a,b,c,d)
#
#             painter.setPen(QPen(Qt.red, 4, Qt.SolidLine))
#             painter.end()
#
#         else:
#             pass



# 创建info主窗口并传入Ui_info


# class myLabel(QLabel):
#
#
#
#     begin_point = QPoint()                             # 1
#     end_point = QPoint()
#
#     def paintEvent(self, QPaintEvent):                          # 2
#         painter = QPainter(self)
#         painter.drawLine(self.begin_point, self.end_point)
#         self.begin_point = self.end_point
#
#     def mousePressEvent(self, QMouseEvent):
#         if QMouseEvent.button() == Qt.LeftButton:
#             self.begin_point = QMouseEvent.pos()
#             self.end_point = self.begin_point
#             self.update()                                       # 3
#
#     def mouseMoveEvent(self, QMouseEvent):
#         if QMouseEvent.buttons() == Qt.LeftButton:
#             self.end_point = QMouseEvent.pos()
#             self.update()

def main():
    app = QApplication(sys.argv)
    map = map()
    sys.exit(app.exec_())





if __name__ =='__main__':
    main()