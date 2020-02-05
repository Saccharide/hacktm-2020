import string
import c

def egcd(a, b): # can be used to test if numbers are co-primes
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)
flag = ""
e = 65537
n = 28150970547901913019901824364390497053600856369839321617996700606130553862041378369018779003752433356889118526332329074054728613209407037089320809898343953157935211086135010436283805891893636870991411236307901650696221491790470635225076251966300189483160148297407974155121570252648252906976186499329924342873
for char1 in c.a:
    for char in string.printable:
        if pow(ord(char), e, n) == char1:
            flag += char
            break


print(flag)
