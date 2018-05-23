# coding: utf-8

import io
import os
import sys
import array
from matplotlib import pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
import wfdb
from zetlabreader import load_xml_header
from zetlabreader import anaread
from zetlabreader import readint
from zetlabreader import readshort

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        count = len(files) #считаем, сколько в командную строку ввели файлов
        #print("count=")
        #print(count)
        sig = np.array([]) #создаем пустой массив-строку
        for fn in files:
            d, fs, n = anaread(fn)
            #print("d=")
            #print(d)
            sig = np.concatenate((sig, d)) #накапливаем в пустой массив-строку данные, полученные из обрабатываемых файлов
            #print("sig=")
            #print(sig)
        
        sigsplit = np.hsplit(sig, count) #дробим массив sig, в котором записаны данные всех файлов, на строки, число которых равно число файлов
        #print("sigsplit=")
        #print(sigsplit)
        signal = np.transpose(sigsplit) #транспонтруем полученный ранее полученный массив (далее его и отправим в wrsamp) 
        #print("signal=")
        #print(signal)
        
        wfdb.wrsamp("name", fs = 2000, units=["mV"]*count,
                    sig_name=["name1", "name2", "name3"],
                    p_signal = signal, fmt=["16"]*count, write_dir="directory\name")
        
        signals, fields = wfdb.rdsamp("directory\name", sampfrom=0, sampto="end", channels="all")

        fs = 2000
        t = np.arange(0, len(signals)/fs, 1.0/fs)
        plt.plot(t, signals)
        plt.xlim([540, 545])
        plt.title("plot")
        print("Look at the plots")
        plt.show()
        
    else:
        print("Задайте несколько файлов")
