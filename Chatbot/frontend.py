import streamlit as st
from backend import chatbot
from langchain_core.messages import AIMessage, HumanMessage

# when we press enter streamlit reruns the script from top to bottom, so we need to store the chat history in session state not in dictionary

config = {'configurable': {'thread_id': 'thread-1'}}

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.markdown(message['content'])

userInput = st.chat_input("Type your message here...")

if userInput:
    st.session_state['message_history'].append({"role": "user", "content": userInput})
    with st.chat_message("user"):
        st.text(userInput)
    
    response = chatbot.invoke({"messages": [HumanMessage(content=userInput)]}, config=config)
    ai_message = response['messages'][-1].content
    st.session_state['message_history'].append({"role": "assistant", "content": ai_message})
    with st.chat_message("assistant"):
        st.text(ai_message)