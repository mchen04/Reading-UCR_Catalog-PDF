import PyPDF2
from tqdm import tqdm

# Initialize the PDF file and reader
FILE_NAME = "UCR_Classes.pdf"

try:
    # Load the PDF document
    doc = PyPDF2.PdfReader(FILE_NAME)
    total_pages = len(doc.pages)
    print(f"\n📘 The UCR Class Catalog contains {total_pages} pages.\n")
except FileNotFoundError:
    print(f"❌ Error: File '{FILE_NAME}' not found. Please check the file path and try again.")
    exit()

# Instructions for the user
print("🔎 Search for a class by entering its code (e.g., 'AHS 180').")
print("💡 You can search for multiple classes in one session.")
print("💡 Type 'quit' to exit the program at any time.\n")

while True:
    # Prompt the user for a keyword to search
    search = input("Enter a class code to search (or type 'quit' to exit): ").strip()

    # Exit condition
    if search.lower() == "quit":
        print("\n👋 Exiting the program. Goodbye!")
        break

    if not search:
        print("⚠️ Please enter a valid class code.\n")
        continue

    # Notify user about the scanning process
    print(f"\n🔍 Searching {total_pages - 1} pages for '{search}'...\n")
    results = []

    # Scan through the document pages
    for page_num in tqdm(range(1, total_pages), desc="Scanning Pages", unit="page"):
        page = doc.pages[page_num]
        page_text = page.extract_text()

        # Check if the search term exists on the page
        if search in page_text:
            after_search = page_text.split(search)[1]
            extracted_text = ""
            period_count = 0

            # Extract text after the search term
            for char in after_search:
                if char == ".":
                    period_count += 1
                extracted_text += char
                if period_count == 2:
                    break

            # Append formatted result
            results.append(f"{search}\n{extracted_text.strip()} Found on page {page_num + 1}\n")

    # Display the results
    if results:
        print("\n📄 Results:\n")
        print("Format: [Course Code, Course Name, Credits, General Info, Prerequisites, Page #]\n")
        search_string = "Prerequisite(s):"

        for result in results:
            # Replace newlines for better readability
            formatted_result = result.replace("\n", " ").replace(".", "\n\t")
            if search_string in formatted_result:
                print(formatted_result + "\n")
    else:
        print(f"❌ No results found for '{search}'. Please try another keyword.\n")

    # Offer the user a chance to continue or exit
    continue_choice = input("Would you like to search for another class? (yes/no): ").strip().lower()
    if continue_choice not in ["yes", "y"]:
        print("\n👋 Exiting the program. Goodbye!")
        break
