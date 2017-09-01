# -*- coding: utf-8 -*-

import json, re
import matplotlib.pyplot as plt
from datetime import datetime


def generate_date(twitter_status, name_text):
    date = datetime.now().strftime('%m%d%H')
    for status in sorted(set(twitter_status)):
        x = date
        y = twitter_status[status]
        date_directory_filename = "./date/"+name_text+"/"+name_text+'_'+re.sub('TC_2017|TC2017_','',status)+'.txt'
        f = open(date_directory_filename, 'a')
        f.write(date+','+str(twitter_status[status])+'\r\n')
    f.close()


def generate_graf(twitter_status, name_text):
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    x_label = []

    for status in sorted(set(twitter_status)):
        date_directory_filename = "./date/"+name_text+"/"+name_text+'_'+re.sub('TC_2017|TC2017_','',status)+".txt"
        f = open(date_directory_filename,"r")
        x = []
        y = []

        for i,date_and_count in enumerate(f):
            date_separate_count = date_and_count.split(',')
            x = x + [i]
            y = y + [date_separate_count[1]]
            x_label = x_label + [date_separate_count[0]]
        ax.plot(x, y,'-',label=re.sub('TC_2017|TC2017_','',status))   
    f.close()

    plt.title(name_text)
    plt.legend(loc='lower left')
    plt.xlabel("date")
    ax.set_xticklabels(x_label,rotation =30,fontsize ="small")
    plt.ylabel(name_text)

    graf_directory = "./graf/"
    plt.savefig(graf_directory+"graf_"+name_text+".png")
    plt.clf()

def generate(twitter_status,name_text):
    generate_date(twitter_status, name_text)
    generate_graf(twitter_status, name_text)

