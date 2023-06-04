# This is a sample Python script.
# Author-Copyright: Devriş İşler IMDEA Networks
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from methods import *
from freqywm_verify import *
import sys
sys.setrecursionlimit(5000)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def test_verification(wm_files, pair_files, rnd, z,optionsample,optionverylowsample,optiondroping1,rep,deletionmax):
    '''
    :param wm_files: name of the file that would be tested against sampling e.g., "wmfiles/data_new_s_0_5_1M.txt"
    :param pair_files: chosen pairs for watermarking, e.g., "wmfiles/chosen_pairs_new_s_0_5_1M.txt"
    :param threshold: threshold needed to accept a pair as a watermarked (t=2)
    :param threshold_ver: threshold needed to accept a dataset as a watermarked ([0,100])
    :param rnd: the high entropy secret generated during wm generation and  needed for verification
    :param z: is used to create for s_{ij} values e.g., s_{ij}=Hash(url_i||url_j||rnd) mod p
    :return: returns
    '''
    #figure/plot
    #creating a sampled data with a percentage perc from the given file wm_files
    #returns the histogram of the sampled data

    # reads the associated chosen pairs, from the correct file, that are needed for verification
    #t=0,1,2,4,10

    pairs = read_from_pairs(pair_files)

    if optionsample==1:
        #x = [10, 20, 30, 50, 70, 90]
        #x = [ 1, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90]
        x = [20, 90]
        x1 = [x, x, x, x, x, x]
        y = []
        y_over = []

    if optionverylowsample==1:
        # 0.0009 ### this case is the one with less unique urls
        #x = np.arange(0.0007, 1.01, step=0.05)  # for very low sample size
        x = np.arange(0.0007, 0.51, step=0.05)
        x1 = [x, x, x, x, x, x]
        y = []
        y_over = []


    if optiondroping1 == 1:
        x = range(deletionmax) # number of deleted tokens
        x1 = [x, x, x, x, x]
        y = []

    # averaged results
    T0 = []
    T1 = []
    T2 = []
    T4 = []
    T10 = []
    T_opt = []

    # averaged results of oversampling
    oT0 = []
    oT1 = []
    oT2 = []
    oT4 = []
    oT10 = []

    # averaged nonfound sample
    N0 = []
    N1 = []
    N2 = []
    N4 = []
    N10 = []


    # averaged nonfound oversample
    oN0 = []
    oN1 = []
    oN2 = []
    oN4 = []
    oN10 = []

    """
    # standard deviations
    S0 = []
    S1 = []
    S2 = []
    S4 = []
    S10 = []
    """

    # Only for example 1: sample attack, very low sample and oversampling
    if (optiondroping1 == 0):
        for i in range(len(x)): # for each percentage
            # reset the sampling arguments
            t0 = []
            t1 = []
            t2 = []
            t4 = []
            t10 = []
            opt_wm = []


            # reset the oversampling arguments
            ot0 = []
            ot1 = []
            ot2 = []
            ot4 = []
            ot10 = []
            o_opt_wm = []


            # reset the non-found arguments for sample
            n0 = []
            n1 = []
            n2 = []
            n4 = []
            n10 = []


            # reset the non-found arguments for oversample
            on0 = []
            on1 = []
            on2 = []
            on4 = []
            on10 = []


            for j in range(rep): #  rep is the number of repetitions to later compute averaged results

                ### Sampling and very low sampling examples:
                if (optionsample == 1) or (optionverylowsample == 1):

                    # Opt method
                    sampled_data_opt, list_hist_opt, original_sample_size_opt = sampling_data(x[i], file='wmfiles/data_obtwm_0_5_1M.txt')

                    #new try devris
                    #sampled_data_opt, list_hist_opt, original_sample_size_opt = sampling_data(x[i], file='wmfiles/new_s_0_7_1M.txt')
                    #sampled_data_opt, list_hist_opt, original_sample_size_opt = sampling_data(x[i], file='wmfiles/data_new_s_0_5_1M.txt')



                    ### Verification algorithm for the sample
                    rate_opt = obtwm_verify(list_hist_opt, rnd, w=[1,1,0,1,0], part_num=20, opt_t=0.0966, condition=0.75, part_size=7)
                    opt_wm.append(rate_opt)



                    # Freqy method:
                    sampled_data, list_hist, original_sample_size = sampling_data(x[i], wm_files)

                    #new save histogram of sample
                    if i==0:
                        write_to_file(list_hist, "sample_20_histogram.txt")
                    if i==1:
                        write_to_file(list_hist, "sample_90_histogram.txt")


                    ### Verification algorithm for the sample
                    res0, rate0, non0 = wm_verify_hist(list_hist, 50, 0, pairs, rnd, z)
                    t0.append(rate0)
                    n0.append(non0)

                    res1, rate1, non1 = wm_verify_hist(list_hist, 50, 1, pairs, rnd, z)
                    t1.append(rate1)
                    n1.append(non1)

                    res2, rate2, non2 = wm_verify_hist(list_hist, 50, 2, pairs, rnd, z)
                    t2.append(rate2)
                    n2.append(non2)

                    res4, rate4, non4 = wm_verify_hist(list_hist, 50, 4, pairs, rnd, z)
                    t4.append(rate4)
                    n4.append(non4)

                    res10, rate10, non10 = wm_verify_hist(list_hist, 50, 10, pairs, rnd, z)
                    t10.append(rate10)
                    n10.append(non10)

                    ### This is to compute the oversampling of the extracted subsample, to reach the size of the

                    # Original data from which the sample was extracted:
                    wanted_sample_size = int(original_sample_size) - int(len(sampled_data))
                    oversampled_data, list_hist_oversampled = oversampling_data(wanted_sample_size, sampled_data)

                    # Verification algorithm for the oversampled data
                    ores0, orate0, onon0 = wm_verify_hist(list_hist_oversampled, 50, 0, pairs, rnd, z)
                    ot0.append(orate0)
                    on0.append(onon0)

                    ores1, orate1, onon1 = wm_verify_hist(list_hist_oversampled, 50, 1, pairs, rnd, z)
                    ot1.append(orate1)
                    on1.append(onon1)

                    ores2, orate2, onon2 = wm_verify_hist(list_hist_oversampled, 50, 2, pairs, rnd, z)
                    ot2.append(orate2)
                    on2.append(onon2)

                    ores4, orate4, onon4 = wm_verify_hist(list_hist_oversampled, 50, 4, pairs, rnd, z)
                    ot4.append(orate4)
                    on4.append(onon4)

                    ores10, orate10, onon10 = wm_verify_hist(list_hist_oversampled, 50, 10, pairs, rnd, z)
                    ot10.append(orate10)
                    on10.append(onon10)





            print("Repetition", j+1, "with Percentage", x[i], "%",  "\n")

            # compute the averaged of t0, t1, etc
            T_opt.append(np.mean(opt_wm))

            T0.append(np.mean(t0))
            N0.append(np.mean(n0))
            T1.append(np.mean(t1))
            N1.append(np.mean(n1))
            T2.append(np.mean(t2))
            N2.append(np.mean(n2))
            T4.append(np.mean(t4))
            N4.append(np.mean(n4))
            T10.append(np.mean(t10))
            N10.append(np.mean(n10))

            print("Non-found url pairs averaged")
            print(N0)
            print(N1)
            print(N2)
            print(N4)
            print(N10)

            print("Results Sample")
            print(T0)
            print(T1)
            print(T2)
            print(T4)
            print(T10)
            print(T_opt)



            if optiondroping1 == 0:
                # compute the averaged of ot0, ot1, etc
                oT0.append(np.mean(ot0))
                oN0.append(np.mean(on0))
                oT1.append(np.mean(ot1))
                oN1.append(np.mean(on1))
                oT2.append(np.mean(ot2))
                oN2.append(np.mean(on2))
                oT4.append(np.mean(ot4))
                oN4.append(np.mean(on4))
                oT10.append(np.mean(ot10))
                oN10.append(np.mean(on10))
                print("Results Oversample")
                print(oT0)
                print(oT1)
                print(oT2)
                print(oT4)
                print(oT10)

            """
            # compute the standard deviation of t0, t1, etc
            S0.append(np.std(t0))
            S1.append(np.std(t1))
            S2.append(np.std(t2))
            S4.append(np.std(t4))
            S10.append(np.std(t10))
            """

    # Only for example 2: deleting attack
    if optiondroping1 == 1: # this runs only for the delete attack
        for i in range(len(x)):  # for each number of deleted tokens
            # reset the sampling arguments
            t0 = []
            t1 = []
            t2 = []
            t4 = []
            t10 = []
            # reset the non-found arguments for sample
            n0 = []
            n1 = []
            n2 = []
            n4 = []
            n10 = []

            for j in range(rep):  # rep is the number of repetitions to later compute averaged results

                list_hist = sampling_histogram(wm_files, x[i]) #sample from the histogram. x[i] is the # of deleted tokens

                ### Verification algorithm for the sample
                res0, rate0, non0 = wm_verify_hist(list_hist, 50, 0, pairs, rnd, z)
                t0.append(rate0)
                n0.append(non0)

                res1, rate1, non1 = wm_verify_hist(list_hist, 50, 1, pairs, rnd, z)
                t1.append(rate1)
                n1.append(non1)

                res2, rate2, non2 = wm_verify_hist(list_hist, 50, 2, pairs, rnd, z)
                t2.append(rate2)
                n2.append(non2)

                res4, rate4, non4 = wm_verify_hist(list_hist, 50, 4, pairs, rnd, z)
                t4.append(rate4)
                n4.append(non4)

                res10, rate10, non10 = wm_verify_hist(list_hist, 50, 10, pairs, rnd, z)
                t10.append(rate10)
                n10.append(non10)

            print("Repetition", j + 1, "with Tokens deleted:", x[i],  "\n")

            # compute the averaged of t0, t1, etc
            T0.append(np.mean(t0))
            N0.append(np.mean(n0))
            T1.append(np.mean(t1))
            N1.append(np.mean(n1))
            T2.append(np.mean(t2))
            N2.append(np.mean(n2))
            T4.append(np.mean(t4))
            N4.append(np.mean(n4))
            T10.append(np.mean(t10))
            N10.append(np.mean(n10))

        print("Non-found url pairs averaged")
        print(N0)
        print(N1)
        print(N2)
        print(N4)
        print(N10)

        print("Results Sample")
        print(T0)
        print(T1)
        print(T2)
        print(T4)
        print(T10)




    # The order is important
    # sample results for plot
    # average
    y.append(T0)
    y.append(T1)
    y.append(T2)
    y.append(T4)
    y.append(T10)
    y.append(T_opt)





    """
    # std
    y2.append(S0)
    y2.append(S1)
    y2.append(S2)
    y2.append(S4)
    y2.append(S10)
    """

    if optiondroping1 == 0:
        # oversample results for plot
        y_over.append(oT0)
        y_over.append(oT1)
        y_over.append(oT2)
        y_over.append(oT4)
        y_over.append(oT10)


    if optionverylowsample == 1:
        x_nonfound = N0

    # sampling
    if (optionsample == 1) or (optionverylowsample == 1):
        plot_title = 'Sampling Attack with ' + '\u03B1=0.5 N=1K S=1M'

        draw_plot_multiple(x1, 'Attack sample size (%)', y, 'Averaged success rate (%)', ['t=0', 't=1', 't=2', 't=4', 't=10', 'WM-OBT'], plot_title,savename='sampledall')

    # very low sample. graph with x-axis  = unique urls non-found
    if optionverylowsample == 1:
        plot_title = 'Sampling Attack with ' + '\u03B1=0.5 N=1K S=1M'
        x_nonfound = [N0, N1, N2, N4, N10]
        draw_plot_multiple(x_nonfound, 'Number of unique tokes not-found', y, 'Averaged accepted pairs (%)', ['t=0', 't=1', 't=2', 't=4', 't=10','WM-OBT'], plot_title,savename='sampledall')


    # oversample only if not droping
    if (optiondroping1 == 0):
        plot_title = 'Oversampling the Sampling Attack with ' + '\u03B1=0.5 N=1K S=1M'

        draw_plot_multiple(x1, 'Attack sample size (%)', y_over, 'Averaged accepted pairs (%)',
                           ['t=0', 't=1', 't=2', 't=4', 't=10', ], plot_title, savename='sampledall')


    if optiondroping1 == 1:
        plot_title = 'Deletion of tokens attack with ' + '\u03B1=0.5 N=1K S=1M'
        draw_plot_multiple(x1, 'Number of tokens deleted', y, 'Averaged accepted pairs (%)',
                          ['t=0', 't=1', 't=2', 't=4', 't=10','WM-OBT'], plot_title, savename='sampledall')
        #print('x1:', x1)
        #print('y:', y)
    # standard deviation of the sampling
    #plot_title = 'Sampling Attack with ' + '\u03B1=0.5 N=1K S=1M'

    #draw_plot_multiple(x1, 'Attack sample size (%)', y2, 'Standard deviation of accepted pairs (%)', ['t=0', 't=1', 't=2', 't=4', 't=10'],
    #                   plot_title, savename='sampledall2')



    #print("Sample results ", y,  "\n")
    #print("Overample results ", y_over,  "\n")
    #end of the test_verification function



#def test_verification_single(sample,t,k,..)
rnd=94150602964623730173619679764343462318710907258738770672733287463602813493207
z=131 #131 #1031 #1001#631#231 #2671 #3911
#pr=[10,33,393,631,1031,2671] #,2671,5001]

wm_pair_files=["wmfiles/chosen_pairs_new_s_0_05_1M.txt","wmfiles/chosen_pairs_new_s_0_2_1M.txt","wmfiles/chosen_pairs_new_s_0_5_1M.txt","wmfiles/chosen_pairs_new_s_0_7_1M.txt","wmfiles/chosen_pairs_new_s_0_9_1M.txt","wmfiles/chosen_pairs_new_s_1_1M.txt"]
wmfiles=["wmfiles/WM_new_s_0_05_1M.txt","wmfiles/WM_new_s_0_2_1M.txt","wmfiles/WM_new_s_0_5_1M.txt","wmfiles/WM_new_s_0_7_1M.txt","wmfiles/WM_new_s_0_9_1M.txt","wmfiles/WM_new_s_1_1M.txt"]
datafile=["wmfiles/data_new_s_0_05_1M.txt","wmfiles/data_new_s_0_2_1M.txt","wmfiles/data_new_s_0_5_1M.txt","wmfiles/data_new_s_0_7_1M.txt","wmfiles/data_new_s_0_9_1M.txt","wmfiles/data_new_s_1_1M.txt"]
test_verification(datafile[2],wm_pair_files[2],rnd,z,1,0,0,rep=1,deletionmax=500)
#files_sampled_50=["wmfiles/Sampled_50_new_s_0_5_1M.txt"]
#read_from_pairs("wmfiles/chosen_pairs_new_s_0_05_1M.txt")

#test for alpha=0.5
#1,0,0: option sample YES, option very low sample NO, optiondroping1 NO
# last argument is the number of repetitions

# Test alpha 0.5 and regular sampling (1,0,0), 100 repetitions:


#Test droping
#test_verification(wmfiles[1],wm_pair_files[1],rnd,p,0,0,1,rep=100,deletionmax=999)

#to-do: try the delete and the sample