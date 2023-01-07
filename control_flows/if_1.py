print ("name in if1",__name__)
import if_2 as a
a = 2
month = ['Janauary',
		'February',
		'March',
		'April',
		'May',
		'June',
		'July',
		'August',
		'September',
		'October',
		'November',
		'December']

if a > 0 or a <= len(month):
    print("Month name is ", month[a+1])

else:
	print("Given value is invalid")
	print("Give value in between 1 to 12")

