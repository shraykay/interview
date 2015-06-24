n = int(raw_input())
nums = raw_input()

numdict = []
subtracted = []
count = {}

for x in nums.split():
	numdict.append(int(x))

for x in range(1,n):
	if (numdict[x] - numdict[x-1]) in count:
		count[numdict[x] - numdict[x-1]] += 1
	else:
		count[numdict[x] - numdict[x-1]] = 1

print count
