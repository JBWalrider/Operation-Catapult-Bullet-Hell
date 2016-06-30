import MainMenu
from Controller import *

c = Controller(500, 700)
menu = MainMenu.Menu(c)
menu.start()

