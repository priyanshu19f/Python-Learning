"""
Q101: File Type Check
Take a filename as input (like report.pdf). Check if it ends with .pdf,
.docx, or . txt and print the file type.
"""

filename = input("Enter filename : ")
if filename.endswith(".pdf"):
    print("pdf file")
elif filename.endswith(".docx"):
    print("document file")
elif filename.endswith(".txt"):
    print("text file")
else:
    print("invalid file")
