import sys
from math import *

def readFile():
	args = []
	
	for arg in sys.argv[1:]:
		args.append(arg)
	
	try:
		file = open(args[0], "r")
		file = file.read()
		file = file.split('\n')
	
	except:
		print('Error')
		exit()
	
	else:
		tab = []
		lenline = -1
	
		for line in file:
			if line == '' :
				del line
			else:
				line = line.split(',')
				if lenline != -1 and len(line) != lenline:
					print('Error:\tBad number of data in line:\t', line)
					exit()
				else:
					tab.append(line)
					lenline = len(line)
	
		return tab

def createTab(tab):
	Slytherin = [['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']]
	Ravenclaw = [['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']]
	Hufflepuff = [['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']]
	Gryffindor = [['Index', 'Hogwarts House', 'First Name', 'Last Name', 'Birthday', 'Best Hand', 'Arithmancy', 'Astronomy', 'Herbology', 'Defense Against the Dark Arts', 'Divination', 'Muggle Studies', 'Ancient Runes', 'History of Magic', 'Transfiguration', 'Potions', 'Care of Magical Creatures', 'Charms', 'Flying']]

	for line in tab:
		if line[1] == 'Slytherin':
			Slytherin.append(line)
		if line[1] == 'Ravenclaw':
			Ravenclaw.append(line)
		if line[1] == 'Hufflepuff':
			Hufflepuff.append(line)
		if line[1] == 'Gryffindor':
			Gryffindor.append(line)
	return Slytherin, Ravenclaw, Hufflepuff, Gryffindor

def collectDataFromTab(tab):
	
	datas = []

	i = 0
	for feature in tab[0]:
		datas.append([feature])
		i += 1
	
	for line in tab[1:]:
		i = 0
		for data in line:
			datas[i].append(data)
			i += 1
	return datas

def infoDict(datas):
	ret = {}

	i = 0
	for i in [0,6,7,8,9,10,11,12,13,14,15,16,17,18]:
		feature = datas[i]
		mean = 0
		digit = []
		for value in feature[1:]:
			try:
				mean += float(value)
				digit.append(float(value))
			except:
				pass
		size = len(digit)
		if size > 0:
			digit.sort()
			mean /= size
			if size % 2 == 0:
				info = {"count" : round(0.0 + size, 6), "mean" : round(mean, 6), "std" : 0.0, "min" : round(digit[0], 6), "25%" : round(digit[int(size / 4)] * (75.0/100) + digit[int(size / 4 - 1)] * (25.0/100),6), "50%" : round((digit[int(size / 2)] + digit[int(size / 2 - 1)]) / 2,6), "75%" : round(digit[int(size -size / 4)] * (25.0/100) + digit[int(size -size / 4 - 1)] * (75.0/100),6), "max" : round(digit[size - 1],6)}
			else:
				info = {"count" : round(0.0 + size, 6), "mean" : round(mean, 6), "std" : 0.0, "min" : round(digit[0], 6), "25%" : round(digit[int(size / 4)], 6), "50%" : round(digit[int(size / 2)], 6), "75%" : round(digit[int(size - size / 4)], 6), "max" : round(digit[size - 1], 6)}
			for value in digit:
				info["std"] += pow(value - info["mean"], 2)
			info["std"] = round(sqrt(info["std"] / size), 6)
			ret[feature[0]] = info
	return ret

def infoTab(tab):
	info = {}
	info["Arithmancy"] = 0 
	info["Astronomy"] = 0 
	info["Herbology"] = 0 
	info["Defense Against the Dark Arts"] = 0 
	info["Divination"] = 0
	info["Muggle Studies"] = 0
	info["Ancient Runes"] = 0
	info["History of Magic"] = 0
	info["Transfiguration"] = 0
	info["Potions"] = 0
	info["Care of Magical Creatures"] = 0
	info["Charms"] = 0
	info["Flying"] = 0
	i = 0
	for line in tab:
		n = 0
		for items in line:
			if items == '':
				line[n] = '0'
			n += 1
		try:
			info["Arithmancy"] += float(line[6])
			info["Astronomy"] += float(line[7])
			info["Herbology"] += float(line[8])
			info["Defense Against the Dark Arts"] += float(line[9])
			info["Divination"] += float(line[10])
			info["Muggle Studies"] += float(line[11])
			info["Ancient Runes"] += float(line[12])
			info["History of Magic"] += float(line[13])
			info["Transfiguration"] += float(line[14])
			info["Potions"] += float(line[15])
			info["Care of Magical Creatures"] += float(line[16])
			info["Charms"] += float(line[17])
			info["Flying"] += float(line[18])
			i += 1
		except:
			pass
	if i != 0:
		info["Arithmancy"] /= i
		info["Astronomy"] /= i
		info["Herbology"] /= i
		info["Defense Against the Dark Arts"] /= i
		info["Divination"] /= i
		info["Muggle Studies"] /= i
		info["Ancient Runes"] /= i
		info["History of Magic"] /= i
		info["Transfiguration"] /= i
		info["Potions"] /= i
		info["Care of Magical Creatures"] /= i
		info["Charms"] /= i
		info["Flying"] /= i
	return info