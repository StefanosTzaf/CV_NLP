import gradio as gr
import numpy as np
import cv2

# Variable to store the coordinates of the clicked points
srcPoints = []

# Function to clear the points if we mis-select them
def clearSrcPoints():
    global srcPoints
    srcPoints = []
    return 0, None


# Function called when we click the input image
def onSelect(value, evt: gr.EventData):
    # Only add points if there are less than 4
    if len(srcPoints) < 4:
        # The 'value' parameter contains the clicked coordinates as (x, y)

        srcPoints.append([evt._data['index']])  # Store the clicked points as a pair of coordinates
    return len(srcPoints)


# Function to fix (unwrap) the image
def fixImg(value):
    img = value
    # Define the destination points (rectangle for the output image)
    dstPoints = np.float32(
        [
            [0, 0],
            [0, 800],
            [600, 800],
            [600, 0]
        ]
    )

    # Ensure there are exactly 4 source points
    if len(srcPoints) == 4:
        # Convert source points to numpy array
        srcFloat = np.float32(srcPoints)

        # Get the homography matrix
        H = cv2.getPerspectiveTransform(srcFloat, dstPoints)

        # Apply the homography matrix to the original image
        outputImage = cv2.warpPerspective(img, H, (600, 800))

        return outputImage
    else:
        return img  # If not enough points, return the original image


# Build the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown('Document Scanner')
    
    # Textbox to show the number of selected coordinates
    coordCounter = gr.Textbox(label='Number of Clicked Coordinates', value=0)

    # First row contains the images
    with gr.Row():
        # Upload the image to be fixed
        inp = gr.Image(label='Input')

        # Event to capture the points when clicked
        inp.select(fn=onSelect, inputs=inp, outputs=coordCounter)

        # Shows the fixed image
        out = gr.Image(label='Output')

    # Second row contains the buttons
    with gr.Row():
        btn = gr.Button('Fix!')
        btn.click(fn=fixImg, inputs=inp, outputs=out)

        btn2 = gr.Button("Reset")
        btn2.click(fn=clearSrcPoints, outputs=[coordCounter, out])

demo.launch()
