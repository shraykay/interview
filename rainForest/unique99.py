sample_data = [0, 1, 100, 99, 0, 10, 90, 30, 55, 33, 55, 75, 50, 51, 49, 50, 51, 49, 51]
sample_data.sort()

print sample_data
pairs = []

for x in range(0,len(sample_data)):
	for y in range(x,len(sample_data)):
		if sample_data[x] + sample_data[y] == 100:
			list = []
			reverse = []
			
			list.append(sample_data[x])
			list.append(sample_data[y])
			reverse.append(sample_data[y])
			reverse.append(sample_data[x])
			
			if list not in pairs and reverse not in pairs:
					pairs.append(list)
print pairs

