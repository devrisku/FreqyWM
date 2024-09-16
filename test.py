# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from freqywm_insert import *
from freqywm_verify import *
#from attacks import *


random_key=94150602964623730173619679764343462318710907258738770672733287463602813493207
modulo_z=131
budget=2

#TEST of FreqyWM
print("---------Test FreqyWM Greedy Insert----------")
wm_pair_size,el,wm_pairs= wm_insert_greedy("new_s_0_5_1M.txt", random_key, modulo_z, budget)

print("---------Test FreqyWM Verify----------")
wm_pairs=read_from_pairs("wmfiles/new_s_0_5_1M_greedy_pairs.txt")
res,percentage=wm_verify("wmfiles/new_s_0_5_1M_greedy.txt",50,2,wm_pairs,random_key,modulo_z)
print("FreqyWM verification success rate: ",percentage)

list_wm=read_from_file("wmfiles/new_s_0_5_1M_greedy.txt")
list_original=read_from_file("wmfiles/new_s_0_5_1M.txt")

#create_plot(list_wm, 'watermarked', list_original, 'original')

# Example usage:
#list_wm = [['url1', 1900], ['url2', 1800], ['url3', 1700], ['url4', 1600]]
#list_original = [['url1', 1800], ['url2', 1700], ['url3', 1600], ['url4', 1500]]

#create_plot(list_wm, list_original)


#print("---------Test FreqyWM Greedy Insert----------")
#wm_insert_greedy("new_s_0_7_1M.txt",rnd,z,2)
#print("---------Test FreqyWM Random Insert----------")
#wm_insert_random("new_s_0_7_1M.txt",rnd,z,2)
#print("---------Test FreqyWM Optimal Insert----------")
#wm_insert_optimal("new_s_0_7_1M.txt",rnd,z,2)
