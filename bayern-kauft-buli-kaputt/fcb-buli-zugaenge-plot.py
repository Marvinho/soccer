import pandas as pd
import matplotlib as mpl 
import matplotlib.pyplot as plt
import numpy as np

from PIL import Image

df = pd.read_csv("bayern-zugang.csv")


df_buli = df[df["Liga"] == "Bundesliga"]
df_buli_transfers = df_buli[df_buli["Transfer-Art"]=="Transfer"]
df_buli_transfers = pd.read_csv("fcb-buli-transfer-zugaenge.csv")

x = df_buli_transfers["Marktwert"].tolist()
y = df_buli_transfers["Ablöse"].tolist()
names = df_buli_transfers["Name"].tolist()


ax_ranges = [-1000000, 61000000]
team = "FC Bayern München"

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


fig, ax = plt.subplots(figsize=(8,8))
fig.set_facecolor(background)
ax.patch.set_facecolor(background)
ax.grid(ls="dotted",lw="0.5",color="lightgrey", zorder=1)

ax.scatter(x, y, s=120, color=filler, edgecolors=background, alpha=0.3, lw=0.5, zorder=2)


for i in [0,1,3,4,5,6,8,9,11,13,19,20]:
    t = ax.text(x[i],y[i]-1000000,names[i],color=textColor,fontsize=12, ha="center", fontfamily=body_font)


fig.text(0.13,1.02,"{}s Bundesliga Zugänge von 10/11 - 21/22".format(team), fontsize=14, fontweight="bold", color = textColor)        


ax.set_xlabel("Marktwert (in €)", fontfamily=title_font, fontweight="bold", fontsize=16, color=textColor)
ax.set_ylabel("Ablöse (in €)", fontfamily=title_font, fontweight="bold", fontsize= 16, color=textColor)

ax.tick_params(axis="both",length=0)

xlabels = ['{:,.0f}'.format(x) + ' Mio.' for x in ax.get_xticks()/1000000]
ax.set_xticklabels(xlabels)
ylabels = ['{:,.0f}'.format(y) + ' Mio.' for y in ax.get_xticks()/1000000]
ax.set_yticklabels(ylabels)

ax = plt.gca()

ax.set_xlim(ax_ranges)
ax.set_ylim(ax_ranges)
ax.plot(ax.get_xlim(), ax.get_ylim(), ls="--", c=textColor)
ax.set_ylim(ax.get_ylim()[::-1])

spines = ["top","right","bottom","left"]
for s in spines:
    if s in ["top","right"]:
        ax.spines[s].set_visible(False)
    else:
        ax.spines[s].set_color(textColor)

ax2 = fig.add_axes([0,0.95,0.15,0.15]) # badge
ax2.axis("off")
img = Image.open("FC-Bayern-Munchen-Logo.png")
ax2.imshow(img)

fig.text(0.05, -0.025, "Created by Marvin Springer / Data by transfermarkt.de",
        fontstyle="italic",fontsize=9, fontfamily=body_font, color=textColor)

plt.tight_layout()
plt.show()