import os 
import PyPDF2
from PyPDF2 import PdfReader , PdfWriter, PdfMerger
pdfFiles = [] # variable 


for root, dirs, filenames in os.walk(os.getcwd()): # Root and directory pathway.
#for filenames in os.listdir(os.curdir):    
    for filename in filenames: 
        if filename.lower().endswith('.pdf'):# for loop for all files with .pdf in the name.
            pdfFiles.append(os.path.join(root,filename)) 
            # Appending files to root name from OS (operating system).
            
# Sorting the files by forcing everything to lower case.
#pdfFiles.sort(key=str.lower)

# Assigning the pdfWriter() function to pdfWriter.
pdfWriter = PyPDF2.PdfWriter()

print(len(pdfFiles))

for filename in pdfFiles: # Starting a for loop.
    pdfFileObj = open(filename, 'rb') # Opens each of the file paths in filename variable.
    pdfReader = PyPDF2.PdfReader(pdfFileObj) # Reads each of the files in the new varaible you've created above and stores into memory.
    pageObj = pdfReader.pages[0] # Reads only those that are in the varaible.
    pdfWriter.add_page(pageObj) # Adds each of the PDFs it's read to a new page.

# Name of the PDF file can be written here.
pdfOutput = open('merged.pdf', 'wb') 

# Writing the output file using the pdfWriter function.
pdfWriter.write(pdfOutput)
pdfOutput.close()