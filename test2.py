# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
#
# class Foo(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(Foo, self).__init__(parent)
#         self.setGeometry(QtCore.QRect(200, 100, 700, 600))
#         self.paint = Paint()
#         self.sizeHint()
#         self.lay = QtWidgets.QVBoxLayout()
#         self.lay.addWidget(self.paint)
#         self.setLayout(self.lay)
#
# class Paint(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         super(Paint, self).__init__(parent)
#         self.setBackgroundRole(QtGui.QPalette.Base)
#         self.setAutoFillBackground(True)
#         self.r = QtCore.QRect(QtCore.QPoint(), QtCore.QSize(200, 300))
#         self._factor = 1.0
#
#     def paintEvent(self, event):
#         self.r.moveCenter(self.rect().center())
#         pen = QtGui.QPen()
#         brush = QtGui.QBrush( QtCore.Qt.darkCyan, QtCore.Qt.Dense5Pattern)
#         painter = QtGui.QPainter(self)
#         painter.setBrush(brush)
#         painter.setPen(pen)
#         painter.setRenderHint(QtGui.QPainter.Antialiasing)
#
#         painter.translate(self.rect().center())
#         painter.scale(self._factor, self._factor)
#         painter.translate(-self.rect().center())
#
#         painter.drawRect(self.r)
#
#     def wheelEvent(self, event):
#         self._factor *= 1.01**(event.angleDelta().y()/15.0)
#         self.update()
#         super(Paint, self).wheelEvent(event)
#
#
# if __name__ == '__main__':
#     app = QtWidgets.QApplication(sys.argv)
#     w = Foo()
#     w.show()
#     sys.exit(app.exec_())

# import nmap
# nm = nmap.PortScanner()
# nm.scan('172.18.3.236') # ip地址和端口，端口不填也可以
# a = nm['addresses']    #返回主机的详细信息
# print(a)

#
# import arprequest
# arprequest.arprequest('1172.18.3.236')

# from scapy.all import *
#
# #
# ip = '172.18.3.236'
# arp_pkt = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=ip)
# res = srp1(arp_pkt, timeout=1, verbose=0)
# print ({"localIP": res.psrc, "mac": res.hwsrc})

import os
import re
def output_cmd(command):
    r = os.popen(command)
    content = r.read()
    r.close()
    return content


def arp_command(ip_address):
    ping_cmd = "ping " + ip_address + " -n 2 "
    result = output_cmd(ping_cmd)
    find_ttl = result.find("TTL")
    if find_ttl != -1:
        arp_cmd = "arp -a %s" % ip_address
        arp_result = output_cmd(arp_cmd)
        mac_regx = re.compile(r'^([0-9A-F]{1,2})' + '\:([0-9A-F]{1,2})' * 5 + '$', re.IGNORECASE)
        ip2 = ip_address + " [ ]+([\w-]+)"
        ip2_mac = re.findall(ip2, arp_result)
        ip3_mac = re.findall(mac_regx)
        if len(ip3_mac):
            return ip3_mac[0]
        else:
            return 0
    else:
        result = u'无人使用的ip'
    return result

if __name__ == '__main__':
    # ip = '172.18.3.236'
    result = arp_command('172.18.2.139')
    print(result)