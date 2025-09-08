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
    
    with st.chat_message('assistant'):

        ai_message = st.write_stream(
            message_chunk[0].content for message_chunk in chatbot.stream(
                {'messages': [HumanMessage(content=userInput)]},
                config= {'configurable': {'thread_id': 'thread-1'}},
                stream_mode= 'messages'
            )
        )

    st.session_state['message_history'].append({'role': 'assistant', 'content': ai_message})