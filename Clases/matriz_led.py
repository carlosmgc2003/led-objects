import wx

from Clases import caracter_led


class MatrizLed(wx.GridSizer):
    """Nuevo Widget personalizado que crea una matriz tipo led en pantalla"""
    def __init__(self, padre: wx.Object, tam_matriz: int, texto_inicial: str = ''):
        super().__init__(rows=tam_matriz, cols=tam_matriz, hgap=1, vgap=1)
        self.TAM_MATRIZ = tam_matriz
        self.padre = padre
        if texto_inicial != '':
            self.dibujarMatriz(texto_inicial)
        else:
            self.texto = ''

    def dibujarMatriz(self, texto: str):
        """Recibe un texto, lo guarda en el objeto y lo muestra en la matriz."""
        self.Clear(delete_windows=True)
        self.texto = texto
        texto = texto.ljust(self.TAM_MATRIZ * self.TAM_MATRIZ)
        for row in range(self.TAM_MATRIZ):
            for col in range(self.TAM_MATRIZ):
                elem = caracter_led.Caracter(self.padre, texto[col + (row * self.TAM_MATRIZ)].upper())
                self.Add(elem, wx.EXPAND)

    def blanquearMatriz(self):
        """Cuando se invoca muestra la matriz en blanco"""
        self.Clear(delete_windows=True)
        for row in range(self.TAM_MATRIZ):
            for col in range(self.TAM_MATRIZ):
                elem = caracter_led.Caracter(self.padre, " ")
                self.Add(elem, wx.EXPAND)
