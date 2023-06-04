from methods import *
import hashlib
import math
import random

def wm_insert_optimal(filename, rnd, z, budget):
    chosen_list = []
    list_o = read_from_file("wmfiles/"+filename)
    list_w = limit_cal(list_o)
    # All elligible items (token) pairs
    el_item = []
    # s_i values
    s = []
    #rnd = secrets.randbits(256)
    #p=random.choice(primes)
    for i in range(len(list_w)):
        # for i in range(20):
        # for j in range(i, len(list_w)):
        for j in range(i + 1, len(list_w)):
            # for j in range(i+1, 15):
           in_msg = list_w[i].get_name() + " " + str(rnd)
           hash_inner = hashlib.sha256(in_msg.encode('utf-8')).hexdigest()
           out_msg = hash_inner + " " + list_w[j].get_name()
           hash_final = hashlib.sha256(out_msg.encode('utf-8')).hexdigest()
           num_hash = int(hash_final, 16)
           num = num_hash % z
           if check_el(list_w[i], num) and check_el(list_w[j], num):  # and (num!=0 or ):
                t = (list_w[i].get_freq() - list_w[j].get_freq()) % num
                el_item.append([list_w[i], list_w[j], t])

                s.append(t)
    if len(s)==0:
        sim = cosine_simil(list_o, list_w)
        return 0,0,[]
    max = np.amax(s) + 1
    G,val=create_graph(el_item,max)
    mwm_match=mwm(G)
    chosen_all=create_list(mwm_match,el_item,max)
#Naive approach to check if MWM produced pairs s.t. similarity is in an acceptable range [100-budget,100]
    for i in range(len(chosen_all)):
        sim = cosine_simil(list_o, list_w)
        if sim >= (100-budget):
            f1, indu1 = get_index_list(list_w, chosen_all[i][0].get_name())
            f2, indu2 = get_index_list(list_w, chosen_all[i][1].get_name())
            list_w[indu1].set_freq(f1 - math.floor(chosen_all[i][2] / 2))
            list_w[indu2].set_freq(f2 + math.ceil(chosen_all[i][2] / 2))

    print("-----Optimal w\o Knapsack-----")
    print('Elligible number of pairs: ', len(el_item))
    print('Chosen number of pairs   : ', len(chosen_all))
    print("The similarity is: ", sim)
    # print(mwm_match)
    # list_w=knapSack(chosen_all,budget)
    name = filename.split('.')
    wm_to_file(list_w, "wmfiles/"+name[0] + '_optimal.txt')
    #wmpair_to_file(chosen_all, name[0] + '_optimal_pairs.txt')
    return len(mwm_match),len(el_item), chosen_all #,100 #, rnd
    # return chosen_list,secrets

def wm_insert_random(filename, rnd, z, budget):
    chosen_el = []
    list_o = read_from_file("wmfiles/"+filename)
    list_wm = limit_cal(list_o)
    wm_list=list_o

    # All elligible items (url) pairs
    el_item = []
    list_w=[]
    # s_i values
    s = []
    mark = []
    # rnd = secrets.randbits(256)
    for i in range(len(list_wm)):

        mark.append([list_wm[i].get_name(), 0])
        for j in range(i + 1, len(list_wm)):
            in_msg = list_w[i].get_name() + " " + str(rnd)
            hash_inner = hashlib.sha256(in_msg.encode('utf-8')).hexdigest()
            out_msg = hash_inner + " " + list_w[j].get_name()
            hash_final = hashlib.sha256(out_msg.encode('utf-8')).hexdigest()
            num_hash = int(hash_final, 16)
            num = num_hash % z

            if check_el(list_wm[i], num) and check_el(list_wm[j], num) :
                t = (list_wm[i].get_freq() - list_wm[j].get_freq()) % num
                el_item.append([list_wm[i].get_name(), list_wm[j].get_name(), t])
                s.append(num)

    random.shuffle(el_item)

    for i in range(len(el_item)):
        val1, ind1 = get_index(mark, el_item[i][0])
        val2, ind2 = get_index(mark, el_item[i][1])
        f1,indu1=get_index_list(list_wm,el_item[i][0])
        f2,indu2 =get_index_list(list_wm,el_item[i][1])
        if val1 == 0 and val2 == 0:
            list_wm[indu1].set_freq(f1 - math.floor(el_item[i][2] / 2))
            list_wm[indu2].set_freq(f2 + math.ceil(el_item[i][2] / 2))
            if check_sim(list_o,list_wm,budget):

                mark[ind1][0] = 1
                mark[ind2][0] = 1
                chosen_el.append(el_item[i])
            else:
                list_wm[indu1].set_freq(f1 + math.floor(el_item[i][2] / 2))
                list_wm[indu2].set_freq(f2 - math.ceil(el_item[i][2] / 2))

    sim=cosine_simil(list_o,list_wm)
    name = filename.split('.')
    wm_to_file(list_w,"wmfiles/"+ name[0] + '_random.txt')
    print("-----Random-----")
    print('Elligible number of pairs: ',len(el_item))
    print('Chosen number of pairs   : ', len(chosen_el))
    print("The similarity is: ",sim)

    return len(chosen_el),len(el_item),chosen_el #, sim

def wm_insert_greedy(filename, rnd, z, budget):
    list_o=read_from_file("wmfiles/"+filename)
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
            in_msg = list_w[i].get_name() + " " + str(rnd)
            hash_inner = hashlib.sha256(in_msg.encode('utf-8')).hexdigest()
            out_msg = hash_inner + " " + list_w[j].get_name()
            hash_final = hashlib.sha256(out_msg.encode('utf-8')).hexdigest()
            num_hash = int(hash_final, 16)
            num = num_hash % z
            if check_el(list_w[i], num) and check_el(list_w[j], num)  :
                t = (list_w[i].get_freq() - list_w[j].get_freq()) % num
                el_item.append([list_w[i].get_name(), list_w[j].get_name(), t])
                # print([list_w[i], "--",list_w[j], "-->",num])
                s.append(num)

    el_item.sort(key=lambda el_item: el_item[2])
    chosen_el=[]

    for i in range(len(el_item)):
        val1,ind1=get_index(mark,el_item[i][0])
        val2,ind2=get_index(mark,el_item[i][1])
        f1, indu1 = get_index_list(list_w, el_item[i][0])
        f2, indu2 = get_index_list(list_w, el_item[i][1])
        if val1 == 0 and val2 == 0 : #and el_item[i][2] != 0:
            list_w[indu1].set_freq(f1 - math.floor(el_item[i][2] / 2))
            list_w[indu2].set_freq(f2 + math.ceil(el_item[i][2] / 2))
            if check_sim(list_o, list_w, budget):
                mark[ind1][0] = 1
                mark[ind2][0] = 1
                chosen_el.append(el_item[i])
            # print(el_item[i])
            else:
                list_w[indu1].set_freq(f1 + math.floor(el_item[i][2] / 2))
                list_w[indu2].set_freq(f2 - math.ceil(el_item[i][2] / 2))
    sim = cosine_simil(list_o, list_w)
    name=filename.split('.')
    wm_to_file(list_w,"wmfiles/"+name[0]+'_greedy.txt')
   # wmpair_to_file(chosen_el,name[0]+'_greedy_pairs.txt')
    print("-----FreqyWM Greedy-----")
    print('Eligible # of pairs: ', len(el_item))
    print('Chosen # of pairs   : ', len(chosen_el))
    print("The similarity is: ", sim)

    return len(chosen_el),len(el_item),chosen_el #,sim
