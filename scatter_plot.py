import read_doc as rd
import matplotlib.pyplot as plt
from math import *

globalInfo = rd.collectDataFromTab(rd.readFile())

for x in ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']:
	xTab = []
	for feature in globalInfo:
		if feature[0] == x:
			for grade in feature[1:]:
				try:
					float(grade)
				except:
					xTab.append('NaN')
				else:
					xTab.append(float(grade))
	for y in ['Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']:
		if y == x:
			pass
		else:
			yTab = []
			for feature in globalInfo:
				if feature[0] == y:
					for grade in feature[1:]:
						try:
							float(grade)
						except:
							yTab.append('NaN')
						else:
							yTab.append(float(grade))

			if len(xTab) < len(yTab):
				yTab = yTab[:len(xTab)]
			elif len(xTab) > len(yTab):
				xTab = xTab[:len(yTab)]

			astronomy = xTab
			defense = yTab

			plt.scatter(astronomy, defense, s=0.5)

			plt.suptitle("Quelles sont les deux features qui sont semblables ?")
			plt.title(x + " et " + y)
			plt.xlabel(x)
			plt.ylabel(y)
			plt.show()