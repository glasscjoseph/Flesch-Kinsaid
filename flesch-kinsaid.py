#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  3 15:46:49 2024

@author: josephglass
"""

### import PyPDF2
import re
from pypdf import PdfReader

'''
def read_pdf(file_path):
    with open(file_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        text = ""
        for page_number in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_number)
            text += page.extractText()

    return text
'''

def read_pdf(file_path):
    pdf = PdfReader(file_path)
    
    text = ""
    for page in pdf.pages:
        text += page.extract_text() + "\n"
        
    return text
    

def syllable_count(word: str) -> int:
    word = re.sub(r"[^a-z]", "", word.lower())
    
    if not word:
        return 0
    
    count = len(re.findall(r"[aeiouy]+", word))
    
    if word.endswith("e") and not re.search(r"[^aeiouy]le$", word):
        count -= 1
    
    return max(count,1)

def total_syllables(text):
    words = re.findall(r"[a-z']+",text.lower())
    
    count = 0
    
    for i in range(len(words)):
        syllables = syllable_count(words[i])
        count += syllables
        
    return count
        
def total_words(text):
    words = re.findall(r"[a-z']+",text.lower())
    
    count = len(words)
    
    return count

def total_sentences(text: str) -> int:
    sentences = re.split(r"(?<=[.!?])\s+(?=[A-Z])", text.strip())
    return len([s for s in sentences if s.strip()])


def what_score(pathway):
    text = read_pdf(pathway)
    
    no_words = total_words(text)
    
    score = 206.835 - 1.015*(no_words/total_sentences(text)) \
            - 84.6*(total_syllables(text)/no_words)
    
    return score
        
print("To get the Flesch-Kinsaid reading score for your text, enter \
      what_score(<file path>)")        
        
        