# from pyecharts import Bar

# bar = Bar("我的第一个图表", "这里是副标题")
# bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
# bar.show_config()
# bar.render()

from wxpython import wx


class App(wx.App):
    def OnInit(self):
        frame = wx.Frame(None, title="Hello wxpython's world!")  # Create a frame.
        frame.Show()  # Show it.
        return True


if __name__ == '__main__':
    app = App()  # create an application object.
    app.MainLoop()  # Then start the event loop.