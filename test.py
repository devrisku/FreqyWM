# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from freqywm_insert import *
from freqywm_verify import *
from attacks import *


rnd=94150602964623730173619679764343462318710907258738770672733287463602813493207
z=131
budget=2

#TEST of FreqyWM
print("---------Test FreqyWM Verify----------")
pairs=read_from_pairs("wmfiles/freqy_wm_chosen_pairs_s_0_5_1M.txt")
res,percentage=wm_verify("wmfiles/freqywm_s_0_5_1M.txt",50,2,pairs,rnd,z)
print("FreqyWM success rate: ",percentage)

#print("---------Test FreqyWM Greedy Insert----------")
#wm_insert_greedy("new_s_0_7_1M.txt",rnd,z,2)
#print("---------Test FreqyWM Random Insert----------")
#wm_insert_random("new_s_0_7_1M.txt",rnd,z,2)
#print("---------Test FreqyWM Optimal Insert----------")
#wm_insert_optimal("new_s_0_7_1M.txt",rnd,z,2)
