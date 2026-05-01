# Install library
!pip install gradio

import gradio as gr
import random

# Your logic converted to function
def process_text(text, mode):
    words_list = text.split(" ")

    words = ("jie","ywe","dgw","rpw","qwc","pow")
    word1 = ("bwi","bvj","ygr","tuo","xsf")

    k = random.choice(words)
    p = random.choice(word1)

    result = []

    if mode == "Encode":
        for i in words_list:
            if len(i) >= 3:
                result.append(k + i[1:] + i[0] + p)
            else:
                result.append(i[::-1])

    else:  # Decode
        for i in words_list:
            if len(i) >= 3:
                c = i[3:-3]
                result.append(c[-1] + c[0:-1])
            else:
                result.append(i[::-1])

    return " ".join(result)


# Reset function
def reset():
    return "", "", "Ready for new input ✨"


# UI Design
with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🔐 Secret Code Encoder & Decoder")
    gr.Markdown("Convert your message into secret code and decode it back!")

    text_input = gr.Textbox(
        label="Enter Your Message",
        placeholder="Type your sentence here..."
    )

    with gr.Row():
        encode_btn = gr.Button("🔒 Encode")
        decode_btn = gr.Button("🔓 Decode")

    output = gr.Textbox(label="Result")

    # Buttons actions
    encode_btn.click(
        fn=lambda x: process_text(x, "Encode"),
        inputs=text_input,
        outputs=output
    )

    decode_btn.click(
        fn=lambda x: process_text(x, "Decode"),
        inputs=text_input,
        outputs=output
    )

    # 🔄 Clear Button
    clear_btn = gr.Button("🔄 Clear / Play Again")

    clear_btn.click(
        fn=reset,
        inputs=[],
        outputs=[text_input, output, output]
    )

# Launch app in browser
demo.launch(share=True)