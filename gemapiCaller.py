import gradio as gr
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load API key from environment variables
def createAPI():
    load_dotenv()
    api_key = os.getenv("api_key")
    genai.configure(api_key=api_key)

# Function to call API
def callAPI(user_input):
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(
        f"""
        Goal
        Provide legal information in the specified language, referencing and citing the provided legal documents. Where appropriate, connect these references to relevant external legal sources or known standards. The information should be geared toward individuals who are not native to the United States, so do not assume they are familiar with US legal or cultural norms.

        Return Format
        Your answer should be in the language that the user used.
        Your answer must have two parts:

        Plain Legal Format (Concise)
        Answer the question concisely and then clearly state the legal information, citing the provided documents.
        Include relevant external references if they apply. Use precise, professional language suitable for a legal context, but keep it direct and succinct.
        

        8th-Grade Reading Level Explanation
        Translate the above legal points into simpler language, at roughly an 8th-grade level.
        Explain or define any US‐specific terms, practices, or norms.
        Use short, clear sentences that are easily understood by someone with limited background in US law.
    

        Warnings
        Do not include flowery or overly lengthy wording. Stay focused on clarity.
        Verify the correctness of legal references and citations.
        Do not assume the reader knows US cultural or legal norms; define or clarify as needed.
        Remember that this is informational only—include a disclaimer that formal legal counsel may be necessary.: {user_input}
        """
    )
    return response.text

# Gradio interface setup
demo = gr.Interface(
    fn=callAPI,
    inputs="textbox",
    outputs="textbox"  
)


if __name__ == "__main__":
    createAPI()
    demo.launch()
