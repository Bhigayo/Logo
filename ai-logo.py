import streamlit as st
import openai
import os

# Set up OpenAI API Key (Replace with your actual API key)
openai.api_key = os.getenv("OPENAI_API_KEY")

# Streamlit App UI
st.title("AI Logo & Brand Identity Generator")
st.write("Enter your brand details to generate a unique logo and identity!")

# User Inputs
brand_name = st.text_input("Brand Name", "Metic Apparel")
industry = st.text_input("Industry", "Fashion, Streetwear")
style = st.selectbox("Logo Style", ["Minimalist", "Bold", "Elegant", "Modern", "Vintage"])
color_preference = st.color_picker("Pick a Primary Brand Color", "#000000")

def generate_logo_prompt():
    return f"Generate a {style.lower()} logo for a brand called '{brand_name}' in the {industry} industry. The primary color should be {color_preference}."

if st.button("Generate Logo"):
    with st.spinner("Generating logo..."):
        response = openai.Image.create(
            prompt=generate_logo_prompt(),
            n=1,
            size="512x512"
        )
        image_url = response["data"][0]["url"]
        st.image(image_url, caption="Generated Logo", use_column_width=True)

st.write("**Note:** This is an early prototype. Future versions will include typography & brand identity suggestions.")
