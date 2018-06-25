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

    def make_graph(self):
        for i in range(0, len(self.difference)):
            self.xs.append(i + 1)
            self.ys.append(self.difference[i])

    def draw(self):
        self.make_graph()
        plt.plot(self.xs, self.ys)
        plt.show()

    def statistic(self):
        xsl = []
        for x in self.xs:
            xsl.append([x])
        model = LinearRegression()
        model.fit(xsl, self.ys)
        predicted = model.predict(xsl)
        plt.plot(self.xs, self.ys, label=self.name)
        plt.plot(self.xs, predicted, label="Trend")
        plt.legend()
        plt.show()


