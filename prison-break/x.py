def main():
    #f = open('Given_File.txt', 'rb') 
    f = open('test.txt', 'rb') 
    l = [[] for _ in xrange(10**7)]
    linez = f.readlines()

    print linez
    for count in xrange(len(linez)):
        print count
        line = linez[count].strip()
        a, b, c = map(int, line.split())
        if  c == 0:
            continue
        if a != b:
            l[a + 1].append((count, c))
            l[b].append((count, c))

    print "L = ", l
    return 
    prod = 1
    for i in xrange(len(l)):
        if l[i] != 0:
            prod *= l[i]

    return pow(prod,1,99999937)

print main() 
