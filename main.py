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
def xor_calculation(x):
    #Hidden layer 1
    xor_w_1 = np.array([
        [[20], [20]]
    ])

    xor_bi_1 = np.array([
        [-10]
    ])

    h1 = matrixes_product(x, xor_w_1, xor_bi_1)

    #Hidden layer 2

    xor_w_2 = np.array([
        [[-20], [-20]]
    ])

    xor_bi_2 = np.array([
        [30]
    ])

    h2 = matrixes_product(x, xor_w_2, xor_bi_2)

    #Last Neuron

    ln_w = np.array([
        [[20], [20]]
    ])

    ln_bi = np.array([
        [-30]
    ])


    ln = np.stack((h1, h2), axis=1)

    print("LN: ", ln)

    matrixes_product(ln, ln_w, ln_bi)

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
    return res_mat

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

    x = np.array([
        [0, 0],
        [1, 0],
        [0, 1],
        [1, 1]
    ])


    #AND

    and_w = np.array([
        [[2], [2]]
    ])

    and_bi = np.array([
        [-1]
    ])


    #OR

    or_w = np.array([
        [[2], [2]]
    ])

    or_bi = np.array([
        [0]
    ])

    #NOR

    nor_w = np.array([
        [[-1], [-1]]
    ])

    nor_bi = np.array([
        [1]
    ])

    #NAND

    nand_w = np.array([
        [[-0.3], [-0.7]]
    ])

    nand_bi = np.array([
        [1]
    ])




    #Calculo de AND
    #matrixes_product(x, and_w, and_bi)

    #Calculo de OR
    #matrixes_product(x, or_w, or_bi)

    #Calculo de NOR
    #matrixes_product(x, nor_w, nor_bi)

    #Calculo de NAND
    #matrixes_product(x, nand_w, nand_bi)

    #Calculo de XOR
    xor_calculation(x)

