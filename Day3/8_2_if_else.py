number =0

# outer if statement
if (number >= 0):
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    elif number > 3:
        print("is more than 3")

    else:
        print('Number is positive')


elif number > -3:
    print("is executed")

# outer else statement
else:
    print('Number is negative')

# Output: Number is positive

only one of the condition below block will be executed in one if /else block;
