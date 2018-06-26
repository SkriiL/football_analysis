#!/usr/bin/env python
# -*- coding: utf8 -*-

from crawler import Crawler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

teams = {"ARG": "Argentinien", "AUS": "Australien", "BEL": "Belgien", "BRA": "Brasilien", "COL": "Kolumbien",
         "CRC": "Costa Rica", "CRO": "Kroatien", "DEN": "Dänemark", "EGY": "Ägypten", "ENG": "England", "ESP": "Spanien",
         "FRA": "Frankreich", "GER": "Deutschland", "IRN": "Iran", "ISL": "Island", "JPN": "Japan", "KOR": "Südkorea",
         "KSA": "Saudi-Arabien", "MAR": "Marokko", "MEX": "Mexiko", "NGA": "Nigeria", "PAN": "Panama", "PER": "Peru",
         "POL": "Polen", "POR": "Portugal", "RUS": "Russland", "SEN": "Senegal", "SRB": "Serbien", "SUI": "Schweitz",
         "SWE": "Schweden", "TUN": "Tunesien", "URU": "Uruguay"}

class Team:
    def __init__(self, short):
        self.short = short
        self.name = teams[short]
        self.difference = Crawler(self.short, self.name).fetch()
        self.xs = [0]
        self.ys = [0]
        self.predicted = []

    def make_graph(self):
        for i in range(0, len(self.difference)):
            self.xs.append(i + 1)
            self.ys.append(self.difference[i])

    def draw(self):
        self.make_graph()
        plt.plot(self.xs, self.ys)
        plt.show()

    def calculate_predicted(self):
        xsl = []
        for x in self.xs:
            xsl.append([x])
        model = LinearRegression()
        model.fit(xsl, self.ys)
        self.predicted = model.predict(xsl)

    def statistic(self):
        plt.plot(self.xs, self.ys, label=self.name)
        plt.plot(self.xs, self.predicted, label="Trend")
        plt.legend()
        plt.show()

    def compare(self, team2):
        print(self.difference)
        self.calculate_predicted()
        team2.calculate_predicted()
        sum = 0
        for result in self.difference:
            sum += result
        d = sum / len(self.difference)
        m = (self.predicted[-1] - self.predicted[0]) / len(self.predicted)
        result_team1 = int(round(d * m + 2 / 5))
        sum = 0
        for result in team2.difference:
            sum += result
        d = sum / len(team2.difference)
        m = (team2.predicted[-1] - team2.predicted[0]) / len(team2.predicted)
        result_team2 = int(round(d * m + 2 / 2.15))
        print(str(result_team1) + ":" + str(result_team2))





