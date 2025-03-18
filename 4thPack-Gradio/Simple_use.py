import gradio as gr
# define function foo
def foo(name,intensity):
    return f"Hello {name}! How are you? {int(intensity)}%"


# define the gradion interface
demo=gr.Interface(
    fn=foo,
    inputs=['text',"slider"],
    outputs=['text']
)

# lunch the interdace 
demo.launch()