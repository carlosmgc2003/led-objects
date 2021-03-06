import wx

from Clases import caracter_led


class MatrizLed(wx.GridSizer):
    """Nuevo Widget personalizado que crea una matriz tipo led en pantalla"""

    def __init__(self, padre: wx.Object, tam_matriz: int, texto_inicial: str = ''):
        super().__init__(rows=tam_matriz, cols=tam_matriz, hgap=1, vgap=1)
        self.TAM_MATRIZ = tam_matriz
        self.padre = padre
        self.caracteres = []
        self.encendido = False
        if texto_inicial != '':
            self.inicializarMatriz(texto_inicial)
        else:
            self.texto = ''

    def inicializarMatriz(self, texto: str):
        """Recibe un texto, lo guarda en el objeto y lo muestra en la matriz."""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for index in range(self.TAM_MATRIZ ** 2):
            elem = caracter_led.Caracter(self.padre, texto[index].upper())
            self.caracteres.append(elem)
            self.Add(elem, wx.EXPAND)
        self.encendido = True

    def blanquearMatriz(self):
        """Cuando se invoca muestra la matriz en blanco"""
        for caracter in self.caracteres:
            caracter.ApagarCaracter()
        self.encendido = False

    def dibujarMatriz(self, texto: str):
        """Repinta los LED para mostrar el caracter"""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for caracter, item in zip(self.caracteres, texto):
            caracter.DibujarCaracter(item)
        self.encendido = True

    def repintarMatriz(self, colorFondo: wx.Colour, colorLetra: wx.Colour):
        """Envia el wx.Colour como mensaje a los carateres"""
        for caracter in self.caracteres:
            caracter.CambiarColorFondo(colorFondo)
            caracter.CambiarColorLetra(colorLetra)

    def obtenerContenido(self):
        """Por similitud a los widgets predefinidos este metodo devuelve el contenido
        que se encuentra mostrando el widget en este momento"""
        return self.texto

    def obtenerEstado(self):
        return self.encendido
