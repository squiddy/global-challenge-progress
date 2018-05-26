import json
import os

import requests


def login(username, password):
    session = requests.Session()
    session.post(
        "https://globalchallenge.virginpulse.com/log-in",
        data={"username": username, "password": password},
    )
    return session


def get_own_team(session):
    res = session.post("https://globalchallenge.virginpulse.com/event/map/visited/null")
    return res.json()["MyMarker"]


def get_other_teams(session):
    res = session.post(
        "https://globalchallenge.virginpulse.com/event/map/organisation-teams"
    )
    return res.json()


session = login(os.environ["VIRGIN_USERNAME"], os.environ["VIRGIN_PASSWORD"])
my_team = get_own_team(session)
other_teams = get_other_teams(session)

my_team = {
    "name": my_team["Name"],
    "steps": int(my_team["StepTotalFormatted"].replace(".", "")),
}
teams = [my_team]
for team in other_teams:
    teams.append({"name": team["Name"], "steps": team["Steps"]})


print(
    """<?xml version="1.0" encoding="UTF-8" ?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
  <style>
    * { fill: #fff }
    .steps { font: bold 14px sans-serif; }
    .name { font: normal 14px sans-serif; }
    .heading { font: bold 24px sans-serif; }
    .my-team .steps, .my-team .name { fill: #87d0f0; }
  </style>
  <text x="100" y="20" class="heading">Challenge</text>
"""
)

for i, t in enumerate(sorted(teams, key=lambda e: e["steps"], reverse=True)):
    print(
        f"""
    <g class="{'my-team' if t['name'] == my_team['name'] else ''}">
        <text x="10" y="{i * 20 + 60}" class="steps">{t['steps']}</text>
        <text x="100" y="{i * 20 + 60}" class="name">{t['name']}</text>
    </g>
    """
    )

print("</svg>")
