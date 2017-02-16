PyWinRing0
===========

Python Wrap For WinRing0

Requirements:
-------------
1,Python3+ (Python2 untested)  
2,WinRing0

Attentions:
-----------
You must put the WinRing0.sys and the WinRing0.dll in the same directory of the windows executable file which interprets the .py scripts.(for example the directory of C:\Program Files\Python33\python.exe)       
Examples:

```python
    from winring0 import *
    re=InitializeOls()
    if not re:
        print("InitializeOls Failed")
    if GetDllStatus()!=0:
        print("GetDllStatus Failed")
    WriteIoPortByte(0x64,0xAE)
    ReadIoPortByte(0x64)
    DeinitializeOls()
```

***
这是WinRing0的python封装

要使用它你必须有:
-----------------
1,Python3+ (Python2 未测试)  
2,WinRing0

注意:
-----
必须把WinRing0的WinRing0.sys和WinRing0.dll文件放在解释python脚本的可执行文件的目录下(例如C:\Program Files\Python33\python.exe所在的目录)
代码示例:
---------

```python
    from winring0 import *
    re=InitializeOls()
    if not re:
        print("InitializeOls Failed")
    if GetDllStatus()!=0:
        print("GetDllStatus Failed")
    WriteIoPortByte(0x64,0xAE)
    ReadIoPortByte(0x64)
    DeinitializeOls()
```
