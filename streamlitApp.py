import streamlit as st
import pickle
import numpy as np

try:
    with open('model.pickle', 'rb') as file:
        classifier = pickle.load(file)
except Exception as e:
    st.error(f"Error loading model: {str(e)}")

with open('Countvectorize.pickle','rb') as file :
    sparserize = pickle.load(file)

st.title('Text Classifier App')

user_input = [st.text_input('Enter text for classification:', '')]

if st.button('Predict'):
     if user_input != None :

         input = sparserize.transform(user_input)

         output = classifier.predict(input)

         st.write(f'Prediction: {prediction[0]}')

     else :
         st.write('Enter text for classification')





