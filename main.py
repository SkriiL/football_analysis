#!/usr/bin/env python
# -*- coding: utf8 -*-

import matplotlib.pyplot as plt
from team import Team
from crawler import Quotes

teams = {"ARG": "Argentinien", "AUS": "Australien", "BEL": "Belgien", "BRA": "Brasilien", "COL": "Kolumbien",
         "CRC": "Costa Rica", "CRO": "Kroatien", "DEN": "Dänemark", "EGY": "Ägypten", "ENG": "England", "ESP": "Spanien",
         "FRA": "Frankreich", "GER": "Deutschland", "IRN": "Iran", "ISL": "Island", "JPN": "Japan", "KOR": "Südkorea",
         "KSA": "Saudi-Arabien", "MAR": "Marokko", "MEX": "Mexiko", "NGA": "Nigeria", "PAN": "Panama", "PER": "Peru",
         "POL": "Polen", "POR": "Portugal", "RUS": "Russland", "SEN": "Senegal", "SRB": "Serbien", "SUI": "Schweitz",
         "SWE": "Schweden", "TUN": "Tunesien", "URU": "Uruguay"}

class Main:
    def __init__(self):
        self.team1 = ""
        self.team2 = ""

    def menu(self):
        print("1 | Vergleiche zwei Teams \n"
              "2 | Trend eines Teams \n"
              "3 | Test")
        choice = input("Option wählen: ")
        if choice == "1":
            self.get_input_compare()
            self.compare()
        elif choice == "2":
            self.get_input_statistic()
            self.statistic()
        elif choice == "3":
            self.test()

    def compare(self):
        self.team1 = Team(self.team1)
        self.team2 = Team(self.team2)
        self.team1.make_graph()
        self.team2.make_graph()
        plt.plot(self.team1.xs, self.team1.ys, label=self.team1.name)
        plt.plot(self.team2.xs, self.team2.ys, label=self.team2.name)
        plt.legend()
        plt.show()
        self.team1.compare(self.team2)

    def get_input_compare(self):
        for short, name in teams.items():
            print(short + " | " + name)
        self.team1 = input("Kürzel des ersten Teams: ")
        self.team2 = input("Kürzel des zweiten Teams: ")

    def statistic(self):
        self.team1 = Team(self.team1)
        self.team1.make_graph()
        self.team1.statistic()

    def get_input_statistic(self):
        for short, name in teams.items():
            print(short + " | " + name)
        self.team1 = input("Kürzel des Teams: ")

    def test(self):
        c = Quotes(Team("AUS"), Team("PER"))
        c.fetch()

m = Main()
while True:
    m.menu()