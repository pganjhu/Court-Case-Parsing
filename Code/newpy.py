# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 16:23:03 2020

@author: Pawan
"""
#importing required packages to carry out the operation

import mmap
import os
import codecs
from bs4 import BeautifulSoup


arr = os.listdir("C://Projects//Old-AWS-Projects//Court-Case-Parsing//html") #to read all .html files in the folder
path='C://Projects//Old-AWS-Projects//Court-Case-Parsing//html//' 
 
def Search_Operation(name): #function to execute step 1, 2 and 3 from instruction template
    retarray=[]
    count=0
	
    for i in range(len(arr)):
        f=codecs.open(path+arr[i], 'rb', 'utf-8')
        s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
        if (s.find(name.encode())!= -1):
            retarray.append(arr[i])
            count+=1
            if count==5:
                break
    return retarray
		

    '''for i in range(len(arr)):
        f=codecs.open(path+arr[i], 'r', 'utf-8')
        document= BeautifulSoup(f.read(),'html.parser').get_text()
        if (document.find(name) != -1): 
            retarray.append(arr[i])
            count+=1
            if count==5:
                break
    return retarray'''

def FileNameParsing(filename): #function to execute step 4 from instruction template
    f=codecs.open(path+filename, 'r', 'utf-8')
    document= BeautifulSoup(f.read(),'html.parser').get_text()
    print(document)
    

while True:
    print("Enter 1 to get file names ")
    print("Enter 2 to parse .html file ")
    print("3 to exit ")
    x=int(input())
    if x==1:       
        name=input("Enter Person name or Case Type : ")
        print("File name are if any : ",Search_Operation(name))
    elif x==2:
        FileNameParsing(input("Enter File name with .html to parse : "))
    else:
        break
