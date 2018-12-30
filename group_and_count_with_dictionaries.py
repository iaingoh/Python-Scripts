names = [
	'mark',
	'henry',
	'matthew',
	'paul',
	'luke',
	'robert',
	'joseph',
	'carl',
	'michael'
]

d = {}

for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)

print(d)

# 1) Loop through the list of names
# 2) Set the variable key to the length of the name
# 3) If the length of that particular name being looped through at the moment does not already exist, set the value of that key to an empty list.
# 4) Append that name to the key
# 5) Continue on to the next name on the list(implicit in the loop; first line)

####################################
from collections import defaultdict

names = [
	'mark',
	'john',
	'mark',
	'fred',
	'paul',
	'john'
	]


d = defaultdict(int)
for name in names:
	d[name] += 1

print(d)

# defaultdict uses a default if it doesn't find the key, in this case we have it using int that means it will call int without passing any value to it.
# The first time d[name] += 1 is called it will add one to zero.

########################################
from collections import Counter

names = ["mark", "john", "mark", "fred", "paul", "john"]

d = Counter(names)

print(d)
print(dict(d))


