import read_doc as rd

datas = rd.collectDataFromTab(rd.readFile())
ret = rd.infoDict(datas)

maxWord = len("Count") + 1
spaces = ""
i = 0
while i < maxWord:
	spaces += ' '
	i+=1
strFeature = "" + spaces
strCount = "Count" + spaces[len("Count"):]
strMean = "Mean" + spaces[len("Mean"):]
strStd = "Std" + spaces[len("Std"):]
strMin = "Min" + spaces[len("Min"):]
str25 = "25%" + spaces[len("25%"):]
str50 = "50%" + spaces[len("50%"):]
str75 = "75%" + spaces[len("75%"):]
strMax = "Max" + spaces[len("Max"):]
test = 0
for cle, value in ret.items():
	maxWord = len(cle) + 1
	spaces = ""
	i = 0
	while i < maxWord:
		spaces += ' '
		i+=1
	test += 1
	strFeature += ' ' + cle
	strCount += spaces[len(str(value["count"])):] + str(value["count"])
	strMean += spaces[len(str(value["mean"])[:(maxWord - 1)]):] + str(value["mean"])[:(maxWord - 1)]
	strStd += spaces[len(str(value["std"])[:(maxWord - 1)]):] + str(value["std"])[:(maxWord - 1)]
	strMin += spaces[len(str(value["min"])[:(maxWord - 1)]):] + str(value["min"])[:(maxWord - 1)]
	str25 += spaces[len(str(value["25%"])[:(maxWord - 1)]):] + str(value["25%"])[:(maxWord - 1)]
	str50 += spaces[len(str(value["50%"])[:(maxWord - 1)]):] + str(value["50%"])[:(maxWord - 1)]
	str75 += spaces[len(str(value["75%"])[:(maxWord - 1)]):] + str(value["75%"])[:(maxWord - 1)]
	strMax += spaces[len(str(value["max"])[:(maxWord - 1)]):] + str(value["max"])[:(maxWord - 1)]

print(strFeature)
print(strCount)
print(strMean)
print(strStd)
print(strMin)
print(str25)
print(str50)
print(str75)
print(strMax)