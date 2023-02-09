#Importing Libraries
#Importing Google Text to Speech library
import os

from gtts import gTTS

#Importing PDF reader PyPDF2
import PyPDF2

#Open file Path
pdf_File = open('Release Form.pdf', 'rb')

#Create PDF Reader Object
pdf_Reader = PyPDF2.PdfReader(pdf_File)
count = len(pdf_Reader.pages) # counts number of pages in pdf
textList = []

#Extracting text data from each page of the pdf file
for i in range(count):
    page = pdf_Reader.pages[i]
    textList.append(page.extract_text())


#Converting multiline text to single line text
textString = " ".join(textList)

print(textString)

#Set language to english (en)
language = 'en'

#Call GTTS
myAudio = gTTS(text=textString, lang=language, slow=False)

#Save as mp3 file
myAudio.save("Audio.mp3")
os.system("Audio.mp3")

# importing required modules
# import PyPDF2
#
# # creating a pdf file object
# pdfFileObj = open('Release Form.pdf', 'rb')
#
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfReader(pdfFileObj)
#
# # printing number of pages in pdf file
# print(len(pdfReader.pages))
#
# # creating a page object
# pageObj = pdfReader.pages[0]
#
# # extracting text from page
# print(pageObj.extract_text())
#
# # closing the pdf file object
# pdfFileObj.close()
