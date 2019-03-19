import read_doc as rd
import matplotlib.pyplot as plt
from math import *

Slytherin, Ravenclaw, Hufflepuff, Gryffindor = rd.createTab(rd.readFile())

SlytherinDatas = rd.infoDict(rd.collectDataFromTab(Slytherin))
RavenclawDatas = rd.infoDict(rd.collectDataFromTab(Ravenclaw))
HufflepuffDatas = rd.infoDict(rd.collectDataFromTab(Hufflepuff))
GryffindorDatas = rd.infoDict(rd.collectDataFromTab(Gryffindor))

# print(SlytherinDatas)
# print(RavenclawDatas)
# print(HufflepuffDatas)
# print(GryffindorDatas)

std = []
feature = []

for cle, data in SlytherinDatas.items():
	print(cle, data["std"])
	if cle == 'Index':
		pass
	else:
		feature.append(cle)
		std.append(data["std"])

x = range(len(std))

plt.subplots(figsize=(35, 12))

plt.title('Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?', 
  loc='center', 
  fontsize=16)

plt.bar(x, std, color='green', alpha=0.2)

std = []
feature = []

for cle, data in RavenclawDatas.items():
	print(cle, data["std"])
	if cle == 'Index':
		pass
	else:
		feature.append(cle)
		std.append(data["std"])


plt.bar(x, std, color='blue', alpha=0.2)

std = []
feature = []

for cle, data in HufflepuffDatas.items():
	print(cle, data["std"])
	if cle == 'Index':
		pass
	else:
		feature.append(cle)
		std.append(data["std"])


plt.bar(x, std, color='yellow', alpha=0.2)

std = []
feature = []

for cle, data in GryffindorDatas.items():
	print(cle, data["std"])
	if cle == 'Index':
		pass
	else:
		feature.append(cle)
		std.append(data["std"])


plt.bar(x, std, color='red', alpha=0.2)

plt.xticks(x, (feature), fontsize = 8)
plt.yticks(fontsize = 8)

plt.ylabel('std')
plt.xlabel('Cours')

plt.show()
