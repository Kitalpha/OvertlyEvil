import pandas as pd

emobank = pd.read_csv("C:/Users/Jordon/Documents/datathon/OvertlyEvil/EmoBank-master/corpus/emobank.csv", index_col=0)
for text in emobank['text']:
    print(str.split(text))