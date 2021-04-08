# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:10:02 2021

@author: Marvin
"""
import pandas as pd
import numpy as np
from pathlib import Path
import os

abs_path = "C:/Users/Marvin/Desktop/Portfolio/soccer/bayern-kauft-buli-kaputt/buli-cl-teams-zugaenge.csv"
# cwd = os.getcwd()
# file_path = (Path(cwd) / "../test.csv").resolve()
# print(cwd, file_path)

df = pd.read_csv(abs_path)

print(df)

def deal_with_vereinslos(df):
    if(df.isnull().values.any()):
        df["Aufnehmender-Verein"] = np.where(df["Abgebende-Liga"] == "-", df["Saison"], df["Aufnehmender-Verein"])
        df["Saison"] = np.where(df["Abgebende-Liga"] == "-", df["Ablöse"], df["Saison"])
        df["Ablöse"] = np.where(df["Abgebende-Liga"] == "-", "-", df["Ablöse"])
    else:
        print("Already dealt with clubless players")
    # df["Aufnehmender-Verein"].replace("-",df["Saison"],inplace=True)
    # df["Saison"]replace("-",df["Ablöse"],inplace=True)



def split_abloese_to_transferart(df):
    if("Transferart" not in df.columns):
        leih_condition = df["Ablöse"].str.contains("Leih")
        # print(leih_condition)
        intern_transfer_condition = df["Ablöse"] == "-"
        conditions = [leih_condition, intern_transfer_condition]
        choices = ["Leihe", "Interner Wechsel"]
        df["Transferart"] = np.select(conditions, choices, default="Transfer")
    else:
        print("Already splitted to transferart")



def format_abloese_to_int(df):
    if(df["Ablöse"].dtype != int):
        df["Leihkosten"] = df["Ablöse"]
        df["Leihkosten"] = np.where(df["Transferart"] != "Leihe", "-", df["Leihkosten"])
        # df["Ablöse"] = np.where(df["Transferart"] == "Leihe", 0, df["Ablöse"])
        mask = ((df["Transferart"] == "Leihe") |
                (df["Ablöse"] == "-") | 
                (df["Ablöse"] == "ablösefrei") |
                (df["Ablöse"] == "?"))
        df.loc[mask, "Ablöse"] = 0
        df["Ablöse"] = df["Ablöse"].str.replace(",","")
        df["Ablöse"] = df["Ablöse"].str.replace(" Mio. €","0000")
        df["Ablöse"] = df["Ablöse"].str.replace(" Tsd. €","000")
        df["Ablöse"].fillna(0, inplace=True)
        df["Ablöse"] = df["Ablöse"].astype(int)
    else:
        print("Already formatted the Ablöse")

def format_marktwert_to_int(df, column):
    if(df[column].dtype != int):
        df[column] = df[column].str.replace("-","0")
        df[column] = df[column].str.replace(",","")
        df[column] = df[column].str.replace(" Mio. €","0000")
        df[column] = df[column].str.replace(" Tsd. €","000")
        df[column].fillna(0, inplace=True)
        df[column] = df[column].astype(int)
    else:
        print("Already formatted the Marktwert")

def fix_bundesliga_öliga(df):
    if("Ö.Bundesliga" in df.loc["Abgebende-Liga"]):
        ö_liga_vereine = ["Sturm Graz", "LASK", "Grödig", "SCR Altach","Austria Wien",
                          "Rapid Wien", "SV Kapfenberg","RB Salzburg","SV Ried"]
        df.loc[df["Abgebender-Verein"].isin(ö_liga_vereine), "Abgebende-Liga"] = "Ö." + df.loc[df["Abgebender-Verein"].isin(ö_liga_vereine), "Abgebende-Liga"]# == "Ö. Bundesliga"
    else:
        print("Already fixed to Ö.Liga")

# bundesliga_vereine = df.loc[df["Abgebende-Liga"] == "Bundesliga"]["Abgebender-Verein"].unique()
# zweite_liga_vereine = df.loc[df["Abgebende-Liga"] == "2. Bundesliga"]["Abgebender-Verein"].unique()


if __name__ == "__main__":
    deal_with_vereinslos(df)  
    split_abloese_to_transferart(df) 
    format_abloese_to_int(df)
    format_marktwert_to_int(df, "Marktwert")
    fix_bundesliga_öliga(df)

# df.to_csv(abs_path)
