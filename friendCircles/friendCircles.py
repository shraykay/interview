def friendCircles(friends):
	newFriends = []
	
	for x in range(len(friends)):
		newFriends.append(friends[x].replace("Y", "Y ").replace("N", "N ").strip())
	
	totaldict = {}
	nums = 0
	
	for x in newFriends:
		linedict = []
		count = 0
		for y in x.split():
			if y == "Y":
				linedict.append(count)
			count += 1
		totaldict[nums] = linedict
		nums += 1

	for x in range(0,len(totaldict)):
		for y in range(0, len(totaldict)):
			if set(totaldict[x]).intersection(totaldict[y]):
				totaldict[y] = set(totaldict[y]).union(totaldict[x])

	final = []
	
	for x in totaldict.values():
		if list(x) not in final:
			final.append(list(x))
	
	return len(final)

_friends_cnt = int(raw_input())
_friends_i=0
_friends = []
while _friends_i < _friends_cnt:
    _friends_item = raw_input()
    _friends.append(_friends_item)
    _friends_i+=1
    
res = friendCircles(_friends);
print str(res)

