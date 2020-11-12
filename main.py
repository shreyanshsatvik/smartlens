# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 23:33:31 2020

@author: Shreyansh Satvik
"""

#import torch
import pytesseract
import streamlit as st
from PIL import Image
import cv2
from pytesseract import Output
import torch
from bs4 import BeautifulSoup
import requests
#import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

#import json 
#from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def main():
    st.title("Smartlens Web App")
    
    st.sidebar.title("SmartLens Web App created by Shreyansh and Aditya")
    for i in range(0,2):
        st.sidebar.text(" \n")

    mode = st.sidebar.radio("Which Mode you want to choose",["Notebook","Medicine"])
    app_mode = st.sidebar.selectbox("Choose the app mode",
        ["About the App","Scan Notebook","Translate","Summarize","Show the source code","Show the architecture of App"])
    if app_mode == "About the App" and mode == "Notebook":
        st.header("The main featurs of this web app is :")
        st.markdown("1. It can scan any handwritten text and can convert it to typed one.")
        st.markdown("2. It can then translate the converted text into any language. (Right Now - Spanish and French)")
        st.markdown("3. If you want it can summarize the story/text/article you scanned.")
        st.markdown("4. If you want to search or buy or to know about the description of any medicine then we can do it for you, and all you just need to do is to scan the medicine you have.")
        for i in range (0,15):
            st.write(" \n")
        st.markdown("Made with ❤️ by Team - Bira Virus ")
    elif app_mode == "Scan Notebook" and mode == "Notebook":
        st.header("Convert any handwritten text to typed one")
        st.write("\n")
        st.markdown("Choose Image of the notebook :")
        #st.button("Choose Image from your local machine")
        uploaded_file = st.file_uploader("Choose an image...", type="jpg")
        if(uploaded_file):
            img = Image.open(uploaded_file)
            image_button = st.button("Uploaded Image")
            if(image_button):
                st.image(img, caption='Uploaded Image.', use_column_width=True)

            img = img.convert('L')
            text = pytesseract.image_to_string(img)
                        
                        
            
            
            
            
            
            text_button=st.button("Converted Text")
            if(text_button):
                st.write(text)
            
            for i in range (0,12):
                st.write(" \n")
            
            st.markdown("Made with ❤️ by Team - Bira Virus ")
            

    elif app_mode == "Summarize" and mode == "Notebook":
        
        device = torch.device('cpu')
        st.header("Summarize any text/news/article/story of any length")
        for i in range (0,3):
                st.write(" \n")
        text = st.text_input('Enter your text here: ')  
        generate_summary = st.button("Generate Summary")
        if(generate_summary):
            preprocess_text = text.strip().replace("\n","")
            t5_prepared_Text = "summarize: "+preprocess_text
            tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
            summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=30,
                                    max_length=200,
                                    early_stopping=True)

            output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            st.write(output)
        for i in range (0,15):
            st.write(" \n")
        st.markdown("Made with ❤️ by Team - Bira Virus ")
    elif app_mode == "Translate" and mode == "Notebook":
        device = torch.device('cpu')
        st.header("Translate any sentence to German or French or Spanish")
        for i in range (0,3):
                st.write(" \n")
        text = st.text_input('Enter your text here: ')
        eng_ger = st.button("Translate English to German")
        eng_spa = st.button("Translate English to Spanish")
        eng_fre = st.button("Translate English to French")
        if(eng_ger):
            preprocess_text = text.strip().replace("\n","")
            t5_prepared_Text = "translate English to German: "+preprocess_text
            tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
            summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=5,
                                    max_length=200,
                                    early_stopping=True)

            output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            st.write(output)
        elif(eng_spa):
            preprocess_text = text.strip().replace("\n","")
            t5_prepared_Text = "translate English to Spanish: "+preprocess_text
            tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
            summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=5,
                                    max_length=200,
                                    early_stopping=True)

            output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            st.write(output)
        elif(eng_fre):
            preprocess_text = text.strip().replace("\n","")
            t5_prepared_Text = "translate English to French: "+preprocess_text
            tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
            summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=5,
                                    max_length=200,
                                    early_stopping=True)

            output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
            st.write(output)
        for i in range (0,10):
            st.write(" \n")
        st.markdown("Made with ❤️ by Team - Bira Virus ")
        

            
    
    for i in range(0,3):
        st.sidebar.text(" \n")
    
    st.sidebar.markdown("Choose Option for Medicine:") 
    medicine_mode = st.sidebar.selectbox("Choose the mode for medicine ",
        ["None","Know about Medicine","Source Code"])
    if(medicine_mode == "Know about Medicine" and mode == "Medicine"):
        st.header("Know details about your medicine")
        med = st.text_input('Enter your medicine name here: ')
        results = st.button("Search Button")
        if(results):
            
            url=""
            if med == "crocin" or med=="fever":
                url="https://www.webmd.com/drugs/2/drug-57595/paracetamol-oral/details"
            elif med=="alegra" or med== "allergy":
                url="https://www.webmd.com/drugs/2/drug-13821-2204/allegra-oral/fexofenadine-oral/details"
            elif med== "corona" or med== "chlororquine":
                url="https://www.webmd.com/drugs/2/drug-8633/chloroquine-oral/details"
            hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
               'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
               'Accept-Encoding': 'none',
               'Accept-Language': 'en-US,en;q=0.8',
               'Connection': 'keep-alive'}
     
            br=requests.get(url,headers=hdr)
            soup=BeautifulSoup(br.text,"html.parser")
            s2=soup.find('div',{"class":"expand-content"}) 
            l=[]
            links=soup.find_all('h2')
            for i in links:
                l.append(i.text)
            
            l1=[]
            content=soup.find_all('div',{'class':'inner-content'})
            for i in content:
                l1.append(i.text)
            
            l2=[]
            m=[]
            s=''
            for i in range(len(l1)-1):
                m=[]
                m=l1[i].split('\n')
                st.markdown(l[i])
                s=m[1]+'\n'+m[2]
                st.write(s)
        
        for i in range (0,15):
            st.sidebar.text(" \n")
        st.markdown("Made with ❤️ by Team - Bira Virus ")
                    
                
            
            
            
    
    
    
    
    
    
    
    
    
    
    for i in range (0,5):
        st.sidebar.text(" \n")
    st.sidebar.markdown("Made with ❤️ by Team - Bira Virus ")
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()
