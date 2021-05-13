# encoding Utf-8
import sys
import configparser
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import *

from gui import *
from planwork import *
from fenbushi import *
from info import *
from xunluoluxian import *


# 全局变量定义
global get_directory_path


# 创建mainWin类并传入Ui_MainWindow
class MainWin(QMainWindow, Ui_MainWindow):
    """主窗口类"""
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)
    # 打开文件夹选择页面，选择生成文件保存路径
    def openFile(self):
        global get_directory_path
        get_directory_path = QFileDialog.getExistingDirectory(self, "选取指定文件夹", "C:/")


# 创建info主窗口并传入Ui_info
class info(QMainWindow, Ui_info):
    """机器人基本信息窗口类"""

    def __init__(self, parent=None):
        super(info, self).__init__(parent)
        self.setupUi(self)


    # 保存机器人基本信息的Button响应函数
    def save_info(self):

        # 将输入的数据暂时存储到临时变量中
        server_ip = self.server_ip.text()
        host_mac = self.host_mac.text()
        robot_mac = self.robot_mac.text()
        mincharge = self.mincharge.text()
        maxcharge = self.maxcharge.text()
        right_eye_port = self.right_eye_port.text()
        left_eye_port = self.left_eye_port.text()
        deluge_gun_port = self.deluge_gun_port.text()
        fenbushi_port = self.fenbushi_port.text()
        yuanhongwai_port = self.yuanhongwai_port.text()
        duojizhuban_port = self.duojizhuban_port.text()
        wddy_port = self.wddy_port.text()
        appserverip = self.appserverip.text()
        camera_ip = self.camera_ip.text()
        x = self.autocharge_x.text()
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
        robot_info.write("# 小车电量的最大值:\n maxcharge = " + maxcharge + "\n")
        robot_info.write("# 右传感器的端口:\n right_eye_port = " + right_eye_port + "\n")
        robot_info.write("# 左传感器的端口:\n left_eye_port = " + left_eye_port + "\n")
        robot_info.write("# 水平转动的端口:\n deluge_gun_port = " + deluge_gun_port + "\n")
        robot_info.write("# 分布式传感器的端口:\n fenbushi_port = " + fenbushi_port + "\n")
        robot_info.write("# 远红外摄像头的端口:\n yuanhongwai_port = " + yuanhongwai_port + "\n")
        robot_info.write("# 舵机主控板的端口:\n duojizhuban_port = " + duojizhuban_port + "\n")
        robot_info.write("# 温度电压的端口:\n wddy_port = " + wddy_port + "\n")
        robot_info.write("# 手机端后台服务器的IP地址:\n appserverip = " + appserverip + "\n")
        robot_info.write("# 监控摄像头的IP地址:\n camera_ip = " + camera_ip + "\n")
        robot_info.write(
            "# 自动充电点坐标x,y,yaw:\n autocharge_x = " + x + "\n autocharge_y = " + y + "\n autocharge_yaw = "+yaw+"\n")
        # 关闭info文件
        robot_info.close()


# 创建fenbushi主窗口并传入Ui_fenbushi
class fenbushi(QMainWindow, Ui_fenbushi):
    """
    分布式传感器窗口类
    """
    def __init__(self, parent=None):
        super(fenbushi, self).__init__(parent)
        self.setupUi(self)


    def add(self):
        fbs_num = self.fensbushi_num.text()
        print(fbs_num)
        self.fenbushi_list = []
        self.fenbushi_lists = []

        for i in range(int(fbs_num)):
            self.fenbushi_list.append(0)
            self.fenbushi_list[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.fenbushi_list[i].setGeometry(QtCore.QRect(30, 40+30*i, 101, 20))
            self.fenbushi_list[i].setObjectName("fenbushi_location")
            self.fenbushi_list[i].setVisible(True)
            self.fenbushi_lists.append(0)
            self.fenbushi_lists[i] = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
            self.fenbushi_lists[i].setGeometry(QtCore.QRect(140, 40+30*i, 161, 21))
            self.fenbushi_lists[i].setObjectName("fenbushi_locations")
            self.fenbushi_lists[i].setVisible(True)

        return self.fenbushi_lists, self.fenbushi_list


    # 保存机器人分布式传感器信息的Button响应函数
    def save_fenbushi(self):
        fbs_num = self.fensbushi_num.text()
        global get_directory_path
        # 打开文件，将数据信息写入文档中
        robot_fenbushi = open(get_directory_path + "/" + "fenbushi" + ".conf", "w+")
        for i in range(int(fbs_num)):
            robot_fenbushi.write('[%02d] \n' % i)
            robot_fenbushi.write("fenbushi_position = " + self.fenbushi_lists[i].text() + "\n")
            robot_fenbushi.write("fenbushi_positions = " + self.fenbushi_lists[i].text()+"\n\n")
            print(self.fenbushi_list[i].text(),self.fenbushi_lists[i].text())
        # # 关闭fenbushi文件
        robot_fenbushi.close()


# 创建planwork主窗口并传入Ui_planwork
class planwork(QMainWindow, Ui_planwork):
    """
    计划任务窗口类
    """

    def __init__(self, parent=None):
        super(planwork, self).__init__(parent)
        self.setupUi(self)





    def add_plan(self):
        global get_directory_path
        xunluo = configparser.ConfigParser()
        xunluo.read(get_directory_path +"/" + "xunluoluxian" + ".conf")
        sections = xunluo.sections()
        self.namelist = []
        self.poilist = []
        for i in sections:
            name = xunluo[i]["xunluoluxian_name"]
            self.namelist.append(name)
            poi = xunluo[i]["xunluoluxian_poi"]
            self.poilist.append(poi)


        rownum = self.plan_showtable.rowCount()
        print(rownum)

        self.plan_showtable.setRowCount(rownum+1)
        # 在新增的一行中添加编辑按钮
        self.editButton = QPushButton("编辑")
        self.editButton.setDown(True)  # 默认为按下的状态
        self.editButton.setStyleSheet('QPushButton{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 0, self.editButton)

        # 添加模式选择下拉控件
        self.patterncombox = QComboBox()
        self.patterncombox.addItems(['时间段', '时间频率'])
        # QSS(类似CSS样式表)
        # 设置所有的QComboBox控件，使得它们的边距为3像素
        self.patterncombox.setStyleSheet('QComboBox{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 2, self.patterncombox)

        # 添加开始时间选择timeedit
        self.starttimeButton = QTimeEdit()
        self.starttimeButton.setStyleSheet('QTimeEdit{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 3, self.starttimeButton)

        # 添加结束时间/时间间隔选择timeedit
        self.endtimeButton = QTimeEdit()
        self.endtimeButton.setStyleSheet('QTimeEdit{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 4, self.endtimeButton)

        # 添加巡逻路线选择下拉控件
        self.xunluocombox = QComboBox()
        self.xunluocombox.addItems(self.namelist)
        # QSS(类似CSS样式表)
        # 设置所有的QComboBox控件，使得它们的边距为3像素
        self.xunluocombox.setStyleSheet('QComboBox{margin:3px};')
        self.plan_showtable.setCellWidget(rownum, 5, self.xunluocombox)


    # 保存机器人计划任务的Button响应函数
    def save_planwork(self):
        global get_directory_path
        # 创建对应存储列表
        self.plan_edit = []
        self.plan_name = []
        self.plan_pattern = []
        self.plan_starttime = []
        self.plan_endtime = []
        self.plan_xunluo = []
        # 打开文件，将数据信息写入文档中
        robot_planwork = open(get_directory_path + "/" + "planworkfile" + ".conf", "w+")
        # robot_planwork.truncate()
        for i in range(self.plan_showtable.rowCount()):
            # 操作
            self.plan_edit.append(i)
            print(self.plan_edit)

            # 一定要判断非空，否则会出现报错
            # 任务名称
            if (self.plan_showtable.item(i, 1) != None):
                p_name = self.plan_showtable.item(i, 1).text()
                print(p_name)
                self.plan_name.append(p_name)
                print(self.plan_name)

            # 任务模式
            if (self.plan_showtable.cellWidget(i, 2) != None):
                p_pattern = self.plan_showtable.cellWidget(i, 2).currentText()

                if str(p_pattern) == '时间段':
                    self.plan_pattern.append(str(0))
                elif str(p_pattern) == '时间频率':
                    self.plan_pattern.append(str(1))
                print(p_pattern)
                # self.plan_pattern.append(p_pattern)
                print(self.plan_pattern)

            # 开始时间
            if (self.plan_showtable.cellWidget(i, 3) != None):
                p_stime = self.plan_showtable.cellWidget(i, 3).text()
                # print(p_name)
                self.plan_starttime.append(p_stime)
                print(self.plan_starttime)

            # 结束时间、时间间隔
            if (self.plan_showtable.cellWidget(i, 4) != None):
                p_etime = self.plan_showtable.cellWidget(i, 4).text()
                # print(p_name)
                self.plan_endtime.append(p_etime)
                print(self.plan_endtime)

            # 巡逻路线
            if (self.plan_showtable.cellWidget(i, 5) != None):
                p_xunluo = self.plan_showtable.cellWidget(i, 5).currentText()
                # print(p_name)
                print(len(self.namelist), p_xunluo)

                for j in range(len(self.namelist)):
                    if p_xunluo == self.namelist[j]:
                        self.plan_xunluo.append(self.poilist[j])
                # self.plan_xunluo.append(p_xunluo)
                print(self.plan_xunluo)

            # 将数据信息写入文档中
            robot_planwork.write("["+self.plan_name[i]+"] \n")
            robot_planwork.write("# 巡逻模式:\n pattern = " + self.plan_pattern[i] + "\n")
            robot_planwork.write("# 开始时间:\n starttime = " + self.plan_starttime[i] + "\n")
            robot_planwork.write("# 结束时间:\n endtime = " + self.plan_endtime[i] + "\n")
            robot_planwork.write("# 巡逻点:\n poilist = " + self.plan_xunluo[i] + "\n\n")
        # 关闭planworkfile文件
        robot_planwork.close()


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
        # 添加路线名称的QLinEdit控件
        self.xunluoluxian_n = QtWidgets.QLineEdit(self.scrollArea)
        self.xunluoluxian_n.setGeometry(QtCore.QRect(20, 40, 80, 20))
        self.xunluoluxian_n.setObjectName("xunluoluxian_name")
        self.xunluoluxian_n.setVisible(True)
        self.xunluoluxian_name.append(self.xunluoluxian_n)
        # 添加路线点的QLinEdit控件
        self.xunluoluxian_p = QtWidgets.QLineEdit(self.scrollArea)
        self.xunluoluxian_p.setGeometry(QtCore.QRect(120, 40, 320, 20))
        self.xunluoluxian_p.setObjectName("xunluoluxian_point")
        self.xunluoluxian_p.setVisible(True)
        self.xunluoluxian_point.append(self.xunluoluxian_p)


    def add_xunluoluxian(self):
        # 点击按钮添加路线名称的QLinEdit控件
        self.xunluoluxian_n = QtWidgets.QLineEdit(self.scrollArea)
        self.xunluoluxian_n.setGeometry(QtCore.QRect(20, self.xunluoluxian_name[len(self.xunluoluxian_name)-1].y()+30, 80, 20))
        self.xunluoluxian_n.setObjectName("xunluoluxian_name")
        self.xunluoluxian_n.setVisible(True)
        self.xunluoluxian_name.append(self.xunluoluxian_n)
        # 点击按钮添加路线点的QLinEdit控件
        self.xunluoluxian_p = QtWidgets.QLineEdit(self.scrollArea)
        self.xunluoluxian_p.setGeometry(QtCore.QRect(120, self.xunluoluxian_point[len(self.xunluoluxian_point)-1].y()+30, 320, 20))
        self.xunluoluxian_p.setObjectName("xunluoluxian_point")
        self.xunluoluxian_p.setVisible(True)
        self.xunluoluxian_point.append(self.xunluoluxian_p)
        self.name_num = len(self.xunluoluxian_name)
        print(self.xunluoluxian_name,len(self.xunluoluxian_name), self.name_num)

    # 保存机器人巡逻路线的Button响应函数
    def save_xunluoluxian(self):
        xllx_num = len(self.xunluoluxian_name)
        global get_directory_path
        # 打开文件，将数据信息写入文档中
        robot_xunluoluxian = open(get_directory_path + "/" + "xunluoluxian" + ".conf", "w+")
        for i in range(int(xllx_num)):
            robot_xunluoluxian.write('[%02d] \n' % i)
            robot_xunluoluxian.write("xunluoluxian_name = " + self.xunluoluxian_name[i].text() + "\n")
            robot_xunluoluxian.write("xunluoluxian_poi = " + self.xunluoluxian_point[i].text()+"\n\n")
            print(self.xunluoluxian_name[i].text(), self.xunluoluxian_point[i].text())
        # # 关闭fenbushi文件
        robot_xunluoluxian.close()


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


def main():
    app = QApplication(sys.argv)
    mwindow = MainWin()
    info_m = info()
    planwork_m = planwork()
    fenbushi_m = fenbushi()
    xunluoluxian_w = xunluoluxian()
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

    sys.exit(app.exec_())

if __name__ =='__main__':
    main()


