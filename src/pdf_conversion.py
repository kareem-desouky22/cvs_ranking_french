# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 14:37:35 2021

@author: KHC
"""
import os
import glob
import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.visible = 0



data_path=os.path.join(os.path.abspath(os.path.join(__file__,r"..\\..\\")),'data')
cvs_folder=os.path.join(data_path,'cvs')
pdfs_path =cvs_folder+'\\' # folder where the .pdf files are stored
print ('cvs folder is:',pdfs_path)
for i, doc in enumerate(glob.iglob(pdfs_path+"*.pdf")):
    print ('I am inside for loop')
    print(doc)
    filename = doc.split('\\')[-1]
    in_file = os.path.abspath(doc)
    print('infile path is; ',in_file)
    wb = word.Documents.Open(in_file)
    out_file = os.path.abspath(pdfs_path +filename[0:-4]+ ".docx".format(i))
  
    print("outfile\n",out_file)
    wb.SaveAs2(out_file, FileFo1rmat=16) # file format for docx
#    wb.SaveAs(out_file) # file format for docx
    print("success...")
    wb.Close()
    word.Quit()

