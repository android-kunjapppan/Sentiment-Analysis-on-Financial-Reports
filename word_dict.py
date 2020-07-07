import pandas as pd
import json

stop_words = open("StopWords_Generic.txt", "r")
stop_words = stop_words.read().lower()
stop_words = stop_words.split("\n")

df0 = pd.read_csv("LoughranMcDonald_MasterDictionary_2018.csv")
df1 = pd.read_excel("constraining_dictionary.xlsx")
df2 = pd.read_excel("uncertainty_dictionary.xlsx")

word_dict = {}
word_dict["positive_words"] = []
word_dict["negative_words"] = []
word_dict["uncertainty_words"] = []
word_dict["constraining_words"] = []

for i in range(0, len(df0["Word"])):
    if df0["Word"][i] not in stop_words:
        if df0["Positive"][i] > 0:
            word_dict["positive_words"].append(df0["Word"][i].lower())
        elif df0["Negative"][i] > 0:
            word_dict["negative_words"].append(df0["Word"][i].lower())

for i in range(0, len(df1["Word"])):
    word_dict["constraining_words"].append(df1["Word"][i].lower())

for i in range(0, len(df2["Word"])):
    word_dict["uncertainty_words"].append(df2["Word"][i].lower())
    
with open("word_dict.json", "w+") as fp:
    json.dump(word_dict, fp)