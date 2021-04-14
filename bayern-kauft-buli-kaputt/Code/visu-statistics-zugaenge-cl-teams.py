# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:01:54 2021

@author: Marvin
"""
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from highlight_text import HighlightText, ax_text, fig_text
print(mpl.__version__)
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
anz1 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "Bundesliga", "Unnamed: 0"].tolist()
anz2 = anzahl_zugaenge.loc[anzahl_zugaenge["Abgebende-Liga"] == "2. Bundesliga", "Unnamed: 0"].tolist()
team_list = [team_dict[i] for i in anz]

def plot_differenz_mw_abloese(df):
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    ax.grid(axis="y", ls="dotted",lw="0.5",color="lightgrey", zorder=1)
    colormap = ["#b3de69","#b3de69","#b3de69","#b3de69","#b3de69","#fa8174","#b3de69","#fa8174"]
    bars = ax.bar(x=asdf.index, height=asdf.tolist(), label='Bundesliga',color=colormap ,zorder=2)
    # ax.bar_label(bars,label_type="center", fmt='%.2f')
    ax.set_xlabel("Aufnehmender Verein", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    ax.set_ylabel("Markwert - Ablöse (in €)", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    xlabels = [team_dict[i] for i in anz]
    ax.set_xticklabels(xlabels)
    ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_yticks()/1000000]
    ax.set_yticklabels(ylabels)
    for x, y, j in zip(asdf.index, asdf.tolist(), team_list):
        path = img_base_path + j+".png"
        if(y > 0):
            ab = AnnotationBbox(OffsetImage(plt.imread(path),zoom=0.08), (x, y-7000000), frameon=False)
        #(zoom=0.15), (0.4,0.5), frameon=False)
        else:
            ab = AnnotationBbox(OffsetImage(plt.imread(path),zoom=0.08), (x, -6000000), frameon=False)
        ax.add_artist(ab)
    ax.set_title("Differenz Marktwert/Ablöse für Zugänge aus Vereinen \nder (2.) Bundesliga, 10/11 - 20/21", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.6, -0.01, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=8, fontfamily=body_font, color=textColor)
    plt.tight_layout()
    plt.show()
    
# plot_differenz_mw_abloese(asdf)    

def plot_marktwert_und_abloese(df):
    plt.style.use('dark_background')
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    ax.grid(axis="y", ls="dotted",lw="0.5",color="lightgrey", zorder=1)
    # colormap = ["#b3de69","#b3de69","#b3de69","#b3de69","#b3de69","#fa8174","#b3de69","#fa8174"]
    
    x = np.arange(8)
    width = 0.35
    bars1 = ax.bar(x-width/2, width=width, height=sum_marktwert_ablöse_zugaenge_de["Marktwert"].tolist(), color= '#482677', label='Bundesliga',zorder=2)
    bars2 = ax.bar(x+width/2, width=width, height=sum_marktwert_ablöse_zugaenge_de["Ablöse"].tolist(),color='#dce319', label='Bundesliga',zorder=2)

    ax.set_xlabel("Aufnehmender Verein", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    ax.set_ylabel("in €", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    # xlabels = [team_dict[i] for i in anz]
    team_list.insert(0, "new")
    ax.set_xticklabels(team_list)
    ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_yticks()/1000000]
    ax.set_yticklabels(ylabels)
    for i, j in enumerate(anz):
        path = img_base_path + j+".png"
        ab = AnnotationBbox(OffsetImage(plt.imread(path),zoom=0.08), (i, 20000000), frameon=False)
        ax.add_artist(ab)
        
    HighlightText(x=0.15, y=1.05,
              s="Gesamt <Marktwert> und <Ablöse> für Zugänge aus Vereinen \nder (2.) Bundesliga, 10/11 - 20/21",  fontsize=14, fontweight="bold",
              highlight_textprops=[{"color": '#482677'}, #['#8dd3c7', '#feffb3', '#bfbbd9', '#fa8174'
                                   {"color": '#dce319'}],
              annotationbbox_kw={'boxcoords': fig.transFigure})
    
    # ax.set_title("Gesamt Marktwert und Ablöse für Zugänge aus Vereinen \nder 1. Bundesliga und 2. Bundesliga, 10/11 - 20/21", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.6, -0.01, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=8, fontfamily=body_font, color=textColor)
    plt.tight_layout()
    plt.show()
plot_marktwert_und_abloese(df)


def anzahl_zugaenge_buli(df):
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    ax.grid(axis="y", ls="dotted",lw="0.5",color="lightgrey",zorder=1)
    
    ax.bar(x=team_list, height=anz1, label='Bundesliga',zorder=2)
    ax.bar(x=team_list, height=anz2, bottom=anz1, label='2.Bundesliga',zorder=2)
    # ax.scatter(x, y, s=120, color=filler, edgecolors=background, alpha=0.3, lw=0.5, zorder=2)           
    
    ax.set_xlabel("Aufnehmender Verein", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    ax.set_ylabel("Anzahl Spieler", fontfamily=title_font, fontweight="bold", fontsize=12, color=textColor)
    
    # ax.tick_params(axis="both",length=3)
        
    for x0,j in enumerate(team_list):
        path = img_base_path + j+".png"
        ab = AnnotationBbox(OffsetImage(plt.imread(path),zoom=0.1), (x0, 2), frameon=False)
        #(zoom=0.15), (0.4,0.5), frameon=False)
        ax.add_artist(ab)
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
        
    ax.set_title("Zugänge aus Vereinen der Bundesliga/2.Bundesliga 10/11 - 20/21", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.7, -0.01, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=8, fontfamily=body_font, color=textColor)

    plt.tight_layout()
    plt.show()
# anzahl_zugaenge_buli(anzahl_zugaenge)
# x_de = sum_marktwert_ablöse_zugaenge_de["Marktwert"].tolist()
# y_de = sum_marktwert_ablöse_zugaenge_de["Ablöse"].tolist()
# names_de = sum_marktwert_ablöse_zugaenge_de.index.tolist()

def scatter_plot_mw_abloese(x, y, labels):
    fig, ax = plt.subplots(figsize=(8,8))
    fig.set_facecolor(background)
    ax.patch.set_facecolor(background)
    

    
    ax.grid(ls="dotted",lw="0.5",color="lightgrey", zorder=1)
    ax.scatter(x, y, s=120, color=filler, edgecolors=background, alpha=0.3, lw=0.5, zorder=2)
    for x, y, j in zip(x, y, team_list):
        path = img_base_path + j+".png"
        ab = AnnotationBbox(OffsetImage(plt.imread(path),zoom=0.05), (x, y), frameon=False)
        #(zoom=0.15), (0.4,0.5), frameon=False)
        ax.add_artist(ab)
        t = ax.text(x,y+20000000,j,color=textColor,fontsize=12, ha="center", fontfamily=body_font)
    
    ax.set_xlabel("Marktwert (in €)", fontfamily=title_font, fontweight="bold", fontsize=16, color=textColor)
    ax.set_ylabel("Ablöse (in €)", fontfamily=title_font, fontweight="bold", fontsize= 16, color=textColor)
    
    ax.tick_params(axis="both",length=3)
    
    ax_ranges = [0, 450000000]
    ax.set_xlim(ax_ranges)
    ax.set_ylim(ax_ranges)
    ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=textColor)
    ax.set_ylim(ax.get_ylim()[::-1])
    
    xlabels = ['{:,.0f}'.format(x) + ' Mio.' for x in ax.get_xticks()/1000000]
    ax.set_xticklabels(xlabels)
    ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_xticks()/1000000]
    ax.set_yticklabels(ylabels)
    
    ax = plt.gca()
    
    
    spines = ["top","right","bottom","left"]
    for s in spines:
        if s in ["top","right"]:
            ax.spines[s].set_visible(False)
        else:
            ax.spines[s].set_color(textColor)
        
    ax.set_title("Summierter Marktwert/Ablöse für Zugänge aus Vereinen \nder (2.) Bundesliga, 10/11 - 20/21", fontsize=14, fontweight="bold", color = textColor)
    fig.text(0.6, -0.01, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=8, fontfamily=body_font, color=textColor)

    plt.tight_layout()
    plt.show()

#marktwert-ablöse-vereine
# scatter_plot_mw_abloese(x_de, y_de, names_de)
# x = np.arange(10)
# y = np.arange(10)
# p = plt.plot(x,y,x,y+1,x,y+2, x,y+3, x,y+4, x,y+5, x,y+6,x,y+7) 
# for i in range(8):
#     print(p[i].get_color())
