import wx
from datetime import datetime
from Clases import matriz_led

TAM_MATRIZ = 6


# TODO: tamaño fijo de ventana style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX
class Ventana(wx.Frame):
    def __init__(self):
        super().__init__(None, -1, title="Led Objects", style= wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX, size=(505, 800))
        self.panel = wx.Panel(self)
        # Solo la matriz y los Sizers quedan sueltos como atributos de clase
        self.matrizBox = matriz_led.MatrizLed(padre=self.panel, tam_matriz=TAM_MATRIZ)
        self.VBoxPrincipal = wx.BoxSizer(wx.VERTICAL)
        self.Botonera = wx.BoxSizer(wx.HORIZONTAL)
        self.VBoxMenu = wx.BoxSizer(wx.VERTICAL)
        self.HBoxColor = wx.BoxSizer(wx.HORIZONTAL)
        self.mostrarHora = False
        self.InitUI()

    def InitUI(self):
        """Metodo que separa la lógica de inicializacion de la UI"""
        self.matrizBox.inicializarMatriz(' ')
        # Todos los widgets como botones, cajas y color picker van en este diccionario
        self.widgets = {}

        self.widgets['entradaTexto'] = wx.TextCtrl(self.panel,  style=wx.TE_CENTRE)
        self.widgets['temporizador'] = wx.Timer()
        self.widgets['btnCerrar'] = wx.Button(self.panel, label="Salir")
        self.widgets['btnBlanquear'] = wx.Button(self.panel, label="Blanquear")
        self.widgets['btnDemo'] = wx.Button(self.panel, label="Demo")
        self.widgets['btnTextoPers'] = wx.Button(self.panel, label="Mostrar")
        self.widgets['btnAbrirArch'] = wx.Button(self.panel, label="Abrir Archivo")
        self.widgets['btnHora'] = wx.Button(self.panel, label="Hora")
        self.widgets['etiquetaClrFondo'] = wx.StaticText(self.panel, label="Color de Fondo", style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.widgets['etiquetaClrLetra'] = wx.StaticText(self.panel, label="Color de Letra", style=wx.ALIGN_CENTRE_HORIZONTAL)
        self.widgets['clrFondo'] = wx.ColourPickerCtrl(self.panel, colour=wx.BLACK)
        self.widgets['clrLetra'] = wx.ColourPickerCtrl(self.panel, colour=wx.GREEN)

        self.widgets['entradaTexto'].SetMaxLength(36)
        self.widgets['entradaTexto'].Bind(wx.EVT_TEXT, self.dibujar_de_caja)
        self.widgets['btnCerrar'].Bind(wx.EVT_BUTTON, self.cerrar)
        self.widgets['btnBlanquear'].Bind(wx.EVT_BUTTON, self.blanquear)
        self.widgets['btnDemo'].Bind(wx.EVT_BUTTON, self.demo)
        self.widgets['btnTextoPers'].Bind(wx.EVT_BUTTON, self.dibujar_de_caja)
        self.widgets['btnAbrirArch'].Bind(wx.EVT_BUTTON, self.abrirarchivo)
        self.widgets['btnHora'].Bind(wx.EVT_BUTTON, self.hora)
        self.widgets['temporizador'].Bind(wx.EVT_TIMER, self.actualizarhora)
        self.widgets['clrFondo'].Bind(wx.EVT_COLOURPICKER_CHANGED, self.cambiarColor)
        self.widgets['clrLetra'].Bind(wx.EVT_COLOURPICKER_CHANGED, self.cambiarColor)


        self.VBoxPrincipal.Add(self.matrizBox, wx.ID_ANY, wx.ALL | wx.EXPAND, 20)
        self.HBoxColor.Add(self.widgets['etiquetaClrFondo'], wx.ID_ANY, wx.ALL | wx.EXPAND, 10)
        self.HBoxColor.Add(self.widgets['clrFondo'], wx.ID_ANY, wx.EXPAND)
        self.HBoxColor.Add(self.widgets['etiquetaClrLetra'], wx.ID_ANY, wx.ALL | wx.EXPAND, 10)
        self.HBoxColor.Add(self.widgets['clrLetra'], wx.ID_ANY, wx.EXPAND)
        self.VBoxMenu.Add(self.widgets['entradaTexto'], wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.widgets['btnTextoPers'], wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.widgets['btnAbrirArch'], wx.ID_ANY, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.widgets['btnHora'], wx.ID_ANY,  wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.VBoxMenu.Add(self.HBoxColor, wx.ID_ANY,  wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.Botonera.Add(self.widgets['btnCerrar'], wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(self.widgets['btnBlanquear'], wx.ID_ANY, wx.EXPAND, border=5)
        self.Botonera.Add(self.widgets['btnDemo'], wx.ID_ANY, wx.EXPAND, border=5)
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
        self.widgets['entradaTexto'].Clear()

    # noinspection PyUnusedLocal
    def demo(self, event):
        """Dibuja un monton de bellos caracteres en pantalla para mostrar
         la matriz de LED en su esplendor"""
        self.matrizBox.dibujarMatriz("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

    # noinspection PyUnusedLocal
    def dibujar_de_caja(self, event):
        """Toma el valor de la caja de texto y lo muestra letra a letra
        en la matriz de led"""
        self.matrizBox.dibujarMatriz(self.widgets['entradaTexto'].GetValue().upper())

    # noinspection PyUnusedLocal
    def hora(self, event):
        """Muestra la hora de manera actual en la matriz de LED, y alterna su permanencia"""
        dt = datetime.now()
        self.matrizBox.dibujarMatriz('{:02d}:{:02d}:{:02d}'.format(dt.hour, dt.minute, dt.second))
        if not self.mostrarHora:
            self.mostrarHora = True
            # Una utilidad del diccionario, aplicar polimorfismo en widgets
            deshabilitar = ['entradaTexto', 'btnTextoPers', 'btnAbrirArch']
            for clave in deshabilitar:
                self.widgets[clave].Disable()
            self.widgets['btnHora'].SetLabel("Parar")
            self.widgets['temporizador'].Start(milliseconds=500)
        else:
            self.mostrarHora = False
            self.widgets['btnHora'].SetLabel("Hora")
            habilitar = ['entradaTexto', 'btnTextoPers', 'btnAbrirArch']
            for clave in habilitar:
                self.widgets[clave].Enable()
            self.widgets['temporizador'].Stop()

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
                    self.widgets['entradaTexto'].Clear()
                    self.widgets['entradaTexto'].SetValue(texto[:36].upper())
            except IOError:
                wx.MessageBox(f"No se puede abrir el archivo {fileDialog.GetFilename()}.")


    def cambiarColor(self, event):
        self.matrizBox.repintarMatriz(self.widgets['clrFondo'].GetColour(), self.widgets['clrLetra'].GetColour())




def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
