import hashlib
from methods import *
#use/replace with hash table for better performance: Python dict[]
def get_index_list(list,token):
    for i in range(len(list)):
        if list[i].get_name()==token:
            return list[i].get_freq(),i
    return -1,-1

def wm_verify(filename,threshold,threshold_ver, pairs, rnd, z):
    """
    This is the verification algorithm based on wm-data and secrets (pairs,rnd,z...)
    :param filename: name of the file which is described as urlname, frequencys
    :param threshold: is the threshold to determine if a verification is successful (e.g., 60% of the wm must be verified)
    :param threshold_ver: is the threshold to decide if we should accept a reminder after modular operation.
    For instance: wm is (f_i-f_j) mod s_m = 0 in insertion. For verification, to verify (f_i-f_j) mod s_m <= s_m/threshold_ver
    :param pairs:all the pairs used for wm
    :param rnd: the high-entropy secret generated during insertion
    :param z: is used to create s_i values e.g., s_1= Hash(url_1||url_2||rnd) mod z
    :return: returns if the verification of wm is successful based on given inputs.
    """
    list_w = read_from_file(filename)
    #list_w=createhistogram()
    count = 0
    result = 0
    non_found_total=0
    for i in range(len(pairs)):
        #print(pairs[i][0], "--",pairs[i][1])
        #f1,ind1=get_index_list(list_w,pairs[i][0].get_name())
        #f2,ind2 = get_index_list(list_w,pairs[i][1].get_name())
        f1, ind1 = get_index_list(list_w, pairs[i][0])
        f2, ind2 = get_index_list(list_w, pairs[i][1])
        if ind2!=-1 and ind1!=-1:
        # if list_w.get(pairs[i][0])!=None and list_w.get(pairs[i][1])!=None:
           msg = list_w[ind1].get_name() + " " + list_w[ind2].get_name() + " " + str(rnd)
           hash_val = hashlib.sha256(msg.encode('utf-8')).hexdigest()
           num_hash = int(hash_val, 16)
           num = num_hash % z
           if ((f1 - f2) % num) <= (threshold_ver):
             # print(f1," - ",f2," mod ",num, " = ",((f1-f2) % num))
              count = count + 1
           else:
              non_found_total=non_found_total+1

    if (count*100)/len(pairs) >= threshold:
            result = 1
    #print("# of accepted pairs (%) for ", filename, " : ",(count*100)/len(pairs))
    return result, (count*100)/len(pairs)
#pairs=read_from_pairs("wmfiles/freqy_wm_chosen_pairs_s_0_5_1M.txt")
#wm_verify("wmfiles/freqywm_s_0_5_1M.txt",50,2,pairs,rnd,131)