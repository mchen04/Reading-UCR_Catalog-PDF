import PyPDF2
import re

file_name = "UCR_Classes.pdf"
doc = PyPDF2.PdfReader(file_name) 

pages = len(doc.pages)
print ("UCR Class Catalog has",pages, "pages.") 

while 1 :
    print ('Input "quit" to exit')
    print ('Format EX: [AHS 180]')
    search = input('Searching Class: ')

    if search == "quit" :
        exit() 

    results = []
    for page_num in range(1, pages) :
        current_page = doc.pages[page_num]
        text = current_page.extract_text() 

        if page_num % 100 == 0: 
            print (page_num,"Pages Scanned")

        if search in text:
            after_word = text.split(search)[1]
            i = 0
            extracted_text = ""
            period_count = 0
            while i < len(after_word) and period_count < 2:
                if after_word[i] == ".":
                    period_count += 1
                extracted_text += after_word[i]
                i += 1
            results.append(f"{search}\n\t{extracted_text} Found on page {page_num + 1}\n")

    results = [word.replace('\n', '') for word in results]
    results = [word.replace('.', '\n\t') for word in results]

    search_string = "Prerequisite(s):"

    for element in results:
        if search_string in element:
            print(element, "\n")


