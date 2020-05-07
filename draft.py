#The json files contain:
#   * COVID-19 research articles PDFs from corpus maintained by the WHO
#   * COVID-19 & coronavirus research articles from PubMed's PMC open access corpus

from nltk.tokenize import word_tokenize
import json
import re #for regular expressions
import spacy #for word tokens, lemmatizing, identifying stopwords
nlp = spacy.load('en')

#set output file to write out to
output = open("output.txt", "w+")

#extract json data and store as a string but ignore the first line: 'This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/bync/4.0/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.'" 
def extractText(json_data):
    string = ''
    for element in json_data['body_text']:
        if (element['text'] != 'This is an Open Access article distributed under the terms of the Creative Commons Attribution Non-Commercial License (http://creativecommons.org/licenses/bync/4.0/) which permits unrestricted non-commercial use, distribution, and reproduction in any medium, provided the original work is properly cited.'):
            string += element['text']
    return string

with open('00a00d0edc750db4a0c299dd1ec0c6871f5a4f24.json', 'r') as file:
    json_data = json.load(file)
    text = extractText(json_data)
    
    doc = nlp(text)
    
    output.write("{: <50} {: <50} {: <50}".format('Token', 'Lemma', 'Stopword') + "\n")
    output.write("-"*100 + "\n")
    for token in doc:
        output.write("{: <50} {: <50} {: <50}".format(f"{token}",f"{token.lemma_}",f"{token.is_stop}") + "\n")