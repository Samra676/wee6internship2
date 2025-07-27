import gradio as gr

def reverse_sentence(sentence):
    return sentence[::-1]

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("## 🔄 **Reverse Sentence App**")
    gr.Markdown("Type any sentence below and see it reversed instantly!")
    
    sentence_input = gr.Textbox(lines=2, placeholder="Enter your sentence here...", label="Your Sentence")
    reverse_button = gr.Button("Reverse")
    
    output = gr.Textbox(label="Reversed Sentence")
    
    reverse_button.click(fn=reverse_sentence, inputs=sentence_input, outputs=output)

demo.launch()
