import PyPDF2

# import the PyPDF2 library
file_name = "UCR_Classes.pdf" 

# assign the name of the file to variable file_name
doc = PyPDF2.PdfReader(file_name) 

# create a pdf reader object using the pdf file
pages = len(doc.pages)

# get the number of pages in the document and assign to variable pages
print ("UCR Class Catalog has",pages, "pages.") 

# print the number of pages in the document
while 1 :
    print ('Input "quit" to exit')
    print ('Format EX: [AHS 180]')
    search = input('Searching Keyword: ')

    # prompt the user to input the keyword to search for
    if search == "quit" :
        exit() 
    # if the user inputs "quit", exit the program

    results = []
    # create an empty list to store the search results

    for page_num in range(1, pages) :
        current_page = doc.pages[page_num]
        text = current_page.extract_text() 

        # extract the text from the current page
        if page_num % 100 == 0: 
            print (page_num,"Pages Scanned")

        # print the number of pages scanned every 100 pages
        if search in text:
            # if the keyword is found in the text, extract the text after the keyword
            after_word = text.split(search)[1]
            i = 0
            extracted_text = ""
            period_count = 0
            while i < len(after_word) and period_count < 2:
                if after_word[i] == ".":
                    period_count += 1
                extracted_text += after_word[i]
                i += 1
            results.append(f"{search}\n{extracted_text} Found on page {page_num + 1}\n")
    
    # remove newlines from the results and replace them with tabs
    results = [word.replace('\n', '') for word in results]
    results = [word.replace('.', '\n\t') for word in results]

    search_string = "Prerequisite(s):"

    # search for results that contain the string "Prerequisite(s):"
    for element in results:
        if search_string in element:
            print ("Output Format: ID, Course Name, Credit Amount, General Info, Prerequisites, Page#")
            print(element, "\n")