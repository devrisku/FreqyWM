from methods import *
import hashlib
import math
def wm_insert_random(filename, rnd, prim, budget):
    chosen_el = []
    list_o, list_wm = read_from_file(filename)
    wm_list=list_o
    #print(wm_list)
    # All elligible items (url) pairs
    el_item = []
    list_w=[]
    # s_i values
    s = []
    mark = []
    # rnd = secrets.randbits(256)
    # p=random.choice(primes)
    p = prim
    rem=np.zeros(p)

    for i in range(len(list_wm)):
        # for i in range(20):
        # for j in range(i, len(list_w)):
        mark.append([list_wm[i].get_name(), 0])
        for j in range(i + 1, len(list_wm)):
            # for j in range(i+1, 15):
            msg = list_wm[i].get_name() + " " + list_wm[j].get_name() + " " + str(rnd)
            hash_val = hashlib.sha256(msg.encode('utf-8')).hexdigest()
            num_hash = int(hash_val, 16)
            num = num_hash % p
            #rem[num]=rem[num]+1
           # if i < 5 and j<5:
            #    print("Hash value (hex)",hash_val)
             #   print("Hash value (decimal)",num_hash)
              #  print("reminder: ",num)

            # num=num_hash%primes[i]

            if check_el(list_wm[i], num) and check_el(list_wm[j], num) : # and num!=0:  # and (num!=0 or ):
                #print("Hash value: ", num_hash)
                t = (list_wm[i].get_freq() - list_wm[j].get_freq()) % num
                # print("Hash value: ", num_hash)
                # if t!=0:
                el_item.append([list_wm[i].get_name(), list_wm[j].get_name(), t])
                #el_item.append([list_wm[i].get_name(), list_wm[j].get_name(), num])
                #print([list_wm[i], "--",list_wm[j], "-->",num])
                s.append(num)
    #print("----All reminders----")
    #print(rem[0:500])
    random.shuffle(el_item)

    for i in range(len(el_item)):
        val1, ind1 = get_index(mark, el_item[i][0])
        val2, ind2 = get_index(mark, el_item[i][1])
        f1,indu1=get_index_list(list_wm,el_item[i][0])
        f2,indu2 =get_index_list(list_wm,el_item[i][1])
        #print("indexes u1 and u2: ",indu1,"--",indu2,"--",el_item[i][2])
        if val1 == 0 and val2 == 0: #and el_item[i][2]!=0:
            list_wm[indu1].set_freq(f1 - math.floor(el_item[i][2] / 2))
            list_wm[indu2].set_freq(f2 + math.ceil(el_item[i][2] / 2))
            if check_sim(list_o,list_wm,budget):

                #print(f1,",",list_wm[indu1].get_freq()) #,"---","[",f2,",",list_wm[indu2].get_freq(),"]")
                mark[ind1][0] = 1
                mark[ind2][0] = 1
                chosen_el.append(el_item[i])
               # print(el_item[i])
            else:
                list_wm[indu1].set_freq(f1 + math.floor(el_item[i][2] / 2))
                list_wm[indu2].set_freq(f2 - math.ceil(el_item[i][2] / 2))


            #Mark the chosen urls as a pair.

            # print(wm_list[indu1],'---',wm_list[indu2])
            #h1,h2=divide(wm_list[indu1],wm_list[indu2],)
    sim=cosine_simil(list_o,list_wm)
    print("-----Random-----")
    print('Elligible number of pairs: ',len(el_item))
    print('Chosen number of pairs   : ', len(chosen_el))
    print("The similarity is: ",sim)

    return len(chosen_el),len(el_item),chosen_el #, sim

def wm_insert_greedy(filename, rnd, z, budget):
    list_o=read_from_file(filename)
    list_w=limit_cal(list_o)
    # All eligible token pairs
    el_item = []
    # s_i values
    s = []
    mark=[]
    # rnd = key_gen(256)
    # z=random.choice(primes)
    for i in range(len(list_w)):
        mark.append([list_w[i].get_name(), 0])
        for j in range(i + 1, len(list_w)):
            msg = list_w[i].get_name() + " " + list_w[j].get_name() + " " + str(rnd)
            hash_val = hashlib.sha256(msg.encode('utf-8')).hexdigest()
            num_hash = int(hash_val, 16)
            num = num_hash % z
            if check_el(list_w[i], num) and check_el(list_w[j], num)  :
                t = (list_w[i].get_freq() - list_w[j].get_freq()) % num
                el_item.append([list_w[i].get_name(), list_w[j].get_name(), t])
                # print([list_w[i], "--",list_w[j], "-->",num])
                s.append(num)

    el_item.sort(key=lambda el_item: el_item[2])
    chosen_el=[]
    #print('number of el pairs: ', len(el_item))
    #print(mark)
    for i in range(len(el_item)):
        #print(el_item[i][0], el_item[i][1], el_item[i][2])
        val1,ind1=get_index(mark,el_item[i][0])
        val2,ind2=get_index(mark,el_item[i][1])
        f1, indu1 = get_index_list(list_w, el_item[i][0])
        f2, indu2 = get_index_list(list_w, el_item[i][1])
        # print("Indices u1 and u2: ",indu1,"--",indu2,"--",el_item[i][2])
        if val1 == 0 and val2 == 0 : #and el_item[i][2] != 0:
            list_w[indu1].set_freq(f1 - math.floor(el_item[i][2] / 2))
            list_w[indu2].set_freq(f2 + math.ceil(el_item[i][2] / 2))
            if check_sim(list_o, list_w, budget):
                #print(f1, ",", list_w[indu1].get_freq())  # ,"---","[",f2,",",list_wm[indu2].get_freq(),"]")
                mark[ind1][0] = 1
                mark[ind2][0] = 1
                chosen_el.append(el_item[i])
            # print(el_item[i])
            else:
                list_w[indu1].set_freq(f1 + math.floor(el_item[i][2] / 2))
                list_w[indu2].set_freq(f2 - math.ceil(el_item[i][2] / 2))
    #print('chosen el: ',len(chosen_el))
    sim = cosine_simil(list_o, list_w)
    name=filename.split('.')
    wm_to_file(list_w,name[0]+'_freqywm.txt')
    wmpair_to_file(chosen_el,name[0]+'_freqywm_pairs.txt')
    print("-----FreqyWM Greedy-----")
    print('Eligible # of pairs: ', len(el_item))
    print('Chosen # of pairs   : ', len(chosen_el))
    print("The similarity is: ", sim)

    return len(chosen_el),len(el_item),chosen_el #,sim
