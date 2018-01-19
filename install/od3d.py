"""
1. Packaging: "pyinstaller od3d.py"
2. Copy cy_ext folder to install package folder.
3. Run od3d(.exe) and input module name "user". 
"""


import sys, importlib


# User modules will be located under cy_ext folder. (TODO This can be done in
#   better way, maybe by pyinstaller options. Also package structure must be
#   well decided.)
sys.path.insert(0, 'cy_ext')

# Allow user modules to use some framework libraries, which have no dependencies
#   to pyinstaller packaging, by referring to them specifically. NOTE For theses
#   libraries will be loaded by user modules, they should be part of system
#   libraries (under Lib/site_packages). (TODO This can be done in better way
#   too, e.g., by pyinstaller options.)
import lazy5f  # @UnusedImport

# Demonstrate dynamic loading of user module.
umod_name = input('User module name? ')
umod = importlib.import_module(umod_name)
print(umod.get_some())


#
# Below is to show a chart.

from numpy import arange, sin, pi
import matplotlib; matplotlib.use('Qt5Agg')  # Make sure that we are using QT5
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtWidgets

class MyMplCanvas(FigureCanvas):

    def __init__(self):
        fig = Figure()
        FigureCanvas.__init__(self, fig)
        
        self.axes = fig.add_subplot(111)
        t = arange(0.0, 3.0, 0.01)
        self.axes.plot(t, sin(2 * pi * t))

qApp = QtWidgets.QApplication(sys.argv)
aw = MyMplCanvas()
aw.show()
sys.exit(qApp.exec_())
