import streamlit as st
from transformers import pipeline

# Initialize the text generation pipeline with the desired model
generator = pipeline("text-generation", model="gpt2")

# Streamlit app title
st.title("Health Chatbot")

# Initialize session state for conversation history
if 'history' not in st.session_state:
    st.session_state.history = []

# Function to generate chatbot responses
def generate_response(user_input):
    response = generator(user_input, max_length=150, num_return_sequences=1,
                          pad_token_id=50256, temperature=0.7, top_k=50, top_p=0.95)
    return response[0]['generated_text']

# Input box for user symptoms
user_input = st.text_input("Describe your symptoms:")

if st.button("Ask"):
    if user_input:
        # Store the user's input in the conversation history
        st.session_state.history.append(f"You: {user_input}")

        # Generate the chatbot's response
        bot_response = generate_response(user_input)

        # Store the chatbot's response in the conversation history
        st.session_state.history.append(f"Bot: {bot_response}")

        # Clear the input box
        user_input = ""

# Display the conversation history
if st.session_state.history:
    st.subheader("Conversation History")
    for message in st.session_state.history:
        st.write(message)
