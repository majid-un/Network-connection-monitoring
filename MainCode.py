import socket
import ssl
import time
import datetime
import os
import sys
from pkg_resources import DistributionNotFound, VersionConflict
import tkinter
from tkinter import filedialog
#     pyuic5 -x form55.ui -o form55.py           Network connection monitoring ##  command in folder  auto-py-to-exe
import speedtest
import datetime
import numpy as np
import time
import matplotlib.pyplot as plt
ss = speedtest.Speedtest() 
import pandas as pd
import pyodbc 
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQueryModel,QSqlQuery
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
qtCreatorFile = 'form.ui' #Esse é o arquivo .ui gerado pelo QtDesigner
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

 
class MyWindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.conn)
        self.pushButton_2.clicked.connect(self.tet)
        self.pushButton_3.clicked.connect(self.plot)
        self.pushButton_4.clicked.connect(self.pat)
        self.pushButton_5.clicked.connect(self.cance)

    def pat(self):
        main_win = tkinter.Tk() 
        main_win.withdraw()

        main_win.overrideredirect(True)
        main_win.geometry('0x0+0+0')

        main_win.deiconify()
        main_win.lift()
        main_win.focus_force()

        #open file selector 
        main_win.sourceFolder = filedialog.askdirectory(parent=main_win, initialdir= "\\",title='Please select a directory')

        #close window after selection 
        main_win.destroy()
        #self.output_rd.clear()
        #print path 
        global pat
        
        pat=main_win.sourceFolder
        #print(main_win.sourceFile )
        #self.output_rd.append(str(path)) 
        #print(path)
        
################################3
    def cance(self):
        s.close()
        
    def conn(self):
        self.textEdit.clear()
        save= pat 
        print(pat)
        name= self.lineEdit_4.text()
        ip= self.lineEdit.text() 
        prt= int(self.lineEdit_2.text()) 
        fg= '%s/%s' %(save,name) 
        print(fg)
        LOG_FNAME =  name 
        FILE = fg
        print(FILE)
        def send_ping_request(host=('%s' %ip) , port=prt, timeout=3):
            try:
                global s
                socket.setdefaulttimeout(timeout)
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((host,port))
            except OSError as error:
                return False
            else:
                s.close()
                return True
        def write_permission_check():
            try:
                with open(FILE, "a") as file:
                    pass
            except OSError as error:
                print("Log file creation failed")
                sys.exit()
            finally:
                pass
        def calculate_time(start, stop):
            time_difference = stop - start
            seconds = float(str(time_difference.total_seconds()))
            return str(datetime.timedelta(seconds=seconds)).split(".")[0]
        ping_freq=2
        monitor_start_time = datetime.datetime.now()
        motd = "Network connection monitoring started at: " + str(monitor_start_time).split(".")[0] + " Sending ping request in " + str(ping_freq) + " seconds"
        print(motd)
        self.textEdit.append(motd) 
        with open(FILE, "a") as file:
            file.write("\n")
            file.write(motd + "\n")
        wait = int(self.lineEdit_5.text()) 
        while wait > 0:
            if send_ping_request():
                time.sleep(ping_freq)
            else:
                down_time = datetime.datetime.now()
                fail_msg = "Network Connection Unavailable at: " + str(down_time).split(".")[0]
                print(fail_msg)
                self.textEdit.append(fail_msg)
                with open(FILE, "a") as file:
                    file.write(fail_msg + "\n")
                    i = 0
                while not send_ping_request():
                    time.sleep(1)
                    i += 1
                    if i >= 3600:
                        i = 0
                        now = datetime.datetime.now()
                        continous_message = "Network Unavailabilty Persistent at: " + str(now).split(".")[0]
                        print(continous_message)
                        self.textEdit.append(continous_message)
                        with open(FILE, "a") as file:
                            file.write(continous_message + "\n")
                up_time = datetime.datetime.now()
                uptime_message = "Network Connectivity Restored at: " + str(up_time).split(".")[0]
        
                down_time = calculate_time(down_time, up_time)
                _m = "Network Connection was Unavailable for " + down_time
        
                print(uptime_message)
                self.textEdit.append(uptime_message) 
                print(_m)
                self.textEdit.append(_m) 
        
                with open(FILE, "a") as file:
                    file.write(uptime_message + "\n")
                    file.write(_m + "\n")
 
            wait = wait - 1   
  
         
    def plot(self):
 
        ss = speedtest.Speedtest()
        point = int(self.lineEdit_3.text()) 
        for i in range(point):
            ping = ss.results.ping
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            downspeed = round((round(ss.download()) / 1048576), 2)
            upspeed = round((round(ss.upload()) / 1048576), 2)
            print(f"ping: {ping},time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
            # 60 seconds sleep
            print(type(ping))
            print(type(time_now))
            print(type(downspeed))
            print(type(upspeed))
            
            plt.scatter(time_now, upspeed)


            plt.pause(0.005)
        plt.show() 
         

    def tet(self):
 
        self.textEdit_2.clear()
        point = int(self.lineEdit_3.text()) 
        for i in range(point):
            ping = ss.results.ping
            time_now = datetime.datetime.now().strftime("%H:%M:%S")
            downspeed = round((round(ss.download()) / 1048576), 2)
            upspeed = round((round(ss.upload()) / 1048576), 2)
            print(f"ping: {ping},time: {time_now}, downspeed: {downspeed} Mb/s, upspeed: {upspeed} Mb/s")
            # 60 seconds sleep
            print(type(ping))
            print(type(time_now))
            print(type(downspeed))
            print(type(upspeed))
            pin="ping :" + str(ping)
            tim="time :" + str(time_now)
            down="downspeed  Mb/s :" + str(downspeed)
            up="upspeed Mb/s :" + str(upspeed)
            self.textEdit_2.append(pin) 
            self.textEdit_2.append(tim)
            self.textEdit_2.append(down)  
            self.textEdit_2.append(up)  
  
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(571, 369)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(500, 310, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 10, 531, 191))
        font = QtGui.QFont()
        font.setBold(True)
        self.groupBox_6.setFont(font)
        self.groupBox_6.setObjectName("groupBox_6")
        self.label = QtWidgets.QLabel(self.groupBox_6)
        self.label.setGeometry(QtCore.QRect(10, 50, 71, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_11 = QtWidgets.QLabel(self.groupBox_6)
        self.label_11.setGeometry(QtCore.QRect(70, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit.setGeometry(QtCore.QRect(10, 70, 121, 22))
        font = QtGui.QFont()
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.groupBox_6)
        self.label_2.setGeometry(QtCore.QRect(140, 50, 49, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 41, 22))
        font = QtGui.QFont()
        font.setBold(False)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_5.setGeometry(QtCore.QRect(80, 110, 51, 22))
        font = QtGui.QFont()
        font.setBold(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setGeometry(QtCore.QRect(190, 130, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setBold(False)
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 150, 101, 24))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 61, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(190, 150, 71, 22))
        font = QtGui.QFont()
        font.setBold(False)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_9 = QtWidgets.QLabel(self.groupBox_6)
        self.label_9.setGeometry(QtCore.QRect(130, 150, 61, 20))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.pushButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton.setGeometry(QtCore.QRect(300, 150, 81, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_6)
        self.pushButton_5.setGeometry(QtCore.QRect(420, 150, 81, 24))
        self.pushButton_5.setObjectName("pushButton_5")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_6)
        self.textEdit.setGeometry(QtCore.QRect(200, 20, 321, 101))
        font = QtGui.QFont()
        font.setBold(False)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(20, 310, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        font.setItalic(True)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 210, 531, 101))
        font = QtGui.QFont()
        font.setBold(True)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 60, 75, 24))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 30, 111, 16))
        font = QtGui.QFont()
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(110, 60, 75, 24))
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 30, 41, 22))
        font = QtGui.QFont()
        font.setBold(False)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(200, 20, 321, 61))
        font = QtGui.QFont()
        font.setBold(False)
        self.textEdit_2.setFont(font)
        self.textEdit_2.setObjectName("textEdit_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Network Connection Monitoring"))
        self.label_8.setText(_translate("MainWindow", "version 1.0"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Connection Monitoring"))
        self.label.setText(_translate("MainWindow", "IP Address"))
        self.label_11.setText(_translate("MainWindow", "expl :0.0.0.0"))
        self.label_2.setText(_translate("MainWindow", "Port"))
        self.label_10.setText(_translate("MainWindow", "expl : xx.log"))
        self.pushButton_4.setText(_translate("MainWindow", "Folder Browser"))
        self.label_4.setText(_translate("MainWindow", "Failed Stop"))
        self.label_9.setText(_translate("MainWindow", "File Name"))
        self.pushButton.setText(_translate("MainWindow", "Start"))
        self.pushButton_5.setText(_translate("MainWindow", "End"))
        self.label_23.setText(_translate("MainWindow", "Trial Test Version"))
        self.groupBox.setTitle(_translate("MainWindow", "Speed Test"))
        self.pushButton_2.setText(_translate("MainWindow", "Text View"))
        self.label_3.setText(_translate("MainWindow", "Monitoring Times"))
        self.pushButton_3.setText(_translate("MainWindow", "Graph View"))

 
if __name__ == "__main__":
 
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())    
    
      
            