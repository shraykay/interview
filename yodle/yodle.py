import sys
f = open('yodle.txt')
pos = 0
sums = []
othersum = 0

for line in f.readlines():
	line = line.strip()
	nums = line.split()
	
	if len(nums) == 1:
		sums.append(int(nums[pos]))
		othersum += int(nums[pos])
		continue
		
	left, right = int(nums[pos]), int(nums[pos+1])

	
	if right >= left:
		sums.append(right)
		pos += 1
	else:
		sums.append(left)
		
	othersum += max(left,right)
	print pos
	
	#for x in range(len(nums)):
	#	if x == pos:
	#		print('*%s*') % (nums[x]),
	#	else:
	#		print(nums[x]),
	#print ('')

print sums
print sum(sums)
print othersum