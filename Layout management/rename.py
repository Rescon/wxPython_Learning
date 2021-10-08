import wx


class Example(wx.Frame):

    def __init__(self, parent, title):
        super(Example, self).__init__(parent, title=title)

        self.InitUI()
        self.Centre()

    def InitUI(self):

        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(4, 4)
        # wx.GridBagSizer(integer vgap, integer hgap)
        # 垂直和水平空白(gap)定义了子部件之间的空白距离.

        text = wx.StaticText(panel, label="Rename To")
        sizer.Add(text, pos=(0, 0), flag=wx.TOP|wx.LEFT|wx.BOTTOM, border=5)
        # Add(self, item, tuple pos, tuple span = wx.DefaultSpan, integer flag = 0, integer border = 0, userData = None)
        # “item” 指你要插入到网格中的部件. “pos” 指定虚拟网格的位置. 左上单元格的 “pos” 值为（0, 0）.“span” 是一个对应部件的跨度值. 比如（3, 2）指一个部件要跨越 3 行 2 列.

        tc = wx.TextCtrl(panel)
        sizer.Add(tc, pos=(1, 0), span=(1, 5), flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=5)

        buttonOk = wx.Button(panel, label="Ok", size=(90, 28))
        buttonClose = wx.Button(panel, label="Close", size=(90, 28))
        sizer.Add(buttonOk, pos=(3, 3))
        sizer.Add(buttonClose, pos=(3, 4), flag=wx.RIGHT|wx.BOTTOM, border=10)
        # In the constructor of the wx.GridBagSizer, we put some space between all widgets. So there is some space already.

        sizer.AddGrowableCol(1)
        sizer.AddGrowableRow(2)
        panel.SetSizer(sizer)


def main():

    app = wx.App()
    ex = Example(None, title='Rename')
    ex.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
