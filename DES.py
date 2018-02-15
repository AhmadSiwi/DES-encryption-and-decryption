def SBoxes(x):
    s = [
    [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13],
    ],
    [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9],
    ],
    [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12],
    ],
    [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14],
    ],
    [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3],
    ],
    [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13],
    ],
    [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12],
    ],
    [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11],
    ]
    ]
    x = str(bin(int(x, 2))[2:]).zfill(48)
    y = ""
    for i in range(8):
        t = int(x[i*6]+x[i*6+5],2)
        u = int(x[i*6+1:i*6+5],2)
        y += str(bin(s[i][t][u])[2:].zfill(4))
    return y

PC1 = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4]
PC2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
IP = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
EP = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
PT = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
FP = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]


def PBox(a, x):
    s = len(a)
    y = ""
    for i in range(s):
        y += x[a[i]-1]
    return y

def PerCho1(x):
    return PBox(PC1, x)

def PerCho2(x):
    return PBox(PC2, x)

def InitPer(x):
    return PBox(IP, x)

def FinalPer(x):
    return PBox(FP, x)

def ExpPer(x):
    return PBox(EP, x)

def PerTabl(x):
    return PBox(PT, x)

def XOR(x,y):
    x = int(x,2)
    y = int(y,2)
    z = x^y
    return str(bin(z)[2:].zfill(32))

'''
def XOR(x,y):
    z = ""
    l = len(x)
    for i in range(l):
        if x[i]==y[i]:
            z += "0"
        else:
            z += "1"
    return z
'''

def HexToBin(x):
    n = len(x)*4
    x = str(bin(int(x, 16))[2:].zfill(n))
    return x

def BinToHex(y):
    return str(hex(int(y, 2)))[2:].upper()

def LeftCircularShift(x):
    l = int(len(x)/2)
    y = ""
    for i in range(l-1):
        y += x[i+1]
    y += x[0]
    for i in range(l,2*l-1):
        y += x[i + 1]
    y += x[l]
    return y

def Round(x, k):
    l0 = x[:32]
    r0 = x[32:]
    l1 = r0
    ep = ExpPer(r0)
#    print("Expansion permutation:", ep)
    xo = XOR(ep, k)
#    print("first xor:", xo)
    sb = SBoxes(xo)
#    print("S-Box", sb)
    p = PerTabl(sb)
#    print("Permutation:", p)
    r1 = XOR(p, l0)
#    print("second xor:", r1)
    y = l1 + r1
#    print("OUTPUT:", y)
#    print("\n")
    return y

def swap32bit(x):
    L0 = x[:32]
    R0 = x[32:]
    y = R0 + L0
    return y

#Useless
'''
def LCS_PC2(R0, p2, rot):
    R1 = R0
    for i in range(rot):
        R1 = LeftCircularShift(R1)
#    print(R1)
    k1 = PBox(p2, R1)
#    print(k1)
    k1 = BinToHex(k1)
    if len(k1)<12:
        y = ""
        for i in range(len(k1),12):
            y += "0"
        k1 = y+k1
    print(k1)
    return R1
'''

Rots = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def Encrypt(key, text):
    key = PerCho1(key)
#    print("key permuted choice 1:", key)
    text = InitPer(text)
#    print("initial permutation:", text)
    for i in range(16):
        for j in range(Rots[i]):
            key = LeftCircularShift(key)
        k = PerCho2(key)
#        print("permuted key of round:", str(i+1), k)
        text = Round(text, k)
#        print("output of round", str(i+1), ":",text)
    text = swap32bit(text)
#    print("after 32 bit swap:", text)
    text = FinalPer(text)
#    print("after final per:", text)
    return text

#Rotations { 1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1 }

key = input()
text = input()
itr = int(input())
key = HexToBin(key)
text = HexToBin(text)
for i in range (itr):
    text = Encrypt(key, text)
text = BinToHex(text).zfill(16)
print(text)

'''
R = []

R.push(PBox(p1, key))
#print(R0)

for i in range(len(Rots)):
    R.push(LCS_PC2(R[i], p2, Rots[i]))


'''
Rots = [0, 27, 26, 26, 26, 26, 26, 26, 27, 26, 26, 26, 26, 26, 26, 27]
