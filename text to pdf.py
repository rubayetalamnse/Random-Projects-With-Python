#python program to convert .txt file to .pdf

from fpdf import FPDF

our_pdf = FPDF()
author = "Rubayet Alam"
#let's create a page in our pdf------------------
our_pdf.add_page() 

#let's set font 
our_pdf.set_font('Times', size=12)

#opening our text file in reading mode------------
file = open("Nuclear Power.txt","r")

for i in file:
    our_pdf.cell(150,5, txt=i, ln=17, align="L") 


our_pdf.output("Nuclear Power python.pdf")