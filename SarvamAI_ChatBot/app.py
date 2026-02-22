import streamlit as st
import os
from sarvamai import SarvamAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="Sarvam AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# Custom CSS for a more premium look
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stChatInputContainer {
        padding-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Sarvam AI Chatbot")
st.markdown("---")

# Initialize Sarvam AI Client
@st.cache_resource
def get_sarvam_client():
    api_key = os.getenv("SarvamAI_API_KEY")
    if not api_key:
        st.error("API Key not found. Please set SarvamAI_API_KEY in your .env file.")
        st.stop()
    return SarvamAI(api_subscription_key=api_key)

client = get_sarvam_client()

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)

    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        try:
            # Call Sarvam AI API
            response = client.chat.completions(
                messages=[
                    {"role": m["role"], "content": m["content"]}
                    for m in st.session_state.messages
                ]
            )
            
            full_response = response.choices[0].message.content
            message_placeholder.markdown(full_response)
            
        except Exception as e:
            st.error(f"Error: {e}")
            full_response = "Sorry, I encountered an error. Please check your connection or API key."
            message_placeholder.markdown(full_response)

    # Add assistant response to history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
