from datetime import datetime

import wx
from Clases import matriz_led

TAM_MATRIZ = 6


class Ventana(wx.Frame):
    """Ventana principal del programa que contiene el resto de los widgets"""
    def __init__(self):
        super().__init__(None, -1, title="Led Objects", style=wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX,
                         size=(505, 800))
        self.panel = wx.Panel(self)
        # Solo la matriz y los Sizers quedan sueltos como atributos de clase
        self.matriz_box = matriz_led.MatrizLed(padre=self.panel, tam_matriz=TAM_MATRIZ)
        self.v_box_principal = wx.BoxSizer(wx.VERTICAL)
        self.botonera = wx.BoxSizer(wx.HORIZONTAL)
        self.v_box_menu = wx.BoxSizer(wx.VERTICAL)
        self.h_box_color = wx.BoxSizer(wx.HORIZONTAL)
        self.mostrar_hora = False
        self._init_ui()

    def _init_ui(self):
        """Metodo que separa la lógica de inicializacion de la UI"""
        self.matriz_box.inicializar_matriz(' ')
        # Todos los widgets como botones, cajas y color picker van en este diccionario
        self.widgets = {'entrada_texto': wx.TextCtrl(self.panel, style=wx.TE_CENTRE),
                        'temporizador': wx.Timer(),
                        'temp_titilar': wx.Timer(),
                        'btn_cerrar': wx.Button(self.panel, label="Salir"),
                        'btn_blanquear': wx.Button(self.panel, label="Blanquear"),
                        'btn_demo': wx.Button(self.panel, label="Demo"),
                        'btn_texto_pers': wx.Button(self.panel, label="Mostrar"),
                        'btn_abrir_arch': wx.Button(self.panel, label="Abrir Archivo"),
                        'btn_hora': wx.Button(self.panel, label="Hora"),
                        'etiqueta_clr_fondo': wx.StaticText(self.panel, label="Color de Fondo",
                                                            style=wx.ALIGN_CENTRE_HORIZONTAL),
                        'etiqueta_clr_letra': wx.StaticText(self.panel, label="Color de Letra",
                                                            style=wx.ALIGN_CENTRE_HORIZONTAL),
                        'clr_fondo': wx.ColourPickerCtrl(self.panel, colour=wx.BLACK),
                        'clr_letra': wx.ColourPickerCtrl(self.panel, colour=wx.GREEN),
                        'cho_titilar': wx.Choice(self.panel, choices=['Ninguna', 'Lenta', 'Rápida'])}

        # Todos los bind de eventos
        self.widgets['entrada_texto'].SetMaxLength(36)
        self.widgets['entrada_texto'].Bind(wx.EVT_TEXT, self.dibujar_de_caja)
        self.widgets['btn_cerrar'].Bind(wx.EVT_BUTTON, self.cerrar)
        self.widgets['btn_blanquear'].Bind(wx.EVT_BUTTON, self.blanquear)
        self.widgets['btn_demo'].Bind(wx.EVT_BUTTON, self.demo)
        self.widgets['btn_texto_pers'].Bind(wx.EVT_BUTTON, self.dibujar_de_caja)
        self.widgets['btn_abrir_arch'].Bind(wx.EVT_BUTTON, self.abrir_archivo)
        self.widgets['btn_hora'].Bind(wx.EVT_BUTTON, self.hora)
        self.widgets['temporizador'].Bind(wx.EVT_TIMER, self.actualizar_hora)
        self.widgets['temp_titilar'].Bind(wx.EVT_TIMER, self.titilar)
        self.widgets['cho_titilar'].Bind(wx.EVT_CHOICE, self.iniciar_titilar)
        self.widgets['clr_fondo'].Bind(wx.EVT_COLOURPICKER_CHANGED, self.cambiar_color)
        self.widgets['clr_letra'].Bind(wx.EVT_COLOURPICKER_CHANGED, self.cambiar_color)

        # Todos los Add a los sizers para armar la ventana.
        self.v_box_principal.Add(self.matriz_box, 0, wx.ALL | wx.EXPAND, 20)

        # h_box_color - Color picker section
        self.h_box_color.Add(self.widgets['etiqueta_clr_fondo'], 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.h_box_color.Add(self.widgets['clr_fondo'], 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.h_box_color.Add(self.widgets['etiqueta_clr_letra'], 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        self.h_box_color.Add(self.widgets['clr_letra'], 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)

        # v_box_menu - Menu section
        self.v_box_menu.Add(self.widgets['entrada_texto'], 0, wx.ALL | wx.EXPAND, 5)
        self.v_box_menu.Add(self.widgets['btn_texto_pers'], 0, wx.ALL | wx.EXPAND, 5)
        self.v_box_menu.Add(self.widgets['btn_abrir_arch'], 0, wx.ALL | wx.EXPAND, 5)
        self.v_box_menu.Add(self.widgets['btn_hora'], 0, wx.ALL | wx.EXPAND, 5)
        self.v_box_menu.Add(self.h_box_color, 0, wx.ALL | wx.EXPAND, 5)
        self.v_box_menu.Add(self.widgets['cho_titilar'], 0, wx.ALL | wx.EXPAND, 5)

        # botonera - Bottom buttons
        self.botonera.Add(self.widgets['btn_cerrar'], 1, wx.ALL | wx.EXPAND, 5)
        self.botonera.Add(self.widgets['btn_blanquear'], 1, wx.ALL | wx.EXPAND, 5)
        self.botonera.Add(self.widgets['btn_demo'], 1, wx.ALL | wx.EXPAND, 5)

        # Adding the sections to the main vertical box
        self.v_box_principal.Add(self.v_box_menu, 0, wx.LEFT | wx.RIGHT | wx.EXPAND, 20)
        self.v_box_principal.Add(self.botonera, 0, wx.LEFT | wx.RIGHT | wx.BOTTOM | wx.EXPAND, 20)

        # Final layout
        self.panel.SetSizer(self.v_box_principal)
        self.v_box_principal.Fit(self)
        self.Centre()

    # noinspection PyUnusedLocal
    def cerrar(self, event):
        """Al ser llamado cierra la ventana principal"""
        self.Close()

    # noinspection PyUnusedLocal
    def blanquear(self, event):
        """Limpia la matriz y la caja de texto de cualquier contenido"""
        self.matriz_box.blanquear_matriz()
        self.widgets['entrada_texto'].Clear()

    # noinspection PyUnusedLocal
    def demo(self, event):
        """Dibuja un monton de bellos caracteres en pantalla para mostrar
        la matriz de LED en su esplendor"""
        self.matriz_box.dibujar_matriz("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")

    # noinspection PyUnusedLocal
    def dibujar_de_caja(self, event):
        """Toma el valor de la caja de texto y lo muestra letra a letra
        en la matriz de led"""
        self.matriz_box.dibujar_matriz(self.widgets['entrada_texto'].GetValue().upper())

    # noinspection PyUnusedLocal
    def hora(self, event):
        """Muestra la hora actual en la matriz de LED, y alterna su permanencia"""
        dt = datetime.now()
        self.matriz_box.dibujar_matriz('{:02d}:{:02d}:{:02d}'.format(dt.hour, dt.minute, dt.second))
        if not self.mostrar_hora:
            self.mostrar_hora = True
            # Una utilidad del diccionario: aplicar polimorfismo en widgets
            deshabilitar = ['entrada_texto', 'btn_texto_pers', 'btn_abrir_arch']
            for clave in deshabilitar:
                self.widgets[clave].Disable()
            self.widgets['btn_hora'].SetLabel("Parar")
            self.widgets['temporizador'].Start(milliseconds=500)
        else:
            self.mostrar_hora = False
            self.widgets['btn_hora'].SetLabel("Hora")
            habilitar = ['entrada_texto', 'btn_texto_pers', 'btn_abrir_arch']
            for clave in habilitar:
                self.widgets[clave].Enable()
            self.widgets['temporizador'].Stop()

    def actualizar_hora(self, event):
        """Actualiza la hora con el evento timer y alterna la aparicion de los : de segundos"""
        dt = datetime.now()
        if dt.second % 2 == 0:
            self.matriz_box.dibujar_matriz('{:02d}:{:02d}:{:02d}'.format(dt.hour, dt.minute, dt.second))
        else:
            self.matriz_box.dibujar_matriz('{:02d} {:02d} {:02d}'.format(dt.hour, dt.minute, dt.second))

    # noinspection PyUnusedLocal
    def abrir_archivo(self, event):
        """Muestra la caja de abrir archivo y al seleccionar uno valido lo muestra en la matriz"""
        with wx.FileDialog(self, "Abrir archivo de texto", wildcard="Archivos txt (*.txt)|*.txt",
                           style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST) as file_dialog:
            # Si el usuario cambia de idea
            if file_dialog.ShowModal() == wx.ID_CANCEL:
                return

            # Proceder a cargar el archivo seleccionado por el usuario
            pathname = file_dialog.GetPath()
            try:
                with open(pathname, 'r') as file:
                    texto = file.readline()
                    self.matriz_box.dibujar_matriz(texto[:36].upper())
                    self.widgets['entrada_texto'].Clear()
                    self.widgets['entrada_texto'].SetValue(texto[:36].upper())
            except IOError:
                wx.MessageBox(f"No se puede abrir el archivo {file_dialog.GetFilename()}.")

    def cambiar_color(self, event):
        """Actualiza los colores de fondo y letra de la matriz con los valores del color picker"""
        self.matriz_box.repintar_matriz(self.widgets['clr_fondo'].GetColour(),
                                        self.widgets['clr_letra'].GetColour())

    def iniciar_titilar(self, event):
        """Cuando se dispara el EVT_CHOICE al seleccionar una opción de la caja se inicia
        o detiene el temp_titilar"""
        valor_choice = self.widgets['cho_titilar'].GetString(self.widgets['cho_titilar'].GetSelection())
        if valor_choice == 'Lenta':
            self.widgets['temp_titilar'].Start(milliseconds=250)
        elif valor_choice == 'Rápida':
            self.widgets['temp_titilar'].Start(milliseconds=125)
        else:
            self.widgets['temp_titilar'].Stop()

    def titilar(self, event):
        """Metodo que apaga o enciende alternativamente la matriz de acuerdo a lo seleccionado
        en el choice titilar"""
        texto_act = self.matriz_box.obtener_contenido()
        if self.matriz_box.obtener_estado():
            self.matriz_box.blanquear_matriz()
        else:
            self.matriz_box.dibujar_matriz(texto_act)


def main():
    app = wx.App()
    ventana = Ventana()
    ventana.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()
