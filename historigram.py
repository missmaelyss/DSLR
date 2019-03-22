import read_doc as rd
import matplotlib.pyplot as plt
from math import *

Slytherin, Ravenclaw, Hufflepuff, Gryffindor = rd.createTab(rd.readFile())

SlytherinDatas = rd.collectDataFromTab(Slytherin)
RavenclawDatas = rd.collectDataFromTab(Ravenclaw)
HufflepuffDatas = rd.collectDataFromTab(Hufflepuff)
GryffindorDatas = rd.collectDataFromTab(Gryffindor)

for histogramme in ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']:
	plt.subplots(figsize=(35, 12))
	plt.suptitle("Quel cours de Poudlard a une repartition des notes homogenes entre les quatres maisons ?")
	plt.title(histogramme)
	plt.ylabel("Nombre d'eleve")
	plt.xlabel("Note")
	g = []
	for feature in GryffindorDatas:
		if feature[0] == histogramme:
			for grade in feature[1:]:
				try:
					float(grade)
				except:
					pass
				else:
					g.append(float(grade))

	h = []
	for feature in HufflepuffDatas:
		if feature[0] == histogramme:
			for grade in feature[1:]:
				try:
					float(grade)
				except:
					pass
				else:
					h.append(float(grade))

	r = []
	for feature in RavenclawDatas:
		if feature[0] == histogramme:
			for grade in feature[1:]:
				try:
					float(grade)
				except:
					pass
				else:
					r.append(float(grade))

	s = []
	for feature in SlytherinDatas:
		if feature[0] == histogramme:
			for grade in feature[1:]:
				try:
					float(grade)
				except:
					pass
				else:
					s.append(float(grade))

	num_bins = 20
	plt.hist([g,s,h,r], num_bins,color=['red', 'green', 'yellow', 'blue'], alpha = 0.7, histtype = 'barstacked', label = ['Gryffindor', 'Slytherin', 'Hufflepuff', 'Ravenclaw'])
	plt.legend()
	plt.show()