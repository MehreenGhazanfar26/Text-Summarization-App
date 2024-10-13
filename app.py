
import streamlit as st
from transformers import pipeline

# Set up the Hugging Face summarization pipeline
summarizer = pipeline("summarization")

# Title of the app
st.title("Text Summarization App")

# Add a text description
st.write("Upload your document below for summarization:")

# File uploader for text-based documents)
uploaded_file = st.file_uploader("Choose a text file", type=["txt"])


if uploaded_file is not None:
    # Read the uploaded file
    text = uploaded_file.read().decode("utf-8")
    
    # Display the original text
    st.subheader("Original Text")
    st.write(text)
        # Truncate the text if it's too long for the model (max ~1024 tokens)
    if len(text) > 2000:  # Adjust the length based on your model's token limit
        st.warning("The uploaded text is too long. It will be truncated for summarization.")
        text = text[:2000]  # Truncate to fit the model's input size

    # Summarize the text
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            summary = summarizer(text, max_length=150, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]['summary_text'])