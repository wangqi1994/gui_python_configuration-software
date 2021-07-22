import sys
import cv2
import configparser
from map import *

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPixmap, QPen, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel




class Ditu_fenbushi(QWidget, Ui_map):
    """地图操作窗口"""
    def __init__(self, parent=None):
        super(Ditu_fenbushi, self).__init__(parent)
        self.setupUi(self)

        # 新建MyLabel的类
        self.map_position = Mylabel_fenbushi(self.scrollAreaWidgetContents)
        # 读取地图文件
        img = cv2.imread('./map.png')
        # 获取图像高度和宽度值
        height, width, bytesPerComponent = img.shape
        # 设置地图尺寸，为坐标计算做准备
        self.map_position.setGeometry(QRect(0, 0, width, height))
        print(self.map_position.width(), self.map_position.height())

        bytesPerLine = 3 * width
        cv2.cvtColor(img, cv2.COLOR_BGR2RGB, img)
        QImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
        self.pixmap = QPixmap.fromImage(QImg)

        self.map_position.setPixmap(self.pixmap)
        # CrossCursor 十字型 PointingHandCursor 手型 ArrowCursor 箭头型
        self.map_position.setCursor(Qt.ArrowCursor)


        # self.show()
    # 重写地图页面的关闭窗口事件
    def closeEvent(self, e):
        # global fenbushi_flag
        self.box = QMessageBox(QMessageBox.Warning, "系统提示信息", "是否完成配置并退出地图？")
        qyes = self.box.addButton(self.tr("是"), QMessageBox.YesRole)
        qno = self.box.addButton(self.tr("否"), QMessageBox.NoRole)
        self.box.exec_()
        if self.box.clickedButton() == qyes:
            print(self.map_position.position,self.map_position.position_str)
            print(type(self.map_position.position))
            # print(fenbushi_list, len(fenbushi_list))
            # print(fenbushi_flag)
            # if fenbushi_flag == 1:
            #     fenbushi_point[0].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[0].setText(self.map_position.position)
            # elif fenbushi_flag == 2:
            #     fenbushi_point[1].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[1].setText(self.map_position.position)
            # elif fenbushi_flag == 3:
            #     fenbushi_point[2].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[2].setText(self.map_position.position)
            # elif fenbushi_flag == 4:
            #     fenbushi_point[3].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[3].setText(self.map_position.position)
            # elif fenbushi_flag == 5:
            #     fenbushi_point[4].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[4].setText(self.map_position.position)
            # elif fenbushi_flag == 6:
            #     fenbushi_point[5].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[5].setText(self.map_position.position)
            # elif fenbushi_flag == 7:
            #     fenbushi_point[6].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[6].setText(self.map_position.position)
            # elif fenbushi_flag == 8:
            #     fenbushi_point[7].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[7].setText(self.map_position.position)
            # elif fenbushi_flag == 9:
            #     fenbushi_point[8].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[8].setText(self.map_position.position)
            # elif fenbushi_flag == 10:
            #     fenbushi_point[9].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[9].setText(self.map_position.position)
            # elif fenbushi_flag == 11:
            #     fenbushi_point[10].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[10].setText(self.map_position.position)
            # elif fenbushi_flag == 12:
            #     fenbushi_point[11].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[11].setText(self.map_position.position)
            # elif fenbushi_flag == 13:
            #     fenbushi_point[12].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[12].setText(self.map_position.position)
            # elif fenbushi_flag == 14:
            #     fenbushi_point[13].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[13].setText(self.map_position.position)
            # elif fenbushi_flag == 15:
            #     fenbushi_point[14].setText(self.map_position.fenbushi_poi)
            #     fenbushi_list[14].setText(self.map_position.position)

            e.accept()
            QWidget.closeEvent(self, e)



            # sys.exit().accept()

        else:
            e.ignore()

# 重写新的Qlabel类-对应分布式地图展示
class Mylabel_fenbushi(QLabel):
    def __init__(self, parent=None):
        super(Mylabel_fenbushi, self).__init__(parent)
        self.x0 = 0
        self.y0 = 0
        self.position = []
        self.begin_point = QPoint()
        self.end_point = QPoint()
        self.position_point = []
        self.position_str = []
        self.flag_click = None  # 左键False 右键 True
        self.flag_left = False
        self.flag_right = False
        self.flag_mid = False

        self.pen1 = QPen()
        self.pen1.setColor(Qt.blue)
        self.pen1.setWidth(10)
        self.pen2 = QPen()
        self.pen2.setColor(Qt.red)
        self.pen2.setWidth(10)

        # 创建一个Qlabal实现鼠标位置跟踪，展示转变后坐标
        self.label = QLabel(self)
        self.label.setText('')
        # 设定初始位置
        print(self.label.height())
        self.label.move(300, 300)
        # 背景色和字体大小设置
        self.label.setStyleSheet('background:white;font-size:15px;')
        # 开启鼠标位置跟踪
        self.setMouseTracking(True)
        print(self.width(), self.height())


    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.flag_left = True
            # self.begin_point = event.pos()
            # self.x0 = event.x()
            # self.y0 = event.y()
            # self.end_point = event.pos()
            # self.update()
        elif event.button() == Qt.RightButton:
            self.flag_right = True

    # 鼠标移动
    def mouseMoveEvent(self, event):
        # # if event.buttons() == Qt.LeftButton:
        # #     self.end_point = event.pos()
        # if event.buttons() and Qt.LeftButton:
        #     self.endPoint = event.pos()
        #
        #     # self.update()
        x = event.localPos().x()
        y = event.localPos().y()
        self.label.move(x, y)
        # 设置标签的显示
        p_move = ",".join([str(i) for i in [int((x - self.width() / 2) * 0.05 * 1000) / 1000,
                                            int((self.height() / 2 - y) * 0.05 * 1000) / 1000, 0]])
        self.label.setText('(' + p_move + ')')
        # 自适应大小：因为x的坐标可能是0，有可能是100，y同理，所以label长度需要自适应
        self.label.adjustSize()
        print(self.height(), self.width())
        print("原先", x, y)
        print("当前鼠标坐标:", p_move)

    def mouseReleaseEvent(self, event):
        painter_p = QPainter(self.pixmap())
        self.end_point = event.pos()

        if event.button() == Qt.LeftButton:
            self.position_point.append(self.end_point)
            print(int((self.position_point[-1].x()-self.width()/2)*0.05*1000)/1000,type((self.position_point[-1].x()-self.width()/2)*0.05))
            # 将坐标点坐标转换为str类型
            position_int_str =",".join( [str(i) for i in[int((self.position_point[-1].x()-self.width()/2)*0.05*1000)/1000, int((self.height()/2-self.position_point[-1].y())*0.05*1000)/1000, 0]])
            # 各个坐标点写入列表
            self.position_str.append(position_int_str)
            # print(round(self.position_str[0],3))
            self.fenbushi_poi = self.position_str[0]
            # print(self.fenbushi_poi)
            self.fenbushi_poilist = self.position_str[1:]
            self.position= ";".join(self.fenbushi_poilist)
            # print(self.height(), self.width())
            # # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
            print(self.position)

            # 设置线颜色（蓝）粗细形式
            if len(self.position_point) == 1:
                painter_p.setPen(QPen(self.pen1))
                painter_p.drawPoint(self.position_point[0])
            else:
                painter_p.setPen(QPen(self.pen2))
                # 画点
                # painter_p.drawPoint(self.begin_point)
                painter_p.drawPoint(self.position_point[-1])
        elif event.button() == Qt.RightButton and len(self.position_point) > 0:
            painter_p.setPen(QPen(Qt.white, 10))
            painter_p.drawPoint(self.position_point[-1])
            del self.position_point[-1]
            # 各个坐标点写入列表
            del self.position_str[-1]
            # print(round(self.position_str[0],3))
            self.fenbushi_poi = self.position_str[0]
            # print(self.fenbushi_poi)
            self.fenbushi_poilist = self.position_str[1:]
            self.position = ";".join(self.fenbushi_poilist)
            # print(self.height(), self.width())
            # # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
            print(self.position)

        self.update()



    def paintEvent(self, event):
        super().paintEvent(event)

        # 实现双缓冲
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pixmap())




if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Ditu_fenbushi()
    demo.show()
    sys.exit(app.exec_())