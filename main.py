import PyPDF2
path = str(input("Enter File Path: "))
pdf = open(path, "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(0)
print(page.extractText())
