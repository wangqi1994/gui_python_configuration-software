# -*- coding: UTF-8 -*-

def info_write():
    robot_info = open("./config/" + "info" + ".conf", "w+")
    robot_info.write("[info] \n")
    server_ip = input("请输入小车的IP地址")
    robot_info.write("# 小车的IP地址\n server_ip = " + server_ip + "\n")
    host_mac = input("请输入工控机的网络物理地址")
    robot_info.write("# 工控机的网络物理地址\n host_mac = " + host_mac + "\n")
    robot_mac = input("请输入小车的网络物理地址")
    robot_info.write("# 小车的网络物理地址\n  robot_mac = " + robot_mac + "\n")
    mincharge = input("请输入小车电量的最小值")
    robot_info.write("# 小车电量的最小值\n mincharge = " + mincharge + "\n")
    maxcharge = input("请输入小车电量的最大值")
    robot_info.write("# 小车电量的最大值\n maxcharge = " + maxcharge + "\n")
    right_eye_port = input("请输入右传感器的端口")
    robot_info.write("# 右传感器的端口\n right_eye_port = " + right_eye_port + "\n")
    left_eye_port = input("请输入左传感器的端口")
    robot_info.write("# 左传感器的端口\n left_eye_port = " + left_eye_port + "\n")
    deluge_gun_port = input("请输入水平转动的端口")
    robot_info.write("# 水平转动的端口\n deluge_gun_port = " + deluge_gun_port + "\n")
    fenbushi_port = input("请输入分布式传感器的端口")
    robot_info.write("# 分布式传感器的端口\n fenbushi_port = " + fenbushi_port + "\n")
    yuanhongwai_port = input("请输入远红外摄像头的端口")
    robot_info.write("# 远红外摄像头的端口\n yuanhongwai_port = " + yuanhongwai_port + "\n")
    duojizhuban_port = input("请输入舵机主控板的端口")
    robot_info.write("# 舵机主控板的端口\n duojizhuban_port = " + duojizhuban_port + "\n")
    wddy_port = input("请输入温度电压的端口")
    robot_info.write("# 温度电压的端口\n wddy_port = " + wddy_port + "\n")
    appserverip = input("请输入手机端后台服务器的IP地址")
    robot_info.write("# 手机端后台服务器的IP地址\n appserverip = " + appserverip + "\n")
    camera_ip = input("请输入监控摄像头的IP地址")
    robot_info.write("# 监控摄像头的IP地址\n camera_ip = " + camera_ip + "\n")
    x = input("请输入自动充电点坐标x")
    y = input("请输入自动充电点坐标y")
    yaw = input("请输入自动充电点坐标yaw")
    robot_info.write("# 自动充电点坐标x,y,yaw\n autocharge_x = " + x + "\n autocharge_y = " + y + "\n autocharge_yaw = yaw\n")

    robot_info.close()


def planwork_write():
    pass



def fenbushi_write():
    pass



def main():

    info_write()
    planwork_write()
    fenbushi_write()











    # 自动充电点坐标x,y,yaw
    autocharge_x = 7.094
    autocharge_y = -8.328
    autocharge_yaw = 0.00





if __name__ == '__main__':
    main()