# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 19:32:08 2021

@author: Marvin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
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