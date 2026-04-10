import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, AIMessage
from dotenv import load_dotenv
import time
import os

load_dotenv()

st.set_page_config(page_title="Nova AI", page_icon="✦")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@800&display=swap');
.nova {
    text-align: center;
    padding: 1.5rem 0 1rem;
    font-family: 'Syne', sans-serif;
    font-size: 2.5rem;
    font-weight: 800;
    background: linear-gradient(135deg, #fff 0%, #c084fc 50%, #f0c060 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.dot {
    display: inline-block;
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #4ade80;
    box-shadow: 0 0 8px #4ade80;
    animation: p 2s ease-in-out infinite;
    vertical-align: middle;
    margin-right: 6px;
}
@keyframes p { 50% { opacity: 0.4; transform: scale(0.8); } }
</style>
<div class="nova">✦ Nova</div>
<p style="text-align:center;color:#888;font-size:.8rem;letter-spacing:.1em">
  <span class="dot"></span>POWERED BY LLAMA 3.1
</p>
<hr style="border-color:#222;margin-bottom:1rem">
""", unsafe_allow_html=True)

llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    api_key=os.getenv("GROQ_API_KEY")
    )

# Memory lives in session state
# without this Chat would reset every time user sends a message
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display full history
for msg in st.session_state.messages:
    role = "user" if isinstance(msg, HumanMessage) else "assistant"
    with st.chat_message(role):
        st.write(msg.content)

# Input & response
if user_input := st.chat_input("Message Nova..."):
    st.session_state.messages.append(HumanMessage(content=user_input))
    with st.chat_message("user"):
        st.write(user_input)

    # # Typewriter effect — line by line
    full_response = llm.invoke(st.session_state.messages).content

    with st.chat_message("assistant"):
        box = st.empty()
        displayed = ""
        for char in full_response:
            displayed += char
            if char == " ":
                # box.markdown(displayed)
                box.markdown(displayed + "▌")
                time.sleep(0.03)
        box.markdown(displayed)    # final render to catch last word

    st.session_state.messages.append(AIMessage(content=full_response))