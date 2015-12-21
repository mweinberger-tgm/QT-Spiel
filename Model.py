__author__ = 'Michael Weinberger'
__date__ = 20151220
__version__ = 1.0

class Model(object):

    """
        Ausgangszustand
    """
    def __init__(self):

        self.games = 0
        self.pending = 15
        self.true = 0
        self.false = 0
        self.total = 0

    """
        Bei Auswahl einer richtigen Zahl
    """
    def success(self):

        self.pending -= 1
        self.true += 1
        self.total += 1

    """
        Bei Auswahl einer falschen Zahl
    """
    def fail(self):

        self.total += 1
        self.false += 1

    """
       Neues Spiel, Reset der Werte
       Inkrementieren des
    """
    def newgame(self):

        self.games += 1
        self.pending = 15
        self.true = 0
        self.false = 0
        self.total = 0
