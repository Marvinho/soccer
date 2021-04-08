# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 21:10:02 2021

@author: Marvin
"""
import pandas as pd
import numpy as np

df = pd.read_csv("buli-cl-teams-zugaenge.csv")

print(df)

def deal_with_vereinslos(df):
    # df["Aufnehmender-Verein"] = np.where(df["Abgebende-Liga"] == "-", df['col2'], df['col1'])
    # df["Aufnehmender-Verein"].replace(nan,)
    pass

def split_abloese_to_transferart(df):
    leih_condition = df["Ablöse"].str.contains("Leih")
    print(leih_condition)
    intern_transfer_condition = df["Ablöse"] == "-"
    conditions = [leih_condition, intern_transfer_condition]
    choices = ["Leihe", "Interner Wechsel"]
    df["Transferart"] = np.select(conditions, choices, default="Transfer")

# format_abloese(df)

def format_abloese_to_int(df):
    df["Leihkosten"] = df["Ablöse"]
    df.loc[df["Transferart"] != "Leihe", "Leihkosten"] = 0
    df.loc[df["Transferart"] == "Leihe", "Transferart"] = 0
    df.loc[df["Ablöse"] == "-", "Transferart"] = 0
    
    
