# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 19:18:45 2021

@author: Marvin
"""
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

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


abs_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/buli-logos/"
imagePaths = ["fcb.png","bvb.png","rbl.png","wob.png","b04.png","hof.png","bmg.png","s04.png"]

plt.style.use('dark_background')
# x = [0,1,2,3,4,5,6,7,8,9,10]
# plt.figure(dpi=1200)

fig, ax = plt.subplots(figsize = (8,8))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)
spines = ["top","right","bottom","left"]
for s in spines:
    if s in ["top","right","bottom","left"]:
        ax.spines[s].set_visible(False)
    else:
        ax.spines[s].set_color(textColor)
team_coord_dict = {"fcb":(0.5,0.5),
             "bvb":(0.9,0.7),
             "wob":(0.9,0.4),
             "b04":(0.35,0.1),
             "bmg":(0.1,0.4),
             "hof":(0.5,0.9),
             "s04":(0.1,0.7),
             "rbl":(0.65,0.1)}        

def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.25)

for keys, values in team_coord_dict.items():
    path = abs_path+keys+".png"
    ab = AnnotationBbox(getImage(path), values, frameon=False)
    ax.add_artist(ab)

for keys, values in team_coord_dict.items():
    if(keys in ["b04"]):
        continue
    else:
        ax.arrow(values[0], values[1], (0.5-values[0])*0.8, (0.5-values[1])*0.8, head_width=0.05, 
                 head_length=0.075,color=textColor,length_includes_head=True)

ax.tick_params(axis='both', which='major', labelsize=20)
# ax.set_xlabel('Saison', fontsize=25)
# ax.set_ylabel('Tabellenplatz', fontsize=25)
# ax.set_title("Top 4 Bundesliga 10/11 - 20/21", fontsize=25)
# plt.xticks(x,saisons[::-1])
# plt.yticks(ticks=[1,2,3,4])
# ax.tick_params(axis="both",which="both", bottom=False, left=False)

# ax.scatter(9.6,3.8,s=100, c="w", marker="*")


# fig.text(0.7, -0.01, "Stand 06.04.2021 / Created by Marvin Springer",
#         fontstyle="italic",fontsize=12, fontfamily=body_font, color=textColor)
plt.tight_layout()
plt.show()
