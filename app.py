import streamlit as st
import google.generativeai as palm
import os

# Configure API key
api_key = "AIzaSyANRYSr7eexKrBxwketjhWxtwt7lrei_OI"
palm.configure(api_key=api_key)

# Streamlit app
def main():
    st.title("Abstract Summarizer with PaLM 2")

    # Get available models
    models = [m.name for m in palm.list_models() if 'generateMessage' in m.supported_generation_methods]

    # Model selection dropdown
    selected_model = st.selectbox("Select a model:", models)
    
    # Default question text
    default_question = "hello, I need a short summary and Indonesian translation of one paragraph. Can you provide a professional Indonesian translation and a short summary? :"

    # Input for user question
    question = st.text_area("Ask a question:", value=default_question, height=300)

    if st.button("Submit"):
        if question:
            # Chat interaction
            response = palm.chat(
                model=selected_model,
                context="You are a professional Indonesian translator and good at summarizing a paragraph.",
                messages=question,
            )

            # Display response
            st.text("Response:")
            st.write(response.last)
        
if __name__ == "__main__":
    main()
