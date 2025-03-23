import gradio as gr
# define function foo
def foo(name,intensity):
    return f"Hello {name}! How are you? {int(intensity)}%"


# define the gradion interface
demo=gr.Interface(
    # we say to Gradio to use the function foo when the button is clicked
    fn=foo,
    inputs=['text',"slider"],
    outputs=['text']
)

# lunch the interdace 
demo.launch()