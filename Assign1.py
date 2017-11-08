import math
def karatsuba (x,y):
	# convert to array
	x = map(int, str(x))
	y = map(int, str(y))

	if (len(x) == 1) and (len(y) == 1):
		x = int(''.join(map(str, x))) #convert the list to number
		y = int(''.join(map(str, y)))
		print("both are single digit number")
		final = x * y
	else:
		#check the number of digits of x and y
		if (len(x) == len(y)):
			if len(x) % 2 != 0: #if both are odd digit nubmers
				x.insert(0,0)
				y.insert(0,0)
		elif (len(x) > len(y)):
			if len(x) % 2 == 0: # e.g. 1234 123
				y.insert(0,0) # 1234 0123
			else: # e.g. x = 123  y = 12
				x.insert(0,0)
				y.insert(0,0)
				y.insert(0,0)
		else:
			if len(y) % 2 == 0: # e.g. 1234 123
				x.insert(0,0) # 1234 0123
			else: # e.g. y = 123  x = 12
				y.insert(0,0)
				x.insert(0,0)
				x.insert(0,0)

		a = x[:len(x)/2]
		b = x[len(x)/2:]
		c = y[:len(y)/2]
		d = y[len(y)/2:]
		
		a = int(''.join(map(str, a)))
		b = int(''.join(map(str, b)))
		c = int(''.join(map(str, c)))
		d = int(''.join(map(str, d)))
		# print ("a is " + str(a))
		# print ("b is " + str(b))
		# print ("c is " + str(c))
		# print ("d is " + str(d))
		final = pow(10,len(x))*karatsuba(a,c) + pow(10,len(x)/2)* (karatsuba(a,d) + karatsuba(b,c)) + karatsuba(b,d)
	# print ("x*y is " + str(final))
	return final

try: # get input from the command line
	x = int(raw_input('1st number:')) 
except ValueError: 
	print "Not a number array"

try: # get input from the command line
	y = int(raw_input('2nd number:')) 
except ValueError: 
	print "Not a number array"

karatsuba(x,y)