#v0.2

import sys
from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from team import Team

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

teams = {"ARG": "Argentinien", "AUS": "Australien", "BEL": "Belgien", "BRA": "Brasilien", "COL": "Kolumbien",
         "CRC": "Costa Rica", "CRO": "Kroatien", "DEN": "Dänemark", "EGY": "Ägypten", "ENG": "England", "ESP": "Spanien",
         "FRA": "Frankreich", "GER": "Deutschland", "IRN": "Iran", "ISL": "Island", "JPN": "Japan", "KOR": "Südkorea",
         "KSA": "Saudi-Arabien", "MAR": "Marokko", "MEX": "Mexiko", "NGA": "Nigeria", "PAN": "Panama", "PER": "Peru",
         "POL": "Polen", "POR": "Portugal", "RUS": "Russland", "SEN": "Senegal", "SRB": "Serbien", "SUI": "Schweitz",
         "SWE": "Schweden", "TUN": "Tunesien", "URU": "Uruguay"}

app = QtWidgets.QApplication(sys.argv)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Fußball - Analyst")

        self.team1 = ""
        self.team2 = ""

        self.ui.compare.clicked.connect(self.compare)
        self.ui.statistic1.clicked.connect(self.statistic1)
        self.ui.statistic2.clicked.connect(self.statistic2)

        self.figure = plt.figure(figsize=(15, 5))
        self.canvas = FigureCanvas(self.figure)
        self.ui.grid.addWidget(self.canvas, 1, 0, 1, 2)

        self.ui.team1_result.hide()
        self.ui.team2_result.hide()

    def get_teams(self):
        self.team1 = self.ui.team1.currentText()
        self.team2 = self.ui.team2.currentText()
        self.team1 = self.get_key_by_value(self.team1)
        self.team2 = self.get_key_by_value(self.team2)

    def get_key_by_value(self, text):
        for key, value in teams.items():
            if value == text:
                return key

    def compare(self):
        self.get_teams()
        self.team1 = Team(self.team1)
        self.team2 = Team(self.team2)
        self.team1.make_graph()
        self.team2.make_graph()
        result = self.team1.compare(self.team2)
        self.ui.team1_result.display(result[0])
        self.ui.team1_result.display(result[1])
        self.ui.team1_result.show()
        self.ui.team2_result.show()
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(self.team1.xs, self.team1.ys, label=self.team1.name, marker="o")
        ax.plot(self.team2.xs, self.team2.ys, label=self.team2.name, marker="o")
        ax.legend()
        self.canvas.draw()

    def statistic1(self):
        self.get_teams()
        self.team1 = Team(self.team1)
        self.team1.make_graph()
        self.team1.calculate_predicted()
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(self.team1.xs, self.team1.ys, label=self.team1.name, marker="o")
        ax.plot(self.team1.xs, self.team1.predicted, label="Trend")
        ax.legend()
        self.canvas.draw()

    def statistic2(self):
        self.get_teams()
        self.team2 = Team(self.team2)
        self.team2.make_graph()
        self.team2.calculate_predicted()
        plt.cla()
        ax = self.figure.add_subplot(111)
        ax.plot(self.team2.xs, self.team2.ys, label=self.team2.name, marker="o")
        ax.plot(self.team2.xs, self.team2.predicted, label="Trend")
        ax.legend()
        self.canvas.draw()



window = MainWindow()

window.show()

sys.exit(app.exec())