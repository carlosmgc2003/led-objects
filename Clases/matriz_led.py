import wx

from Clases import caracter_led


class MatrizLed(wx.GridSizer):
    """Nuevo Widget personalizado que crea una matriz tipo led en pantalla"""
    def __init__(self, padre: wx.Object, tam_matriz: int, texto_inicial: str = ''):
        super().__init__(rows=tam_matriz, cols=tam_matriz, hgap=1, vgap=1)
        self.TAM_MATRIZ = tam_matriz
        self.padre = padre
        self.caracteres = []
        if texto_inicial != '':
            self.inicializarMatriz(texto_inicial)
        else:
            self.texto = ''

    def inicializarMatriz(self, texto: str):
        """Recibe un texto, lo guarda en el objeto y lo muestra en la matriz."""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for row in range(self.TAM_MATRIZ):
            for col in range(self.TAM_MATRIZ):
                elem = caracter_led.Caracter(self.padre, texto[col + (row * self.TAM_MATRIZ)].upper())
                self.caracteres.append(elem)
                self.Add(elem, wx.EXPAND)

    def blanquearMatriz(self):
        """Cuando se invoca muestra la matriz en blanco"""
        for caracter in self.caracteres:
            caracter.ApagarCaracter()

    def dibujarMatriz(self, texto: str):
        """Repinta los LED para mostrar el caracter"""
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for caracter, item in zip(self.caracteres, texto):
            caracter.DibujarCaracter(item)