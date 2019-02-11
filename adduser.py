#-*-coding:utf-8-*-
# coding=utf-8
import sys
import os
import time
import win32gui
import win32api
import win32con
import pyautogui
os.system("net user")
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

#输出MMCMainFrame的窗口名称
MMCMainFrame = win32gui.FindWindow("MMCMainFrame", None)
# print("#######################")
titlename = (win32gui.GetWindowText(MMCMainFrame))
# print(titlename)
# print("#######################")

hWndChildList = []
a = win32gui.EnumChildWindows(MMCMainFrame, lambda hWnd, param: param.append(MMCMainFrame),  hWndChildList)
# print(a)

#获取窗口左上角和右下角坐标
a, b, c, d = win32gui.GetWindowRect(MMCMainFrame)
# print(a, b, c, d)


#计算窗口的长和宽 方便后面计算比例
# h = c - a 
# print(h)
# w = d - b
# print(w)

# 计算得出MMCMainFrame窗口的顶边距离“用户”这个标签120个坐标点 该值除非调动 否则不变
# userPosH = 237 -117
# print(userPosL)
# userPosL = 120
#计算得出MMCMainFrame窗口的坐标边距离“用户”这个标签120个坐标点 该值除非调动 否则不变
# userPosH = 1145 - 915
# print(userPosH)
# userPosH = 230

userPOS = (a + 230, b + 120 )
# print(userPOS)

#左键双击用户标签
win32api.SetCursorPos((a + 230, b + 120))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,a + 230, b + 120,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,a + 230, b + 120,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,a + 230, b + 120,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,a + 230, b + 120,0,0)

#右键单击Administrator标签下50左右 弹出新建用户窗口
win32api.SetCursorPos((a + 230, b + 170))
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,a + 230, b + 170,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,a + 230, b + 170,0,0)

#左键单击新用户标签
win32api.SetCursorPos((a + 240, b + 180))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,a + 240, b + 180,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,a + 240, b + 180,0,0)


def inputCoolCat():
  win32api.keybd_event(0x43,0,0,0)
  win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4F,0,0,0)
  win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4F,0,0,0)
  win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4C,0,0,0)
  win32api.keybd_event(0x4C,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x43,0,0,0)
  win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x41,0,0,0)
  win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x54,0,0,0)
  win32api.keybd_event(0x54,0,win32con.KEYEVENTF_KEYUP,0)
  time.sleep(0.01)
  #coolcat
  win32api.keybd_event(9,0,0,0)
def inputPassword():
  win32api.keybd_event(0x43,0,0,0)
  win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4F,0,0,0)
  win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4F,0,0,0)
  win32api.keybd_event(0x4F,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x4C,0,0,0)
  win32api.keybd_event(0x4C,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x43,0,0,0)
  win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x41,0,0,0)
  win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x54,0,0,0)
  win32api.keybd_event(0x54,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x60,0,0,0)
  win32api.keybd_event(0x60,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x61,0,0,0)
  win32api.keybd_event(0x61,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0x62,0,0,0)
  win32api.keybd_event(0x62,0,win32con.KEYEVENTF_KEYUP,0)
  win32api.keybd_event(0xBE,0,0,0)
  win32api.keybd_event(0xBE,0,win32con.KEYEVENTF_KEYUP,0)
  #coolcat123.
  time.sleep(0.01)
  win32api.keybd_event(9,0,0,0)

#输入用户名
inputCoolCat()
#输入全名
inputCoolCat()
#输入描述
inputCoolCat()
#输入密码
inputPassword()
#确认密码
inputPassword()

#发送回车键
win32api.keybd_event(0x0D,0,0,0)
win32api.keybd_event(0x0D,0,win32con.KEYEVENTF_KEYUP,0)

#发送ESC键
win32api.keybd_event(0x1B,0,0,0) 
win32api.keybd_event(0x1B,0,win32con.KEYEVENTF_KEYUP,0)


#发送Alt + F键
win32api.keybd_event(0x12,0,0,0) 
win32api.keybd_event(0x46,0,0,0) 
win32api.keybd_event(0x12,0,win32con.KEYEVENTF_KEYUP,0)
win32api.keybd_event(0x46,0,win32con.KEYEVENTF_KEYUP,0) 


#发送X键
win32api.keybd_event(0x58,0,0,0) 
win32api.keybd_event(0x58,0,win32con.KEYEVENTF_KEYUP,0) 


os.system("net user")
