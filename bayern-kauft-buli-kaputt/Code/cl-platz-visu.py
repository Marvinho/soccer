import matplotlib as mpl 
import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from PIL import Image
import numpy as np

abs_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/buli-logos/"

title_font = "Alegreya Sans"
body_font = "Open Sans"
textColor = "w"
background = "#212529"
filler = "lightgrey"

mpl.rcParams['xtick.color'] = textColor
mpl.rcParams['ytick.color'] = textColor
mpl.rcParams['xtick.labelsize'] = 10
mpl.rcParams['ytick.labelsize'] = 10

def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.15)

buliTabPlaetze = {
"fcb": [1,1,1,1,1,1,1,1,1,2,3],
"bvb" : [5,2,2,4,3,2,7,2,2,1,1],
"rbl" : [2,3,3,6,2,19,19,19,19,19,19],
"bmg" : [9,4,5,9,9,4,3,6,8,4,16],
"b04" : [6,5,4,5,12,3,4,4,3,5,2],
"hof" : [12,6,9,3,4,15,8,9,16,11,11],
"wob" : [3,7,6,16,16,8,2,5,11,8,15],
"s04" : [18,12,14,2,10,5,6,3,4,3,14],
"ffurt": [4,19,19,19,19,19,19,19,19,19,19],
"96": [19,19,19,19,19,19,19,19,19,19,4] }

imagePaths = ["fcb.png","bvb.png","rbl.png","wob.png","b04.png","hof.png","bmg.png","s04.png"]
plt.style.use('dark_background')
x = [0,1,2,3,4,5,6,7,8,9,10]
# plt.figure(dpi=1200)

fig, ax = plt.subplots(figsize = (16,8))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)

saisons = ["10/11", "11/12", "12/13", "13/14", "14/15", "15/16", "16/17", "17/18", "18/19", "19/20", "20/21"]
ax.set_ylim([0.5,4.5])
ax.set_ylim(ax.get_ylim()[::-1])
ax.set_xlim([-0.5,10.5])
ax.set_xlim(ax.get_xlim()[::-1])
# ax.plot(x,buliTabPlaetze["fcb"])

spines = ["top","right","bottom","left"]
for s in spines:
    if s in ["top","right","bottom","left"]:
        ax.spines[s].set_visible(False)
    else:
        ax.spines[s].set_color(textColor)

path = "../buli-logos/fcb2.png"
for keys, values in buliTabPlaetze.items():
    path = abs_path + keys+".png"
    for x0, y0 in zip(x, values):
        ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
        ax.add_artist(ab)

ax.tick_params(axis='both', which='major', labelsize=20)
ax.set_xlabel('Saison', fontsize=25)
ax.set_ylabel('Tabellenplatz', fontsize=25)
ax.set_title("Top 4 Bundesliga 10/11 - 20/21", fontsize=25)
plt.xticks(x,saisons[::-1])
plt.yticks(ticks=[1,2,3,4])
ax.tick_params(axis="both",which="both", bottom=False, left=False)

ax.scatter(9.6,3.8,s=100, c="w", marker="*")
fig.text(0.05, -0.01,"* in der Saison 10/11 hatte Deutschland nur 3 Champions League Startplätze",
        fontstyle="italic",fontsize=15, fontfamily=body_font, color=textColor)

fig.text(0.7, -0.01, "Stand 06.04.2021 / Created by Marvin Springer",
        fontstyle="italic",fontsize=12, fontfamily=body_font, color=textColor)
plt.tight_layout()
plt.show()