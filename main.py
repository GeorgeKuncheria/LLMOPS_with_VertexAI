import vertexai
import streamlit as st

from vertexai.preview.generative_models import (
    GenerativeModel,

)
from dotenv import load_dotenv
import os

load_dotenv()

project_id = os.getenv("project_id")
region = os.getenv("region")



#Authenticate with Google Cloud
vertexai.init(project=project_id, location=region)


#load the model
model_name=GenerativeModel("gemini-2.0-flash-001")

def user_interfaces():
    st.set_page_config("Vertex AI")

    st.header("Vertex AI - Generative Models")

    user_question =st.text_input("Ask me anything...")

    if user_question:
        response = model_name.generate_content(user_question,stream=True)

        for res in response:
            st.write(res.text,end=" ")

    
if __name__ == "__main__":
    user_interfaces()

