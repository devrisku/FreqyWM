import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
import math
import statistics
import secrets
import hashlib
import networkx as nx
import random
from collections import Counter
import matplotlib.pyplot as plt
class token:
    def __init__(self, token_name, freq):
        self.token_name = token_name
        self.freq = freq
    def display(self):
        new_value = self.token_name + str(self.freq)
        print(new_value)
    def get_freq(self):
        return int(float(self.freq))
    def set_freq(self, freq_new):
        self.freq = str(freq_new)
    def __repr__(self):
        return f'token_name: {self.token_name} freq: {self.freq}'
    def get_name(self):
        return self.token_name
class wm_token(token):
    # list_url= []
    def __init__(self, token_name, freq, lim_up, lim_down):
        super().__init__(token_name, freq)
        self.lim_up = lim_up  # self.set_lim_up(list)
        self.lim_down = lim_down  # self.lim_down = lim_down # self.set_lim_down(list)

    # self.list=list use it as []
    def __repr__(self):
        return f'token_name: {self.token_name} freq: {self.freq},lim_up: {self.lim_up}, lim_down: {self.lim_down}'
        # % ( self.domain_name, self.freq, self.lim_up, self.lim_down)

    def set_lim_up(self, lim_up_new):
        self.lim_up = lim_up_new

    def set_lim_down(self, lim_down_new):
        self.lim_down = lim_down_new

    def get_up(self):
        if self.lim_up==np.infty:
            return np.infty
        else:
            return int(self.lim_up)

    def get_down(self):
        return int(self.lim_down)

    def up_bound_check(self, val):
        if val >= int(self.lim_up):
            print("ERROR: Up-limit has been exceeded!!")
            return False
        else:
            return True

    def down_bound_check(self, val):
        if val <= int(self.lim_down):
            print("ERROR: Down-limit has been exceeded!!!")
            return False
        else:
            return True
def read_from_pairs(filename):
    pair_file = open(filename, 'r')
    pairs=[]
    for line in pair_file:
        line2 = line.split(',')
        #print(str(line2[0]), str(line2[1]).strip('\n'))
        pairs.append([str(line2[0]),str(line2[1]).strip('\n')])
        #t = url(line2[0], line2[1])
        #pairs.append(t)
    pair_file.close()
    return pairs
def read_from_file(filename):
    '''
     :param filename: File is two-dimensional (e.g., url1,1800) where each attribute is separated by a comma
     :return:return the file as a list
    '''
    file1 = open(filename, 'r')
    #list_or = {}
    list_or = []
    # Using for loop
    for line in file1:
        line2 = line.split(',')
        #print(line2[0], "", line2[1])
        t= token(line2[0], line2[1])
        list_or.append(t)
        #list_or[line2[0]]=line2[1]
    file1.close()
    return list_or
def wm_to_file(list_w,filename):
    '''
    :param list_w: watermarked histogram as a list of tokens
    :param filename: filename for watermarked data, e.g. wm_filename.txt
    :return: creates a .txt file to save watermarked histogram data.
    '''
    output = open(filename, "w")
    for element in list_w:
        dn=element.token_name
        fr=str(element.get_freq())
        sng=dn+','+fr
        output.write(sng+"\n")
    output.close()
def wmpair_to_file(pairs,filename):
    '''
    :param pairs: chosen pairs for watermarking which will be stored a secret
    :param filename: filename to save the chosen pairs as
    :return: creates a .txt file to save secret chosen pairs needed for verification
    '''
    output = open(filename, "w")
    for element in pairs:
        pair=str(element[0]+","+element[1])
        output.write(pair+"\n")
    output.close()
def histogram_gen(filename,groupname):
    '''
    :param filename: Dataset to generate histogram from [.csv, .txt, etc.]
    :param groupname: Token definition as a list ['url',...] ['age','gender']
    :return: Saves the histogram to a txt file where the frequencies are sorted in descending order.
    '''
    file=pd.read_csv(filename)#,sep=' ')
    df=pd.DataFrame(file)
    #print(df)
    #group_object = df.groupby(groupname)
    list_req = list(df.groupby(groupname).groups.keys())
    list_req_count = df.groupby(groupname).size().sort_values(ascending=False)
    list_fin=[]
    #print(len(list_req))
    for i in range(len(list_req)):
        list_fin.append([list_req[i],list_req_count.__getitem__(list_req[i])])

    list_fin.sort(key = lambda i: i[1],reverse = True)
    #write_to_file(list_fin, 'groupby_'+groupname+filename)
    print(list_fin)
    return list_fin
def key_gen(security_param):
    '''
    :param security_param: security parameter
    :return: generates a random value with the given security parameter
    '''
    return secrets.randbits(security_param)
def limit_cal(list_or):
    list_wm = []
    for index, obj in enumerate(list_or):
        lim_up = 0
        lim_down = 0

        if index == 0:
            lim_up = np.infty
            lim_down = int(list_or[0].freq) - int(list_or[1].freq)
            # print(str(lim_down))
            list_wm.append(wm_token(list_or[index].token_name, list_or[index].freq, lim_up, lim_down))
            # print([list_wm[0]])
        elif index > 0 and index < len(list_or) - 1:
            lim_up = int(list_or[index - 1].freq) - int(list_or[index].freq)
            # print(list_or[index-1].freq+ "-"+list_or[index].freq+ "="+str(lim_up))
            lim_down = int(list_or[index].freq) - int(list_or[index + 1].freq)
            # print(str(lim_down))
            list_wm.append(wm_token(list_or[index].token_name, list_or[index].freq, lim_up, lim_down))
        else:
            lim_up = int(list_or[index - 1].freq) - int(list_or[index].freq)
            lim_down = 0
            list_wm.append(wm_token(list_or[index].token_name, list_or[index].freq, lim_up, lim_down))
            # print("index: " + str(index))
    return list_wm
def check_el(tkn, n):
    if (tkn.get_up() > np.floor(n/2)) and (tkn.get_down() > np.floor(n/2) ) and n!=0 and n!=1:
        return True
    else:
        return False
def get_index(mark,tkn):
    for i in range(len(mark)):
        if  mark[i][0]==tkn:
            return mark[i][1],i
    return -1,-1
def get_index_list(list,tkn):
    for i in range(len(list)):
        if list[i].get_name()==tkn:
            return list[i].get_freq(),i
    return -1,-1
def cosine_simil(list_o, list_w):
    list_o_1, list_w_1 = [], []
    for i in range(len(list_o)):
        list_o_1.append(list_o[i].get_freq())
        list_w_1.append(list_w[i].get_freq())
    cos_sim = dot(list_o_1, list_w_1) / (norm(list_o_1) * norm(list_w_1))
    cos_sim = cos_sim * 100
    return cos_sim
def check_sim(list_o, list_w, sim):
    '''
    :param list_o: original histogram
    :param list_w: watermarked histogram
    :param sim: budget
    :return: Checks if the similarity limit between wm-data and original data
               has reached the given similarity tolerance/budget.
    '''
    sim_r = (100 - cosine_simil(list_o, list_w))
    if sim_r <= sim:
        return True
    else:
        return False
def write_to_file(list,filename):
    output = open(filename, "w")
    cnt = 1
    for element in list:
        fr = str(element)
        output.write(fr + "\n")
        cnt = cnt + 1
    output.close()
def create_data(filename):
    file1 = open(filename, 'r')
    list_or = []
    # Using for loop
    for line in file1:
        line2 = line.split(',')
        # print(line2[0], "", line2[1])
        t = token(line2[0], line2[1])
        for i in range(int(t.freq)):
            list_or.append(t.domain_name)
    file1.close()
    name="sample_"+filename
    #name="data_new_s_1_1M.txt"
    write_to_file(list_or,name)
def read_from_file_to_list(filename):
    file1 = open(filename, 'r')
    list_or = []
    # Using for loop
    for line in file1:
        #line2 = line.split(',')
        #print(line2[0], "", line2[1])
        #t= url(line2[0], line2[1])
        list_or.append(str(line.strip('\n')))
       # print([t])
        # print("xxx---",[list_or[0]])
    file1.close()
    #list_ow = limit_cal(list_or)
    return list_or #, list_ow
def create_histogram(sampledata):
    list_hist=[]
    counter_object = Counter(sampledata)
    distinct_tokens=set(sampledata)
    counts = Counter(sampledata)
    for i in distinct_tokens:
        tk_with_freq = token(i, int(counts[i]))
        #print(url_with_freq)
        list_hist.append(tk_with_freq)
    return list_hist
def sampling_data(percentage,file):
    list_data=read_from_file_to_list(file)
   # print(float(len(list_data))*percentage/100)
    original_sample_size = float(len(list_data))
    sample_size = original_sample_size*percentage/100
    sample_data = random.sample(list_data, int(sample_size))
    histogram_data = create_histogram(sample_data)
    print("Extraction of sample with percentage:",str(percentage),"Unique urls in the subsample:",len(histogram_data)," Total subsample size: ",len(sample_data))
    return sample_data, histogram_data, original_sample_size
def oversampling_data(wanted_samplesize,sample):
    oversampled_data = np.random.choice(sample, wanted_samplesize, replace=True)
    histogram_data = create_histogram(oversampled_data)
    print("Oversample size:", len(oversampled_data), "Size of subsample:", len(sample), "Unique urls in oversampled:",len(histogram_data))
    return oversampled_data, histogram_data
def remove_values_from_list(the_list, val):
    remaining_sample = the_list
    the_list.remove()
    for i in range(len(val)):
        remaining_sample = [value for value in remaining_sample if value != val[i]]
    return remaining_sample
def remove_token_from_hist(histogram_list, selected_to_drop):
    remaining_sample_histogram = histogram_list
    for i in range(len(selected_to_drop)):
        remaining_sample_histogram.remove(selected_to_drop[i])
    return remaining_sample_histogram
def sampling_histogram(file,numberofdeletedtokens): #delete a number of unique tokens from the histogram
    #list_data = read_from_file_to_list(file)
    #histogram_list=create_histogram(list_data)
    # list of urls
    #unique_urls = set(list_data)
    #selected_to_drop = random.sample(unique_urls,numberofdeletedtokens)
    #sample_hist_data = remove_values_from_list(histogram_list,selected_to_drop)
    #histogram_data = create_histogram(sample_data)
    histogram_list,wm_list = read_from_file(file) # file is a histogram now
    selected_to_drop = random.sample(histogram_list, numberofdeletedtokens)
    print(selected_to_drop)
    sample_hist_data = remove_token_from_hist(histogram_list, selected_to_drop)
    return sample_hist_data
def draw_plot_multiple(x,xname,y,yname,linename,plotname,savename):
    """
    !!!Make sure that the sizes of x and y are the same.
    !!!Make sure that linename has enough number of names
    :param x: a matrix holds x values e.g. : x = [[1, 2, 3],[1, 2, 3],[8, 12, 13]]
    :param xname: name of the x-axis
    :param y: a matrix holds y values e.g. : y = [[2, 4, 1],[4, 1, 3],[3, 5, 7]]
    :param yname: name of the y-axis
    :param linename: an array consists of the names given to each line e.g., linename=['line-1','line-2','line-3']
    :param plotname: name of the plot
    :param savename: name of the png file
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
    plt.title(plotname)
    # show a legend on the plot
    plt.legend(loc='lower right')
    name=savename+'.png'
    plt.savefig(name)
    # function to show the plot
    plt.show()
    #x, np.log(x), 'g'
''' ***********METHODS NEEDED FOR OPTIMAL FreqyWM********'''
def create_graph(el_items, max):
    G = nx.Graph()
    for i in range(len(el_items)):
        # for j in range(len(el_items)):
        G.add_edge(el_items[i][0].get_name(), el_items[i][1].get_name(), weight=max - el_items[i][2])
    val = [G.__sizeof__()]
    for i in range(len(val)):
        val[i] = 1
    return G, val

#maximum weight  matching result on graph G
def mwm(G):
    mwm_matching=nx.max_weight_matching(G,maxcardinality=False)
    return mwm_matching

def create_list(mwm_match,el_item,max):
    list_mwm=[]
    result=[]
    for e in mwm_match:
       list_mwm.append([e[0],e[1]])

    #print(list_mwm[0])
    for i in range(len(el_item)):
        for j in range(len(list_mwm)):
            if (el_item[i][0].get_name()==list_mwm[j][0] or el_item[i][0].get_name()==list_mwm[j][1]) and (el_item[i][1].get_name()==list_mwm[j][0] or el_item[i][1].get_name()==list_mwm[j][1]):
                result.append(el_item[i])
                break

    return result

''' ***********METHODS NEEDED FOR OBTWM********'''
def obtwm_to_file(list_w,filename):
    '''
    :param list_w: watermarked histogram as a list of tokens
    :param filename: filename for watermarked data, e.g. wm_filename.txt
    :return: creates a .txt file to save watermarked histogram data.
    '''
    file=filename.split('.')
    filename=file+'_obtwm.txt'
    output = open(filename, "w")
    for i in range(len(list_w)):
        for j in range(len(list_w[i])):
            sng = list_w[i][j][0] + ',' + str(list_w[i][j][1])
        output.write(sng+"\n")
    output.close()

def mean_and_stdev(partition):
    values = []
    for i in range(len(partition)):
        values.append(partition[i][1])
    mean = statistics.mean(values)
    std = statistics.stdev(values)
        # values.insert(0,r)
        # values.append(mean)
        # values.append(std)
    return mean, std, values

def sigmoid(x,alpha,ref):
    try:
        sig = 1 - (1 / (1 + math.exp(alpha * (x - ref))))
    except OverflowError:
       if (alpha * (x - ref))<0:
           sig=0
       elif (alpha * (x - ref))>0:
           sig=1
       else:
           sig=0.5
    return sig

def sigmoid_calculation(partition,alpha,condition):
    '''
    :param part: a partition
    :param alpha: the value used for computing sum of sigmoid functions
    :param condition: condition, same as the one used for watermark insertion
                      to compute the reference point for the given partition , is a real value between [0,1]
    :return: the sum of sigmoid functions for given partition
    '''
    value=0
    mean,stdev,values=mean_and_stdev(partition)
    ref=mean+condition*stdev
    #print("ref: ",ref)
    total=0
    for i in range(len(values)):
        total=total+sigmoid(values[i],alpha,ref)
    value=total/len(values)
    return value

def find_partition(list,r):
    '''
    :param list: list of partitions
    :param r: partition number
    :return: rth partition
    '''
    res=[]
    part_r = [i for i in range(len(list)) if list[i][2] == r]
    for i in part_r:
        res.append([list[i][0],list[i][1]])
    return res

def get_partition(list,rnd,part_num):
    '''
    :param list: a database/histogram
    :param rnd: a high entropy secret
    :param part_num: the number of partitions
    :return: partitions with the size of part_num
    '''
    part_list=[]
    for i in range(len(list)):
        in_msg = list[i].get_name() + " " + str(rnd)
        # MAC(K,m)=H(K,h(K,m))
        hash_inner = hashlib.sha256(in_msg.encode('utf-8')).hexdigest()
        out_msg=hash_inner+" "+str(rnd)
        hash_final=hashlib.sha256(out_msg.encode('utf-8')).hexdigest()
        num_hash = int(hash_final, 16)
        r=num_hash % part_num
        #print("Des. location of ",list[i][0]," ",i, " -> ",r)
        part_list.append([list[i].get_name(),list[i].get_freq(),r])
    return part_list

def obtwm_verify(filename,rnd,w,part_num,opt_t,condition,part_size):
    '''
    :param filename: name of the file we want to run the exp./verification on
    :param rnd: the high entropy secret
    :param w: watermark e.g. w=[0,1,1,1,0]
    :param part_num: the number of partitions (e.g. 20)
    :param opt_t: T* in the paper that is a threshold for minimizing the decode error.
    :param condition: c value (e.g., 0.75)
    :param part_size: minimum size that a partition should have (e.g. 2)
    :return:
    '''
    w_det=[0 for x in range(len(w))]
    zeros=[0 for x in range(len(w))]
    ones=[0 for x in range(len(w))]
    list_o=filename # Comment list_o, list_w = read_from_file(filename) and set list_o=filenam where filename is a list.
    #Otherwise we can create another function where filename is replaced with a list
    #list_o, list_w = read_from_file(filename)
    list_part=get_partition(list_o,rnd,part_num)
    for i in range(part_num):
        part = find_partition(list_part, i)
        if len(part) >= part_size:
            r= i % len(w)
            value=sigmoid_calculation(part,alpha=5,condition=0.75)
            #print("Num Part: ",i," value: ",value,"pos: ",r)
            if value >= opt_t:
                ones[r]=ones[r]+1
            else:
                zeros[r]=zeros[r]+1
    for i in range(len(w)):
        if ones[i]>zeros[i]:
            w_det[i]=1
        elif ones[i]<zeros[i]:
            w_det[i]=0
        else:
            w_det[i]=9 #9 represents x in the paper which represents erasures
    count=0
    #print("Watermark: ",w)
   # print("Watermark length: ", len(w))
    for i in range(len(w)):
       # print("MVote: ", w_det[i])
        if w[i]==w_det[i]:
          #  print("MVote: ",w[i])
            count=count+1
    succ_rate=count/len(w)*100
    #print("Success rate: ",succ_rate)
    #return w_det,succ_rate
    return succ_rate

