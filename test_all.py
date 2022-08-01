import statistics

from methods import *
from freqywm_insert import *
from freqywm_verify import *
import matplotlib.pyplot as plt
import random
import timeit
import sys
sys.setrecursionlimit(5000)
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89,
          97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197,
          199,
          211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331,
          337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457,
          461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
          601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733,
          739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877,
          881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013, 1019,
          1021,
          1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069, 1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129,
          1151,
          1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223, 1229, 1231, 1237, 1249, 1259, 1277, 1279,
          1283,
          1289, 1291, 1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373, 1381, 1399, 1409, 1423, 1427,
          1429,
          1433, 1439, 1447, 1451, 1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511, 1523, 1531, 1543,
          1549,
          1553, 1559, 1567, 1571, 1579, 1583, 1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657, 1663,
          1667,
          1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733, 1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801,
          1811,
          1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889, 1901, 1907, 1913, 1931, 1933, 1949, 1951,
          1973,
          1979, 1987, 1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053, 2063, 2069, 2081, 2083, 2087,
          2089,
          2099, 2111, 2113, 2129, 2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213, 2221, 2237, 2239,
          2243,
          2251, 2267, 2269, 2273, 2281, 2287, 2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357, 2371,
          2377,
          2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423, 2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521,
          2531,
          2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617, 2621, 2633, 2647, 2657, 2659, 2663, 2671,
          2677,
          2683, 2687, 2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741, 2749, 2753, 2767, 2777, 2789,
          2791,
          2797, 2801, 2803, 2819, 2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903, 2909, 2917, 2927,
          2939,
          2953, 2957, 2963, 2969, 2971, 2999, 3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079, 3083,
          3089,
          3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181, 3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253,
          3257,
          3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331, 3343, 3347, 3359, 3361, 3371, 3373, 3389,
          3391,
          3407, 3413, 3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511, 3517, 3527, 3529, 3533, 3539,
          3541,
          3547, 3557, 3559, 3571, 3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643, 3659, 3671, 3673,
          3677,
          3691, 3697, 3701, 3709, 3719, 3727, 3733, 3739, 3761, 3767, 3769, 3779, 3793, 3797, 3803, 3821, 3823,
          3833,
          3847, 3851, 3853, 3863, 3877, 3881, 3889, 3907, 3911, 3917, 3919, 3923, 3929, 3931, 3943, 3947, 3967,
          3989,
          4001, 4003, 4007, 4013, 4019, 4021, 4027, 4049, 4051, 4057, 4073, 4079, 4091, 4093, 4099, 4111, 4127,
          4129,
          4133, 4139, 4153, 4157, 4159, 4177, 4201, 4211, 4217, 4219, 4229, 4231, 4241, 4243, 4253, 4259, 4261,
          4271,
          4273, 4283, 4289, 4297, 4327, 4337, 4339, 4349, 4357, 4363, 4373, 4391, 4397, 4409, 4421, 4423, 4441,
          4447,
          4451, 4457, 4463, 4481, 4483, 4493, 4507, 4513, 4517, 4519, 4523, 4547, 4549, 4561, 4567, 4583, 4591,
          4597,
          4603, 4621, 4637, 4639, 4643, 4649, 4651, 4657, 4663, 4673, 4679, 4691, 4703, 4721, 4723, 4729, 4733,
          4751,
          4759, 4783, 4787, 4789, 4793, 4799, 4801, 4813, 4817, 4831, 4861, 4871, 4877, 4889, 4903, 4909, 4919,
          4931,
          4933, 4937, 4943, 4951, 4957, 4967, 4969, 4973, 4987, 4993, 4999, 5003, 5009, 5011, 5021, 5023, 5039,
          5051,
          5059, 5077, 5081, 5087, 5099, 5101, 5107, 5113, 5119, 5147, 5153, 5167, 5171, 5179, 5189, 5197, 5209,
          5227,
          5231, 5233, 5237, 5261, 5273, 5279, 5281, 5297, 5303, 5309, 5323, 5333, 5347, 5351, 5381, 5387, 5393,
          5399,
          5407, 5413, 5417, 5419, 5431, 5437, 5441, 5443, 5449, 5471, 5477, 5479, 5483, 5501, 5503, 5507, 5519,
          5521,
          5527, 5531, 5557, 5563, 5569, 5573, 5581, 5591, 5623, 5639, 5641, 5647, 5651, 5653, 5657, 5659, 5669,
          5683,
          5689, 5693, 5701, 5711, 5717, 5737, 5741, 5743, 5749, 5779, 5783, 5791, 5801, 5807, 5813, 5821, 5827,
          5839,
          5843, 5849, 5851, 5857, 5861, 5867, 5869, 5879, 5881, 5897, 5903, 5923, 5927, 5939, 5953, 5981, 5987,
          6007,
          6011, 6029, 6037, 6043, 6047, 6053, 6067, 6073, 6079, 6089, 6091, 6101, 6113, 6121, 6131, 6133, 6143,
          6151,
          6163, 6173, 6197, 6199, 6203, 6211, 6217, 6221, 6229, 6247, 6257, 6263, 6269, 6271, 6277, 6287, 6299,
          6301,
          6311, 6317, 6323, 6329, 6337, 6343, 6353, 6359, 6361, 6367, 6373, 6379, 6389, 6397, 6421, 6427, 6449,
          6451,
          6469, 6473, 6481, 6491, 6521, 6529, 6547, 6551, 6553, 6563, 6569, 6571, 6577, 6581, 6599, 6607, 6619,
          6637,
          6653, 6659, 6661, 6673, 6679, 6689, 6691, 6701, 6703, 6709, 6719, 6733, 6737, 6761, 6763, 6779, 6781,
          6791,
          6793, 6803, 6823, 6827, 6829, 6833, 6841, 6857, 6863, 6869, 6871, 6883, 6899, 6907, 6911, 6917, 6947,
          6949,
          6959, 6961, 6967, 6971, 6977, 6983, 6991, 6997, 7001, 7013, 7019, 7027, 7039, 7043, 7057, 7069, 7079,
          7103,
          7109, 7121, 7127, 7129, 7151, 7159, 7177, 7187, 7193, 7207, 7211, 7213, 7219, 7229, 7237, 7243, 7247,
          7253,
          7283, 7297, 7307, 7309, 7321, 7331, 7333, 7349, 7351, 7369, 7393, 7411, 7417, 7433, 7451, 7457, 7459,
          7477,
          7481, 7487, 7489, 7499, 7507, 7517, 7523, 7529, 7537, 7541, 7547, 7549, 7559, 7561, 7573, 7577, 7583,
          7589,
          7591, 7603, 7607, 7621, 7639, 7643, 7649, 7669, 7673, 7681, 7687, 7691, 7699, 7703, 7717, 7723, 7727,
          7741,
          7753, 7757, 7759, 7789, 7793, 7817, 7823, 7829, 7841, 7853, 7867, 7873, 7877, 7879, 7883, 7901, 7907,
          7919]

def wrapper(func, *args, **kwargs):
    def wrapped():
        return func(*args, **kwargs)
    return wrapped

def test_opt(filename,primes,rnd,budget):
    """
    Test the optimal insertion algorithm
    :param filename: the list of filenames
    :param primes: z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al = []
 #
    '''
    ch, el, ch_list = wm_insert(filename, rnd, primes, budget)
    name = "chosen_pairs_" + filename
    wmpair_to_file(ch_list, name)
    al.append(ch)
    '''
    for i in range(len(filename)):
        ch, el,ch_list = wm_insert_optimal(filename[i], rnd, primes, budget)
        #name="chosen_pairs_"+filename[i]
        #wmpair_to_file(ch_list,name)
        al.append(ch)
        #t.append(sim)

    return al #,t
def test_opt_p(filename,primes,rnd,budget):
    """
    Test the optimal insertion algorithm
    :param filename: the list of filenames
    :param primes:  z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al = []
    for i in range(len(primes)):
        ch, el,ch_list = wm_insert_optimal(filename, rnd, primes[i], budget)
        al.append(ch)
    return al

def test_greedy_p(filename,primes,rnd,budget):
    """
    Test the greedy based insertion algorithm
    :param filename: the list of filenames
    :param primes: z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al=[]
    for i in range(len(primes)):
       ch,el,ch_list= wm_insert_greedy(filename, rnd, primes[i], budget)
       al.append(ch)
    return al
def test_random_p(filename,z,rnd,budget):
    """
    Test the insertion algorithm with random choose
    :param filename: the list of filenames
    :param primes: z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al = []
    for i in range(len(z)):
        ch, el,ch_list = wm_insert_random(filename, rnd, z[i], budget)
        al.append(ch)
    return al
def test_greedy(filename,primes,rnd,budget):
    """
    Test the greedy based insertion algorithm
    :param filename: the list of filenames
    :param primes: z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al=[]
    #t=[]
    for i in range(len(filename)):
       ch,el,ch_list= wm_insert_greedy(filename[i], rnd, primes, budget)
       al.append(ch)
       #t.append(sim)

    return al #,t

def test_random(filename,z,rnd,budget):
    """
    Test the insertion algorithm with random choose
    :param filename: the list of filenames
    :param primes: z value chosen to generate s_i values to test
    :param rnd: the high entropy (random) value generated based on security parameter (e.g.256)
    :param budget: the tolerance on distortion created by watermarking
    :return: Testing...
    """
    al = []
    '''
    ch, el, ch_list = wm_insert_random(filename, rnd, z, budget)
    al.append(ch)
    #t=[]
    '''
    for i in range(len(filename)):
        ch, el,ch_list = wm_insert_random(filename[i], rnd, z, budget)
        al.append(ch)

      #  t.append(sim)
    return al #,t
def time_all_gen(func,filename,rnd,z,budget):
    for i in range(len(filename)):
        wrapped = wrapper(func, filename[i],rnd, z, budget)
        x = timeit.timeit(wrapped, number=1)
        print("Generation time for : ",x, " ", filename[i])
   # wrapped = wrapper(func, filename, rnd, z, budget)
   # x = timeit.repeat(wrapped, number=1, repeat=10)
    #avg=sum(x)/len(x)
    sum=0
    #for i in range(3):
   # x = timeit.timeit(wrapped, number=1)
    #sum=sum+x
    #x=sum/3
   # print("Running time (in sec) of ",filename," : ",x) #round(x,2))
    return

def time_all_verify(func,filename,threshold,threshold_ver, chosen_list, rnd, z):
    for i in range(len(filename)):
     ch, el, ch_list = wm_insert_optimal(filename[i], rnd, z, budget)
     wrapped = wrapper(func,filename[i],50,2, ch_list, rnd, z)
     x = timeit.timeit(wrapped, number=1)
     print("Running time (in sec) of verification ", filename, " : ", x)   # x = timeit.repeat(wrapped, number=1, repeat=10)
    #avg=sum(x)/len(x)
    sum=0
    #for i in range(3):

    #sum=sum+x
    #x=sum/3
    #print("Running time (in sec) of ",filename," : ",x) #round(x,2))
    #return x

def time_rep(func,filename,threshold,threshold_ver, items, rnd, z):
    wrapped = wrapper(func,filename,threshold,threshold_ver, items, rnd, z)
    #x = timeit.repeat(wrapped, number=1, repeat=30)
    #avg=x/30
    sum=0
    for i in range(30):
        x = timeit.timeit(wrapped, number=1)
        print(i,'th iter: ',x)
        sum=sum+x
    x=sum/30
    print("Running time (in sec) of verification ", filename, " : ", x)  # round(x,2))
    return x

def test_alpha(filename,z,rnd,budget,name):
    """
    :param filename: is a list of file names as [file1.txt,file2.txt]
    :param z: z chosen to calculate s_i values as s_1=H(rnd||token1||token2) mod z
    :param rnd: a high entropy secret (e.g., 256 bits)
    :param budget: distortion tolerance on the data after watermarked
    :return: a plot
    """
    x = [[0.05, 0.2, 0.5, 0.7, 0.9, 1], [0.05, 0.2, 0.5, 0.7, 0.9, 1],[0.05, 0.2, 0.5, 0.7, 0.9, 1]]
    y = []
    t=[]
    print("-------TESTING BASED ON ALPHA VALUES-------\n")

    y1 = test_opt(filename, z, rnd, budget)
    print('The result of optimal : ', y1)

    y2 = test_greedy(filename, z, rnd, budget)
    print('The result of greedy  : ', y2)

    y3 = test_random(filename, z, rnd, budget)
    print('The result of random  : ', y3)

   # y1 = test_random(filename, z, rnd, budget)
    #print('The result of optimal : ', y1)


    y.append(y1)
    y.append(y2)
    y.append(y3)


   # print('The data w alpa values: ', x[0])


    print('The result of random  : ', y[2])
    nam='Number of chosen Pairs vs. Alpha : '+name
    draw_plot_multiple(x, 'Skewness parameter (\u03B1)', y,'Chosen pairs', ['Optimal','Greedy','Random'], nam)
   # namx='Cosine similarity vs Alpha : '+name
    #draw_plot_multiple(x, 'alpha', t, 'Cosine Similarity', ['Optimal', 'Greedy', 'Random'], namx)

def test_budgets(filename,z,rnd,budget):
    x=[[2,5,10,15],[2,5,10,15],[2,5,10,15]]
    y1 = []
    y2 = []
    y3 = []
    for i in range(len(budget)):
        ch1, el1,cho1 = wm_insert_optimal(filename[2], rnd, z, budget[i])
        y1.append(ch1)
        ch2, el2,cho2 = wm_insert_greedy(filename[2], rnd, z, budget[i])
        y2.append(ch2)
        ch3, el3,cho3 = wm_insert_random(filename[2], rnd, z, budget[i])
        y3.append(ch3)

    y = []
    y.append(y1)
    y.append(y2)
    y.append(y3)
    draw_plot_multiple(x, 'Budget (b)', y, 'Chosen pairs', ['Optimal', 'Greedy','Random'], 'Number of chosen Pairs vs. Budgets')

def test_size(filename,z,rnd,budget):
    """
    :param filename: is a list of file names as [file1.txt,file2.txt]
    :param z: z chosen to calculate s_i values as s_1=H(rnd||token1||token2) mod z
    :param rnd: a high entropy secret (e.g., 256 bits)
    :param budget: distortion tolerance on the data after watermarked
    :return: a plot
    """
    #x = [[100, 300, 500, 1000, 10000], [100, 300, 500, 1000, 10000],[100, 300, 500, 1000, 10000]]
    x = [[100, 300, 500, 1000], [100, 300, 500, 1000], [100, 300, 500, 1000]]
    y = []
    print("-------TESTING BASED ON ALPHA=0.5 with different sizes-------\n")

    y1 = test_opt(filename, z, rnd, budget)
    print('The result of optimal : ', y1)

    y2 = test_greedy(filename, z, rnd, budget)
    print('The result of greedy  : ', y2)

    y3 = test_random(filename, z, rnd, budget)
    print('The result of random  : ', y3)


    y.append(y1)
    y.append(y2)
    y.append(y3)
   # print('The data w alpa values: ', x[0])


    #print('The result of random  : ', y[2])

    draw_plot_multiple(x, 'Size', y,'Chosen pairs', ['Optimal','Greedy','Random'], 'Number of chosen Pairs vs Size, alpha=0.5')

def test_p(filename,z,rnd,budget):
    """
        :param filename: is a list of file names as [file1.txt,file2.txt]
        :param z: z chosen to calculate s_i values as s_1=H(rnd||token1||token2) mod z
        :param rnd: high entropy secret (e.g., 256 bits)
        :param budget: distortion tolerance on the data after watermarked
        :return: a plot
        """
    # x = [[100, 300, 500, 1000, 10000], [100, 300, 500, 1000, 10000],[100, 300, 500, 1000, 10000]]
    x = [z, z, z]
    y = []
    print("-------TESTING BASED ON ALPHA=%s -------\n"%(filename))

    y1 = test_opt_p(filename, z, rnd, budget)
    print('The result of optimal : ', y1)

    y2 = test_greedy_p(filename, z, rnd, budget)
    print('The result of greedy  : ', y2)

    y3 = test_random_p(filename, z, rnd, budget)
    print('The result of random  : ', y3)

    y.append(y1)
    y.append(y2)
    y.append(y3)
    # print('The data w alpa values: ', x[0])

    # print('The result of random  : ', y[2])

    draw_plot_multiple(x, 'Modulo value (z)', y, 'Chosen pairs', ['Optimal', 'Greedy', 'Random'],
                       'Number of chosen Pairs vs z value ')

def draw_plot_multiple(x,xname,y,yname,linename,plotname):
    """
    Make sure that the sizes of x and y are the same.
    Make sure that linename has enough number of names
    :param x: a matrix holds x values e.g. : x = [[1, 2, 3],[1, 2, 3],[8, 12, 13]]
    :param xname: name of the x-axis
    :param y: a matrix holds y values e.g. : y = [[2, 4, 1],[4, 1, 3],[3, 5, 7]]
    :param yname: name of the y-axis
    :param linename: an array consists of the names given to each line e.g., linename=['line-1','line-2','line-3']
    :param plotname: name of the plot
    :return: returns a plot with the possibility of multiple lines in one plot
    """
    for i in range(len(x)):
     plt.rc('font', size=15)
     plt.rc('font', weight='bold')
     plt.plot(x[i], y[i], '--o', linewidth=5, label=linename[i])
     #if i==0:
     #    plt.plot(x[i], y[i], '--o', linewidth=5, label=linename[i], color='orange')
     #else:
     #    plt.plot(x[i], y[i], '--o', linewidth=5, label=linename[i], color='green')

    #print(x[0])
   # print(y[0])
   # plt.plot(x[0], y[0], label=linename[0])
    #plt.plot(x[1], y[1], label=linename[1])
   # plt.plot(x[2], y[2], label=linename[2])
    plt.xlabel(xname,fontweight='bold')
    # naming the y axis
    plt.ylabel(yname,fontweight='bold')
    # giving a title to my graph
    #plt.title(plotname)
    # show a legend on the plot
    plt.legend()
    plt.savefig('bvspair.png')

    # function to show the plot
    plt.show()
    #x, np.log(x), 'g'
def draw_exec(files,x,xname,rnd,z,budget):
    t=[]
    for i in range(len(files)):
        # print(files[i])
        t.append(time_all_gen(wm_insert_greedy, files[i], rnd, z, budget))
    m = []
    m.append(t)
    draw_plot_multiple(x, xname, m, 'Time (sec)', ['line-1'], 'Total Execution-time')

#draw_plot_multiple([[0.1,0.2,0.5,0.7,0.9]],'alpha',[[112,223,110,450,300]],'elligible items',['test'],'alpha-elligible items')


#x = [[1, 2, 3]]
#y = [[2, 4, 1]]
# plotting the line 1 points



xname='alpha'
yname='Chosen pairs'
linename=['Optimal','Greedy'] #,'Random']
plotname='Number of chosen Pairs vs Alpha'
#draw_plot_multiple(x,xname,y,yname,linename,plotname)

#primes=[2671]
#z = random.choice(primes)
#rnd = secrets.randbits(256)
rnd=94150602964623730173619679764343462318710907258738770672733287463602813493207
z=131 #131 #1031 #1001#631#231 #2671 #3911
pr=[10,33,393,631,1031,2671] #,2671,5001]
budget=2
x=[[0,0.2,0.5,0.7,0.9,1],[0,0.2,0.5,0.7,0.9,1]]
files=["sample_alpha_0.txt","sample_alpha_0_2.txt","sample_alpha_0_5.txt","sample_alpha_0_7.txt","sample_alpha_0_9.txt","sample_alpha_1_1_p_3.txt"]
files_sk=["sample_0_5_100.txt","sample_0_5_300.txt","sample_0_5_500.txt","sample_0_5_1000.txt"]#,"sample_0_5_10000.txt"]
files_1K_10K=["s_0_05_1k_10K.txt","s_0_2_1k_10K.txt","s_0_5_1k_10K.txt","s_0_7_1k_10K.txt","s_0_9_1k_10K.txt","s_1_1k_10K.txt"]
files_1K_100K=["new_s_0_05.txt","new_s_0_2.txt","new_s_0_5.txt","new_s_0_7.txt","new_s_0_9.txt","new_s_1.txt"]

files_new_10K=["s_0_05_10k_1M.txt","s_0_2_10k_1M.txt","s_0_5_10k_1M.txt","s_0_7_10k_1M.txt","s_0_9_10k_1M.txt","s_1_10k_1M.txt"]
eyewndr=["eyewndr.txt"]
files_new_1M=["new_s_0_05_1M.txt","new_s_0_2_1M.txt","new_s_0_5_1M.txt","new_s_0_7_1M.txt","new_s_0_9_1M.txt","new_s_1_1M.txt"]
files_new_10M=["s_0_05_1k_10M.txt","s_0_2_1k_10M.txt","s_0_5_1k_10M.txt","s_0_7_1k_10M.txt","s_0_9_1k_10M.txt","s_1_1k_10M.txt"]
files_alpha_0_5=["s_0_5_100.txt","s_0_5_300.txt","s_0_5_500.txt","s_0_5_1000.txt"] #,"s_0_5_10K.txt"]
#print("rnd: ",rnd, " z: ",z)
#print("new_s_0_7.txt : "+ str(total("new_s_0_7.txt")))
#test_budgets(files_new_1M,33,rnd,[2,5,10,15])
#for i in range(len(eyewndr)):
 #   print(str(total(eyewndr[i])))
#print("new_s_0_2.txt: "+str(total("s_0_2_1k_10K.txt")))
#"eyewndr.txt"
real_data=["hist_taxi_id.txt","hist_adult_age.txt","hist_adult_age_workclass.txt"]
nf10K='N=10K, S=1M'
name1M='N=1K, S=1M'
#test_alpha(files_new_10K,z,rnd,budget,nf10K)
#list_o,list_ow=read_from_file("hist_taxi_id.txt")
#print(list_ow)
#r_opt=test_opt(real_data,z,rnd,2)
#print("chosen: ",r_opt)
#r_rnd=test_random(real_data,z,rnd,2)
#r_rnd=test_greedy(real_data,z,rnd,2)
#time_all_gen(wm_insert,real_data,rnd,z,2)
time_all_verify(wm_verify,real_data,50,20,[],rnd,z)
r_rnd=test_random(real_data,z,rnd,2)
r_rnd=test_greedy(real_data,z,rnd,2)

'''

r_random=[]
for i in range(10):
   r_random.append(test_random(real_data[1],z,rnd,2)[0])
print("Mean random: ",statistics.mean((r_random)))
'''
#print("Optimal: ",r_opt,"Random: ",r_rnd," Greedy: ",r_greedy)
#y=[]
#y1=round(time_all(wm_insert_greedy,'new_s_0_5_1M.txt',rnd,z,2),3)
#y.append(y1)
#y2=round(time_all(wm_insert_random,'new_s_0_5_1M.txt',rnd,z,2),3)
#y.append(y2)
#y3=round(time_all(wm_insert,'new_s_0_5_1M.txt',rnd,z,2),3)
#y.append(y3)
#print(y)
#wm_insert("new_s_0_5_1M.txt")
#test_p("new_s_0_7_1M.txt",pr,rnd,2) #new_s_0_7_1M.txt
#------test_opt(files_new_1M,z,rnd,budget)
#test_p("s_0_7_1k_10M.txt",pr,rnd,2)
#test_p("new_s_0_7_10K.txt",pr,rnd,2)
#draw_exec(files_new_1M,2)
#test_random(files_new_10K,z,rnd,budget)
#test_greedy(files_new_10K,z,rnd,budget)
#test_size(files_alpha_0_5,1031,rnd,budget)
#name10K='N=1K, S=10K'
#test_alpha(files_1K_10K,z,rnd,budget,name10K)
#name100K='N=1K, S=100K'
#test_alpha(files_1K_100K,z,rnd,budget,name100K)

#test_alpha(files_new_1M,z,rnd,budget,name1M)
#name10M='N=1K, S=10M'
#test_alpha(files_new_10M,z,rnd,budget,name10M)
#wm_insert_random(files[3],rnd,z,2)
#wm_insert_greedy("sample_0_5_1K.txt",rnd,z,2)
#test_budgets(files,z,rnd,[2,5,10,15])
#al=test_random(eyewndr,z,rnd,budget)
#print(al)
#test_opt(files,z,rnd,budget)
#wm_insert("sample_alpha_0_7.txt",rnd,z,2)
#print("Greedy")
#wm_insert_greedy(eyewndr[0],rnd,z,2)
#wm_insert_greedy(eyewndr[0],rnd,z,1)
#wm_insert_greedy(eyewndr[0],rnd,z,0.01)

#wm_insert("sample_alpha_4.txt", primes, 2)
#y1=time_all(wm_insert,"eyewndr.txt", rnd,z,2)
#y2=time_all(wm_insert_greedy,"eyewndr.txt", rnd,z,2)
#y3=time_all(wm_insert_random,"eyewndr.txt", rnd,z,2)

#ch,el,chosen_list=wm_insert("new_s_0_5_1M.txt",rnd,z,2)
#destroy_atck("WM_new_s_0_5_1M.txt")
#time_rep(wm_verify,"WM_new_s_0_5_1M.txt",50,2,chosen_list,rnd,p)
#ch,el,chosen_list=wm_insert("eyewndr.txt",rnd,z,2)
#time_rep(wm_verify,"WM_eyewndr.txt",50,2,chosen_list,rnd,p)

#result,verified=wm_verify("WM_eyewndr.txt",50,2,chosen_list,rnd,p)

#y1=time_all(wm_insert,"new_s_0_5_1M.txt", rnd,z,2)
#y2=time_all(wm_insert_greedy,"new_s_0_5_1M.txt", rnd,z,2)
#y3=time_all(wm_insert_random,"new_s_0_5_1M.txt", rnd,z,2)

#draw_plot_multiple(x,xname,m,'execution time',linename,'execution-time')

#draw_exec(files,x,xname,rnd,z,2)

#x1 = [0,0.2,0.5,0.7,0.9,1]
#y1 = [136, 147, 135, 130, 130, 127]
#y2 = [131, 144, 133, 126, 127, 124]
#y3 = [135, 143, 134, 128, 129, 123]

#x=[[0.0000002,2,5],[0.0000002,2,5]]
#y=[[123/134,131/139,131/139],[122/134,133/139,134/139]]
#draw_plot_multiple(x, 'Budget (b)', y, 'Chosen pairs w.r.t. Optimal', [ 'Greedy', 'Random'],    'Pairs norm by opt vs. Budgets')
