import random
import json
import pickle
import warnings
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
warnings.simplefilter('ignore')
from keras.models import load_model


#load the content
intents=json.loads(open("intents.json").read())
classes=pickle.load(open('classes.pkl','rb'))
words=pickle.load(open('words.pkl','rb'))
model=load_model('chatBot_model.h5')
lemmatizer =WordNetLemmatizer()


#preprocessing the input text

#tokenization & lammatization

def preprocess_text(text):
    text_words=nltk.word_tokenize(text)
    text_words=[lemmatizer.lemmatize(word.lower()) for word in text_words]
    return text_words

def bag_of_word(text):
    text_words=preprocess_text(text)
    bow=[1 if word in text_words else 0 for word in words]
    return np.array(bow)


def predict_class(text):
    bow=bag_of_word(text)

    res=model.predict(np.array([bow]))[0]
    # Make a prediction using the trained model and obtain the highest probability prediction

    threshold=0.25
    #minimum accepted probability

    results=[[i,r] for i, r in enumerate(res) if r>threshold]
    #filter the results with probability higher than 0.25 and enmurate for each probability the index of crossponding class

    results.sort(key=lambda x:x[1] ,reverse=True)
    #sort the results by probability in descending order
    returned_lst=[]
    for r in results:
        returned_lst.append({'tag': classes[r[0]], 'probability':str(r[1])})
    return returned_lst

# text="Tell me joke "
# response_options=predict_class(text)
# tag=response_options[0]['tag']
# for intent in intents['intents']:
#     if intent['tag'] == tag:
#         print("Result  :  ", intent['responses'])
#         break


def get_reponse(text):
 response_options=predict_class(text)
 tag=response_options[0]['tag']
 for intent in intents['intents']:
     if intent['tag'] == tag:
         reponse=random.choice(intent['responses'])
         return reponse

 return "I'm sorry, I don't understand that."  # Default response for unrecognized intents


print("Bot is running!")

# while True:
#     text=input("")
#     response=get_reponse(text)
#     print(response)



