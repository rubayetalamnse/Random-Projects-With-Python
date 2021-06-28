import PyPDF2
a= PyPDF2.PdfFileReader("machine_learning_tutorial.pdf")
#print(a.getDocumentInfo())
#print(a.getNumPages())
str = ""


with open("machine_learning_tutorial.txt","w",encoding="utf-8") as f:
    f.write(str)
    for i in range(1,36):
        str+=print(a.getPage(i).extractText())