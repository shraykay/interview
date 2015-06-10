n = int(raw_input())
nums = raw_input()

numdict = []
subtracted = []

for x in nums.split():
	numdict.append(int(x))

for x in range(1,n):
	subtracted.append(numdict[x]-numdict[x-1])

print subtracted

biggest = subtracted[0]
position = 0

for x in range(0,len(subtracted)):
	if subtracted[x] > biggest:
		position = x
		biggest = subtracted[x]

print biggest, position
