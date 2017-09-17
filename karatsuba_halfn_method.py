def karatsuba(x, y):

	# Copy values x and y into strings in order to compare lengths
	temp_x = str(x).strip()
	temp_y = str(y).strip()
	
	# Base Case: If x and y are both 1 digit numbers, simply multiply
	if len(temp_x) == 1 and len(temp_y) == 1:
		return x * y

	'''
		We compare the lengths of x and y. 
		Whichever length is greater, we use that variable to
		determine the number of digits in our b and d values for
		Karatsuba multplication. 

		When the split value is equal to the number of digits in
		the smaller of x and y, we set the left half of
		the smaller split to 0 and the right half equal
		to the original variable
	
		If the length of the larger number is odd, we round up
		by 1.
	'''
	elif len(temp_x) > len(temp_y):
		
		if len(temp_x) % 2 != 0:
			half_n = (len(temp_x) + 1) // 2
		else:
			half_n = len(temp_x) // 2

		# Ensuring the right half of each split has the same
		# number of digits
		a = int( str(x)[ : len(temp_x) - half_n] )
		b = int( str(x)[len(temp_x) - half_n : len(temp_x)] )

		# Python throws an invalid literal error, so we catch 
		# with a try/except parameter
		try:
			c = int( str(y)[ : len(temp_y) - half_n] ) 
			d = int( str(y)[len(temp_y) - half_n : len(temp_y)])
		except:
			c = 0
			d = y

	elif len(temp_x) < len(temp_y):

		if len(temp_y) % 2 != 0:
			half_n = (len(temp_y) + 1) // 2
		else:
			half_n = len(temp_y) // 2

		try:
			a = int( str(x)[ : len(temp_x) - half_n] )
			b = int( str(x)[len(temp_x) - half_n : len(temp_x)] )
		except:
			a = 0
			b = x

		print(half_n)
		c = int( str(y)[ : len(temp_y) - half_n] )
		d = int( str(y)[len(temp_y) - half_n : len(temp_y)] )

	else: 	

		half_n = len(temp_x) // 2
		a = int( str(x)[ : len(temp_x)//2] )
		b = int( str(x)[len(temp_x)//2 : len(temp_x)] )

		c = int( str(y)[ : len(temp_y)//2] )
		d = int( str(y)[len(temp_y)//2 : len(temp_y)] )

	part_1 = karatsuba(a, c)
	part_2 = karatsuba(b, d)
	part_3 = karatsuba((a+b),(c+d))
	part_4 = part_3 - part_1 - part_2
	
	product = 10**(half_n * 2)*part_1  +  10**(half_n)*(part_4)  +  part_2

	return product


x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627


test = karatsuba(x, y)

print(test)
print(x * y == test)