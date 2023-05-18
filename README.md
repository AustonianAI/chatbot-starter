# ChatBot Starter with Streamlit, OpenAI, and LangChain

This repository contains a simple yet powerful chatbot built with Streamlit, OpenAI, and LangChain. The chatbot maintains conversational memory, meaning it can reference past exchanges in its responses.

## Overview

The chatbot is a demonstration of integrating OpenAI's GPT model, the LangChain library, and Streamlit for creating interactive web applications. The bot's conversational memory allows it to maintain context during the chat session, leading to a more coherent and engaging user experience. Importantly, this feature-rich chatbot application is implemented in less than 40 lines of code (excluding whitespace and comments)!

### Key Features

- **Streamlit:** A powerful, fast Python framework used to create the web interface for the chatbot.
- **OpenAI's GPT:** A state-of-the-art language processing AI model that generates the chatbot's responses.
- **LangChain:** A wrapper library for the ChatGPT model that helps manage conversation history and structure the model's responses.

## Demo App

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-starter.streamlit.app/)

## How to Run

### Prerequisites

- Python 3.6 or higher
- Streamlit
- LangChain
- OpenAI API key

### Steps

1. Clone this repository.
2. Install the necessary Python packages using the command `pip install -r requirements.txt`.
3. Set the environment variable for your OpenAI API key.
4. Run the Streamlit app using the command `streamlit run streamlit_app.py`.

## Usage

The chatbot starts with a system message that sets the tone for the conversation. It then alternates between receiving user inputs and generating AI responses. The conversation history is stored and used as context for generating future responses, allowing the chatbot to maintain conversational continuity.

## Contribution

Contributions, issues, and feature requests are welcome. Feel free to check the [Issues](https://github.com/AustonianAI/chatbot-starter/issues) page if you want to contribute.

## License

This project is licensed under the terms of the MIT license.
