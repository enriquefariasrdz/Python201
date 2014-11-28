import string
for x, y in enumerate(string.ascii_lowercase, 1):
    print(x, y)
    
import string
for x, y in zip(range(1, 27), string.ascii_lowercase):
    print(x, y)



import string
for x, y in enumerate(string.ascii_lowercase, 1):
    print(x, y)


for x, y in ( (x+1, chr(ord('a')+x)) for x in range(26) ):
    print(x, y)
    
for x, y in ( (x+1, chr(ord('a')+x)) for x in range(26) ):
    print( "The letter", y, "has the position number: ", x )
    
import string
	for x, y in enumerate(string.ascii_lowercase, 1):
    print("The letter", y, "has the position number: ", x )
	
	import string
	for x, y in enumerate(string.ascii_uppercase, 1):
    print("The letter", y, "has the position number: ", x )
    
