# CH1 exercises

############# R 1.1 ################
'''

def is_multiple( n, m):
	if n%m == 0 :
		return True

	else : 
		return False

print(is_multiple(4,2))

'''
############# R 1.2 ####################
'''
def is_even(k):
	b = True
	while(b):
		k -= 2
		if k == 0:
			b = False
			return True
		if k < 0:
			b = False
			return b
print(is_even(5))
'''

############ R- 1.3 #######################

'''def minmax(data):
	min = data[0]
	max = data[0]
	for n in data:
		if min > n :
			min = n
		elif max < n:
			max = n
	return min,max

print(minmax([2,3,4,9,6,4,2,1,0]))'''

# R-1.4
'''
def sumsquare(n):
	sumsq = 0
	for x in range(n):
		sumsq += x**2

	return sumsq

print(sumsquare(5))
'''

# R-1.5
'''
def sumsquare(n):

	return sum(x**2 for x in range(n))

print(sumsquare(2))
'''
# R-1.6/1.7
'''
def sq_sum_odd(n):
	
	return sum(x**2 for x in range(1,n,2))

print(sq_sum_odd(6))
'''
# R-1.11

#  print([2**k for k in range(9)])

# R-1.12
'''

from random import randrange

def ch(data):
	return data[randrange(len(data))]

print(ch([1,2,3,4]))

'''

# c-1.13

# pseudo-code

'''

k = 1
rev_list = []
for x in list
	rev_list += list[len(list) - k]
	k ++

'''

# print([x for x in reversed([1,2,3,4,5,6,7])])


# C-1.14

'''def is_pr_odd(seq):
	k = 0
	for n in seq:
		if n%2 != 0:
			k+=1

	if k >= 2:
		return True
	else:
		return False

print(is_pr_odd([2,3,5]))
'''
# C-1.15
'''

def distinct(seq):
	k = 0
	for n in seq:
		for x in seq:
			if n==x :
				k +=1
	if k > len(seq):
		return False
	else:
		return True

print(distinct([1,8,5,4,8]))


'''
# C-1.18
'''
def incl():
	l = []
	k = 0
	for n in range(10):
		k += n*2
		l += [k]
		
	print(l)

incl()
'''

# C-1.19

'''print([chr(x) for x in range(97,123)])

print(ord('a'))'''

# C-1.20
'''
from random import randint
def shuffle(seq):
	# same as the shuffle func of random

	l = []

	while(len(seq) > 0 ):
		r = randint(0,len(seq)-1)
		l += [seq[r]]
		del seq[r]

	print(l)



seq = [1,2,3,4]
shuffle(seq)
'''
# C-1.23

'''c = []
try:
	c[3] = 3
except Exception:
	print("shu shu")'''

# C- 1.24
'''k = 0
string = "aeiousaeiousaueiousaeious"
for x in ['a','e','o','i','u']:
	for y in string:
		if x == y:
			k += 1

print(k)'''


# C-1.25
'''
string = "Hello, World!"
punc = [ '\'' , ';',',','.','\"', '!']
print([x for x in punc])  

for x in punc:
	string = string.replace(x,"")
print(string)
'''
# C - 1.26
'''
def valid(a, b, c):
	if a + b == c:
		return True
	elif a == b - c:
		return True
	elif a*b == c:
		return True
	else :
		return False

print(valid(2,2,4))
'''
# C- 1.29
'''
def norm( v,p=2):
	sum_sq = 0
	for Vi in v:
		sum_sq += Vi**p

	p_norm = sum_sq**(1/p)
	return p_norm

print(norm([3,4]))

'''

# P - 1.29

# all possible combinations of 
'''
l = [ 'c', 'a', 't', 'd', 'o', 'g']

n = len(l)
comb = []

for i in range(n):
	u = l[i:] + l[:i]
	for k in range( 1, n):
		o = [u[0]] + u[k:] + u[1:k]
		for j in range( 2, n):
			m = o[0:2] + o[j:] + o[2:j]
			for v in range(3, n):
				e = m[0:3] + m[v:] + m[2:v]
				for p in range(4, n):
					z = e[0:4] + e[p:] + e[2:p]
					s = ''
					for i in range(n):
						s += (z[i])
					comb += [s]


print(comb)
print(len(set(comb)))
'''



# C-1.30
# Write a Python program that can take a positive integer greater than 2 as
# input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.

'''def div(n):
	k = 0 
	while(n>=2):
		n /= 2
		k +=1

	return k
print(div(10))
'''
# P-1.36

def count_times(st, words):
	k = 0
	for s in words:
		if s == st:
			k += 1
	return k








def coun(s):
	words = s.split()
	set_word = set(words)

	count = {}

	for word in set_word:
		count[word] = count_times(word, words)

	return count

print(coun("a b c d e f e a c g c e d f aman aman agrawal agrawal"))
































