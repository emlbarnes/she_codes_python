
mylist = [None, 6, None, 1, 2, 5, 0]

for item in mylist:
    print()
    print (item)
    if item is None:
        print ('None!')
    elif item < 3:
        print ('Little!')

