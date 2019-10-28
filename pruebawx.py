import wx
from Clases import Caracter


class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(None,-1,title="Prueba", style=wx.DEFAULT_FRAME_STYLE, size=(400,600))
        self.InitUI()
        self.Centre()

    def InitUI(self):
        self.panel = wx.Panel(self)
        self.panel.SetBackgroundColour("gray")
        vbox = wx.BoxSizer(wx.VERTICAL)
        lineaBox = wx.BoxSizer(wx.HORIZONTAL)
        lineaList = []
        for i in range(7):
            caracter = Caracter.Caracter(self.panel, 'A')
            lineaList.append(caracter)
            lineaBox.Add(lineaList[i], wx.EXPAND, 5)
        btn1 = wx.Button(self.panel, label = "Salir")
        vbox.Add(lineaBox, wx.ID_ANY,wx.ALL | wx.EXPAND, 20)
        vbox.Add(btn1,wx.ID_ANY,wx.ALIGN_CENTER, border=5)
        self.panel.SetSizer(vbox)

def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()
