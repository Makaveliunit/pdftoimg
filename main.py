import os
from pdf2image import convert_from_path

#files directory
mylist = os.listdir('C:\\Users\\Anonymous\\OneDrive\\Desktop\\pdf_file')

count = 0

#for loop pdf to png converter
for x in mylist:
    pages = convert_from_path('C:\\Users\\Anonymous\\OneDrive\\Desktop\\pdf_file\\' + x)
    count +=1
    print(str(count) + '/' + str(len(mylist)) + ' successfully converted')

    for page in pages:
        page.save('C:\\Users\\Anonymous\\OneDrive\\Desktop\\output\\' + x[0:-4]+'.png', 'PNG')
print("Program Terminated")
