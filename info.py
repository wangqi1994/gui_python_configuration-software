# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info(object):
    def setupUi(self, info):
        info.setObjectName("info")
        info.resize(900, 900)
        self.centralwidget = QtWidgets.QWidget(info)
        self.centralwidget.setObjectName("centralwidget")
        self.y = QtWidgets.QLabel(self.centralwidget)
        self.y.setGeometry(QtCore.QRect(68, 508, 16, 16))
        self.y.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.y.setObjectName("y")
        self.x = QtWidgets.QLabel(self.centralwidget)
        self.x.setGeometry(QtCore.QRect(68, 436, 16, 16))
        self.x.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.x.setObjectName("x")
        self.cameraip = QtWidgets.QLabel(self.centralwidget)
        self.cameraip.setGeometry(QtCore.QRect(500, 380, 114, 16))
        self.cameraip.setObjectName("cameraip")
        self.camera_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.camera_ip.setGeometry(QtCore.QRect(709, 380, 133, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.camera_ip.sizePolicy().hasHeightForWidth())
        self.camera_ip.setSizePolicy(sizePolicy)
        self.camera_ip.setMinimumSize(QtCore.QSize(0, 0))
        self.camera_ip.setReadOnly(True)
        self.camera_ip.setObjectName("camera_ip")
        self.r_mac = QtWidgets.QLabel(self.centralwidget)
        self.r_mac.setGeometry(QtCore.QRect(68, 239, 72, 16))
        self.r_mac.setObjectName("r_mac")
        self.mincharg = QtWidgets.QLabel(self.centralwidget)
        self.mincharg.setGeometry(QtCore.QRect(68, 311, 102, 16))
        self.mincharg.setObjectName("mincharg")
        self.duojizhuban = QtWidgets.QLabel(self.centralwidget)
        self.duojizhuban.setGeometry(QtCore.QRect(499, 165, 121, 16))
        self.duojizhuban.setObjectName("duojizhuban")
        self.h_mac = QtWidgets.QLabel(self.centralwidget)
        self.h_mac.setGeometry(QtCore.QRect(68, 167, 84, 16))
        self.h_mac.setObjectName("h_mac")
        self.duojizhuban_port = QtWidgets.QLineEdit(self.centralwidget)
        self.duojizhuban_port.setGeometry(QtCore.QRect(708, 165, 133, 20))
        self.duojizhuban_port.setReadOnly(True)
        self.duojizhuban_port.setObjectName("duojizhuban_port")
        self.autocharge_x = QtWidgets.QLineEdit(self.centralwidget)
        self.autocharge_x.setGeometry(QtCore.QRect(277, 436, 133, 20))
        self.autocharge_x.setObjectName("autocharge_x")
        self.autocharge_xyz = QtWidgets.QLabel(self.centralwidget)
        self.autocharge_xyz.setGeometry(QtCore.QRect(68, 372, 132, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(50)
        sizePolicy.setHeightForWidth(self.autocharge_xyz.sizePolicy().hasHeightForWidth())
        self.autocharge_xyz.setSizePolicy(sizePolicy)
        self.autocharge_xyz.setMinimumSize(QtCore.QSize(20, 0))
        self.autocharge_xyz.setObjectName("autocharge_xyz")
        self.fenbushi_port = QtWidgets.QLineEdit(self.centralwidget)
        self.fenbushi_port.setGeometry(QtCore.QRect(710, 90, 133, 20))
        self.fenbushi_port.setReadOnly(True)
        self.fenbushi_port.setObjectName("fenbushi_port")
        self.host_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.host_mac.setGeometry(QtCore.QRect(277, 167, 133, 20))
        self.host_mac.setReadOnly(True)
        self.host_mac.setObjectName("host_mac")
        self.app_ip = QtWidgets.QLabel(self.centralwidget)
        self.app_ip.setGeometry(QtCore.QRect(500, 308, 150, 16))
        self.app_ip.setObjectName("app_ip")
        self.mincharge = QtWidgets.QLineEdit(self.centralwidget)
        self.mincharge.setGeometry(QtCore.QRect(277, 311, 133, 20))
        self.mincharge.setReadOnly(False)
        self.mincharge.setObjectName("mincharge")
        self.wddy = QtWidgets.QLabel(self.centralwidget)
        self.wddy.setGeometry(QtCore.QRect(499, 241, 78, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wddy.sizePolicy().hasHeightForWidth())
        self.wddy.setSizePolicy(sizePolicy)
        self.wddy.setObjectName("wddy")
        self.server_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.server_ip.setGeometry(QtCore.QRect(277, 95, 133, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.server_ip.sizePolicy().hasHeightForWidth())
        self.server_ip.setSizePolicy(sizePolicy)
        self.server_ip.setDragEnabled(True)
        self.server_ip.setReadOnly(True)
        self.server_ip.setObjectName("server_ip")
        self.autocharge_yaw = QtWidgets.QLineEdit(self.centralwidget)
        self.autocharge_yaw.setGeometry(QtCore.QRect(277, 580, 133, 20))
        self.autocharge_yaw.setObjectName("autocharge_yaw")
        self.s_ip = QtWidgets.QLabel(self.centralwidget)
        self.s_ip.setGeometry(QtCore.QRect(68, 95, 78, 16))
        self.s_ip.setObjectName("s_ip")
        self.yaw = QtWidgets.QLabel(self.centralwidget)
        self.yaw.setGeometry(QtCore.QRect(68, 580, 18, 16))
        self.yaw.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yaw.setObjectName("yaw")
        self.fenbushi = QtWidgets.QLabel(self.centralwidget)
        self.fenbushi.setGeometry(QtCore.QRect(501, 90, 54, 16))
        self.fenbushi.setObjectName("fenbushi")
        self.autocharge_y = QtWidgets.QLineEdit(self.centralwidget)
        self.autocharge_y.setGeometry(QtCore.QRect(277, 508, 133, 20))
        self.autocharge_y.setObjectName("autocharge_y")
        self.appserverip = QtWidgets.QLineEdit(self.centralwidget)
        self.appserverip.setGeometry(QtCore.QRect(709, 308, 133, 20))
        self.appserverip.setObjectName("appserverip")
        self.robot_mac = QtWidgets.QLineEdit(self.centralwidget)
        self.robot_mac.setGeometry(QtCore.QRect(277, 239, 133, 20))
        self.robot_mac.setReadOnly(True)
        self.robot_mac.setObjectName("robot_mac")
        self.wddy_port = QtWidgets.QLineEdit(self.centralwidget)
        self.wddy_port.setGeometry(QtCore.QRect(708, 237, 133, 20))
        self.wddy_port.setReadOnly(True)
        self.wddy_port.setObjectName("wddy_port")
        self.ok_info = QtWidgets.QPushButton(self.centralwidget)
        self.ok_info.setGeometry(QtCore.QRect(637, 767, 75, 23))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ok_info.sizePolicy().hasHeightForWidth())
        self.ok_info.setSizePolicy(sizePolicy)
        self.ok_info.setCheckable(False)
        self.ok_info.setChecked(False)
        self.ok_info.setAutoDefault(False)
        self.ok_info.setObjectName("ok_info")
        self.yiqueren = QtWidgets.QLabel(self.centralwidget)
        self.yiqueren.setEnabled(False)
        self.yiqueren.setGeometry(QtCore.QRect(650, 800, 45, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.yiqueren.setFont(font)
        self.yiqueren.setAlignment(QtCore.Qt.AlignCenter)
        self.yiqueren.setObjectName("yiqueren")
        info.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(info)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 23))
        self.menubar.setObjectName("menubar")
        self.menuFiles = QtWidgets.QMenu(self.menubar)
        self.menuFiles.setObjectName("menuFiles")
        self.menuNew = QtWidgets.QMenu(self.menuFiles)
        self.menuNew.setObjectName("menuNew")
        info.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(info)
        self.statusbar.setObjectName("statusbar")
        info.setStatusBar(self.statusbar)
        self.actionOpen = QtWidgets.QAction(info)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(info)
        self.actionSave.setObjectName("actionSave")
        self.actionRobot_info = QtWidgets.QAction(info)
        self.actionRobot_info.setObjectName("actionRobot_info")
        self.actionFenbushi = QtWidgets.QAction(info)
        self.actionFenbushi.setObjectName("actionFenbushi")
        self.actionPlanwork = QtWidgets.QAction(info)
        self.actionPlanwork.setObjectName("actionPlanwork")
        self.menuNew.addAction(self.actionRobot_info)
        self.menuNew.addAction(self.actionFenbushi)
        self.menuNew.addAction(self.actionPlanwork)
        self.menuFiles.addAction(self.menuNew.menuAction())
        self.menuFiles.addAction(self.actionOpen)
        self.menuFiles.addAction(self.actionSave)
        self.menubar.addAction(self.menuFiles.menuAction())

        self.retranslateUi(info)
        QtCore.QMetaObject.connectSlotsByName(info)

    def retranslateUi(self, info):
        _translate = QtCore.QCoreApplication.translate
        info.setWindowTitle(_translate("info", "创能机器人配置软件"))
        self.y.setText(_translate("info", "y"))
        self.x.setText(_translate("info", "x"))
        self.cameraip.setText(_translate("info", "监控摄像头的IP地址:"))
        self.camera_ip.setText(_translate("info", "192.168.1.120"))
        self.r_mac.setText(_translate("info", "小车MAC地址:"))
        self.mincharg.setText(_translate("info", "小车电量的最小值:"))
        self.duojizhuban.setText(_translate("info", "工控机之间通讯端口:"))
        self.h_mac.setText(_translate("info", "工控机MAC地址:"))
        self.duojizhuban_port.setText(_translate("info", "COM6"))
        self.autocharge_xyz.setText(_translate("info", "自动充电点坐标x,y,yaw:"))
        self.fenbushi_port.setText(_translate("info", "COM5"))
        self.app_ip.setText(_translate("info", "手机端后台服务器的IP地址:"))
        self.mincharge.setText(_translate("info", "5"))
        self.wddy.setText(_translate("info", "温度电压端口:"))
        self.server_ip.setText(_translate("info", "192.168.8.2"))
        self.s_ip.setText(_translate("info", "小车的IP地址:"))
        self.yaw.setText(_translate("info", "yaw"))
        self.fenbushi.setText(_translate("info", "Lora端口:"))
        self.wddy_port.setText(_translate("info", "COM4"))
        self.ok_info.setText(_translate("info", "确认"))
        self.yiqueren.setText(_translate("info", "已确认"))
        self.menuFiles.setTitle(_translate("info", "文件"))
        self.menuNew.setTitle(_translate("info", "新建"))
        self.actionOpen.setText(_translate("info", "打开"))
        self.actionSave.setText(_translate("info", "保存"))
        self.actionRobot_info.setText(_translate("info", "机器人基本信息"))
        self.actionFenbushi.setText(_translate("info", "分布式传感器"))
        self.actionPlanwork.setText(_translate("info", "计划任务"))
