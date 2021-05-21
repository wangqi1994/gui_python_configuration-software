# gui_python_configuration-software
用于生成机器人配置文件的人机交互页面

## PYQt开发记录
主程序创建类之前，需要将对应窗口模块导入
```
import sys
from PyQt5.QtWidgets import *

from gui import *
from planwork import *
from fenbushi import *
from info import *
from xunluoluxian import *
```
### 1.创建类并传入对应的窗口类
```
# 创建mainWin类并传入Ui_MainWindow
class MainWin(QMainWindow, Ui_MainWindow):
    """主窗口类"""
    def __init__(self, parent=None):
        super(MainWin, self).__init__(parent)
        self.setupUi(self)
        
# 创建info主窗口并传入Ui_info
class info(QMainWindow, Ui_info):
    """机器人基本信息窗口类"""

    def __init__(self, parent=None):
        super(info, self).__init__(parent)
        self.setupUi(self)
```
### 2.创建主函数调用窗口显示
```
def main():
    app = QApplication(sys.argv)
    # 实例化窗口才能在当前函数调用窗口内所含的组件参数
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
    
    # 退出展示页面
    sys.exit(app.exec_())

if __name__ =='__main__':
    main()
    ```
