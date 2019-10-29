import wx
from Clases import Caracter

TAM_MATRIZ = 6


# TODO: tamaño fijo de ventana style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, title="Prueba", size=(505, 800))
        self.matrizBox = wx.GridSizer(rows=TAM_MATRIZ, cols=TAM_MATRIZ, hgap=1, vgap=1)
        self.panel = wx.Panel(self)
        self.InitUI()
        self.Centre()

    def InitUI(self):
        #TODO: Mover toda la logica de la matriz al paquete
        self.panel.SetBackgroundColour("gray")
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.dibujarMatriz("NAHUEL")
        btnCerrar = wx.Button(self.panel, label="Salir")
        btnCerrar.Bind(wx.EVT_BUTTON, self.cerrar)
        vbox.Add(self.matrizBox, wx.ID_ANY, wx.ALL | wx.EXPAND, 20)
        vbox.Add(btnCerrar, wx.ID_ANY, wx.ALIGN_CENTER, border=5)
        self.panel.SetSizer(vbox)

    def cerrar(self, event):
        self.Close()

    def dibujarMatriz(self, texto: str):
        texto = texto.ljust(TAM_MATRIZ * TAM_MATRIZ)
        for row in range(TAM_MATRIZ):
            for col in range(TAM_MATRIZ):
                caracter = Caracter.Caracter(self.panel, texto[col + (row * TAM_MATRIZ)])
                self.matrizBox.Add(caracter, wx.EXPAND)


def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
