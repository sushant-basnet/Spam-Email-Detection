import pickle
import streamlit as st
from win32com.client import Dispatch

def speak(text):
   speak=Dispatch(("SAPI.SpVoice"))
   speak.Speak(text)

model=pickle.load(open("spam.pkl","rb"))
cv=pickle.load(open("vectorizer.pkl","rb"))

def main():
   st.title("Email Spam Classification")
   st.subheader("Build with Streamlit and Python")
   msg=st.text_input("Enter a Text: ")
   if st.button("Predict"):
       df=[msg]
       vect=cv.transform(df).toarray()
       prediction=model.predict(vect)
       result=prediction[0]
       if result==1:
           st.error("This is a Spam Mail")
           speak("This is a Spam Mail")
       else:
           st.success("This is not a Spam Mail")
           speak("This is not a Spam Mail")
main()