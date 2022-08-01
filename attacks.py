
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import math
import statistics

from methods import *
from freqywm_insert import *
from freqywm_verify import *
import random
import numpy as np

def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

def gen_alpha(item):
    #x=item.get_up()-item.get_down()
    up=item.get_up()
    if up==np.infty:
        up=item.get_freq()*2

    down=-1*item.get_down()
    x=random.randint(down,up)

    return x
def pick_random(list_w):
    x = random.randint(0, len(list_w))
    return x

def perc(filename,perc):
    list_o, list_w = read_from_file(filename)
    list_temp = list_w
    count=0
    for i in range(len(list_temp)):
        ch=math.ceil(list_temp[i].get_freq()*perc/100)
        up = list_temp[i].get_up()
        if up==np.infty:
            down = list_temp[i].get_down()
            up1 = 1000* (perc / 100)
            down1 = math.floor(down * perc / 100)
            a = random.randint(-down1, up1)
        else:
            down = list_temp[i].get_down()
            up1 = math.floor(up * perc / 100)
            down1 = math.floor(down * perc / 100)
            a = random.randint(-down1, up1)

        print(min," changed")
        freq = list_temp[i].get_freq()
        if a != 0:
            count=count+1

        list_temp[i].set_freq(freq + a)
        list_temp[i].set_lim_up(up - a)
        list_temp[i].set_lim_down(down + a)
        if i < (len(list_w)-1):
          list_temp[i+1].set_lim_up(list_temp[i+1].get_up() + a)
    wm_to_file(list_temp, str(perc)+"_bnd_" + filename)
    sim = cosine_simil(list_o, list_temp)
    print("------CONTROLLED Attack-----\n")
    print("similarity: ", sim, " total changes: ", (count * 100) / len(list_w))
    # print(list_temp)
    return list_temp, sim

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
     plt.plot(x[i], y[i],'--o', linewidth = 5, label=linename[i])

    plt.xlabel(xname,fontweight='bold')
    # naming the y axis
    plt.ylabel(yname,fontweight='bold')
    # giving a title to my graph
    #plt.title(plotname)
    # show a legend on the plot
    plt.legend()
    plt.savefig('uncontAttack.png')
    #plt.savefig('uncontAttack.png')
    # function to show the plot
    plt.show()

def test_per():
    x=[0,1,2,3,4,5,6,7,8,9,10]
    x1=[[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]]
    rnd = 94150602964623730173619679764343462318710907258738770672733287463602813493207
    z = 131
    budget = 2
    ch, el, chosen_list = wm_insert_optimal("new_s_0_5_1M.txt", rnd, z, budget)

    y=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]
    ym=[]
    y5 =[]
    y6 = []
    y7 = []
    y8 = []
    y9 = []
    yt=[]


    for i in range(len(x)):
         result1, verified1 = wm_verify("wmfiles/new_s_0_7_1M.txt", 50, x[i], chosen_list, rnd, z)
         y1.append(verified1)
         print("\n")
         result2, verified2 = wm_verify("wmfiles/new_s_0_2_1M.txt", 50, x[i], chosen_list, rnd, z)
         y2.append(verified2)
         print("\n")
         result3, verified3 = wm_verify("wmfiles/WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y3.append(verified3)
         print("\n")
         result4, verified4 = wm_verify("wmfiles/2_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y4.append(verified4)
         print("\n")
         result5, verified5 = wm_verify("wmfiles/3_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y5.append(verified5)
         print("\n")
         result6, verified6 = wm_verify("wmfiles/5_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y6.append(verified6)
         print("\n")
         result7, verified7 = wm_verify("wmfiles/10_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y7.append(verified7)
         print("\n")
         result8, verified8 = wm_verify("wmfiles/30_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y8.append(verified8)
         print("\n")
         result9, verified9 = wm_verify("wmfiles/50_perc_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y9.append(verified9)
         print("\n")

    y.append(y1)
    y.append(y2)
    y.append(y3)
    y.append(y4)

    ym.append(y3)
    ym.append(y5)
    ym.append(y6)
    ym.append(y7)

    yt.append(y3)
    yt.append(y2)
    yt.append(y8)
    yt.append(y9)

    nam = 'Verified pairs (%) vs t_ver p='+str(z)+' N=1K S=1M'
    draw_plot_multiple(x1, '(t_wm) Threshold for accepting a pair', y, 'Verified pairs (%)', ['alpha=0.7', 'alpha=0.2', '(Origin WM) alpha=0.5','Attack: 2%'], nam)


    draw_plot_multiple(x1, '(t_wm) Threshold for accepting a pair', ym, 'Verified pairs (%)',
                       ['(Origin WM) alpha=0.5', 'Attack: 3%', 'Attack: 5%', 'Attack: 10%'],
                       nam)
    draw_plot_multiple(x1, '(t_wm) Threshold for accepting a pair', yt, 'Verified pairs (%)',
                       ['(Origin WM) alpha=0.5', 'alpha=0.2', 'Attack: 30%', 'Attack: 50%'],
                       nam)
def test():
    x=[0,1,2,3,4,5,6,7,8,9,10]
    x1=[[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]]#,[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10],[0,1,2,3,4,5,6,7,8,9,10]]
    rnd = 94150602964623730173619679764343462318710907258738770672733287463602813493207
    z = 1031
    budget = 2

    ch, el, chosen_list = wm_insert_optimal("wmfiles/new_s_0_5_1M.txt", rnd, z, budget)

    y=[]
    y1=[]
    y2=[]
    y3=[]
    y4=[]

    for i in range(len(x)):
         result1, verified1 = wm_verify("new_s_0_7_1M.txt", 50, x[i], chosen_list, rnd, z)
         y1.append(verified1)
         result2, verified2 = wm_verify("cntrl_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y2.append(verified2)
         result3, verified3 = wm_verify("WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y3.append(verified3)
         result4, verified4 = wm_verify("1_bnd_WM_new_s_0_5_1M.txt", 50, x[i], chosen_list, rnd, z)
         y4.append(verified4)



    y.append(y3)
    y.append(y1)
    y.append(y2)
    y.append(y4)


    nam = 'Verified pairs (%) vs t z='+str(z)+' N=1K S=1M'
    draw_plot_multiple(x1, 'Threshold value for accepting a pair (t)', y, 'Accepted pairs (%)', ['$D_w$','$D_{non}$' ,'$D^r_W$','$D^1_W$'], nam)

def destroy_percentage_total(filename,perc):
    '''
    :param filename: name of the dataset to attack
    :param perc: is a percentage which refers to percentage of data change (e.g., 10%)
    :return: new file with 10% changes
    '''
    list_o, list_w = read_from_file(filename)
    list_temp=list_w
    #change=math.ceil(len(list_w)*(perc/100))
    #ch=[change]
    #ch=np.zeros(change)
    pick=[]
    count=0
    for i in range(len(list_w)):
        coin=random.randint(0,1)

        if(coin==0):
            x= - math.floor(list_temp[i].get_freq()*perc/100) #pick_random(list_w)
        else:
            x = math.ceil(list_temp[i].get_freq()*perc/100)

        #print("Change: ",x,"for ",list_temp[i].get_freq())
        up = list_temp[i].get_up()
        down = list_temp[i].get_down()
        freq = list_temp[i].get_freq()
        list_temp[i].set_freq(freq + x)
        list_temp[i].set_lim_up(up - x)
        list_temp[i].set_lim_down(down + x)
        if i < (len(list_w) - 1):
            list_temp[i+ 1].set_lim_up(list_temp[i + 1].get_up() + x)

    wm_to_file(list_temp,str(perc)+"_total_"+filename)
    sim=cosine_simil(list_o,list_temp)
    print("------Total attack-----\n")
    print("similarity: ",sim, " total changes: ", (count*100)/len(list_w))
    #print(list_temp)
    return list_temp,sim

def destroy_percentage(filename,perc):
    '''
    :param filename: name of the dataset to attack
    :param perc: is a percentage which refers to percentage of data change (e.g., 10%)
    :return: new file with 10% changes
    '''
    list_o, list_w = read_from_file(filename)
    list_temp=list_w
    change=math.ceil(len(list_w)*(perc/100))
    #ch=[change]
    ch=np.zeros(change)
    pick=[]
    count=0
    for i in range(change):

        ch[i]=random.randint(-500,500)
        x= random.randint(0, len(list_temp)-1) #pick_random(list_w)
        x=int(x)
        #print("x: ",x)
        pick.append(x)
        if ch[i] != 0:
            count = count + 1
       # try:

         #  pick.index(x)
          # break
        #except ValueError:
         #   print("Oops!  That was no valid number.  Try again...")

        up = list_temp[x].get_up()
        down = list_temp[x].get_down()
        freq = list_temp[x].get_freq()
        list_temp[x].set_freq(freq + ch[i])
        list_temp[x].set_lim_up(up - ch[i])
        list_temp[x].set_lim_down(down + ch[i])
        if x < (len(list_w) - 1):
            list_temp[x + 1].set_lim_up(list_temp[x + 1].get_up() + ch[i])

    wm_to_file(list_temp,str(perc)+"_uncntrl_"+filename)
    sim=cosine_simil(list_o,list_temp)
    print("------UNCONTROLLED Attack-----\n")
    print("similarity: ",sim, " total changes: ", (count*100)/len(list_w))
    #print(list_temp)
    return list_temp,sim

def destroy_atck(filename):
    '''

    :param filename:  name of the dataset to attack
    A random value between limits (random integer \in [lim_down,lim_up]) of the item (url) is chosen
    :return:
    '''
    list_o,list_w=read_from_file(filename)
    #list_att=[len(list_w)]
    list_temp = list_w
    alpha=[]
    count=0
    for i in range(len(list_w)):
        up=list_temp[i].get_up()
        down=list_temp[i].get_down()
        freq=list_temp[i].get_freq()
        a=gen_alpha(list_temp[i])

        if a != 0:
            count=count+1

        list_temp[i].set_freq(freq + a)
        list_temp[i].set_lim_up(up - a)
        list_temp[i].set_lim_down(down + a)
        if i < (len(list_w)-1):
          list_temp[i+1].set_lim_up(list_temp[i+1].get_up() + a)

        alpha.append(a)
    wm_to_file(list_temp,"cntrl_"+filename)
    sim=cosine_simil(list_o,list_temp)
    print("------CONTROLLED Attack-----\n")
    print("similarity: ",sim, " total changes: ", (count*100)/len(list_w))
    #print(list_temp)
    return list_temp,sim

def percentage(filename,perc):
    list_o, list_w = read_from_file(filename)
    list_temp = list_w
    pick = []
    count = 0

    for i in range(len(list_w)):
        freq=list_temp[i].get_freq()
        lim=math.floor(list_temp[i].get_freq()*(perc/100))
        up=list_temp[i].get_up()
        down=list_temp[i].get_down()
        if lim <= up:
            count=count+1
            list_temp[i].set_freq(freq + lim)
            list_temp[i].set_lim_up(up - lim)
            list_temp[i].set_lim_down(down + lim)
            if i < (len(list_w) - 1):
               list_temp[i + 1].set_lim_up(list_temp[i + 1].get_up() + lim)
        elif lim <=down:
            count=count+1
            list_temp[i].set_freq(freq - lim)
            list_temp[i].set_lim_up(up + lim)
            list_temp[i].set_lim_down(down - lim)
            if i < (len(list_w) - 1):
               list_temp[i + 1].set_lim_up(list_temp[i + 1].get_up() - lim)
        else:
            count=count+1
            x= random.randint(-down, up)
            list_temp[i].set_freq(freq + x)
            list_temp[i].set_lim_up(up - x)
            list_temp[i].set_lim_down(down + x)
            if i < (len(list_w) - 1):
               list_temp[i + 1].set_lim_up(list_temp[i + 1].get_up() + x)

    wm_to_file(list_temp, str(perc) + "_perc_" + filename)
    sim = cosine_simil(list_o, list_temp)
    print("------Percentage Attack-----\n")
    print("similarity: ", sim, " total changes: ", (count * 100) / len(list_w))
    # print(list_temp)
    return list_temp, sim

def test_destroy(filename,perc,rnd,p,budget,threshold,threshold_ver):
    ch, el, chosen_list = wm_insert_optimal(filename, rnd, p, budget)
    x=[]
    y=[]
    wm_name="wmfiles/WM_"+filename
    for i in range(len(perc)):
        list_un, simi = destroy_percentage(wm_name, perc[i])
        atck_filename=str(perc[i])+"_uncntrl_"+wm_name
        result, verified = wm_verify(atck_filename,threshold, threshold_ver, chosen_list, rnd, p)
        y.append(verified)
        x.append(perc[i])
        print("result: ", result, " Total count: ", verified)

    draw_plot(x,'Percentage',y,'Success Rate','Robustness Against Destroy Attack')

def test_percentage_total(rnd,p,percentage):
    wm_bit = [1, 1, 0, 1, 0]
    ch, el, chosen_list = wm_insert_optimal("wmfiles/new_s_0_5_1M.txt", rnd, p, budget=2)
    res_obtwm10=[]
    res_freqy10=[]
    res_obtwm30 = []
    res_freqy30 = []
    res_obtwm50 = []
    res_freqy50 = []
    res_obtwm60 = []
    res_freqy60 = []
    res_obtwm80 = []
    res_freqy80 = []
    res_obtwm90 = []
    res_freqy90 = []


    for j in range(100):
       for i in range(len(percentage)):
           destroy_percentage_total("wmfiles/WM_new_s_0_5_1M.txt",percentage[i])

       result, verified = wm_verify("wmfiles/10_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy10.append(verified)
       result, verified = wm_verify("wmfiles/30_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy30.append(verified)
       result, verified = wm_verify("wmfiles/50_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy50.append(verified)
       result, verified = wm_verify("wmfiles/60_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy60.append(verified)
       result, verified = wm_verify("wmfiles/80_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy80.append(verified)
       result, verified = wm_verify("wmfiles/90_total_WM_new_s_0_5_1M.txt", 50, 4, chosen_list, rnd, p)
       res_freqy90.append(verified)


    mean_freqy=[statistics.mean(res_freqy10),statistics.mean(res_freqy30),statistics.mean(res_freqy50),statistics.mean(res_freqy60),statistics.mean(res_freqy80),statistics.mean(res_freqy90)]
    print("FreqyWM: ",mean_freqy)



def draw_plot(x, xname, y, yname, plotname):
        """
        Make sure that the sizes of x and y are the same.
        Make sure that linename has enough number of names
        :param x: a matrix holds x values e.g. : x = [[1, 2, 3],[1, 2, 3],[8, 12, 13]]
        :param xname: name of the x-axis
        :param y: a matrix holds y values e.g. : y = [[2, 4, 1],[4, 1, 3],[3, 5, 7]]
        :param yname: name of the y-axis
        :param plotname: name of the plot
        :return: returns a plot with the possibility of multiple lines in one plot
        """
        #for i in range(len(x)):
        #    plt.plot(x[i], y[i])
        plt.rc('font', size=15)
        plt.plot(x, y,'g-o',linewidth=5)
        # print(x[0])
        # print(y[0])
        # :param linename: an array consists of the names given to each line e.g., linename=['line-1','line-2','line-3']
        # plt.plot(x[0], y[0], label=linename[0])
        # plt.plot(x[1], y[1], label=linename[1])
        # plt.plot(x[2], y[2], label=linename[2])
        plt.xlabel(xname)
        # naming the y axis
        plt.ylabel(yname)
        # giving a title to my graph
        plt.title(plotname)
        # show a legend on the plot
        plt.legend()
        #plt.update_layout(xaxis_type="log", yaxis_type="log")
        # function to show the plot
        plt.show()



rnd=94150602964623730173619679764343462318710907258738770672733287463602813493207
z=1031 #131
budget=2

percen=[10,30,50,60,80,90]
test_percentage_total(rnd,z,percen)
