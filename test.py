# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from freqywm_insert import *
from obtwm_insert import *
from freqywm_verify import *
from obtwm_verify import *

rnd=94150602964623730173619679764343462318710907258738770672733287463602813493207
z=131
budget=2
#TEST of FreqyWM
print("---------Test FreqyWM----------")
pairs=read_from_pairs("wmfiles/freqy_wm_chosen_pairs_s_0_5_1M.txt")
res,percentage=wm_verify("wmfiles/freqywm_s_0_5_1M.txt",50,2,pairs,rnd,z)
print("FreqyWM success rate: ",percentage)

print("---------Test FreqyWM Insert----------")
wm_insert_greedy("wmfiles/new_s_0_7_1M.txt",rnd,z,2)

#Test of OBT-WM
print("---------Test OBT-WM----------")
alpha=5
part_num=20
part_size=7
condition=0.75
opt_threshold=0.0966
wm=[1,1,0,1,0]
result=obtwm_verification("wmfiles/obtwm_s_0_5_10.txt",rnd,wm,part_num,opt_threshold,alpha,condition,part_size)
print("OBT-WM success rate: ",result)

print("---------Test OBT-WM Insert----------")
opt_threshold_0_7=obtwm_insert("wmfiles/new_s_0_7_1M.txt",rnd,condition,alpha,wm,part_num) #would save new_s_0_7_1M_obtwm.txt
