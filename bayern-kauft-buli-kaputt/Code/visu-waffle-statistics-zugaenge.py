# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 10:44:08 2021

@author: Marvin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from pywaffle import Waffle
from highlight_text import HighlightText, ax_text, fig_text
abs_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/bayern-kauft-buli-kaputt/buli-cl-teams-zugaenge.csv"
img_base_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/buli-logos/"

df = pd.read_csv(abs_path)
df = df.loc[df["Saison"] != 2021]
de_liga = ["Bundesliga", "2. Bundesliga"]
de_liga2 = ["Bundesliga", "2. Bundesliga", "3. Liga","A-Junioren Bundesliga Nord/Nordost","A-Junioren Bundesliga Süd/Südwest","A-Junioren Bundesliga West","Regionalliga West (bis 11/12)",
            "Regionalliga West","Regionalliga Südwest","Regionalliga Nord (bis 11/12)","Regionalliga Nord","Regionalliga Bayern"]
team_dict = {"fcb":"FCB",
             "bvb":"BVB",
             "wob":"WOB",
             "b04":"B04",
             "bmg":"BMG",
             "hof":"HOF",
             "s04":"S04",
             "rbl":"RBL"}

de_zugaenge = df.loc[(df["Abgebende-Liga"].isin(de_liga)) & (df["Transferart"]=="Transfer")]
int_zugaenge = df.loc[(~df["Abgebende-Liga"].isin(de_liga2)) & (df["Transferart"]=="Transfer")]
anzahl_zugaenge = de_zugaenge.groupby(["Aufnehmender-Verein","Abgebende-Liga"], as_index=False)["Unnamed: 0"].count()

sum_marktwert_ablöse_zugaenge_de = de_zugaenge.groupby(["Aufnehmender-Verein"])["Marktwert", "Ablöse"].apply(sum)
mean_marktwert_ablöse_zugaenge_de = de_zugaenge.groupby(["Aufnehmender-Verein"])["Marktwert", "Ablöse"].mean()
season_grouped_mw_ablöse_zugaenge_de = de_zugaenge.groupby(["Aufnehmender-Verein","Saison"])["Ablöse"].apply(sum)

sum_marktwert_ablöse_zugaenge_int = int_zugaenge.groupby(["Aufnehmender-Verein"])["Marktwert", "Ablöse"].apply(sum)
mean_marktwert_ablöse_zugaenge_int = int_zugaenge.groupby(["Aufnehmender-Verein"])["Marktwert", "Ablöse"].mean()
season_grouped_mw_ablöse_zugaenge_int = int_zugaenge.groupby(["Aufnehmender-Verein","Saison"])["Ablöse"].apply(sum)
# print(mean_marktwert_ablöse_zugaenge) 

asdf = sum_marktwert_ablöse_zugaenge_de["Marktwert"] - sum_marktwert_ablöse_zugaenge_de["Ablöse"]
# asdf = de_zugaenge.sort_values("Ablöse")

title_font = "Alegreya Sans"
body_font = "Open Sans"
textColor = "w"
background = "#212529"
filler = "lightgrey"
primary = "red"

mpl.rcParams['xtick.color'] = textColor
mpl.rcParams['ytick.color'] = textColor
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10

anz = anzahl_zugaenge["Aufnehmender-Verein"].unique().tolist()
anz_buli1 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "Bundesliga", "Unnamed: 0"].tolist()
anz_buli2 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "2. Bundesliga", "Unnamed: 0"].tolist()
team_list = [team_dict[i] for i in anz]

def plot_waffle_anzahl_buli_zugaenge():

    fig = plt.figure(FigureClass=Waffle,rows=5,icons='user',font_size= 12,figsize=(12,8),plots={
        '331': {
            'values': [anz_buli1[0], anz_buli2[0]],
            'title': {"y":-0.2,'label': 'Gesamt: 32','loc': 'left',"fontfamily":body_font,"fontsize":12,"color":textColor},
            },
        331: {
            "values": [1],
            "title": {"y":1,'label': 'Bayer 04 Leverkusen','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor}
            },
        '332': {
            'values': [anz_buli1[6], anz_buli2[6]],
            'title': {'label': 'FC Schalke 04','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor},
            },
        '333': {
            'values': [anz_buli1[1], anz_buli2[1]],
            'title': {'label': 'Borussia Mönchengladbach','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor}
            
            },
        '334': {
            'values': [anz_buli1[3], anz_buli2[3]],
            'title': {'label': 'FC Bayern München','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor},
            },
        '335': {
            'values': [anz_buli1[4], anz_buli2[4]],
            'title': {'label': 'TSG 1899 Hoffenheim','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor},
            },
        '336': {
            'values': [anz_buli1[5], anz_buli2[5]],
            'title': {'label': 'RasenBallsport Leipzig', 'loc': 'left', "fontfamily":title_font,"fontweight":"bold", "fontsize":12,"color":textColor},
            },
        '337': {
            'values': [anz_buli1[2], anz_buli2[2]],
            'title': {'label': 'Borussia Dortmund','loc': 'left',"fontfamily":title_font,"fontweight":"bold","fontsize":12,"color":textColor},
            },
        '338': {
            'values': [anz_buli1[7], anz_buli2[7]],
            'title': {'label': 'VFL Wolfsburg','loc': 'left',"fontfamily":title_font,  "fontweight":"bold", "fontsize":12,"color":textColor},
            "labels": ["Bundesliga", "2. Bundesliga"],
            "legend": {'loc': 'right', 'bbox_to_anchor': (2.5,0.5),'framealpha': 0,'fontsize': 16,"labelcolor":textColor}
            },
        338: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 32','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            },
        337: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 32','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        336: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 22','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        335: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 39','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        334: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 23','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        333: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 22','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        332: {
            'values': [0],
            'title': {"y":-0.2,'label': 'Gesamt: 40','loc': 'left',"fontfamily":title_font, "fontsize":12,"color":textColor},
            }, 
        },
    )
    fig.set_facecolor(background)
    fig.patch.set_facecolor(background)
    fig.suptitle(t="Anzahl Zugänge aus Vereinen der (2.)Bundesliga, 10/11-20/21",x=0.5, y=1.01,va="center", fontweight ="bold", fontsize=16, c=textColor)
    # ax = fig.add_axes([0,0.95,0.75,0.15]) # badge
    # ax.axis("off")


plot_waffle_anzahl_buli_zugaenge()
