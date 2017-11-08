count = 0
def mergeSort(array_input):
	n = len(array_input)
	global count 

	if n > 1:
		front = array_input[:n/2]
		back = array_input[n/2:]

		front = mergeSort(front)
		back = mergeSort(back)


		merge = [0]*n
		#print ("front is " + str(front))
		#print ("back is " + str(back))
		i = 0
		j = 0
		k = 0
		#print ("front[" + str(i) + "] is " + str(front[i]) )
		#print ("back[" + str(j) + "] is " + str(back[j]) )

		# when both parts have not finished
		while i < len(front) and j < len(back):
			if front[i] < back[j]:
				merge[k] = front[i]
				i = i + 1
			else:
				merge[k] = back[j]
				j = j + 1
				# Add the number of inversion 
				count = count + (len(front) - i)
			k = k + 1

		# when the front part finished
		while j < len(back):
			merge[k] = back[j]
			j = j + 1
			k = k + 1

		# when the back part finished
		while i < len(front):
			merge[k] = front[i]
			i = i + 1
			k = k + 1
		print merge
		return merge

	else: # only one element left then just return it
		return array_input




# try: # get input from the command line
# 	raw_input = int(raw_input('Input Array:')) 
# except ValueError: 
# 	print "Not a number array"

# fname = 'W2_test.txt'
fname = 'Assign2_test.txt'

with open(fname) as f:
    content = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
alist = [x.strip() for x in content] 
# print alist

# convert to array
array_input = map(int, alist)
print array_input
mergeSort(array_input)
print count


