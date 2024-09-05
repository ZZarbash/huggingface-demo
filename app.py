from transformers import pipeline
import gradio as gradio

model = pipeline("summarization")

def predict(prompt):
    summary = model(prompt)[0]["summary_text"]
    return summary

with gr.Blocks() as demo:
    textbox = gr.TextBox(placeholder="Enter text for summarization, lines=4")
    gr.Interface(fn=predict, inpits=textbox, outputs="text")

demo.launch()