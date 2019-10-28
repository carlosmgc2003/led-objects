import wx

class Caracter(wx.Panel):
    def __init__(self, padre : wx.Panel, caracter : str, lado : int = 7):
        super().__init__(padre)
        self.caracter = caracter
        self.lado = lado
        self.paneles = []
        self.grilla = wx.GridSizer(rows=self.lado, cols=self.lado, hgap=5, vgap=5)
        self.InitUI()

    def InitUI(self):
        for i in range(self.lado ** 2):
            self.paneles.append(wx.Panel(self))

        for value,panel in zip(self.ValoresLED(), self.paneles):
            if value == 1:
                panel.SetBackgroundColour("black")
            else:
                panel.SetBackgroundColour("white")
            panel.SetSize((20, 20))
            self.grilla.Add(panel,0,wx.EXPAND)


        self.SetSizer(self.grilla)

    def ValoresLED(self) -> list:
        valores = {
            'A':[0,0,0,0,0,0,0,
                 0,0,0,1,0,0,0,
                 0,0,1,0,1,0,0,
                 0,1,0,0,0,1,0,
                 0,1,1,1,1,1,0,
                 0,1,0,0,0,1,0,
                 0,0,0,0,0,0,0],
            'B':[0,0,0,0,0,0,0,
                 0,1,1,1,1,0,0,
                 0,1,0,0,0,1,0,
                 0,1,1,1,1,0,0,
                 0,1,0,0,0,1,0,
                 0,1,1,1,1,0,0,
                 0,0,0,0,0,0,0]
        }
        return valores[self.caracter]
