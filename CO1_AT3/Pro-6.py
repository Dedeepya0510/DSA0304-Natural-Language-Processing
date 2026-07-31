import re

text = """
Meeting on 12/09/2026
Call 9876543210
#NLP
@OpenAI
natural language processing
Machine Learning
"""

while True:
    print("\n===== MENU =====")
    print("1. Search Date")
    print("2. Search Phone Number")
    print("3. Search Hashtag")
    print("4. Search Mention")
    print("5. Search Prefix")
    print("6. Search Suffix")
    print("7. Search Word")
    print("8. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        print(re.findall(r'\b\d{2}/\d{2}/\d{4}\b', text))

    elif choice == "2":
        print(re.findall(r'\b[6-9]\d{9}\b', text))

    elif choice == "3":
        print(re.findall(r'#\w+', text))

    elif choice == "4":
        print(re.findall(r'@\w+', text))

    elif choice == "5":
        prefix = input("Enter Prefix: ")
        print(re.findall(r'\b' + re.escape(prefix) + r'\w*', text, re.IGNORECASE))

    elif choice == "6":
        suffix = input("Enter Suffix: ")
        print(re.findall(r'\b\w*' + re.escape(suffix) + r'\b', text, re.IGNORECASE))

    elif choice == "7":
        word = input("Enter Word: ")
        print(re.findall(r'\b' + re.escape(word) + r'\b', text, re.IGNORECASE))

    elif choice == "8":
        print("Program Ended")
        break

    else:
        print("Invalid Choice")
