import random
Transaction_Register = []
Registr = []
fileRead = open("input.txt", "r")
no_Trans = int(fileRead.readline())
if (no_Trans > 0):
    for i in range(no_Trans):
        Transaction_Register.append(fileRead.readline())
for j in Transaction_Register:
    if j.startswith('l'):
        a = j.lstrip('l ')    #storing the transaction amount without 'l' in a
        a = int(a) * (-1)     #lend so negative
        Registr.append(a)
    else:
        a = j.lstrip('d ')    #storing the transaction amount without 'l' in a
        a = int(a) * (1)      #deposit so positive
        Registr.append(a)
numOfTrans = 10
popultn = []
for i in range(10):
    gene = []
    for c in range(no_Trans):
        s = random.randrange(0,1)
        gene.append(s)
    popultn.append(gene)

def fitn_func(g,r):         #g=gene,r=register
    total_sum = 0
    i = 0
    for clonig in g:
        total_sum = total_sum + clonig * r[i]
        i = i + 1
    return total_sum

def select_choice(popln, fitn, Reg):
    chosen_pop = []
    parent_list = []
    for c in popln:
        after_cross = fitn(c,Reg)
        chosen_pop.append(after_cross)
    final_chosen_pop = sorted(chosen_pop)
    final_chosen_pop = final_chosen_pop[0:5]       # 5 digits
    xy = random.choice(final_chosen_pop)
    i = 0
    for c in chosen_pop:
        if c == xy:
            parent_list = popln[i]
        i = i + 1
    return parent_list

def cross_func(a,b):
    indvdl_char = random.randrange(0,len(a)-1)          #range from 0 to 2nd last of length
    front = a[:indvdl_char]
    back = b[indvdl_char:]
    xxxy = front+back
    return xxxy       #xxxy= child after mutation

def mutate_func(kid):
    itertin = random.randrange(1,3)
    for i in range(itertin):
        indvdl_char = random.randrange(0,len(kid)-1)
        if kid[indvdl_char] == 1:
            kid[indvdl_char] = 0
        else:
            kid[indvdl_char] = 1
    return kid

def genetic_algo(ppltn,final_fit,regstr):
    max_itertn = 100
    One_counts = [0] * len(regstr)
    for i in range(max_itertn):
        new_ppltn = []
        for i in ppltn:
            parentOne = select_choice(ppltn, final_fit, regstr)
            parentTwo = select_choice(ppltn, final_fit, regstr)
            new_gen = cross_func(parentOne,parentTwo)
            if random.randrange(1,100):
                new_gen = mutate_func(new_gen)
            if final_fit(new_gen,regstr) == 0:
                return new_gen
            new_ppltn.append(new_gen)
        ppltn = new_ppltn
    return One_counts

final_res = genetic_algo(popultn,fitn_func,Registr)
if final_res == [0] * len(Registr):
    print(-1)
else:
    print(final_res)


