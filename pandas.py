#!/usr/bin/env python

# coding: utf-8

# In[31]:

for line in open("file.txt"):
 if "perro" in line:
   print line


# In[1]:

f = open('file.txt')
for line in iter(f):
    print line
f.close()


# In[2]:

from collections import Counter

data = '''ashwin programmer india
amith programmer india'''

c = Counter()
for line in data.splitlines():
    c.update(line.split())
print(c)


# In[4]:



from collections import Counter;
cnt = Counter ();

for line in open ('TEST.txt', 'r'):
  for word in line.split ():
    cnt [word] += 1

print cnt



# In[ ]:

index = ("notes.txt",["isotope","proton","electron","neutron"])

def index():
    infile=open("test.txt", "r")
    content=infile.read()
    print(content)
    infile.close()


# In[17]:

def word_find(line,words):
    return list(set(line.strip().split()) & set(words))

def main(file,words):
    with open('TEST.txt') as f:
        for i,x in enumerate(f, start=1):
            common = word_find(x,words)
            if common:
                print i, "".join(common)

if __name__ == '__main__':
    main('file', words)


# In[24]:

f = open('TEST.txt', 'r')

for word in f:

    print(word)


# In[25]:

with open('TEST.txt','r') as f:
    for line in f:
        for word in line.split():
           print(word)    


# In[28]:

f = open("TEST.txt","r") #opens file with name of "test.txt"
#print(f.read(1))
print(f.read())
f.close()


# In[30]:

f = open("TEST.txt","r") #opens file with name of "test.txt"
myList = ["a","b","c","d"]
for line in f:

    myList.append(line)

print(myList)

print(f.read())
f.close() 


# In[32]:

list = ['physics', 'chemistry', 1997, 2000];

print "Value available at index 2 : "
print list[2]
list[2] = 2001;
print "New value available at index 2 : "
print list[2]


# In[33]:

str = raw_input("Enter your input: ");
print "Received input is : ", str


# In[37]:

fo = open("TEST.txt", "r+")
str = fo.read(10);
print "Read String is : ", str

position = fo.tell();
print "Current file position : ", position

# Reposition pointer at the beginning once again
position = fo.seek(0, 0);
str = fo.read(10);
print "Again read String is : ", str
# Close opend file
fo.close()


# In[42]:


var = 1

if ( var  == 1 ) : print "Value of expression is 1"

print "Good bye!"


# In[43]:

with open('TEST.txt') as fp:
    for line in fp:
        print line


# In[210]:

f = open('TEST.txt', 'r')

searchstrings = ('proton', 'neutron', 'isotope', 'india')

for line in f.readlines():
    for word in searchstrings:
        if word in line:
            print line
f.close()


# In[209]:

f = open("TEST.txt","r") #opens file with name of "test.txt"
print(f.read())
f.close()


# In[63]:

import re


ss = '''qhvfgbhgozr
yytuuuyuyuuuyuyuuyy
jhfg tryy error  jjfkhdjhfjh ttrtr
aaaeeedddeedaeaeeaeeea
jhzdgcoiua zfaozifh cohfgdyg fuo'''

regx = re.compile('^(.*)\r?\n(.*?error.*)\r?\n(.*)', re.MULTILINE)

print regx.search(ss).groups()


# In[64]:

mystr = '1 2 3 4 5 6'
parts = mystr.split()
print parts[3:5]


# In[73]:

def str( msg, n ):
    for i in range(n):
        print msg

str( "chidote!", 10 )


# In[89]:

rawProfiles = '''
Tim Fake, 1982/03/21, I like to
eat, sleep and
relax

Lisa Test, 1990/05/12, I like long
walks of the beach, watching sun-sets,
and listening to slow jazz

42342342
234234
33333
'''

profilesList = re.split(r'\n{2,}', rawProfiles)
profilesList


# In[82]:

profilesList = [ re.sub(r'\n', ' ', profile) for profile in profilesList ]

profilesList


# In[90]:

profilesList = [ re.split(r',', profile, maxsplit=2) for profile in profilesList ]
for profile in profilesList:
    print profile


# In[92]:

from subprocess import call

call( "echo hello world",shell=True)


# In[97]:

import os

content = dir(os)

print content


# In[103]:

def Pots():
   print "I'm Pots Phone"
Pots()


# In[106]:

fo = open("TEST.txt", "wb")
print "Name of the file: ", fo.name
print "Closed or not : ", fo.closed
print "Opening mode : ", fo.mode
print "Softspace flag : ", fo.softspace


# In[109]:

n = 1

while n < 10:
    print(n)
    n += 1


# In[121]:

import string
string.uppercase
'abcdefghijklmnopqrstuvwxyz'


# In[122]:

for line in string.lowercase:
    print(line)
    
    print(string.uppercase)


# In[123]:

for i in range(4, 10, 2):
    print(i)


# In[124]:

for i in range(4, 10):
    print(i)


# In[125]:

import timeit
def costly_func():
    return map(lambda x: x^2, range(10))

# Measure it since costly_func is a callable without argument
timeit.timeit(costly_func)


# In[126]:

import time
time.gmtime()


# In[127]:

current_time = time.localtime()
time.strftime('%a, %d %b %Y %H:%M:%S GMT', current_time)


# In[128]:

time.strftime('%a, %d %b %Y %H:%M', current_time)


# In[129]:

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print i, a[i]


# In[135]:

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while b < n:
        print b,
        a, b = b, a+b
 
# Now call the function we just defined:
fib(2000)


# In[140]:

#! python
# work with strings

# Strings can be concatenated (glued together) with the + operator, and repeated with *: 


word = 'Help' + ' ' + 'Enrique' + ' '
print word

print word*11


# In[141]:

st='str' 'ing'             #  <-  This is ok
print st
st='str'.strip() + 'ing'   #  <-  This is ok
print st


# In[142]:

print word[4]

print word[0:2]

print word[2:4]


# In[143]:

s = 'supercalifragilisticexpialidocious'
print s
print len(s)


# In[145]:

a = ['spam', 'eggs', 100, 1234]
print " list a=",a


# In[146]:

nn=1000000
a = []
i=0

while i


# In[147]:

a = [-1, 1, 66.6, 333, 333, 1234.5]
del a[0]
print a


# In[148]:

a = [-1, 1, 66.6, 333, 333, 1234.5]
del a[0]
print a


# In[149]:

a = [-1, 1, 66.6, 333, 333, 1234.5]
del a[2:4]
print a


# In[156]:

for x in range(1, 11):
    print repr(x).rjust(2), repr(x*x).rjust(3),
    # Note trailing comma on previous line
    print repr(x*x*x).rjust(4)


# In[ ]:

from Tkinter import *

class Alarm(Frame):
    def repeater(self):                          
        self.bell()                              
        self.after(self.msecs, self.repeater)    
    def __init__(self):              
        Frame.__init__(self)
        self.msecs = 1000
        self.pack()
        stopper = Button(self, text='Stop the beeps!', command=self.quit)
        stopper.pack()
        stopper.config(bg='navy', fg='white', bd=8) 
        self.stopper = stopper
        self.repeater()

if __name__ == '__main__': 
   Alarm().mainloop()


# In[164]:

database = [
    ['A',  '1234'],
    ['B',  '4242'],
    ['C',  '7524'],
    ['D',  '9843']
]

username = raw_input('User name: ')
pin = raw_input('PIN code: ')

if [username, pin] in database: print 'Access granted'

           
       

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')          # search for position
print where                           

S = S[:where] + 'EGGS' + S[(where+4):]
print S


# In[165]:

string2 = "Odd or even"

# find index of "even"
try:
   print '"even" index is', string2.index( "even" )
except ValueError:
   print '"even" does not occur in "%s"' % string2

if string2.startswith( "Odd" ):
   print '"%s" starts with "Odd"' % string2

if string2.endswith( "even" ):
   print '"%s" ends with "even"\n' % string2

           
       




# In[169]:

import numpy
import numpy as np

cvalues = [25.3, 24.8, 26.9, 23.9]

C = np.array(cvalues)
print(C)


# In[170]:

x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78] ])
print(np.shape(x))


# In[171]:

A = np.array([[[ 0,  1],
               [ 2,  3],
               [ 4,  5],
               [ 6,  7]],
              [[ 8,  9],
               [10, 11],
               [12, 13],
               [14, 15]],
              [[16, 17],
               [18, 19],
               [20, 21],
               [22, 23]]])
Flattened_X = A.flatten()
print(Flattened_X)
print(A.flatten(order="C"))
print(A.flatten(order="F"))
print(A.flatten(order="A"))


# In[172]:

np.histogram([1, 2, 1], bins=[0, 1, 2, 3])


# In[174]:

import matplotlib.pyplot as plt
plt.hist([1, 2, 1], bins=[0, 1, 2, 3])
plt.show()


# In[175]:

import numpy as np    
hist, bin_edges = np.histogram([1, 1, 2, 2, 2, 2, 3], bins = range(5))


# In[176]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.__version__


# In[177]:

get_ipython().magic(u'matplotlib inline')


# In[180]:

sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])
sales.head()


# In[181]:

sales.describe()


# In[182]:

sales['unit price'].describe()


# In[183]:

sales.dtypes


# In[184]:

customers = sales[['name','ext price','date']]
customers.head()


# In[185]:

customer_group = customers.groupby('name')
customer_group.size()


# In[192]:

sales_totals = customer_group.sum()
sales_totals.sort(columns='ext price').head()


# In[193]:

my_plot = sales_totals.plot(kind='bar')


# In[195]:

my_plot = sales_totals.sort(columns='ext price',ascending=False).plot(kind='bar',legend=None,title="Total Sales by Customer")
my_plot.set_xlabel("Customers")
my_plot.set_ylabel("Sales ($)")


# In[196]:

purchase_patterns = sales[['ext price','date']]
purchase_patterns.head()


# In[197]:

purchase_plot = purchase_patterns['ext price'].hist(bins=20)
purchase_plot.set_title("Purchase Patterns")
purchase_plot.set_xlabel("Order Amount($)")
purchase_plot.set_ylabel("Number of orders")


# In[198]:

purchase_patterns = purchase_patterns.set_index('date')
purchase_patterns.head()


# In[199]:

purchase_patterns.resample('M',how=sum)


# In[202]:

purchase_plot = purchase_patterns.resample('M',how=sum).plot(title="Total Sales by Month",legend=None)


# In[203]:

# Standard import for pandas, numpy and matplot
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read in the csv file and display some of the basic info
sales=pd.read_csv("sample-salesv2.csv",parse_dates=['date'])
print "Data types in the file:"
print sales.dtypes
print "Summary of the input file:"
print sales.describe()
print "Basic unit price stats:"
print sales['unit price'].describe()

# Filter the columns down to the ones we need to look at for customer sales
customers = sales[['name','ext price','date']]

#Group the customers by name and sum their sales
customer_group = customers.groupby('name')
sales_totals = customer_group.sum()

# Create a basic bar chart for the sales data and show it
bar_plot = sales_totals.sort(columns='ext price',ascending=False).plot(kind='bar',legend=None,title="Total Sales by Customer")
bar_plot.set_xlabel("Customers")
bar_plot.set_ylabel("Sales ($)")
plt.show()

# Do a similar chart but break down by category in stacked bars
# Select the appropriate columns and group by name and category
customers = sales[['name','category','ext price','date']]
category_group = customers.groupby(['name','category']).sum()

# Plot and show the stacked bar chart
stack_bar_plot = category_group.unstack().plot(kind='bar',stacked=True,title="Total Sales by Customer",figsize=(9, 7))
stack_bar_plot.set_xlabel("Customers")
stack_bar_plot.set_ylabel("Sales")
stack_bar_plot.legend(["Total","Belts","Shirts","Shoes"], loc=9,ncol=4)
plt.show()

# Create a simple histogram of purchase volumes
purchase_patterns = sales[['ext price','date']]
purchase_plot = purchase_patterns['ext price'].hist(bins=20)
purchase_plot.set_title("Purchase Patterns")
purchase_plot.set_xlabel("Order Amount($)")
purchase_plot.set_ylabel("Number of orders")
plt.show()

# Create a line chart showing purchases by month
purchase_patterns = purchase_patterns.set_index('date')
month_plot = purchase_patterns.resample('M',how=sum).plot(title="Total Sales by Month",legend=None)
fig = month_plot.get_figure()

#Show the image, then save it
plt.show()
fig.savefig("total-sales.png")


# In[ ]:



