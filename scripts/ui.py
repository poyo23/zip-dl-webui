from modules import script_callbacks
import gradio as gr

from scripts.dl_module import donwload_images

def dl_tab():
    with gr.Blocks() as main_block:
        with gr.Row():
            with gr.Column():
                download_button = gr.Button(value="Download!!", variant="primary")
                gr.HTML(value="detail setting")
                grid_images_chk = gr.Checkbox(label="Include grid images (Unix only)", value=False)

            with gr.Column():
                output_zip = gr.File(label="outputs.zip")
                output_html = gr.HTML(elem_id=f'output_text')

        download_button.click(
            fn=donwload_images,
            # _js="ProgressUpdate",
            inputs=[grid_images_chk
                   ] ,
            outputs=[output_html,output_zip],
#            show_progress = True,
        )

    return (main_block, "Download images", "download_images"),


script_callbacks.on_ui_tabs(dl_tab)


