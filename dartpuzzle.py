red = [ 13, 9, (17*2), (11*2), (7*3), (6*3) ]
blue = [ 6, 20, 17, (8*2), (9*2), (7*2), (13*3), (11*3), (20*3) ]
green = [ 8, 7, 11, (13*2), (6*2), (20*2), (8*3), (17*3), (9*3) ]

for i in red:
	for j in blue:
		for k in green:
			if i+j+k == 91 and (i<j<k or i>j>k):
				print "Red: %d" % i
				print "Blue: %d" % j
				print "Green: %d\n" % k

