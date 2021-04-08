# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:01:54 2021

@author: Marvin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

abs_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/bayern-kauft-buli-kaputt/buli-cl-teams-zugaenge.csv"

df = pd.read_csv(abs_path)

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

asdf = de_zugaenge.sort_values("Ablöse")

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
anz1 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "Bundesliga", "Unnamed: 0"].tolist()
anz2 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "2. Bundesliga", "Unnamed: 0"].tolist()
team_list = [team_dict[i] for i in anz]
def anzahl_zugaenge_buli(df):
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    ax.grid(axis="y", ls="dotted",lw="0.5",color="lightgrey",zorder=1)
    
    ax.bar(x=team_list, height=anz1, label='Bundesliga',zorder=2)
    ax.bar(x=team_list, height=anz2, bottom=anz1, label='2.Bundesliga',zorder=2)
    # ax.scatter(x, y, s=120, color=filler, edgecolors=background, alpha=0.3, lw=0.5, zorder=2)           
    
    ax.set_xlabel("Vereine", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    ax.set_ylabel("Anzahl Spieler", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    
    # ax.tick_params(axis="both",length=3)
    
    # ax_ranges = [0, 65000000]
    # ax.set_xlim(ax_ranges)
    # ax.set_ylim(ax_ranges)
    # ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=textColor)
    # ax.set_ylim(ax.get_ylim()[::-1])
    
    # xlabels = ['{:,.0f}'.format(x) + ' Mio.' for x in ax.get_xticks()/1000000]
    # ax.set_xticklabels(xlabels)
    # ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_xticks()/1000000]
    # ax.set_yticklabels(ylabels)
    ax.legend()
    ax = plt.gca()
    
    
    spines = ["top","right","bottom","left"]
    for s in spines:
        if s in ["top","right"]:
            ax.spines[s].set_visible(False)
        else:
            ax.spines[s].set_color(textColor)
    
    # for i,name in enumerate(labels):
    #     t = ax.text(x[i],y[i]-1000000,labels[i],color=textColor,fontsize=12, ha="center", fontfamily=body_font)
        
    ax.set_title("Zugänge von Spielern aus Vereinen der Bundesliga/2.Bundesliga", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.7, -0.01, "Stand 06.04.2021 / Created by Marvin Springer",
        fontstyle="italic",fontsize=8, fontfamily=body_font, color=textColor)

    plt.tight_layout()
    plt.show()
anzahl_zugaenge_buli(anzahl_zugaenge)

def make_scatter_plot(x, y, labels):
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    

    
    ax.grid(ls="dotted",lw="0.5",color="lightgrey", zorder=1)
    ax.scatter(x, y, s=120, color=filler, edgecolors=background, alpha=0.3, lw=0.5, zorder=2)           
    
    ax.set_xlabel("Marktwert (in €)", fontfamily=title_font, fontweight="bold", fontsize=16, color=textColor)
    ax.set_ylabel("Ablöse (in €)", fontfamily=title_font, fontweight="bold", fontsize= 16, color=textColor)
    
    ax.tick_params(axis="both",length=3)
    
    ax_ranges = [0, 65000000]
    ax.set_xlim(ax_ranges)
    ax.set_ylim(ax_ranges)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=textColor)
    ax.set_ylim(ax.get_ylim()[::-1])
    
    # xlabels = ['{:,.0f}'.format(x) + ' Mio.' for x in ax.get_xticks()/1000000]
    # ax.set_xticklabels(xlabels)
    # ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_xticks()/1000000]
    # ax.set_yticklabels(ylabels)
    
    ax = plt.gca()
    
    
    spines = ["top","right","bottom","left"]
    for s in spines:
        if s in ["top","right"]:
            ax.spines[s].set_visible(False)
        else:
            ax.spines[s].set_color(textColor)
    
    for i,name in enumerate(labels):
        t = ax.text(x[i],y[i]-1000000,labels[i],color=textColor,fontsize=12, ha="center", fontfamily=body_font)
        
    fig.text(0.13,1.02,"Überschrift", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.05, -0.025, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=9, fontfamily=body_font, color=textColor)

    plt.tight_layout()
    plt.show()

#marktwert-ablöse-vereine
x_de = sum_marktwert_ablöse_zugaenge_de["Marktwert"].tolist()
y_de = sum_marktwert_ablöse_zugaenge_de["Ablöse"].tolist()
names_de = sum_marktwert_ablöse_zugaenge_de.index.tolist()
make_scatter_plot(x_de, y_de, names_de)

#marktwert-ablöse-spieler
x_player = de_zugaenge["Marktwert"].tolist()
y_player = de_zugaenge["Ablöse"].tolist()
names_player = de_zugaenge["Name"].tolist()
make_scatter_plot(x_player, y_player, names_player)

