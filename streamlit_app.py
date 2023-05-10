from dotenv import load_dotenv

import streamlit as st
from streamlit_chat import message
from streamlit_extras.colored_header import colored_header
from streamlit_extras.add_vertical_space import add_vertical_space

from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.schema import (
    SystemMessage,
    HumanMessage,
    AIMessage
)

load_dotenv()

st.set_page_config(page_title="Staples Chat")

with st.sidebar:
    st.title('Staples Chat')
    add_vertical_space(2)
    st.write(
        'Made by [Austin Johnson](<https://github.com/AustonianTX>)')

if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        SystemMessage(
            content="You are a pirate.  Always answer the in form of a pirate.")
    ]

st.write(st.session_state)

input_container = st.container()
colored_header(label='', description='', color_name='blue-30')
response_container = st.container()
input_container_bottom = st.container()

chat = ChatOpenAI(
    temperature=0.5
)

# User input


def submit_text():
    st.session_state.text_input = st.session_state.prompt_input
    st.session_state.prompt_input = ""

# Response output


def generate_response(prompt):

    ai_response = chat(st.session_state['messages'])

    return ai_response.content


with response_container:
    if "text_input" in st.session_state:
        prompt = st.session_state.text_input
        st.session_state['messages'].append(
            HumanMessage(content=prompt)
        )

        for i, message_obj in enumerate(st.session_state['messages'][1:], start=1):
            is_user_message = isinstance(message_obj, HumanMessage)
            text = message_obj.content

            message(text, is_user=is_user_message, key=str(i))

        response = generate_response(prompt)

        st.session_state['messages'].append(
            AIMessage(content=response))

        message(response, is_user=False, key=str(
            len(st.session_state['messages'])))

with input_container_bottom:
    if "text_input" not in st.session_state:
        st.session_state["text_input"] = ""

    st.text_input('YOU: ', key='prompt_input', on_change=submit_text)
