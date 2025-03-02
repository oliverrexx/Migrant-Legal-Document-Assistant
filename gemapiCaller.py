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
        You are the assistant of an immigration officer. 
        Your goal is to assist in the creating, processing, 
        and ensuring correctness in a legal document. 
        Ensure to use both the context and provided documents 
        in assistance. Address this using an 8th-grade reading level. 
        

        Ensure final judgments are left to the human, 
        but nudge them if they are not following proper 
        practices. AVOID using words like 'alien'. Use a tone that is not
        necessarily bubbly and friendly but generally more inviting.

        Respond in the language given in the user request. 

        User request: {user_input}
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
