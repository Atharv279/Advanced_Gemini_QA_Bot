"""from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="GOOGLE_API_KEY")

## function to load gemini pro model to get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def get_gemini_respose(question):
    response=chat.send_message(question,stream=True)
    return response

## initilize our streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Apllication")

#initialize session state for chat history if it doesnt exist
if "Chat_history" not in  st.session_state:
    st.session_state["Chat_history"]=[]

input=st.text_input("input:",key="input")
submit=st.button("Ask the question")

if submit and input:
        response=get_gemini_respose(input)
            ## add user query and response to session chat history
        st.session_state=["Chat_history"].append(("You",input))
        st.subheader("The response is")

                ##all the dat coming through llm model should be disply over the front end screen
            for chunk in response:
                st.write(chunk.text)
                st.session_state["Chat_history"].append(("Bot",chunk.text))

st.subheader("The chat history is")
 
for role,text in st.session_state["chat_history"]:
    st.write(f"{role}:{text}")"""
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini model
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to load Gemini Pro model and get response
def get_gemini_response(question):
    return chat.send_message(question, stream=True)

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

# Initialize session state for chat history if it doesn't exist
if "Chat_history" not in st.session_state:
    st.session_state["Chat_history"] = []

# User input and button
user_input = st.text_input("Input:", key="input")
submit = st.button("Ask the question")

if submit and user_input:
    # Get response from Gemini model
    try:
        response = get_gemini_response(user_input)
        # Add user input to chat history
        st.session_state["Chat_history"].append(("You", user_input))
        st.subheader("The response is:")
        
        # Process response chunks
        bot_response = ""
        for chunk in response:
            st.write(chunk.text)
            bot_response += chunk.text
        
        # Add bot's response to chat history
        st.session_state["Chat_history"].append(("Bot", bot_response))
    except Exception as e:
        st.error(f"An error occurred: {e}")

# Display chat history
st.subheader("The chat history is:")
for role, text in st.session_state["Chat_history"]:
    st.write(f"{role}: {text}")
