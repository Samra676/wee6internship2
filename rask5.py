import gradio as gr

def square_number(number):
    return f"The square of {number} is {number ** 2}"

with gr.Blocks(theme=gr.themes.Base(), css="body { background-color: black; }") as demo:
    gr.Markdown("## 🌙 **Square Calculator (Dark Mode)**", elem_classes="title")
    gr.Markdown("Enter a number below and click the button to see its square.")
    
    with gr.Row():
        number_input = gr.Number(label="Enter a number")
        calc_button = gr.Button("Calculate")
    
    output = gr.Textbox(label="Result")
    
    calc_button.click(fn=square_number, inputs=number_input, outputs=output)

demo.launch()
