import numpy as np

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

    main(npa)
