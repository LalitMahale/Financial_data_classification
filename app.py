import gradio as gr

# Sample classes
class ResultA:
    def __init__(self, query):
        self.response = f"Result from Function A for query: {query}"

class ResultB:
    def __init__(self, query):
        self.response = f"Result from Function B for query: {query}"

class ResultC:
    def __init__(self, query):
        self.response = f"Result from Function C for query: {query}"

# Functions that return class instances
def function_a(query):
    return ResultA(query)

def function_b(query):
    return ResultB(query)

def function_c(query):
    return ResultC(query)

# Function to handle user input
def handle_query(function_choice, query):
    function_map = {
        "Function A": function_a,
        "Function B": function_b,
        "Function C": function_c,
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
