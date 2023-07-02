import pythoncom
import pyHook

def on_mouse_event(event):
    if event.MessageName == "mouse left down":
        print(f"鼠标按下事件：({event.Position})")
    return True

# 创建一个鼠标钩子管理器
hm = pyHook.HookManager()

# 监听鼠标事件并关联处理函数
hm.MouseLeftDown = on_mouse_event

# 设置钩子
hm.HookMouse()

# 开始消息循环
pythoncom.PumpMessages()