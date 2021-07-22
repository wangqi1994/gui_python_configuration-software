# -*- coding: utf-8 -*-
# @Time    : 2021/5/10 18:29
# @Author  : Luc-wang
# @Email   :
# @File    : main.py
# @Software: PyCharm

import sys
import configparser
import os
import re
# import socket
import cv2
import uuid
# import pic_rc
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap, QImage, QPen, QPainter
from PyQt5.QtCore import QRect, Qt, QPoint

# import pyqtgraph as pg
# import pyqtgraph.examples


from gui import *
from planwork import *
from fenbushi import *
from info import *
from xunluoluxian import *
from ditu import *
# from setting import *
# from map import *

# 全局变量定义
global get_directory_path
global fenbushi_button
global xunluoluxian_buttons
global fenbushi_list
global xunluoluxian_list
global fenbushi_point
global fenbushi_flag
global xunluoluxian_flag
fenbushi_button = [0 for i in range(0, 15)]
fenbushi_list = [0 for i in range(0, 15)]
fenbushi_point = [0 for i in range(0, 15)]
xunluoluxian_buttons = [0 for i in range(0, 10)]
xunluoluxian_list = [0 for i in range(0, 10)]
fenbushi_flag = 0
xunluoluxian_flag = 0



# 创建mainWin类并传入Ui_MainWindow
class MainWin(QMainWindow, Ui_MainWindow):
    """主窗口类"""
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)

        # self.sb = QPushButton("编辑", self)
        # self.sb.setDown(False)  # 默认为未按的状态
        # self.sb.setGeometry(QtCore.QRect(630, 35 + 30 , 60, 30))
        # self.sb.setStyleSheet('QPushButton{margin:3px};')
        # self.sb.setVisible(True)


        # # 图片路径
        img_path = ("./image_sy.jpg")     # "image_sy.jpg"
        # # 加载图片,并自定义图片展示尺寸
        image = QtGui.QPixmap(img_path).scaled(407, 591)

        # # 显示图片
        self.pic_show_label.setPixmap(image)

    # 打开文件夹选择页面，选择生成文件保存路径
    def openFile(self):
        global get_directory_path
        # 获取选择的文件路径
        get_directory_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹", "C:/")


# 创建info主窗口并传入Ui_info
class info(QMainWindow, Ui_info):
    """机器人基本信息窗口类"""

    def __init__(self, parent=None):
        super(info, self).__init__(parent)
        self.setupUi(self)
        # 自动获取IP和物理地址
        # ip = socket.gethostbyname(socket.gethostname())
        mac_address = uuid.UUID(int=uuid.getnode()).hex[-12:].upper()
        mac_address = ':'.join([mac_address[i:i + 2] for i in range(0, 11, 2)])
        print(mac_address)
        # 设置host_mac
        self.host_mac.setText(mac_address)
        self.yiqueren.setVisible((False))
        # 获取小车mac地址
        self.result = self.arp_command('192.168.8.2')
        result_upper = self.result.upper()
        resuli_mid = result_upper.split('-')
        print(resuli_mid)
        self.mac_robot= ':'.join(resuli_mid)
        print(self.mac_robot)

        self.robot_mac.setText(self.mac_robot)

    def output_cmd(self, command):
        r = os.popen(command)
        content = r.read()
        r.close()
        return content

    def arp_command(self, ip_address):
        ping_cmd = "ping " + ip_address + " -n 2 "
        result = self.output_cmd(ping_cmd)
        find_ttl = result.find("TTL")
        if find_ttl != -1:
            arp_cmd = "arp -a %s" % ip_address
            arp_result = self.output_cmd(arp_cmd)
            ip2 = ip_address + " [ ]+([\w-]+)"
            ip2_mac = re.findall(ip2, arp_result)
            if len(ip2_mac):
                return ip2_mac[0]
            else:
                return 0
        else:
            result = u'机器人地盘未启动'
        return result

    # 保存机器人基本信息的Button响应函数
    def save_info(self):
        # 将输入的数据暂时存储到临时变量中
        server_ip = self.server_ip.text()  # 小车IP
        host_mac = self.host_mac.text()  # 工控机物理地址
        robot_mac = self.robot_mac.text()  # 小车物理地址
        mincharge = self.mincharge.text()  # 小车最低电量
        # maxcharge = self.maxcharge.text()  # 小车最大电量
        # right_eye_port = self.right_eye_port.text()  # 右侧传感器串口
        # left_eye_port = self.left_eye_port.text()  # 左侧传感器串口
        # deluge_gun_port = self.deluge_gun_port.text()  # 水平转动端口
        fenbushi_port = self.fenbushi_port.text()  # 分布式传感器串口
        # yuanhongwai_port = self.yuanhongwai_port.text()  # 远红外摄像头串口
        duojizhuban_port = self.duojizhuban_port.text()  # 舵机主板串口
        wddy_port = self.wddy_port.text()  # 温度电压串口
        appserverip = self.appserverip.text()  # 后台手机APP端IP
        camera_ip = self.camera_ip.text()  # 摄像机IP
        x = self.autocharge_x.text()  # 充电点坐标
        y = self.autocharge_y.text()
        yaw = self.autocharge_yaw.text()

        global get_directory_path

        # 打开文件，将数据信息写入文档中
        robot_info = open(get_directory_path + "/"+ "info" + ".conf", "w+")
        robot_info.write("[info] \n")
        robot_info.write("# 小车的IP地址:\n server_ip = " + server_ip + "\n")
        robot_info.write("# 工控机的网络物理地址:\n host_mac = " + host_mac + "\n")
        robot_info.write("# 小车的网络物理地址:\n  robot_mac = " + robot_mac + "\n")
        robot_info.write("# 小车电量的最小值:\n mincharge = " + mincharge + "\n")
        # robot_info.write("# 小车电量的最大值:\n maxcharge = " + maxcharge + "\n")
        # robot_info.write("# 右传感器的端口:\n right_eye_port = " + right_eye_port + "\n")
        # robot_info.write("# 左传感器的端口:\n left_eye_port = " + left_eye_port + "\n")
        # robot_info.write("# 水平转动的端口:\n deluge_gun_port = " + deluge_gun_port + "\n")
        robot_info.write("# 分布式传感器的端口:\n fenbushi_port = " + fenbushi_port + "\n")
        # robot_info.write("# 远红外摄像头的端口:\n yuanhongwai_port = " + yuanhongwai_port + "\n")
        robot_info.write("# 舵机主控板的端口:\n duojizhuban_port = " + duojizhuban_port + "\n")
        robot_info.write("# 温度电压的端口:\n wddy_port = " + wddy_port + "\n")
        robot_info.write("# 手机端后台服务器的IP地址:\n appserverip = " + appserverip + "\n")
        robot_info.write("# 监控摄像头的IP地址:\n camera_ip = " + camera_ip + "\n")
        robot_info.write(
            "# 自动充电点坐标x,y,yaw:\n autocharge_x = " + x + "\n autocharge_y = " + y + "\n autocharge_yaw = "+yaw+"\n")
        # 关闭info文件
        robot_info.close()

        self.yiqueren.setVisible(True)


# 创建fenbushi主窗口并传入Ui_fenbushi
class fenbushi(QMainWindow, Ui_fenbushi):
    """
    分布式传感器窗口类
    """
    def __init__(self, parent=None):
        super(fenbushi, self).__init__(parent)
        self.setupUi(self)
        self.hint_fenbushi.setVisible(False)
        self.kong_fenbushi.setVisible(False)
        # map_w = Ditu

        self.fenbushi_id = []
        self.fenbushi_points = []
        self.fenbushi_lists = []
        self.fenbushi_editButton = []

        for i in range(15):
            # 分布式传感器id输入框
            self.fenbushi_id.append(0)
            self.fenbushi_id[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.fenbushi_id[i].setGeometry(QtCore.QRect(30, 40 + 30 * i, 120, 20))
            self.fenbushi_id[i].setObjectName("fenbushi_id")
            self.fenbushi_id[i].setPlaceholderText("保留两位数字")
            self.fenbushi_id[i].setVisible(False)
            # 分布式传感器编辑按钮
            self.fenbushi_editButton.append(0)
            self.fenbushi_editButton[i] = QPushButton("编辑", self.scrollAreaWidgetContents)
            self.fenbushi_editButton[i].setDown(False)  # 默认为未按的状态
            self.fenbushi_editButton[i].setGeometry(QtCore.QRect(630, 35 + 30 * i, 60, 30))
            self.fenbushi_editButton[i].setStyleSheet('QPushButton{margin:3px};')
            self.fenbushi_editButton[i].setVisible(False)
            self.fenbushi_editButton[i].setObjectName("fenbushi" + str(i))

            # 分布式传感器本身位置输入框
            self.fenbushi_points.append(0)
            self.fenbushi_points[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.fenbushi_points[i].setGeometry(QtCore.QRect(170, 40 + 30 * i, 120, 21))
            self.fenbushi_points[i].setObjectName("fenbushi_points")
            self.fenbushi_points[i].setPlaceholderText("填写示例：x1,y1,yaw1")
            self.fenbushi_points[i].setVisible(False)
            fenbushi_point[i] = self.fenbushi_points[i]
            # 分布式传感器对应位置输入框
            self.fenbushi_lists.append(0)
            self.fenbushi_lists[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.fenbushi_lists[i].setGeometry(QtCore.QRect(300, 40 + 30 * i, 320, 21))
            self.fenbushi_lists[i].setObjectName("fenbushi_locations")
            self.fenbushi_lists[i].setPlaceholderText("填写示例：x1,y1,yaw1;x2,y2,yaw")
            self.fenbushi_lists[i].setVisible(False)
            fenbushi_list[i] = self.fenbushi_lists[i]

            self.yiqueren.setVisible(False)


    def add(self):
        # 获取分布式传感器的数量
        fbs_num = self.fensbushi_num.text()
        print(fbs_num, len(fbs_num))
        # global fenbushi_list

        if len(fbs_num) == 0 or int(fbs_num) == 0:
            self.kong_fenbushi.setVisible(True)
            self.hint_fenbushi.setVisible(False)
        else:
            self.kong_fenbushi.setVisible(False)
            self.kong_fenbushi.setVisible(False)
            if int(fbs_num) <= 15:
                # 存储分布式传感器本身位置和对应位置
                # 生成对应数量的输入框
                for i in range(int(fbs_num)):
                    # 分布式传感器id输入框
                    # self.fenbushi_id.append(0)
                    # self.fenbushi_id[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                    # self.fenbushi_id[i].setGeometry(QtCore.QRect(30, 40 + 30 * i, 120, 20))
                    # self.fenbushi_id[i].setObjectName("fenbushi_id")
                    # self.fenbushi_id[i].setPlaceholderText("保留两位数字")
                    self.fenbushi_id[i].setVisible(True)

                    # 分布式传感器编辑按钮
                    self.fenbushi_points[i].setVisible(True)

                    # 分布式传感器对应位置输入框
                    # self.fenbushi_lists.append(0)
                    # self.fenbushi_lists[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
                    # self.fenbushi_lists[i].setGeometry(QtCore.QRect(170, 40 + 30 * i, 450, 21))
                    # self.fenbushi_lists[i].setObjectName("fenbushi_locations")
                    # # self.fenbushi_lists[i].setText(fenbushi_list[i])
                    # self.fenbushi_lists[i].setPlaceholderText("填写示例：x1,y1,yaw1;x2,y2,yaw")
                    self.fenbushi_lists[i].setVisible(True)

                    # 显示编辑按钮
                    self.fenbushi_editButton[i].setVisible(True)

                return self.fenbushi_lists, self.fenbushi_id, self.fenbushi_editButton
            else:
                self.kong_fenbushi.setVisible(False)
                self.hint_fenbushi.setVisible(True)




    # 保存机器人分布式传感器信息的Button响应函数
    def save_fenbushi(self):

        # 获取分布式传感器的数量
        fbs_num = self.fensbushi_num.text()
        # 获取保存位置
        global get_directory_path
        # 打开文件，将数据信息写入文档中
        robot_fenbushi = open(get_directory_path + "/" + "fenbushi" + ".conf", "w+")
        for i in range(int(fbs_num)):
            fenbushi_id = int(self.fenbushi_id[i].text())
            robot_fenbushi.write('[%02d] \n' % fenbushi_id)
            # robot_fenbushi.write("fenbushi_position = " + self.fenbushi_lists[i].text() + "\n")
            robot_fenbushi.write("fenbushi_positions = " + self.fenbushi_lists[i].text()+"\n\n")
        # # 关闭fenbushi文件
        robot_fenbushi.close()

        self.yiqueren.setVisible(True)




# 创建planwork主窗口并传入Ui_planwork
class planwork(QMainWindow, Ui_planwork):
    """
    计划任务窗口类
    """
    def __init__(self, parent=None):
        super(planwork, self).__init__(parent)
        self.setupUi(self)
        self.yiqueren.setVisible(False)


    def add_plan(self):
        # 获取巡逻路线存储位置
        global get_directory_path
        xunluo = configparser.ConfigParser()
        xunluo.read(get_directory_path +"/" + "xunluoluxian" + ".conf")
        sections = xunluo.sections()
        # 存储巡逻路线名称及对应巡逻点
        self.namelist = []
        self.poilist = []
        for i in sections:
            name = xunluo[i]["xunluoluxian_name"]
            self.namelist.append(name)
            poi = xunluo[i]["xunluoluxian_poi"]
            self.poilist.append(poi)
        # 获取现有表格中行数
        rownum = self.plan_showtable.rowCount()
        # 新增空白行数据
        self.plan_showtable.setRowCount(rownum+1)

        # 新增任务名称设置默认值
        misson_name_init = "mission"+str(rownum+1)
        m_name_init= QTableWidgetItem(misson_name_init)
        self.plan_showtable.setItem(rownum, 0, m_name_init)

        # # 在新增的一行中添加编辑按钮
        # self.editButton = QPushButton("编辑")
        # self.editButton.setDown(False)  # 默认为未按的状态
        # self.editButton.setStyleSheet('QPushButton{margin:3px};')
        # self.plan_showtable.setCellWidget(rownum, 0, self.editButton)

        # 添加模式选择下拉控件
        self.patterncombox = QComboBox()
        self.patterncombox.addItems(['时间段', '时间频率'])
        # QSS(类似CSS样式表)
        # 设置所有的QComboBox控件，使得它们的边距为3像素
        self.patterncombox.setStyleSheet('QComboBox{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 1, self.patterncombox)

        # 添加开始时间选择timeedit
        self.starttimeButton = QTimeEdit()
        self.starttimeButton.setStyleSheet('QTimeEdit{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 2, self.starttimeButton)

        # 添加结束时间选择timeedit
        self.endtimeButton = QTimeEdit()
        self.endtimeButton.setStyleSheet('QTimeEdit{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 3, self.endtimeButton)

        # 添加时间间隔选择timeedit
        self.intervalButton = QTimeEdit()
        self.intervalButton.setStyleSheet('QTimeEdit{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 4, self.intervalButton)

        # 添加巡逻路线选择下拉控件
        self.xunluocombox = QComboBox()
        self.xunluocombox.addItems(self.namelist)
        # QSS(类似CSS样式表)
        # 设置所有的QComboBox控件，使得它们的边距为3像素
        self.xunluocombox.setStyleSheet('QComboBox{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 5, self.xunluocombox)


    # 保存机器人计划任务的Button响应函数
    def save_planwork(self):
        # 获取保存文件位置
        global get_directory_path
        # 创建对应存储列表
        self.plan_edit = []
        self.plan_name = []
        self.plan_pattern = []
        self.plan_starttime = []
        self.plan_endtime = []
        self.plan_interval = []
        self.plan_xunluo = []
        # 打开文件，将数据信息写入文档中
        robot_planwork = open(get_directory_path + "/" + "planworkfile" + ".conf", "w+")
        # 提取表格中数据并存储到文件对应位置
        for i in range(self.plan_showtable.rowCount()):
            # 操作
            self.plan_edit.append(i)
            print(self.plan_edit)

            # 表格中单元格一定要判断非空，否则会出现报错

            # 任务名称
            if (self.plan_showtable.item(i, 0) != None):
                p_name = self.plan_showtable.item(i, 0).text()
                print(p_name)
                self.plan_name.append(p_name)
                print(self.plan_name)

            # 任务模式
            if (self.plan_showtable.cellWidget(i, 1) != None):
                p_pattern = self.plan_showtable.cellWidget(i, 1).currentText()

                if str(p_pattern) == '时间段':
                    self.plan_pattern.append(str(1))
                elif str(p_pattern) == '时间频率':
                    self.plan_pattern.append(str(0))
                print(p_pattern)
                print(self.plan_pattern)

            # 开始时间
            if (self.plan_showtable.cellWidget(i, 2) != None):
                p_stime = self.plan_showtable.cellWidget(i, 2).text()
                self.plan_starttime.append(p_stime)
                print(self.plan_starttime)

            # 结束时间
            if (self.plan_showtable.cellWidget(i, 3) != None):
                p_etime = self.plan_showtable.cellWidget(i, 3).text()
                self.plan_endtime.append(p_etime)
                print(self.plan_endtime)
            # 时间间隔
            if (self.plan_showtable.cellWidget(i, 4) != None):
                p_interval = self.plan_showtable.cellWidget(i, 4).text()
                self.plan_interval.append(p_interval)
                print(self.plan_interval)

            # 巡逻路线
            if (self.plan_showtable.cellWidget(i, 5) != None):
                p_xunluo = self.plan_showtable.cellWidget(i, 5).currentText()
                print(len(self.namelist), p_xunluo)
                if len(self.namelist) != 0:
                    for j in range(len(self.namelist)):
                        if p_xunluo == self.namelist[j]:
                            self.plan_xunluo.append(self.poilist[j])
                    print(self.plan_xunluo)
                else:
                    pass


            # 将数据信息写入文档中
            robot_planwork.write("["+self.plan_name[i]+"] \n")
            robot_planwork.write("# 巡逻模式:\n plan_work_flag = " + self.plan_pattern[i] + "\n")
            robot_planwork.write("# 开始时间:\n starttime = " + self.plan_starttime[i] + "\n")
            robot_planwork.write("# 结束时间:\n endtime = " + self.plan_endtime[i] + "\n")
            robot_planwork.write("# 时间间隔:\n interval = " + self.plan_interval[i] + "\n")
            if len(self.namelist):
                robot_planwork.write("# 巡逻点:\n poilist = " + self.plan_xunluo[i] + "\n\n")
            else:
                robot_planwork.write("# 巡逻点:\n poilist = 无 \n\n")
        # 关闭planworkfile文件
        robot_planwork.close()

        self.yiqueren.setVisible(True)


# 创建巡逻路线窗口并传入Ui_xunluoluxian
class xunluoluxian(QWidget, Ui_xunluoluxian):
    """
    添加巡逻路线窗口类
    """

    def __init__(self, parent=None):
        super(xunluoluxian, self).__init__(parent)
        self.setupUi(self)

        # 创建对应路线名称和点的列表
        self.xunluoluxian_name = []
        self.xunluoluxian_point = []
        self.xunluoluxian_button = []

        # 添加路线名称的QLinEdit控件
        self.xunluoluxian_n = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.xunluoluxian_n.setGeometry(QtCore.QRect(20, 40, 80, 20))
        self.xunluoluxian_n.setObjectName("xunluoluxian_name")
        num = len(self.xunluoluxian_name)
        self.xunluoluxian_n.setText("巡逻路线"+str(num))
        self.xunluoluxian_n.setVisible(True)
        self.xunluoluxian_name.append(self.xunluoluxian_n)
        self.name_num = len(self.xunluoluxian_name)
        # 添加路线点的QLinEdit控件
        self.xunluoluxian_p = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.xunluoluxian_p.setGeometry(QtCore.QRect(120, 40, 240, 20))
        self.xunluoluxian_p.setObjectName("xunluoluxian_point")
        self.xunluoluxian_p.setPlaceholderText("示例：x1,y1,yaw1;x2,y2,yaw2")
        self.xunluoluxian_p.setVisible(True)
        self.xunluoluxian_point.append(self.xunluoluxian_p)
        xunluoluxian_list[0] = self.xunluoluxian_point[0]
        # 编辑按钮
        self.xunluoluxian_b = QPushButton("编辑", self.scrollAreaWidgetContents)
        self.xunluoluxian_b.setDown(False)  # 默认为未按的状态
        self.xunluoluxian_b.setGeometry(QtCore.QRect(370, 35, 60, 30))
        self.xunluoluxian_b.setStyleSheet('QPushButton{margin:3px};')
        self.xunluoluxian_b.setVisible(True)
        self.xunluoluxian_button.append(self.xunluoluxian_b)
        xunluoluxian_buttons[0] = self.xunluoluxian_button[0]

        for i in range(9):
            self.xunluoluxian_b = QPushButton("编辑", self.scrollAreaWidgetContents)
            self.xunluoluxian_b.setDown(False)  # 默认为未按的状态
            self.xunluoluxian_b.setGeometry(
                QtCore.QRect(370, self.xunluoluxian_button[len(self.xunluoluxian_button) - 1].y() + 30, 60, 30))
            self.xunluoluxian_b.setStyleSheet('QPushButton{margin:3px};')
            self.xunluoluxian_b.setVisible(False)
            self.xunluoluxian_button.append(self.xunluoluxian_b)
            xunluoluxian_buttons[i+1] = self.xunluoluxian_button[i+1]

        self.yiqueren.setVisible(False)


    def add_xunluoluxian(self):
        if self.name_num <=10:
            # 点击按钮添加路线名称的QLinEdit控件
            self.xunluoluxian_n = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.xunluoluxian_n.setGeometry(QtCore.QRect(20, self.xunluoluxian_name[len(self.xunluoluxian_name)-1].y()+30, 80, 20))
            self.xunluoluxian_n.setObjectName("xunluoluxian_name")
            num = len(self.xunluoluxian_name)
            self.xunluoluxian_n.setText("巡逻路线"+str(num))
            self.xunluoluxian_n.setVisible(True)
            self.xunluoluxian_name.append(self.xunluoluxian_n)
            # 点击按钮添加路线点的QLinEdit控件
            self.xunluoluxian_p = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.xunluoluxian_p.setGeometry(QtCore.QRect(120, self.xunluoluxian_point[len(self.xunluoluxian_point)-1].y()+30, 240, 20))
            self.xunluoluxian_p.setObjectName("xunluoluxian_point")
            self.xunluoluxian_p.setPlaceholderText("示例：x1,y1,yaw1;x2,y2,yaw2")
            self.xunluoluxian_p.setVisible(True)
            self.xunluoluxian_point.append(self.xunluoluxian_p)
            xunluoluxian_list[num] = self.xunluoluxian_point[num]
            print(xunluoluxian_list)
            self.name_num = len(self.xunluoluxian_name)

            # 点击按钮添加编辑按钮
            for i in range(10):
                if self.xunluoluxian_button[i].isVisible() and not self.xunluoluxian_button[i+1].isVisible():
                    self.xunluoluxian_button[i+1].setVisible(True)
                    break
                else:
                    continue


            print(self.xunluoluxian_name, len(self.xunluoluxian_name), self.name_num)
            print(self.xunluoluxian_button)
        else:
            pass

    # 保存机器人巡逻路线的Button响应函数
    def save_xunluoluxian(self):
        # 获取巡逻路线数量
        xllx_num = len(self.xunluoluxian_name)
        # 获取文件存储位置
        global get_directory_path
        # 打开文件，将数据信息写入文档中
        robot_xunluoluxian = open(get_directory_path + "/" + "xunluoluxian" + ".conf", "w+")
        for i in range(int(xllx_num)):
            robot_xunluoluxian.write('[%02d] \n' % i)
            robot_xunluoluxian.write("xunluoluxian_name = " + self.xunluoluxian_name[i].text() + "\n")
            robot_xunluoluxian.write("xunluoluxian_poi = " + self.xunluoluxian_point[i].text()+"\n\n")
            print(self.xunluoluxian_name[i].text(), self.xunluoluxian_point[i].text())
        # # 关闭巡逻路线文件
        robot_xunluoluxian.close()

        self.yiqueren.setVisible(True)


# 创建分布式地图类并传入Ui_map
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
            print(fenbushi_list, len(fenbushi_list))
            print(fenbushi_flag)
            if fenbushi_flag == 1:
                fenbushi_point[0].setText(self.map_position.fenbushi_poi)
                fenbushi_list[0].setText(self.map_position.position)
            elif fenbushi_flag == 2:
                fenbushi_point[1].setText(self.map_position.fenbushi_poi)
                fenbushi_list[1].setText(self.map_position.position)
            elif fenbushi_flag == 3:
                fenbushi_point[2].setText(self.map_position.fenbushi_poi)
                fenbushi_list[2].setText(self.map_position.position)
            elif fenbushi_flag == 4:
                fenbushi_point[3].setText(self.map_position.fenbushi_poi)
                fenbushi_list[3].setText(self.map_position.position)
            elif fenbushi_flag == 5:
                fenbushi_point[4].setText(self.map_position.fenbushi_poi)
                fenbushi_list[4].setText(self.map_position.position)
            elif fenbushi_flag == 6:
                fenbushi_point[5].setText(self.map_position.fenbushi_poi)
                fenbushi_list[5].setText(self.map_position.position)
            elif fenbushi_flag == 7:
                fenbushi_point[6].setText(self.map_position.fenbushi_poi)
                fenbushi_list[6].setText(self.map_position.position)
            elif fenbushi_flag == 8:
                fenbushi_point[7].setText(self.map_position.fenbushi_poi)
                fenbushi_list[7].setText(self.map_position.position)
            elif fenbushi_flag == 9:
                fenbushi_point[8].setText(self.map_position.fenbushi_poi)
                fenbushi_list[8].setText(self.map_position.position)
            elif fenbushi_flag == 10:
                fenbushi_point[9].setText(self.map_position.fenbushi_poi)
                fenbushi_list[9].setText(self.map_position.position)
            elif fenbushi_flag == 11:
                fenbushi_point[10].setText(self.map_position.fenbushi_poi)
                fenbushi_list[10].setText(self.map_position.position)
            elif fenbushi_flag == 12:
                fenbushi_point[11].setText(self.map_position.fenbushi_poi)
                fenbushi_list[11].setText(self.map_position.position)
            elif fenbushi_flag == 13:
                fenbushi_point[12].setText(self.map_position.fenbushi_poi)
                fenbushi_list[12].setText(self.map_position.position)
            elif fenbushi_flag == 14:
                fenbushi_point[13].setText(self.map_position.fenbushi_poi)
                fenbushi_list[13].setText(self.map_position.position)
            elif fenbushi_flag == 15:
                fenbushi_point[14].setText(self.map_position.fenbushi_poi)
                fenbushi_list[14].setText(self.map_position.position)

            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)



            # sys.exit().accept()

        else:
            e.ignore()

# 重写新的Qlabel类-对应分布式地图展示
class Mylabel_fenbushi(QLabel):
    def __init__(self, parent=None):
        super(Mylabel_fenbushi, self).__init__(parent)
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

# 创建巡逻路线地图类并传入Ui_map
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
            print(fenbushi_list, len(fenbushi_list))
            print(fenbushi_flag)
            if xunluoluxian_flag == 1:
                xunluoluxian_list[0].setText(self.map_position.position)
            elif xunluoluxian_flag == 2:
                xunluoluxian_list[1].setText(self.map_position.position)
            elif xunluoluxian_flag == 3:
                xunluoluxian_list[2].setText(self.map_position.position)
            elif xunluoluxian_flag == 4:
                xunluoluxian_list[3].setText(self.map_position.position)
            elif xunluoluxian_flag == 5:
                xunluoluxian_list[4].setText(self.map_position.position)
            elif xunluoluxian_flag == 6:
                xunluoluxian_list[5].setText(self.map_position.position)
            elif xunluoluxian_flag == 7:
                xunluoluxian_list[6].setText(self.map_position.position)
            elif xunluoluxian_flag == 8:
                xunluoluxian_list[7].setText(self.map_position.position)
            elif xunluoluxian_flag == 9:
                xunluoluxian_list[8].setText(self.map_position.position)
            elif xunluoluxian_flag == 10:
                xunluoluxian_list[9].setText(self.map_position.position)


            e.accept()
            QtWidgets.QWidget.closeEvent(self, e)

            # sys.exit().accept()

        else:
            e.ignore()

# 重写新的Qlabel类-对应巡逻路线地图展示
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

            self.y0 = float(read_info[i]["autocharge_y"])

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
        elif event.button() == Qt.RightButton:
            self.flag_right = True

    #鼠标移动
    def mouseMoveEvent(self, event):
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
            self.update()

    # 鼠标滚轮事件
    #滚轮滑动事件

    # def wheelEvent(self, event):



    def paintEvent(self, event):
        super().paintEvent(event)
        # # 实现双缓冲
        painter2 = QPainter(self)
        painter2.drawPixmap(0, 0, self.pixmap())




# 界面切换函数
def menu_triggered(mwindow, info_m, planwork_m, fenbushi_m):
    # 主窗口菜单页面切换
    # 切换到info界面
    mwindow.actionRobot_info.triggered.connect(mwindow.openFile)
    mwindow.actionRobot_info.triggered.connect(info_m.show)
    mwindow.actionRobot_info.triggered.connect(mwindow.close)
    # 切换到分布式界面
    mwindow.actionFenbushi.triggered.connect(mwindow.openFile)
    mwindow.actionFenbushi.triggered.connect(fenbushi_m.show)
    mwindow.actionFenbushi.triggered.connect(mwindow.close)
    # 切换到planwork界面
    mwindow.actionPlanwork.triggered.connect(mwindow.openFile)
    mwindow.actionPlanwork.triggered.connect(planwork_m.show)
    mwindow.actionPlanwork.triggered.connect(mwindow.close)

    # info页面菜单页面切换
    # 切换到分布式界面
    info_m.actionFenbushi.triggered.connect(fenbushi_m.show)
    info_m.actionFenbushi.triggered.connect(info_m.close)
    # 切换到planwork界面
    info_m.actionPlanwork.triggered.connect(planwork_m.show)
    info_m.actionPlanwork.triggered.connect(info_m.close)

    # 分布式页面菜单页面切换
    # 切换到info界面
    fenbushi_m.actionRobot_info.triggered.connect(info_m.show)
    fenbushi_m.actionRobot_info.triggered.connect(fenbushi_m.close)
    # 切换到planwork界面
    fenbushi_m.actionPlanwork.triggered.connect(planwork_m.show)
    fenbushi_m.actionPlanwork.triggered.connect(fenbushi_m.close)

    # planwork页面菜单页面切换
    # 切换到分布式界面
    planwork_m.actionFenbushi.triggered.connect(fenbushi_m.show)
    planwork_m.actionFenbushi.triggered.connect(planwork_m.close)
    # 切换到info界面
    planwork_m.actionRobot_info.triggered.connect(info_m.show)
    planwork_m.actionRobot_info.triggered.connect(planwork_m.close)



def change_fenbushi_flag(n):
    global fenbushi_flag
    fenbushi_flag = n
    print(fenbushi_flag)
    # return fenbushi_flag


def change_xunluoluxian_flag(n):
    global xunluoluxian_flag
    xunluoluxian_flag = n

    # return fenbushi_flag


def main():
    # pyqtgraph 示例
    # pyqtgraph.examples.run()
    app = QApplication(sys.argv)
    mwindow = MainWin()
    info_m = info()
    planwork_m = planwork()
    fenbushi_m = fenbushi()
    xunluoluxian_w = xunluoluxian()

    # map_m = Ditu()
    # 展示主窗口

    mwindow.show()

    #调用页面切换函数
    menu_triggered(mwindow, info_m, planwork_m, fenbushi_m)

    # info页面按钮调用保存信息函数
    info_m.ok_info.clicked.connect(info_m.save_info)

    # fenbushi页面确定分布式传感器数量
    fenbushi_m.ok_fenbushinum.clicked.connect(fenbushi_m.add)

    # fenbushi页面保存分布式传感器位置
    fenbushi_m.ok_fenbushi.clicked.connect(fenbushi_m.save_fenbushi)

    # planwork页面打开巡逻路线添加页面
    planwork_m.xunluoluxian_button.clicked.connect(xunluoluxian_w.show)

    # 巡逻路线界面添加路线
    xunluoluxian_w.add_xllx.clicked.connect(xunluoluxian_w.add_xunluoluxian)

    # 巡逻路线界面结束编辑
    xunluoluxian_w.ok_addxllx.clicked.connect(xunluoluxian_w.save_xunluoluxian)
    xunluoluxian_w.ok_addxllx.clicked.connect(xunluoluxian_w.close)
    xunluoluxian_w.re_addxllx.clicked.connect(xunluoluxian_w.close)

    # planwork页面添加一条任务计划
    planwork_m.add_planwork.clicked.connect(planwork_m.add_plan)
    # 保存计划任务
    planwork_m.ok_planwork.clicked.connect(planwork_m.save_planwork)

    # 分布式页面弹出地图编辑函数


    # fenbushi_ditu(fenbushi_m)

    # 巡逻路线弹出地图编辑函数

    # xunluoluxian_ditu(xunluoluxian_w)

    # 暂时无法通过调用函数处理-之前可以
    # 分布式

    map_f_1 = Ditu_fenbushi()
    map_f_2 = Ditu_fenbushi()
    map_f_3 = Ditu_fenbushi()
    map_f_4 = Ditu_fenbushi()
    map_f_5 = Ditu_fenbushi()
    map_f_6 = Ditu_fenbushi()
    map_f_7 = Ditu_fenbushi()
    map_f_8 = Ditu_fenbushi()
    map_f_9 = Ditu_fenbushi()
    map_f_10 = Ditu_fenbushi()
    map_f_11 = Ditu_fenbushi()
    map_f_12 = Ditu_fenbushi()
    map_f_13 = Ditu_fenbushi()
    map_f_14 = Ditu_fenbushi()
    map_f_15 = Ditu_fenbushi()

    fenbushi_m.fenbushi_editButton[0].clicked.connect(lambda: change_fenbushi_flag(1))
    fenbushi_m.fenbushi_editButton[0].clicked.connect(map_f_1.show)

    fenbushi_m.fenbushi_editButton[1].clicked.connect(map_f_2.show)
    fenbushi_m.fenbushi_editButton[1].clicked.connect(lambda : change_fenbushi_flag(2))

    fenbushi_m.fenbushi_editButton[2].clicked.connect(map_f_3.show)
    fenbushi_m.fenbushi_editButton[2].clicked.connect(lambda : change_fenbushi_flag(3))

    fenbushi_m.fenbushi_editButton[3].clicked.connect(map_f_4.show)
    fenbushi_m.fenbushi_editButton[3].clicked.connect(lambda : change_fenbushi_flag(4))

    fenbushi_m.fenbushi_editButton[4].clicked.connect(map_f_5.show)
    fenbushi_m.fenbushi_editButton[4].clicked.connect(lambda : change_fenbushi_flag(5))

    fenbushi_m.fenbushi_editButton[5].clicked.connect(map_f_6.show)
    fenbushi_m.fenbushi_editButton[5].clicked.connect(lambda : change_fenbushi_flag(6))

    fenbushi_m.fenbushi_editButton[6].clicked.connect(map_f_7.show)
    fenbushi_m.fenbushi_editButton[6].clicked.connect(lambda : change_fenbushi_flag(7))

    fenbushi_m.fenbushi_editButton[7].clicked.connect(map_f_8.show)
    fenbushi_m.fenbushi_editButton[7].clicked.connect(lambda : change_fenbushi_flag(8))

    fenbushi_m.fenbushi_editButton[8].clicked.connect(map_f_9.show)
    fenbushi_m.fenbushi_editButton[8].clicked.connect(lambda : change_fenbushi_flag(9))

    fenbushi_m.fenbushi_editButton[9].clicked.connect(map_f_10.show)
    fenbushi_m.fenbushi_editButton[9].clicked.connect(lambda : change_fenbushi_flag(10))

    fenbushi_m.fenbushi_editButton[10].clicked.connect(map_f_11.show)
    fenbushi_m.fenbushi_editButton[10].clicked.connect(lambda : change_fenbushi_flag(11))

    fenbushi_m.fenbushi_editButton[11].clicked.connect(map_f_12.show)
    fenbushi_m.fenbushi_editButton[11].clicked.connect(lambda : change_fenbushi_flag(12))

    fenbushi_m.fenbushi_editButton[12].clicked.connect(map_f_13.show)
    fenbushi_m.fenbushi_editButton[12].clicked.connect(lambda : change_fenbushi_flag(13))

    fenbushi_m.fenbushi_editButton[13].clicked.connect(map_f_14.show)
    fenbushi_m.fenbushi_editButton[13].clicked.connect(lambda : change_fenbushi_flag(14))

    fenbushi_m.fenbushi_editButton[14].clicked.connect(map_f_15.show)
    fenbushi_m.fenbushi_editButton[14].clicked.connect(lambda : change_fenbushi_flag(15))

    # 巡逻路线
    map_x_1 = Ditu_xunluoluxian()
    map_x_2 = Ditu_xunluoluxian()
    map_x_3 = Ditu_xunluoluxian()
    map_x_4 = Ditu_xunluoluxian()
    map_x_5 = Ditu_xunluoluxian()
    map_x_6 = Ditu_xunluoluxian()
    map_x_7 = Ditu_xunluoluxian()
    map_x_8 = Ditu_xunluoluxian()
    map_x_9 = Ditu_xunluoluxian()
    map_x_10 = Ditu_xunluoluxian()

    xunluoluxian_w.xunluoluxian_button[0].clicked.connect(map_x_1.show)
    xunluoluxian_w.xunluoluxian_button[0].clicked.connect(lambda: change_xunluoluxian_flag(1))

    xunluoluxian_w.xunluoluxian_button[1].clicked.connect(map_x_2.show)
    xunluoluxian_w.xunluoluxian_button[1].clicked.connect(lambda: change_xunluoluxian_flag(2))

    xunluoluxian_w.xunluoluxian_button[2].clicked.connect(map_x_3.show)
    xunluoluxian_w.xunluoluxian_button[2].clicked.connect(lambda: change_xunluoluxian_flag(3))

    xunluoluxian_w.xunluoluxian_button[3].clicked.connect(map_x_4.show)
    xunluoluxian_w.xunluoluxian_button[3].clicked.connect(lambda: change_xunluoluxian_flag(4))

    xunluoluxian_w.xunluoluxian_button[4].clicked.connect(map_x_5.show)
    xunluoluxian_w.xunluoluxian_button[4].clicked.connect(lambda: change_xunluoluxian_flag(5))

    xunluoluxian_w.xunluoluxian_button[5].clicked.connect(map_x_6.show)
    xunluoluxian_w.xunluoluxian_button[5].clicked.connect(lambda: change_xunluoluxian_flag(6))

    xunluoluxian_w.xunluoluxian_button[6].clicked.connect(map_x_7.show)
    xunluoluxian_w.xunluoluxian_button[6].clicked.connect(lambda: change_xunluoluxian_flag(7))

    xunluoluxian_w.xunluoluxian_button[7].clicked.connect(map_x_8.show)
    xunluoluxian_w.xunluoluxian_button[7].clicked.connect(lambda: change_xunluoluxian_flag(8))

    xunluoluxian_w.xunluoluxian_button[8].clicked.connect(map_x_9.show)
    xunluoluxian_w.xunluoluxian_button[8].clicked.connect(lambda: change_xunluoluxian_flag(9))

    xunluoluxian_w.xunluoluxian_button[9].clicked.connect(map_x_10.show)
    xunluoluxian_w.xunluoluxian_button[9].clicked.connect(lambda: change_xunluoluxian_flag(10))

    sys.exit(app.exec_())

if __name__ =='__main__':
    main()


