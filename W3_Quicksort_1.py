count = 0
quick_count = 0
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


def quickSort(array_input):
	global quick_count
	n = len(array_input)
	if n == 1 or n == 0:
		# print("single number " + str(array_input))
		return array_input
	else:
		quick_count = quick_count + n -1
		p = ChoosePivot(n, array_input) #return pivot index
		# print p
		# print ("pivot is " + str(array_input[p]))
		# print array_input
		array_input = swap(p, 0, array_input)
		# print array_input
		(out, index) = Partition_first(array_input,0, n, 0)
		# (out, index) =Partition_mid(array_input,0, n, p)
		# (out, index) =Partition_last(array_input,0, n, p)
		# print out
		# print ("firsthalf is " + str(out[0:index])) 
		firsthalf = quickSort(out[0:index])
		# print ("secondhalf is " + str(out[index+1:n]))
		secondhalf = quickSort(out[index+1:n])
		final = firsthalf + [out[index]] + secondhalf
		# print ("final is " + str(final))
		return final
		


def ChoosePivot(n, input):
	#first element's index
	#return 0 

	# final element's index
	# return n-1 

	# middle element's index
	if n%2 == 1:
		middle = n/2
	else:
		middle = n/2-1
	# print input[0]
	# print input[middle]
	# print input[-1]
	if input[0]< input[-1]< input[middle] or input[0]>input[-1]>input[middle]:
		return -1
	elif input[-1]< input[0]<input[middle] or input[-1]> input[0]>input[middle]:
		return 0
	else:
		return middle
	

def Partition_first (input, l, r, p_i):
	p = input[p_i]
	i = l+1
	j = l+1
	while j<r:
		if input[j] < p:
			input = swap(j, i, input)
			i = i+1
		j = j+1
	input = swap(l, i-1, input)
	return (input,i-1)

####### faster than the swap as required in the assignment
def Partition_last (input, l, r, p_i):
	global quick_count 
	quick_count = quick_count + r - 1
	p = input[p_i]
	i = l
	j = l
	while j<r-1:
		if input[j] < p:
			input = swap(j, i, input)
			i = i+1
		j = j+1
	input = swap(p_i, i, input)
	# return {'output':input,'p_i':(i-1)}
	return (input,i)

####### choose the middle number as pivot
def Partition_mid (input, l, r, p_i):
	p = input[p_i]
	i = l
	j = l
	while j<r-1:
		if j == p_i:
			j = j+1
		if input[j] < p:
			input = swap(j, i, input)
			i = i+1
			if i == p_i:
				i = i + 1
		j = j+1
	if i < p_i: #pivot at right of the wall 
		input = swap(p_i, i, input)
		return (input,i)
	else:
		input = swap(p_i, i-1, input)
		return (input,i-1)

def swap(a,b,array):
	temp = array[b]
	array[b] = array[a]
	array[a] = temp
	return array




######### get input from the command line
# try: 
# 	raw_input = int(raw_input('Input Array:')) 
# except ValueError: 
# 	print "Not a number array"


######### get input from a file
# fname = 'W2_test.txt'
# fname = 'list.txt'
fname = 'quicksort.txt'
with open(fname) as f:
    content = f.readlines()
# remove whitespace characters like `\n` at the end of each line
alist = [x.strip() for x in content] 

# convert to array
array_input = map(int, alist)
# print ("input array is " + str(array_input))
# mergeSort(array_input)
quickSort(array_input)
print quick_count
# print count



