# coding: utf-8

import io
import os
import sys
import array
from matplotlib import pyplot as plt
import numpy as np
import xml.etree.ElementTree as ET
import wfdb
from zetlabreadern import load_xml_header
from zetlabreadern import anaread
from zetlabreadern import readint
from zetlabreadern import readshort

#def build_args():
    #parser = ArgumentParser()

   # parser.add_argument(
        #"-o", "--out-file",
        #type=str,
        #help="Output file name"
    #)

    #return parser.parse_known_args()

if __name__ == "__main__":
    
    if len(sys.argv) > 1:
        files = sys.argv[1:]
        count = len(files)
        #print("count=")
        #print(count)
        sig = np.array([])
        for fn in files:
            d, fs, n = anaread(fn)
            #print("d=")
            #print(d)
            sig = np.concatenate((sig, d))
            #print("sig=")
            #print(sig)
        
        sigsplit = np.hsplit(sig, count)
        #print("sigsplit=")
        #print(sigsplit)
        signal = np.transpose(sigsplit)
        #print("signal=")
        #print(signal)
        
        wfdb.wrsamp("ECG", fs = 2000, units=["mV"]*count,
                    sig_name=["name1", "name2", "name3"],
                    p_signal = signal, fmt=["16"]*count, write_dir="C:\PyFile\ecg")
        
        signals, fields = wfdb.rdsamp("C:\PyFile\ecg\ECG", sampfrom=0, sampto="end", channels="all")

        fs = 2000
        t = np.arange(0, len(signals)/fs, 1.0/fs)
        plt.plot(t, signals)
        plt.xlim([540, 545])
        plt.title("plot")
        print("Look at the plots")
        plt.show()
        
    else:
        print("Задайте несколько файлов")
