# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 10:52:17 2025

@author: biol0117
"""

from PyQt5.QtWidgets import QDialog, QGridLayout, QVBoxLayout, QGroupBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavBar
import plotpreviewcanvas

class PlotPreviewWindow(QDialog):
    """Window containing the preview plotspace and toolbar components."""

    def __init__(self, plotType, filepath):
        """
        Parameters
        ----------
        canvas : PlotCanvas
            The associated plot canvas.
        plotType : string
            Description of plot. Options include "Coordinates".
        """
        super().__init__()
        self.title = plotType + " file plot preview"
        self.left = 900
        self.top = 400
        self.width = 500
        self.height = 600
        self.setWindowIcon(QIcon('web.png'))
        self.setWindowFlags(self.windowFlags() ^ Qt.WindowContextHelpButtonHint)  # removes window help button
        self.canvas = self.createCanvas(plotType)
        self.toolbar = NavBar(self.canvas)
        self.initUI()
        self.canvas.plot(filepath) # plot upon construction since only want instant static plots

    def initUI(self):
         """ Initialises the UI. """
         self.setWindowTitle(self.title)
         self.setGeometry(self.left, self.top, self.width, self.height)  # sets position and size of window

         self.createGridLayout()  # creates layout to place widgets in window
         windowLayout = QVBoxLayout()
         windowLayout.addWidget(self.horizontalGroupBox)
         self.setLayout(windowLayout)

    def createGridLayout(self):
        """ Places UI components on a grid layout. """
        self.horizontalGroupBox = QGroupBox()
        layout = QGridLayout()
        layout.addWidget(self.toolbar, 0, 0, 1, 5)
        layout.addWidget(self.canvas, 1, 0, 1, 5)
        self.horizontalGroupBox.setLayout(layout)
        
    def createCanvas(self, plotType):
        """
        Creates the corresponding plot canvas for the selected plot type.

        Parameters
        ----------
        plotType : string
            Description of plot type.

        Returns
        -------
        canvas : PlotCanvas
            Plot canvas.

        """
        canvas = None
        if plotType == "Coordinates":
            canvas = plotpreviewcanvas.CoordsInputPlotCanvas()
        return canvas
