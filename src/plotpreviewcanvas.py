# -*- coding: utf-8 -*-
"""
Created on Tue Aug 12 12:02:53 2025

@author: biol0117
"""
import numpy as np
from plotcanvas import PlotCanvas
import re

class CoordsInputPlotCanvas(PlotCanvas):
    """ Creates a plot figure of coordinate points. """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Parameters
        ----------
        parent : TYPE, optional
            DESCRIPTION. The default is None.
        width : float, optional
            Figure width (inches). The default is 5.
        height : float, optional
            Figure height (inches). The default is 4.
        dpi : float, optional
            Figure dpi (resolution in dots-per-inch). The default is 100.
        """
        super().__init__(parent, width, height, dpi)

    def plot(self, file, *args):
        """
        Scatter plots the points from the data file.

        Parameters
        ----------
        file : os.path for coords data file
        *args :

        Returns
        -------
        None.
        """
        self.axes.clear()
        data = np.loadtxt(file, ndmin=2, usecols=(0,1)) # don't use last column (release sites)

        def findReleaseSites(f):
            isRelSiteData = np.loadtxt(f, dtype='str', ndmin=2, usecols=(2))
            relSitesIndices = []
            notRelSitesIndices = []
            for site in range(0, len(isRelSiteData)):
                if isRelSiteData[site] == "y":
                    relSitesIndices.append(site)
                else:
                    notRelSitesIndices.append(site)
            return (relSitesIndices, notRelSitesIndices)
                  
        relSitesIndices, notRelSitesIndices = findReleaseSites(file)
        x = data[:, 0]
        y = data[:, 1]
        xRel = data[relSitesIndices, 0]
        yRel = data[relSitesIndices, 1]
        xNot = data[notRelSitesIndices, 0]
        yNot = data[notRelSitesIndices, 1]

        self.axes.scatter(xRel, yRel, marker='*', color="royalblue", label="release sites")
        self.axes.scatter(xNot, yNot, marker='.', color="peru", label=None) # label None so don't show in legend

        if len(x) == 1:
            self.axes.set_xlim(x - x/2, x + x/2)
        else:
            self.axes.set_xlim(np.amin(x), np.amax(x))
        if len(y) == 1:
            self.axes.set_ylim(y - y/2, y + y/2)
        else:
            self.axes.set_ylim(np.amin(y), np.amax(y))
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("y")
        self.axes.set_aspect('equal') # set equal aspect ratio for both axes
        self.axes.legend()
        self.draw()


class RainfallInputPlotCanvas(PlotCanvas):
    """ Creates a plot figure of rainfall data. """
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        """
        Parameters
        ----------
        parent : TYPE, optional
            DESCRIPTION. The default is None.
        width : float, optional
            Figure width (inches). The default is 5.
        height : float, optional
            Figure height (inches). The default is 4.
        dpi : float, optional
            Figure dpi (resolution in dots-per-inch). The default is 100.
        """
        super().__init__(parent, width, height, dpi)

    def plot(self, file, *args):
        """
        Plots the data from the data file.

        Parameters
        ----------
        file : os.path for coords data file
        *args :

        Returns
        -------
        None.
        """
        self.axes.clear()
        data = np.loadtxt(file, ndmin=2)
        x = np.arange(1, len(data)+1)
        y = data[:, 0]
        self.axes.plot(x, y, color="cornflowerblue")
        self.axes.set_xlabel("Day")
        self.axes.set_ylabel("Rainfall")
        self.draw()
