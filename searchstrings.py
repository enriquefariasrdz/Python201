f = open('TEST.txt', 'r')

searchstrings = ('proton', 'neutron', 'isotope', 'india')

for line in f.readlines():
    for word in searchstrings:
        if word in line:
            print line
f.close()
