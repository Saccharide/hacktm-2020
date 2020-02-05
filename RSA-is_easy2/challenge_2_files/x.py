import gmpy2
import string
import math
import c

def egcd(a, b): # can be used to test if numbers are co-primes
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)



flag = ""
e = 65537
dec = pow(ord('H'),e)

n = dec - c.a[0]
print(pow(ord('H'),e,n))
print(c.a[0])
print(n)

print("[+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+][+]")
list_of_n = []
#for i in string.printable:
#    for j in string.printable:
#        cd = gmpy2.gcd(pow(ord(i),e)-c.a[0], pow(ord(j),e)-c.a[1])
#        if cd > 10000:
#            n = cd
#

n = 53361144550014053166721365196980912889938802302767543436340298420353476899874610747222379321544658210212273658744624182437888528301817525619324262586755752560722184172889301780332276353612167586294259101340749155939404015704537471927068307582449663907783314406726655255040519664154112497941090624585931831047
#print(list_of_n)
#for i in list_of_n:
#    for j in list_of_n:
#        if i != j:
#            print(gmpy2.gcd(i,j))
#    
for char1 in c.a:
    for char in string.printable:
        if pow(ord(char), e, n) == char1:
            flag += char
            print(char)
            break

    
    #test = max(c.a)
    #print("max = ",test)
    
    #while dec != char1:
    #    test += 1
    #    dec = pow(ord('H'),e,test)
    #print(test)
    #print("normal dec = ", dec)
    #print("a[0]= ", char1)
    #break


print(flag)

a = "when it comes to crypto or carpet never roll your own"
b = "HackTM{" +a.replace(" ", "_") + "}"
print(b)
