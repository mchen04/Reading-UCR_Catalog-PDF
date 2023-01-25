# Reading-UCR_Catalog-PDF

PDF Search
This script allows you to search for keywords in the UCR Catalog PDF document and returns the text after the keyword, along with the page number it was found on. This script uses the PyPDF2 library to read the PDF document.

Usage
Install the PyPDF2 library by running pip install PyPDF2
Run the script using python main.py
Enter the keyword you want to search for when prompted.
The script will return the text following the keyword and the page number it was found on.
To exit the script, enter "quit" when prompted for a keyword.

Note
The script will display the output in the format "ID, Course Name, Credit Amount, General Info, Prerequisites, Page#"

Limitations
Currently, this script can only search for one keyword at a time and cannot search for multiple keywords at once. Additionally, it is limited to the UCR Catalog.
