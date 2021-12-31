import matplotlib.pyplot as plt
import numpy as np; np.random.seed(1)
import math

class AnnoteFinder(object):
    """callback for matplotlib to display an annotation when points are
    clicked on.  The point which is closest to the click and within
    xtol and ytol is identified.

    Register this function like this:

    scatter(xdata, ydata)
    af = AnnoteFinder(xdata, ydata, annotes)
    connect('button_press_event', af)
    """

    def __init__(self, xdata, ydata, ax=None, xtol=None, ytol=None):
        self.data = list(zip(xdata, ydata))
        if xtol is None:
            xtol = ((max(xdata) - min(xdata)) / float(len(xdata))) / 2
        if ytol is None:
            ytol = ((max(ydata) - min(ydata)) / float(len(ydata))) / 2
        self.xtol = xtol
        self.ytol = ytol
        if ax is None:
            self.ax = plt.gca()
        else:
            self.ax = ax
        self.drawnAnnotations = {}
        self.links = []
        self.selected_points = []

    def distance(self, x1, x2, y1, y2):
        """
        return the distance between two points
        """
        return (math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

    def __call__(self, event):

        if event.inaxes:

            clickX = event.xdata
            clickY = event.ydata
            if (self.ax is None) or (self.ax is event.inaxes):
                annotes = []
                # print(event.xdata, event.ydata)
                for x, y in self.data:
                    # print(x, y, a)
                    if ((clickX - self.xtol < x < clickX + self.xtol) and
                            (clickY - self.ytol < y < clickY + self.ytol)):
                        annotes.append(
                            (self.distance(x, clickX, y, clickY), x, y))
                if annotes:
                    distance, x, y = annotes[0]

                    if len(self.drawnAnnotations) == 2:
                        if (x, y) in self.drawnAnnotations:
                            self.drawAnnote(event.inaxes, x, y, '')
                    else:
                        if len(self.drawnAnnotations) == 1:
                            if (x, y) in self.drawnAnnotations:
                                self.drawAnnote(event.inaxes, x, y, '')
                            else:
                                keys = list(self.drawnAnnotations.keys())
                                point = self.drawnAnnotations[keys[0]]
                                if point[2] == 'P':
                                    self.drawAnnote(event.inaxes, x, y, 'Q')
                                if point[2] == 'Q':
                                    self.drawAnnote(event.inaxes, x, y, 'P')
                        else:
                            if not self.drawnAnnotations:
                                self.drawAnnote(event.inaxes, x, y, 'P')

    def get_selected_points(self):
        points_dict = {}
        for key in self.drawnAnnotations:
            points_dict[self.drawnAnnotations[key][2]] = key

        return points_dict

    def drawAnnote(self, ax, x, y, annote):
        """
        Draw the annotation on the plot
        """
        if (x, y) in self.drawnAnnotations:
            markers = self.drawnAnnotations[(x, y)]
            for m in markers:
                if not type(m) == str:
                    m.set_visible(not m.get_visible())
            del self.drawnAnnotations[(x, y)]
            self.ax.figure.canvas.draw_idle()
        else:
            t = ax.text(x, y, " %s" % (annote), )
            m = ax.scatter([x], [y], marker='d', c='r', zorder=100)
            self.drawnAnnotations[(x, y)] = (t, m, annote)
            self.ax.figure.canvas.draw_idle()
