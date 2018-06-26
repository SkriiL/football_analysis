#v0.2

from bs4 import BeautifulSoup
import requests
import string

class Crawler:
    def __init__(self, short, name):
        self.short = short
        self.name = name
        self.website = "https://www.sportschau.de/fifa-wm-2018/spielplan/spielplan216~_eam-59846f3a6a80e59c34abfaef8c7f7402_eap__bereich-team_eap__liga-WM_eap__saison-2018_eap__sportart-fb_eap__team-" + self.short + ".html?eap=8oI34N4hym4RDV6dhKK0OnLYM%2FNzIoiKmKv2HkJYKgPxCIifwJGZmigVNLw42zmko7u1BzkuenhteE%2FSifHaWb%2BD5g3qtsFGHf4hK1Y74dEG7qbSVS7%2B4ufIxbo1iSZVqPHD4Oz4HQTQ9cNW16t1Kw%3D%3D"
        self.difference = []
        self.home_team = []
        self.guest_team = []
        self.home = []

    def fetch(self):
        request = requests.get(self.website)
        doc = BeautifulSoup(request.text, "html.parser")

        for match in doc.select(".begegnungen"):
            for opponents in match.select(".ttxt"):
                text = opponents.text
                if self.name + " gegen" in text:
                    self.home.append(True)
                elif ": " + self.name in text:
                    self.home.append(False)
            print(self.home)

            numbers = string.digits

            for result in match.select(".tnr"):
                text = result.text
                for number in numbers:
                    if number + ": zu" in text:
                        self.home_team.append(number)
                    if "zu " + number in text:
                        self.guest_team.append(number)
            print(self.home_team)
            print(self.guest_team)

            for i in range(0, len(self.home_team)):
                if self.home[i]:
                    self.difference.append(int(self.home_team[i]) - int(self.guest_team[i]))
                else:
                    self.difference.append(int(self.guest_team[i]) - int(self.home_team[i]))

            print(self.difference)
            return self.difference


class Quotes:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.website = "https://www.interwetten.com/de/sportwetten/top-leagues?topLinkId=7"

    def fetch(self):
        request = requests.get(self.website)
        doc = BeautifulSoup(request.text, "html.parser")

        names = []
        quotes = []

        table = doc.select_one(".bets")
        for match in table.select(".even.group3"):
            if self.team1.name in match.text and self.team2.name in match.text:
                for result in match("span"):
                    names.append(result.text)
                for result in match("strong"):
                    quotes.append(result.text)

        if "" in names:
            names.remove("")
        if "" in quotes:
            quotes.remove("")

        dict = {}
        for i in range(len(names)):
            q_number = quotes[i].replace(",", ".")
            dict[names[i]] = q_number
        print(dict)
        return dict