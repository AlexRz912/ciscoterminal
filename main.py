
from textual.app import App
from textual.containers import Horizontal, Vertical
from textual.widgets import Button, Input, Static



class ButtonsAndInputsApp(App):
    CSS_PATH = "test.tcss"
    def compose(self):
        with Horizontal():
            yield Static("(Config)#:", id="line-interface")
            yield Input(placeholder="type command here")

     
if __name__ == "__main__":

    app = ButtonsAndInputsApp()
    app.run()





# use compose for composing the backbone elements of the TUI
        # Buttons
        #yield Button("Click me!")
        #yield Button("Primary!", variant="primary")
        #yield Button.success("Success!")
        #yield Button.warning("Warning!")
        #yield Button.error("Error!")

        # Inputs
        #yield Input()
        #yield Input(placeholder="Password", password=True)
        #yield Input(placeholder="Type a number here",type="number",tooltip="Digits only please!",)
