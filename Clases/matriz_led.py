import wx

from Clases import caracter_led


class MatrizLed(wx.GridSizer):
    """Nuevo Widget personalizado que crea una matriz tipo led en pantalla"""

    def __init__(self, padre: wx.Window, tam_matriz: int, texto_inicial: str = ''):
        super().__init__(rows=tam_matriz, cols=tam_matriz, hgap=1, vgap=1)
        self.TAM_MATRIZ = tam_matriz
        self.padre = padre
        self.caracteres = []
        self.encendido = False
        if texto_inicial != '':
            self.inicializar_matriz(texto_inicial)
        else:
            self.texto = ''

    def inicializar_matriz(self, texto: str):
        """Recibe un texto, lo guarda en el objeto y lo muestra en la matriz."""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for index in range(self.TAM_MATRIZ ** 2):
            elem = caracter_led.Caracter(self.padre, texto[index].upper())
            self.caracteres.append(elem)
            self.Add(elem, wx.EXPAND)
        self.encendido = True

    def blanquear_matriz(self):
        """Cuando se invoca muestra la matriz en blanco"""
        for caracter in self.caracteres:
            caracter.apagar_caracter()
        self.encendido = False

    def dibujar_matriz(self, texto: str):
        """Repinta los LED para mostrar el texto"""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for caracter, item in zip(self.caracteres, texto):
            caracter.dibujar_caracter(item)
        self.encendido = True

    def repintar_matriz(self, color_fondo: wx.Colour, color_letra: wx.Colour):
        """Envia el wx.Colour como mensaje a los caracteres"""
        for caracter in self.caracteres:
            caracter.cambiar_color_fondo(color_fondo)
            caracter.cambiar_color_letra(color_letra)

    def obtener_contenido(self):
        """Por similitud a los widgets predefinidos este metodo devuelve el contenido
        que se encuentra mostrando el widget en este momento"""
        return self.texto

    def obtener_estado(self):
        """Devuelve True si la matriz esta encendida, False si esta blanqueada"""
        return self.encendido
