# -*- coding: utf-8 -*-
"""Project 2 - PYBTCMP-1 / a2b2hny.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AzpGYUr3cvHXu4TWvqgFgVxTP7EuD3L-

PROJECT II

TEAM: PYBTCMP-1

SUBTEAM: a2b2hny
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("NetflixOriginals.csv", encoding='latin-1')

"""mission1 = Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız."""

mission1 = data[data["Runtime"] > 90] # 90 dakika üzerindeki filmler uzun soluklu film olarak tanımlanmıştır.
plt.bar(mission1["Language"], mission1["Runtime"], color = "brown")
plt.title("Long-Running Movies by Language")
plt.xticks(rotation = 90)
plt.show()

"""mission2 = 2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz."""

data["Premiere"] = pd.to_datetime(data["Premiere"])
data["Premiere"] = pd.to_datetime(data["Premiere"], format="%Y-%m-%d")
filtered_date = data.loc[(data["Premiere"] > "2019-01-01") & (data["Premiere"] < "2020-06-30")]
mission2 = filtered_date[filtered_date.Genre == "Documentary"]
new_date = pd.to_datetime(filtered_date["Premiere"], format = "%Y-%m")

plt.bar(new_date, filtered_date["IMDB Score"], color = "purple")
plt.xticks(rotation = 90)
plt.title("IMDB Scores of Documentary Movies by the year of 2019/01/01 - 2020/06/30")
plt.show()

"""mission3 = İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?"""

mission3 = data[data.Language == "English"].sort_values(by = ["IMDB Score"], ascending = False).head(1)
result = mission3[["Genre", "Language", "IMDB Score"]]
print(result)

"""mission4 = 'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?"""

mission4 = data[data.Language == "Hindi"]
mission4["Runtime"].mean()

"""mission5 = 'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz."""

def categories_of_genre(df):
    df = df.groupby(('Genre')).count()
    df = df.iloc[:, 1]
    plot = df.plot.pie(y='genres', figsize=(25, 25), rotatelabels = True)
    print(df)
    plt.show()

categories_of_genre(df=data)

"""mission6 = Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz."""

mission6 = data["Language"].value_counts().head(3)
mission6

"""mission7 = IMDB puanı en yüksek olan ilk 10 film hangileridir?"""

mission7 = data.sort_values(by = ["IMDB Score"], ascending = False).head(10)
result = pd.DataFrame(mission7[["Title", "IMDB Score"]])
result

"""mission8 = IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz."""

data["Runtime"].corr(data["IMDB Score"])
sns.heatmap(data.corr(), annot= True, linewidth=.5, fmt=".2f")

# There is strong negative correlation between IMDB Score and Runtime.

"""mission9 = IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz."""

DF = data.sort_values(by=["IMDB Score"], ascending=False)
first = DF[["Genre", "IMDB Score"]].drop_duplicates(["Genre"]).head(10)

plt.plot(first["Genre"], first["IMDB Score"], color = "aqua")
plt.title("First 10 Genres - Line Plot")
plt.xticks(rotation=90)
plt.show()

"""mission10 = 'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz."""

mission10 = data.sort_values(by = ["Runtime"], ascending = False).head(10)
mission10

plt.bar(mission10["Title"], mission10["Runtime"], color = "orange")
plt.xticks(rotation = 90)
plt.title("Top 10 Movies with Highest Runtime")
plt.show()

"""mission11 = Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz."""

data["Premiere"] = pd.to_datetime(data["Premiere"])
data["Premiere"] = pd.to_datetime(data["Premiere"], format="%Y-%m-%d")
year = data["Premiere"].dt.to_period("Y")
x = data.groupby(year).count()
y = x["Title"].values.tolist()
explode = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.3, 0.0)
plt.pie(y, labels = x.index, explode = explode, startangle = 90, radius = 2, rotatelabels = True)
plt.show()

"""mission12 = Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz."""

x = pd.DataFrame(data["IMDB Score"].groupby(data["Language"]).mean())
plt.plot(x)
plt.xticks(rotation = 90)
plt.grid()
plt.title("Movies by Language & Lowest IMDB Score")
plt.show()

"""mission13 = Hangi yılın toplam "runtime" süresi en fazladır?"""

data["Premiere"] = pd.to_datetime(data["Premiere"])
year = data["Premiere"].dt.to_period("Y")
x = pd.DataFrame(data["Runtime"].groupby(year).sum())
x.sort_values(by = ["Runtime"], ascending = False).head(1)

"""mission14 = Her bir dilin en fazla kullanıldığı "Genre" nedir?"""

mission14 = data.groupby("Language")["Genre"].max()
pd.DataFrame(mission14)

"""mission15 = Veri setinde outlier veri var mıdır? Açıklayınız."""

table = data["Runtime"].copy()
sns.boxplot(x = table)

table2 = data["IMDB Score"].copy()
sns.boxplot(x = table2)