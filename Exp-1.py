import re

text = "My phone number is 9876543210"

# Search for a 10-digit number
result = re.search(r"\d{10}", text)

if result:
    print("Number found:", result.group())
else:
    print("Number not found")
