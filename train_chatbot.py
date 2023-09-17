import random
import json
import pickle
import string
import warnings
import numpy as np
import tensorflow as tf
import nltk
from nltk.stem import WordNetLemmatizer
warnings.simplefilter('ignore')
#load the content
intents=json.loads(open("intents.json").read())

# with open(("intents.json"),'r') as file:
#     intents=json.load(file)
#preprocessing


#stop words
stopWords=nltk.corpus.stopwords.words('english')

#Lemmatization
lemmatizer =WordNetLemmatizer()

documents=[]
classes=set()
#to get unique tags
words=[]
punctuation=set(string.punctuation)
for intent in intents['intents']:
    tag=intent['tag']
    classes.add( tag )
    for pattern in intent['patterns']:
        # tokenize pattern and lemmatize
        wordList=[lemmatizer.lemmatize(word.lower()) for word in nltk.word_tokenize(pattern) if word not in punctuation]
        # put all words mentioned in intents file
        words.extend(wordList)
        # use tuple to associate the words in the pattern with their corresponding intent tag
        documents.append((wordList, tag))
        # collect unique intent tags in a classes


# Remove duplicates from 'words' and sort
words = sorted(set(words))
classes = sorted(classes)
classes=list(classes)

pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes, open('classes.pkl','wb'))
#preparing data for training
classesNum=len(classes)
# make vector of zeros for one-hot-encoded
zerosvec=[0]*classesNum

training_data=[]
for doc in documents:
 bow=[]
 #create bag of word matrix for encoding
 tokens=doc[0]
 #take the wordlist in document

 bow=[1 if word in tokens else 0 for word in words]
 # assign 1 for each  word appear in the document
 classesvec=list(zerosvec)
 #make vector of zeros and assign 1 for the class belong to (one-hot-encoding)
 classesvec[classes.index(doc[1])]=1
 training_data.append(bow + classesvec)

random.shuffle(training_data)
training_data=np.array(training_data)

wordelen=len(words)
train_x=training_data[:,:wordelen]
train_y=training_data[:,wordelen:]




#set up a feedforward neural network for classification task

model=tf.keras.Sequential()
#intilize model

model.add(tf.keras.layers.Dense(128,input_shape=(len(train_x[0]),), activation='relu'))

model.add(tf.keras.layers.Dropout(0.5))
#add dropout layer for regularization to avoid overfitting

model.add(tf.keras.layers.Dense(64, activation='relu'))

model.add(tf.keras.layers.Dropout(0.5))

model.add(tf.keras.layers.Dense(len(train_y[0]),activation='softmax'))
#add the output layer with the number of units = number of clasess , use softmax for mutliclass classification


#optimizer

sgd=tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#training the model

hist=model.fit(np.array(train_x),np.array(train_y), epochs=200, batch_size=5, verbose=1)

model.save('chatBot_model.h5',hist)

print("####################")
