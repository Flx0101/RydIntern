import PyPDF2 as pdf
import re
from pprint import pprint

pdfFileObj=open('The_Living_World.pdf','rb')

pdfReader=pdf.PdfFileReader(pdfFileObj)
temp=[]
for i in range(int(pdfReader.numPages)):
    pageObj = pdfReader.getPage(i) 
# extracting text from page 
    #print(pageObj.extractText()) 
    with open('text.docx','a+') as f:
        f.write(pageObj.extractText())
        
# closing the pdf file object 
pdfFileObj.close() 
# lists=[]
# with open('text.txt','r') as f:
#     for i in f.readlines():
#         lists.append(list((i.strip().split("\n"))))
#         # if(str(1)+".") in i):
#         #     print(i)
# temp=1
# sindex=0
# eindex=0
# ques=[]
# for i in range(len(lists)):
#     if(str(temp)+"." in str(lists[i])):
#         sindex=str(lists[i]).index(str(temp)+".")
#         ques.append([i,sindex])
#         temp=temp+1
#         pass
# # print(ques)
# # try:
#     # pprint(lists)
# for i in lists[:30]:
#     # print(i)
#     if re.match(r'[0-9][0-9]+.*', str(i)):
#         print(i)
# # except:
#     # pass

