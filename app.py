import gradio as gr
from gen_ai import traditional_model,llm_model

# Functions that return class instances
def function_a(query):
    return traditional_model(query).predict()

def function_b(query):
    return llm_model(query)


# Function to handle user input
def handle_query(function_choice, query):
    function_map = {
        "FinBERT": function_a,
        "Function B": function_b,

    }
    
    if function_choice in function_map:
        result = function_map[function_choice](query)
        return result.response
    else:
        return "Invalid selection."

# Gradio Interface
iface = gr.Interface(
    fn=handle_query,
    inputs=[
        gr.Radio(["Function A", "Function B", "Function C"], label="Select Function"),
        gr.Textbox(label="Enter Query")
    ],
    outputs=gr.Textbox(label="Response"),
    title="Function Selector",
    description="Select a function, enter a query, and get a response.",
        # Adding footer details
    article="""
    **About this application:**
    This tool allows users to select a function, input a query, and get a response based on the selected function.
    Developed using Gradio.
    """
)

iface.launch()
