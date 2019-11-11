import wx
from datetime import datetime
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
        self.entradaTexto = wx.TextCtrl(self.panel,  style=wx.TE_CENTRE)
        self.entradaTexto.SetMaxLength(36)
        self.temporizador = wx.Timer()
        self.mostrarHora = False
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

        self.btnTextoPers = wx.Button(self.panel, label="Mostrar")
        self.btnTextoPers.Bind(wx.EVT_BUTTON, self.dibujar_de_caja)
        self.entradaTexto.Bind(wx.EVT_TEXT, self.dibujar_de_caja)

        self.btnAbrirArch = wx.Button(self.panel, label="Abrir Archivo")
        self.btnAbrirArch.Bind(wx.EVT_BUTTON, self.abrirarchivo)

        self.btnHora = wx.Button(self.panel, label="Hora")
        self.btnHora.Bind(wx.EVT_BUTTON, self.hora)
        self.temporizador.Bind(wx.EVT_TIMER, self.actualizarhora)


        self.VBoxPrincipal.Add(self.matrizBox, wx.ID_ANY, wx.ALL | wx.EXPAND, 20)
        self.VBoxMenu = wx.BoxSizer(wx.VERTICAL)
        self.VBoxMenu.Add(self.entradaTexto, wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.btnTextoPers, wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.btnAbrirArch, wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.btnHora, wx.ID_ANY,  wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.Botonera.Add(btnCerrar, wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(btnBlanquear, wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(btnDemo, wx.ID_ANY, wx.EXPAND, border=5)
        self.VBoxPrincipal.Add(self.VBoxMenu, wx.ID_ANY, wx.EXPAND)
        self.VBoxPrincipal.Add(self.Botonera, wx.ID_ANY,  wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.panel.SetSizer(self.VBoxPrincipal)
        self.Centre()

    # noinspection PyUnusedLocal
    def cerrar(self, event):
        self.Close()

    # noinspection PyUnusedLocal
    def blanquear(self, event):
        self.matrizBox.blanquearMatriz()
        self.entradaTexto.Clear()

    # noinspection PyUnusedLocal
    def demo(self, event):
        """Dibuja un monton de bellos caracteres en pantalla para mostrar
         la matriz de LED en su esplendor"""
        self.matrizBox.dibujarMatriz("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

    # noinspection PyUnusedLocal
    def dibujar_de_caja(self, event):
        """Toma el valor de la caja de texto y lo muestra letra a letra
        en la matriz de led"""
        self.matrizBox.dibujarMatriz(self.entradaTexto.GetValue().upper())

    # noinspection PyUnusedLocal
    def hora(self, event):
        """Muestra la hora de manera actual en la matriz de LED, y alterna su permanencia"""
        dt = datetime.now()
        self.matrizBox.dibujarMatriz('{:02d}:{:02d}:{:02d}'.format(dt.hour, dt.minute, dt.second))
        if not self.mostrarHora:
            self.mostrarHora = True
            self.btnHora.SetLabel("Parar")
            self.entradaTexto.Disable()
            self.btnTextoPers.Disable()
            self.btnAbrirArch.Disable()
            self.temporizador.Start(milliseconds=500)
        else:
            self.mostrarHora = False
            self.btnHora.SetLabel("Hora")
            self.entradaTexto.Enable()
            self.btnTextoPers.Enable()
            self.btnAbrirArch.Enable()
            self.temporizador.Stop()

    def actualizarhora(self, event):
        """Actualiza la hora con el evento timer y alterna la aparicion de los : de segundos"""
        dt = datetime.now()
        if dt.second % 2 == 0:
            self.matrizBox.dibujarMatriz('{:02d}:{:02d}:{:02d}'.format(dt.hour, dt.minute, dt.second))
        else:
            self.matrizBox.dibujarMatriz('{:02d} {:02d} {:02d}'.format(dt.hour, dt.minute, dt.second))

    def abrirarchivo(self, event):
        """Muestra la caja de abrir archivo y al seleccionar uno valido lo muestra en la matriz"""
        with wx.FileDialog(self, "Abrir archivo de texto", wildcard="Archivos txt (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as fileDialog:
            # Si el usuario cambia de idea
            if fileDialog.ShowModal() == wx.ID_CANCEL:
                return

            # Proceder a cargar el archivo seleccionado por el usuario
            pathname = fileDialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    texto = file.readline()
                    self.matrizBox.dibujarMatriz(texto[:36].upper())
                    self.entradaTexto.Clear()
                    self.entradaTexto.SetValue(texto[:36].upper())
            except IOError:
                wx.MessageBox(f"No se puede abrir el archivo {fileDialog.GetFilename()}.")




def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
