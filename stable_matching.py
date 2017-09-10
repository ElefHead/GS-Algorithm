from pprint import pprint
from random import sample
from copy import deepcopy

#Get inputs
with open("./pref_men.txt") as men:
	M = [(m, prefs.split(', ')) for [m,prefs] in (line.strip().split(': ') for line in men)]

with open("./pref_women.txt") as women:
	W = [(w,prefs.split(", ")) for [w,prefs] in (line.strip().split(": ") for line in women)]

#Preprocess
men = list(m[0] for m in M)
women = list(w[0] for w in W)

pref_men = dict([(men.index(m),[women.index(w) for w in prefs]) for (m,prefs) in M])
pref_women = dict([(women.index(w),[men.index(m) for m in prefs]) for (w,prefs) in W])

free_men = list(range(len(M)))
free_women = list(range(len(W)))

###
## Optional : All random preferences, comment all above code to run below code
###

# men = list(range(10))
# print(men)
# women = list(range(10))
# pref_men = dict((m,sample(range(0,len(men)),len(men))) for m in men)
# pref_women = dict((w, sample(range(0,len(women)),len(women))) for w in women)
# M = deepcopy([(k,v) for (k,v) in pref_men.items()])
# W = list(pref_women.items())
# free_men = list(men)
# free_women = list(women)

pairs = dict()

#GS Algorithm
while len(free_men) :
	man = free_men.pop(0)
	woman = pref_men[man].pop(0)
	if woman in free_women:
		pairs[woman] = man
		free_women.remove(woman)
	else :
		pref = pref_women[woman]
		current_man = pairs[woman]
		if pref.index(man)<pref.index(current_man):
			pairs[woman] = man
			free_men.append(current_man)
		else:
			free_men.append(man)

proper_pairs = [(men[m],women[w]) for (w,m) in pairs.items()]

average_mrank = 1.0*sum([M[m][1].index(women[w])+1 for (w,m) in pairs.items()])/len(M)
average_wrank = 1.0*sum([W[w][1].index(men[m])+1 for (w,m) in pairs.items()])/len(M)

#print result
pprint(proper_pairs)
pprint("Average MRank : %f" %average_mrank)
pprint("Average WRank : %f" %average_wrank)