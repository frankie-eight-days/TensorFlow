import csv

prices = []
train_x = []
train_y = []

def openCSV():
	with open('prices.csv', 'rt') as csvFile:
		reader = csv.reader(csvFile, delimiter=',', quotechar='|')

		for row in reader:
			if row[1] == 'NFLX':
				prices.append(row[3])

def makeTrainingData():
	sizeDataSet = 30
	for i in range(len(prices)-sizeDataSet):
		train_x.append([])

		for x in range(sizeDataSet):
			train_x[i].append(prices[i+x])
	
		if i != len(prices)-sizeDataSet-1:
			currentDay = prices[sizeDataSet + i]
			nextDay = prices[sizeDataSet+i+1]

		if nextDay >= currentDay:
			train_y.append([1, 0])
		else:
			train_y.append([0, 1])

	print(len(train_x), len(train_y))

	
openCSV()
makeTrainingData()