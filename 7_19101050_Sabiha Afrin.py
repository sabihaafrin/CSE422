import math
import random
import numpy as np
def main():

    stdid = input('Enter student id: ')
    neghprange = input('MinMax range for neg HP: ').split(' ')
    minneghp = neghprange[0]
    maxneghp = neghprange[1]
    turnno = int(stdid[0])  # 1 .. 19101050
    neghprange = int(stdid[-2:][::-1])  # 50 -->05
    bulletno = int(stdid[2])
    d = turnno * 2
    leafnodeno = bulletno ** d
    val =(np.random.randint(minneghp, maxneghp, size=leafnodeno))
    terminal_state = [19, 22, 9, 2, 26, 16, 16, 27, 16]
    print(f'Depth : Branch:  {d}:{bulletno}')
    print(f'Terminal State:  {val}')
    killed, cmp = abp(terminal_state, d, bulletno).run()
    print(f'Left hp of the def after max kill caused by the att: {abs(neghprange - killed)}')
    print(f'After ABP algo, Leaf Node Comparisons: {cmp}')

class abp:
    def __init__(self, p, d, b, alv=-math.inf, btv=+math.inf, maxval=True, cmpval=0):
        self.cmval = 0
        self.pval = p
        self.dval = d
        self.bval = b
        self.alpval = alv
        self.btval = btv
        self.mxval = maxval
        self.cmval = cmpval

    def run(self):
        if self.dval == 0:
            self.cmval = 1 + self.cmval
            return self.pval.pop(0), self.cmval
        if self.mxval:
            maxi = -math.inf
            for z in range(self.bval):
                e, i = abp(self.pval, self.dval - 1, self.bval, self.alpval, self.btval, False, self.cmval).run()
                self.cmval = i if self.cmval < i else self.cmval
                maxi = max(maxi, e)
                self.alpval = max(self.alpval, e)
                if self.btval <= self.alpval:
                    if len(self.pval) == 1:
                        self.pval.pop(0)
                    break

            return maxi, self.cmval

        else:
            mini = +math.inf
            for z in range(self.bval):
                e, cmn = abp(self.pval, self.dval - 1, self.bval, self.alpval, self.btval, True, self.cmval).run()
                self.cmval = cmn if self.cmval < cmn else self.cmval
                mini = min(mini, e)
                self.btval = min(self.btval, e)
                if self.btval <= self.alpval:
                    if len(self.pval) == 1:
                        self.pval.pop(0)
                    break

            return mini, self.cmval

if __name__ == '__main__':
    main()
