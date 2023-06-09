def And(x1, x2):
    w1, w2, b = 0.5, 0.5, -0.7
    y = x1*w1 + x2*w2 + b
    if y > 0:
        return 1
    elif y <= 0:
        return 0

print(And(0,0))
print(And(0,1))
print(And(1,0))
print(And(1,1))

import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    y = np.sum(x*w) + b
    if y > 0:
        return 1
    else:
        return 0

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-.5,-.5])
    b = 0.7
    y = np.sum(x*w) + b
    if y > 0:
        return 1
    else:
        return 0

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    y = np.sum(x*w) + b
    if y > 0:
        return 1
    else:
        return 0

def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y

print('XOR 1, 1 :', XOR(1,1))
print('XOR 1, 0 :', XOR(1,0))
print('XOR 0, 1 :', XOR(0,1))
print('XOR 0, 0 :', XOR(0,0))
