from pwn import *
import gmpy2
import ast

def parse_tuple(string):
    try:
        s = ast.literal_eval(str(string))
        if type(s) == tuple:
            return s
        return
    except:
        return

def egcd(a, b): # can be used to test if numbers are co-primes
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

s = remote("138.68.67.161",60005)

rsa_private_keys = {}
list_of_n = []

target_n = 2318553827267041599931064141028026591078453523755133761420994537426231546233197332557815088229590256567177621743082082713100922775483908922217521567861530205737139513575691852244362271068595653732088709994411183164926098663772268120044065766077197167667585331637038825079142327613226776540743407081106744519
x = 0
while x < 500:
    print(s.recvuntil("> "))
    s.sendline("k")
    res = s.recvuntil("((e,n),(d,n ))\n").decode('utf-8')
    #print("res = ", res)

    # Getting RSA key
    key = s.recvuntil("\n").decode('utf-8').split("\n")[0]
    (pub, priv) = parse_tuple(key)
    #print("priv = ", priv)
    (d,n) = parse_tuple(priv)
    print("public  key = ", pub)
    print("private key = ", priv)
    #print("private key = ", d)
    rsa_private_keys[n] = d
    list_of_n.append(n)

    print("gcd = ", gmpy2.gcd(n,target_n))
    x += 1

total_cd = []
big_cd = []
print("list_of_n = ", list_of_n)
for i in list_of_n:
    if i != target_n:
        cd = gmpy2.gcd(i,target_n)[0]
        total_cd.append(cd)
        if cd > 1000:
            big_cd.append(cd)
            #print("[+] GCD of {} and {} is {}".format(i,j,cd))

    else:
        print("FOUND PRIVATE KEY!!!")
        print(rsa_private_keys[i])


print("total_cd = ", total_cd)
print("big_cd = ", big_cd)
print(rsa_private_keys)
