import convertapi
import spacy
import os

# Name of PDF file in current directory
# Name of txt file will be the name of the pdf file + the txt extension (test.pdf -> test.txt)
file_name = "ENTER_TEXT_HERE.pdf"


# API Key for ConvertAPI
convertapi.api_secret = 'zxpcH1W9dAliqW2F'


# Load SpaCy English tokenizer, tagger, parser and NER
nlp = spacy.load('en_core_web_sm')


# Replaces file_name extension with .txt
file_name_to_txt = file_name[:-4] + '.txt'


# Calls API to convert pdf to txt
convertapi.convert('txt', {'File': file_name}, from_format = 'pdf').save_files(file_name_to_txt)


# Open the txt file and deletes all newlines
file = open(file_name_to_txt)
file = file.read().replace("\n", "")


# Process the whole txt file through SpaCy
doc = nlp(file)


# Empty the txt file
open(file_name_to_txt, 'w').close()


# Reopen txt file and prepare for appending
new_txt_file = open(file_name_to_txt, 'a')


# Put all sentences detected by SpaCy into txt file
for sentence in doc.sents:
    new_txt_file.write(str(sentence))


# Close the txt file
new_txt_file.close()