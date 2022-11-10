import numpy as np
import math
def main(npa):
    '''
    :param npa: numpy array representing an input boolean value in the function
    :return:
    '''
    for i in range(0, np.size(npa, 0)):
        print("================================================")
        res1 = not npa[i][1] and not npa[i][2] and npa[i][3]
        res2 = not npa[i][0] and npa[i][2] and npa[i][3]
        res3 = npa[i][0] and npa[i][1] and npa[i][2] and npa[i][3]
        res4 = not npa[i][0] and not npa[i][1] and npa[i][2] and npa[i][3]
        res5 = not npa[i][0] and not npa[i][1] and not npa[i][2] and npa[i][3]
        res6 = not npa[i][0] and not npa[i][1] and not npa[i][3]
        print("Res1: ", res1)
        print("Res2: ", res2)
        print("Res3: ", res3)
        print("Res4: ", res4)
        print("Res5: ", res5)
        print("Res6: ", res6)
        print("Result: ", bool(res1 or res2 or res3 or res4 or res5 or res6))

def sigmoid(value):
    print(1 / (1 + math.pow(math.e, -value)))
    return round(1 / (1 + math.pow(math.e, -value)))


def matrixes_product(x, w, b):
    res_mat = np.empty(np.size(x, 0))
    for i in range(np.size(x, 0)):
        for j in range(np.size(w, 0)):
            for k in range(np.size(b, 0)):
                res = np.dot(x[i], w[j]) + b[k]
                res_mat[i] = sigmoid(res)
    print(res_mat)

if __name__ == '__main__':
    npa = np.array([
        [False, False, False, False],
        [False, False, False, True],
        [False, False, True, False],
        [False, False, True, True],
        [False, True, False, False],
        [False, True, False, True],
        [False, True, True, False],
        [False, True, True, True],
        [True, False, False, False],
        [True, False, False, True],
        [True, False, True, False],
        [True, False, True, True],
        [True, True, False, False],
        [True, True, False, True],
        [True, True, True, False],
        [True, True, True, True]
        ])

    '''
        and_x = np.array([
           # [0, 1, 0, 1], #Entrada de A
            [0, 0, 1, 1] #Entrada de B
        ])

    [
        [A1, B1],
        [A2, B2],
        [A3, B3],
        [A4, B4]
    ]
    
    [
        [[2], [2]]
    ]
    
    [
        [b1],
    ]
    
    '''

    and_x = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1]
    ])

    and_w1 = np.array([
        [[2], [2]]
    ])

    and_bi = np.array([
        [-1]
    ])


    #main(npa) #Solves the function
    matrixes_product(and_x, and_w1, and_bi)


