# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 12:48:35 2020

@author: Shreyansh Satvik
"""

from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
#import pickle
import numpy as np
#import torch
import json 
from transformers import T5Tokenizer, T5ForConditionalGeneration, T5Config

app = Flask(__name__)
api = Api(app)

model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
#device = torch.device('cpu')

parser = reqparse.RequestParser()
parser.add_argument('query')

class Predict(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        
    

        # Output either 'Negative' or 'Positive' along with the score
        preprocess_text = user_query.strip().replace("\n","")
        t5_prepared_Text = "summarize: "+preprocess_text
        #print ("original text preprocessed: \n", preprocess_text)
        
        tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt")
        
        
        summary_ids = model.generate(tokenized_text,
                                            num_beams=4,
                                            no_repeat_ngram_size=2,
                                            min_length=30,
                                            max_length=200,
                                            early_stopping=True)
        
        output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
         
        return output
    
api.add_resource(Predict, '/')


if __name__ == '__main__':
    app.run(debug=False)
    
"""


model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

text ="""
"Ultimately what really matters is you getting two points. What T20s have shown is that there are a few games that don't go your way and then there are some that go your way even when you haven't earned it. Today I felt we did a very good job even in batting. There was some purpose with the bat and the batsmen assessed the situation very well. With a total like 160, it all depends on the start you get in the first six overs. The fast bowlers did the job, the spinners came into play and it was one game that was as close to being perfect. It was a par score and I usually assess scores after the first six overs. If there are misfields in the first six overs then a par score becomes an under par score. A lot depended on the fast bowlers. I just told them to be expressive on the field and hit their areas. There are some two paced balls, some swing and some don't swing, some get extra bounce. What was needed was good execution of the plans and that was done by the fast bowlers. To an extent yes (these pitches). But we used an extra spinner because an Indian batter hasn't done well for us. That's why Sam Curran went up and it wasn't fair on Jagadeesan as well to bat at seven or eight. Sam Curran is a complete cricketer for us. You need a seamin all-rounder, he plays the spinners well and he can give us those 15-45 runs."

"""

preprocess_text = text.strip().replace("\n","")
t5_prepared_Text = "summarize: "+preprocess_text
#print ("original text preprocessed: \n", preprocess_text)

tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)


summary_ids = model.generate(tokenized_text,
                                    num_beams=4,
                                    no_repeat_ngram_size=2,
                                    min_length=30,
                                    max_length=200,
                                    early_stopping=True)

output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)



print ("\n\nSummarized text: \n",output)

"""
