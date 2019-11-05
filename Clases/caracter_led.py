import wx


class Caracter(wx.Panel):
    """Clase que devuelve un conjunto de widgets que representan caracteres
    al estilo pantalla de LED que se puede redibujar"""

    def __init__(self, padre=wx.Frame, caracter: str = ' ', lado: int = 7,
                 color_letra: str = 'blue', color_fondo: str = 'black'):
        super().__init__(padre)
        self.caracter = caracter  # Letra que se desea mostrar
        self.lado = lado  # Cantidad de cuadraditos de lado
        self.color_fondo = color_fondo  # Color de fondo, de los buit-in en wxpython
        self.color_letra = color_letra  # Color de letra, de los buit-in en wxpython
        self.paneles = []  # Lista que guarda las referencias a los paneles de colores
        self.InitUI()

    def InitUI(self):
        """Convierte el caracter con el que se creó el objeto
        en un bonito arreglo de frames de colores, solo para
        inicializar! no usar para redibujar!"""
        grilla = wx.GridSizer(rows=self.lado, cols=self.lado, hgap=1, vgap=1)

        for _ in range(self.lado ** 2):
            self.paneles.append(wx.Panel(self, id=wx.ID_ANY, size=wx.Size(10, 10)))

        for value, panel in zip(self.ValoresLED(self.caracter), self.paneles):
            if value == 1:
                panel.SetBackgroundColour(self.color_letra)
            else:
                panel.SetBackgroundColour(self.color_fondo)
            grilla.Add(panel, 0, wx.EXPAND)
        self.SetSizer(grilla)

    def ApagarCaracter(self):
        """Metodo que coloca a todos los paneles integrantes del
        caracter del color de fondo."""
        for led in self.paneles:
            led.SetBackgroundColour(self.color_fondo)
            led.Refresh()

    def DibujarCaracter(self, caracter: str):
        """Repinta los paneles con un caracter determinado"""
        for value, led in zip(self.ValoresLED(caracter), self.paneles):
            if value == 1:
                led.SetBackgroundColour(self.color_letra)
            else:
                led.SetBackgroundColour(self.color_fondo)
            led.Refresh()

    def ValoresLED(self, caracter: str) -> list:
        """Devuelve una lista ceros y unos para cada caracter pre cargado,
        en caso de error devuelve !!!"""

        try:
            valores = {
                ' ': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'A': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'B': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'C': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'D': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'E': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'F': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'G': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 1, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'H': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'I': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'J': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 1, 1, 0,
                      0, 0, 0, 0, 1, 0, 0,
                      0, 0, 0, 0, 1, 0, 0,
                      0, 1, 0, 0, 1, 0, 0,
                      0, 0, 1, 1, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'K': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 1, 0, 0,
                      0, 1, 1, 1, 0, 0, 0,
                      0, 1, 0, 0, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'L': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'M': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 0, 1, 1, 0,
                      0, 1, 0, 1, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'N': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 0, 0, 1, 0,
                      0, 1, 0, 1, 0, 1, 0,
                      0, 1, 0, 0, 1, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'O': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'P': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'Q': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 1, 0, 1, 0,
                      0, 1, 0, 0, 1, 0, 0,
                      0, 0, 1, 1, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'R': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'S': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'T': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'U': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'V': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'W': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 1, 0, 1, 0, 1, 0,
                      0, 1, 1, 0, 1, 1, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'X': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'Y': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                'Z': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '0': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 1, 1, 0,
                      0, 1, 0, 1, 0, 1, 0,
                      0, 1, 1, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '1': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '2': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '3': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 0, 0, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '4': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 1, 0, 0,
                      0, 0, 1, 0, 1, 0, 0,
                      0, 1, 0, 0, 1, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '5': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '6': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 1, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '7': [0, 0, 0, 0, 0, 0, 0,
                      0, 1, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 0, 0, 0, 1, 0, 0,
                      0, 0, 0, 1, 0, 0, 0,
                      0, 0, 1, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '8': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                '9': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 1, 1, 1, 0, 0,
                      0, 1, 0, 0, 0, 1, 0,
                      0, 0, 1, 1, 1, 1, 0,
                      0, 0, 0, 0, 0, 1, 0,
                      0, 1, 1, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
                ':': [0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 0, 0, 0, 0,
                      0, 0, 0, 1, 1, 0, 0,
                      0, 0, 0, 0, 0, 0, 0, ],
            }
            return valores[caracter]
        except KeyError:
            inexistente = [0, 0, 0, 0, 0, 0, 0,
                           0, 1, 0, 1, 0, 1, 0,
                           0, 1, 0, 1, 0, 1, 0,
                           0, 1, 0, 1, 0, 1, 0,
                           0, 0, 0, 0, 0, 0, 0,
                           0, 1, 0, 1, 0, 1, 0,
                           0, 0, 0, 0, 0, 0, 0, ]
            return inexistente
