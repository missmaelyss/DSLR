import read_doc as rd
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

globalInfo = rd.collectGoodDataFromTab(rd.readFile())

dico = {}

for feature in globalInfo[6:]:
	dico[feature[0]] = []
	for value in feature[1:]:
		dico[feature[0]].append(float(value))

color = {
		'Gryffindor': 'red',
		'Slytherin': 'green',
		'Ravenclaw': 'blue',
		'Hufflepuff': '#EBEB11'
	}

dico['Houses'] = globalInfo[1][1:]

df = pd.DataFrame(dico)
sns.set(font_scale=0.8)
sns.pairplot(df, hue="Houses", palette=color, plot_kws={"s": 7})
plt.show()