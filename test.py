import sys
import cv2
import configparser
from map import *

from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QPainter, QPixmap, QPen, QImage
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
global get_directory_path

class Ditu_xunluoluxian(QWidget, Ui_map):
    """地图操作窗口"""

    def __init__(self, parent=None):
        super(Ditu_xunluoluxian, self).__init__(parent)
        self.setupUi(self)

        # 新建MyLabel的类
        self.map_position = Mylabel_xunluoluxian(self.scrollAreaWidgetContents)
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

        self.suofangimg = self.pixmap.scaled(self.size())  # 初始化缩放图
        self.singleOffset = QPoint(0, 0)  # 初始化偏移值

        # self.show()

    # 重写地图页面的关闭窗口事件
    def closeEvent(self, e):
        # global fenbushi_flag
        self.box = QMessageBox(QMessageBox.Warning, "系统提示信息", "是否完成配置并退出地图？")
        qyes = self.box.addButton(self.tr("是"), QMessageBox.YesRole)
        qno = self.box.addButton(self.tr("否"), QMessageBox.NoRole)
        self.box.exec_()
        if self.box.clickedButton() == qyes:
            print(self.map_position.position, self.map_position.position_str)
            print(type(self.map_position.position))
            e.accept()

            QWidget.closeEvent(self, e)

            # sys.exit().accept()

        else:
            e.ignore()

class Mylabel_xunluoluxian(QLabel):
    def __init__(self, parent=None):
        super(Mylabel_xunluoluxian, self).__init__(parent)

        self.x0 = 0
        self.y0 = 0
        self.flag_left = False
        self.flag_right = False
        self.flag_mid = False
        self.position_point = []
        self.position = []
        self.begin_point = QPoint()
        self.end_point = QPoint()
        self.position_str = []
        self.flag_click = None  # 左键False 右键 True


        global get_directory_path
        get_directory_path = "C:/Users/zxcwa/Desktop/info.conf"
        read_info = configparser.ConfigParser()
        read_info.read(get_directory_path )
        sections = read_info.sections()
        for i in sections:
            self.x0 = float(read_info[i]["autocharge_x"])
            # self.x0_tr = self.x0/0.05 + self.width()/2
            self.y0 = float(read_info[i]["autocharge_y"])
            # self.y0_tr = self.height()/2 - self.y0/0.05
            # print(self.x0,self.x0_tr,self.y0,self.y0_tr,self.width(),self.height())
            yaw0 = read_info[i]["autocharge_yaw"]
            # print(self.x0,type(int(0)))

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



    # 鼠标点击未释放
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

    #鼠标移动
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
        p_move = ",".join( [str(i) for i in[int((x-self.width()/2)*0.05*1000)/1000, int((self.height()/2-y)*0.05*1000)/1000, 0]])
        self.label.setText('(' + p_move + ')')
        # 自适应大小：因为x的坐标可能是0，有可能是100，y同理，所以label长度需要自适应
        self.label.adjustSize()
        print(self.height(),self.width())
        print("原先", x, y)
        print("当前鼠标坐标:", p_move)


    # 鼠标释放
    def mouseReleaseEvent(self, event):
        # 实例化Qpainter对象
        painter = QPainter(self.pixmap())
        # 鼠标左键添加操作
        if event.button() == Qt.LeftButton and not self.flag_mid:
            # 获取点击位置信息
            self.end_point = event.pos()

            # 依次存储点击位置信息
            self.position_point.append(self.end_point)
            # 充电点坐标转换
            self.x0_tr = self.x0 / 0.05 + self.width() / 2
            self.y0_tr = self.height() / 2 - self.y0 / 0.05
            # print(self.x0, self.x0_tr, self.y0, self.y0_tr, self.width(), self.height())
            # 设置充电点颜色大小
            painter.setPen(QPen(Qt.green, 10))
            # 画充电点

            painter.drawPoint(int(self.x0_tr), int(self.y0_tr))

            # 设置点颜色大小
            painter.setPen(QPen(Qt.red, 10))
            # 画点
            painter.drawPoint(self.position_point[-1])
            self.flag_left = False
            print(self.position_point)
            print(self.position_point[0].x())
            # 鼠标点击flag改为False，代表左键
            self.flag_click = False
            # 将坐标点坐标转换为str类型
            position_int_str = ",".join([str(i) for i in [int((self.position_point[-1].x() - self.width() / 2) * 0.05 * 1000) / 1000,
                                                          int((self.height() / 2 - self.position_point[-1].y()) * 0.05 * 1000) / 1000, 0]])
            # 各个坐标点写入列表
            self.position_str.append(position_int_str)
            self.position = ";".join(self.position_str)
            print(self.height(), self.width())
            # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
            print(self.position)
            print(self.begin_point)
            print(self.end_point)

            self.update()
        # 鼠标右键撤销操作
        elif event.button() == Qt.RightButton:
            if self.position_point:
                # 设置取消点颜色
                if not self.flag_mid:
                    painter.setPen(QPen(Qt.white, 10))
                    painter.drawPoint(self.position_point[-1])
            elif len(self.position_point) == 0:
                print('xiaochu')
                painter.setPen(QPen(Qt.white, 10))
                painter.drawPoint(int(self.x0_tr), int(self.y0_tr))

            self.flag_right = False

            print(self.position_point)
            # 鼠标点击flag改为True，代表右键
            self.flag_click = True

            self.update()

        if len(self.position_point) >= 1 and event.button:
            if not self.flag_click and not self.flag_mid:
                print(len(self.position_point),1)
                # 设置线颜色大小
                painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
                if len(self.position_point) == 1 :
                    painter.drawLine(int(self.x0_tr),int(self.y0_tr),int(self.position_point[0].x()),int(self.position_point[0].y()))
                    # print(type(self.x0),self.y0,type(self.position_point[0].x()),self.position_point[0].y())
                # painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
                else:
                    painter.drawLine(self.position_point[-2], self.position_point[-1])
                    # print(self.x0_tr, self.y0_tr, self.position_point[0].x(), self.position_point[0].y())
                self.flag_click = None
                self.update()

            if event.button() == Qt.MidButton:
                painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
                painter.drawLine(self.position_point[-1].x(), self.position_point[-1].y(), int(self.x0_tr),
                                 int(self.y0_tr))
                self.flag_mid = True

            if self.flag_click :
                print(len(self.position_point),2)
                # 设置取消线颜色大小
                painter.setPen(QPen(Qt.white, 4, Qt.SolidLine))
                if self.flag_mid:
                    painter.drawLine(self.position_point[-1].x(), self.position_point[-1].y(), int(self.x0_tr),
                                     int(self.y0_tr))
                    self.flag_mid = False
                elif len(self.position_point) == 1:
                    painter.drawLine(int(self.x0_tr), int(self.y0_tr), int(self.position_point[0].x()),
                                     int(self.position_point[0].y()))
                    if len(self.position_point) == 1:
                        self.position_point = []
                    self.position_str = []
                    self.position = ";".join(self.position_str)
                    print(self.height(), self.width())
                    # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
                    print(self.position)
                    print(self.begin_point)
                    print(self.end_point)
                # elif len(self.position_point) == 0:
                #     print('xiaochu')
                #     painter.drawPoint(int(self.x0_tr), int(self.y0_tr))
                else:
                    painter.drawLine(self.position_point[-2], self.position_point[-1])
                # 删除最后一个点

                    del self.position_point[-1]
                    del self.position_str[-1]
                    self.position = ";".join(self.position_str)
                    print(self.height(), self.width())
                    # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
                    print(self.position)
                    print(self.begin_point)
                    print(self.end_point)
                    print(len(self.position_point))
                self.update()
            self.flag_click = None
            # if event.button() == Qt.MidButton:
            #     painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
            #     painter.drawLine(self.position_point[-1].x(), self.position_point[-1].y(),int(self.x0_tr),int(self.y0_tr))
            #     self.flag_mid = True


            self.update()

    # 鼠标滚轮事件
    # 滚轮滑动事件

    def wheelEvent(self, event):
        #        if event.delta() > 0:                                                 # 滚轮上滚,PyQt4
        # This function has been deprecated, use pixelDelta() or angleDelta() instead.
        # self.pixmap = self.pixmap.scaled(self.size())  # 初始化缩放图
        # self.singleOffset = QPoint(0, 0)  # 初始化偏移值

        angle = event.angleDelta() / 8  # 返回QPoint对象，为滚轮转过的数值，单位为1/8度
        angleX = angle.x()  # 水平滚过的距离(此处用不上)
        angleY = angle.y()  # 竖直滚过的距离
        if angleY > 0:  # 滚轮上滚
            print("鼠标中键上滚")  # 响应测试语句
            self.suofangimg = self.pixmap().scaled(self.suofangimg.width() + 5,
                                                   self.suofangimg.height() + 5)
            newWidth = event.x() - (self.suofangimg.width() * (event.x() - self.singleOffset.x())) \
                       / (self.suofangimg.width() - 5)
            newHeight = event.y() - (self.suofangimg.height() * (event.y() - self.singleOffset.y())) \
                        / (self.suofangimg.height() - 5)
            self.singleOffset = QPoint(newWidth, newHeight)  # 更新偏移量
            self.update()
            # self.repaint()  # 重绘
        # else:  # 滚轮下滚
        #     print("鼠标中键下滚")  # 响应测试语句
        #     self.scaledImg = self.pixmap().scaled(self.scaledImg.width() - 5,
        #                                            self.scaledImg.height() - 5)
        #     newWidth = event.x() - (self.scaledImg.width() * (event.x() - self.singleOffset.x())) \
        #                / (self.scaledImg.width() + 5)
        #     newHeight = event.y() - (self.scaledImg.height() * (event.y() - self.singleOffset.y())) \
        #                 / (self.scaledImg.height() + 5)
        #     self.singleOffset = QPoint(newWidth, newHeight)  # 更新偏移量
        #     self.repaint()  # 重绘

        # self.flag = False
        # self.end_point = event.pos()
        # # with open("./info.conf", 'r') as read_info:
        # #     x = read_info.read()
        # #     print(x,type(x))
        # if not self.begin_point:
        #     self.begin_point = self.end_point
        #     # self.begin_point = self.charge_point
        # # 将坐标点坐标转换为str类型
        # position_int_str =",".join( [str(i) for i in[int((self.x0-self.width()/2)*0.05*1000)/1000, int((self.height()/2-self.y0)*0.05*1000)/1000, 0]])
        # # 各个坐标点写入列表
        # self.position_str.append(position_int_str)
        # self.position= ";".join(self.position_str)
        # print(self.height(), self.width())
        # # self.position.append([(self.x0-self.map_position.width()/2)*0.05, (self.map_position.height()/2-self.y0)*0.05, 0])
        # print(self.position)
        # print(self.begin_point)
        # print(self.end_point)

        # self.update()



    def paintEvent(self, event):
        super().paintEvent(event)

        # 实现双缓冲
        # painter2 = QPainter(self)
        # painter2.drawPixmap(0, 0, self.pixmap())



        # # 实例化QPainter
        # painter = QPainter(self.pixmap())
        # # 设置线颜色（蓝）粗细形式
        # # painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        # # 开始绘画
        # painter.begin(self)
        # 画线
        # if event.button() == Qt.RightButton:

        # if len(self.position_point) == 1:
        #     painter.drawLine(self.position_point[-1], self.position_point[-1])


        # if len(self.position_point) > 1:
        #     if not self.flag_click:
        #         print(len(self.position_point),1)
        #         painter.setPen(QPen(Qt.blue, 4, Qt.SolidLine))
        #         painter.drawLine(self.position_point[-2], self.position_point[-1])
        #
        #     else:
        #         print(len(self.position_point),2)
        #         painter.setPen(QPen(Qt.white, 4, Qt.SolidLine))
        #         painter.drawLine(self.position_point[-2], self.position_point[-1])
        # 将前一个点赋值给起点，保证连续画线
        # self.begin_point = self.end_point
        # 结束绘画
        # painter.end()



        # painter_p = QPainter(self.pixmap())
        # # 设置点颜色形状
        # # painter_p.setPen(QPen(Qt.red, 10))
        # # 开始绘画
        # painter_p.begin(self)
        # # 画点
        # if len(self.position_point) >= 1:
        #     print(len(self.position_point))
        #     if self.flag_left:
        #         print("tianjia")
        #     # for i in range(len(self.position_point)):
        # #     if event.button() == Qt.LeftButton:
        # #     painter_p.drawPoint(self.position_point[-1])
        #         painter_p.setPen(QPen(Qt.red, 10))
        #         painter_p.drawPoint(self.position_point[-1])
        #         self.flag_left = False


                 # self.update()
        #     elif event.button() == Qt.RightButton:
        #         painter_p.
        # if len(self.position_point) >= 1:
        #     print(len(self.position_point))
        #     painter_p.drawPoint(self.self.position_point[-1])
        #     print(len(self.position_point))
        # elif len(self.position_point) > 1:
        #     painter_p.drawPoint(self.self.position_point[-2])
        #     painter_p.drawPoint(self.self.position_point[-1])
        # painter_p.drawPoint(self.begin_point)
        # 将前一个点赋值给起点，保证连续画线
        # self.begin_point = self.end_point
        # 结束绘画
        # painter_p.end()

        # # 实现双缓冲
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pixmap())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Ditu_xunluoluxian()
    demo.show()
    sys.exit(app.exec_())