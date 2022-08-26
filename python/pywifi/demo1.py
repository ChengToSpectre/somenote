import pywifi
from pywifi import const

def gic():
    
    wifi = pywifi.PyWiFi()#创建一个无线对象

    ifaces = wifi.interfaces()[0]#获得第一个无线网卡

    wifiname = ifaces.name()#获得网卡的名字

    wifistatus = ifaces.status()#获得WiFi状态

    if wifistatus == const.IFACE_DISCONNECTED:#0没有可读性
        print("not link to wifi")
    else :
        print("have linked to wifi")
    
    bies(ifaces,wifistatus)

def bies(ifaces,wifistatus):

    if wifistatus == const.IFACE_DISCONNECTED:
        
        ifaces.scan()#通过网卡扫描wifi

        print(ifaces.scan_results)#查看扫描结果


gic()
