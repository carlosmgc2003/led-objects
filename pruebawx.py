import wx

from Clases import matriz_led

TAM_MATRIZ = 6


# TODO: tamaño fijo de ventana style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, title="Prueba", style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(505, 800))
        self.panel = wx.Panel(self)
        self.matrizBox = matriz_led.MatrizLed(padre=self.panel, tam_matriz=TAM_MATRIZ)
        self.VBoxPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.Botonera = wx.BoxSizer(wx.HORIZONTAL)
        self.InitUI()

    def InitUI(self):
        """Metodo que separa la lógica de inicializacion de la UI"""
        self.panel.SetBackgroundColour("gray")
        self.matrizBox.inicializarMatriz(' ')

        btnCerrar = wx.Button(self.panel, label="Salir")
        btnCerrar.Bind(wx.EVT_BUTTON, self.cerrar)

        btnBlanquear = wx.Button(self.panel, label="Blanquear")
        btnBlanquear.Bind(wx.EVT_BUTTON, self.blanquear)

        btnDemo = wx.Button(self.panel, label="Demo")
        btnDemo.Bind(wx.EVT_BUTTON, self.demo)

        self.VBoxPrincipal.Add(self.matrizBox, wx.ID_ANY, wx.ALL | wx.EXPAND, 20)
        self.Botonera.Add(btnCerrar, wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(btnBlanquear, wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(btnDemo, wx.ID_ANY, wx.EXPAND, border=5)
        self.VBoxPrincipal.Add(self.Botonera, wx.ID_ANY, wx.EXPAND)
        self.panel.SetSizer(self.VBoxPrincipal)
        self.Centre()

    # noinspection PyUnusedLocal
    def cerrar(self, event):
        self.Close()

    def blanquear(self, event):
        self.matrizBox.blanquearMatriz()

    def demo(self, event):
        self.matrizBox.dibujarMatriz("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")


def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
