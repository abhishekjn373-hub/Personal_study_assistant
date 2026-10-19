import os
from google import genai as g
import gradio as gr
from google.genai import types
client = g.Client(api_key = os.getenv("GEMINI_API_KEY"))
proffession = {
    "Friendly": '''You are a very knowledgeable friend who helps to understand the concepts in 
    a better manner by explaining the concepts giving realworld examples and analogies 
    and also asking follow up questions.''',
    "Academic" : '''You are a very knowledgeable academic(down to earth and strict who have led 
    the succesful journey of many students who helps to understand the concepts in 
    a better manner by explaining the concepts giving realworld examples and analogies 
    and also asking follow up questions.'''
}
def study_as(question,persona):
    sys_prom = proffession[persona]
    response = client.models.generate_content(
        model ="gemini-3.1-flash-lite",
        config = types.GenerateContentConfig(
            system_instruction = sys_prom,
            temperature = 0.4,
            max_output_tokens = 1500
        ),
        contents = question
    )
    return response.text

demo = gr.Interface(
    fn = study_as,
    inputs = [
        gr.Textbox(label = "Question",lines = 6,placeholder="Ask a Question...."),
        gr.Radio(choices = list(proffession.keys()),label = "Persona",value = "Friendly")
    
    ],
    outputs = gr.Textbox(label = "Answer",lines = 10),
    title = "Simple QNA Study Assistant!!",
    description = "Ask a question and recive a output tailored to your desired persona!!"

)
demo.launch(debug = True)
