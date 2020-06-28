import PyPDF2 
import re
  
# creating a pdf file object 
pdfFileObj = open('The_Living_World.pdf', 'rb') 
  
# creating a pdf reader object 
pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
list_ = []  
set_ = set(['The Living WorldAakash Educational Services Pvt. Ltd.','Solutions of Assignment (Set-2)', 'The Living WorldSolutions of Assignment (Set-2)','Aakash Educational Services Pvt. Ltd.','- Regd. Office : Aakash Tower, 8,',
'Pusa Road,','New Delhi-1','10005 Ph.011-47623456'])
# printing number of pages in pdf file 
for i in range(pdfReader.numPages):   
    # creating a page object 
    pageObj = pdfReader.getPage(i) 
    # extracting text from page 
    for line in pageObj.extractText().split('\n'):
        if line and line.strip() not in set_ and not line.isdigit():
            if line[-1] == '.':
                line=line + '\n'   
            else:
                line=line
        with open("temp.txt","a+") as f:
            f.write(line)
        f.close()
# closing the pdf file object 
pdfFileObj.close() 

# Aakash Educational Services Pvt. Ltd. - Regd. Office : Aakash Tower, 8, Pusa Road, New Delhi-110005 Ph.011-47623456

temp=[]

with open("temp.txt","rb") as f:
    test=str(f.readlines())
    # print(test)
    test=test.replace('Aakash Educational Services Pvt. Ltd. - Regd. Office : Aakash Tower, 8, Pusa Road, New Delhi-110005 Ph.011-47623456', '')
    test=test.replace('Solutions', '')
    test=test.replace('SECTION', '')
    test=test.replace('Objective Type Questions', '')
    test=test.replace('b','')
    test=test.replace('The Living World','')
    test=test.replace('Assignment ','')
    test=test.replace(' - ','')
    test=test.replace('\r\n','')
    
    test = re.sub("\r\n", "", test)
    print(test)
    fin = open("out.txt", "wt")
    fin.write(test)
    fin.close()

with open("out.txt","rb") as f:
    i=str(f.readline())
    # while("." in i):
    #     tp=i.index(".")
    #     if(i[tp-1] in ['1','2','3','4','5','6','7','8','9','0']):
    #         print(i[tp-1 :tp+1])
    #         temp.append(tp-2)
    #         i=i[tp+1:]
    #     else:
            
f.close()
print(temp)