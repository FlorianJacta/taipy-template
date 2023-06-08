from taipy.gui import Gui, Markdown, notify

value = 0

single_page = Markdown("""
# Taipy Application

Check the documentation [here](https://docs.taipy.io/en/latest/manuals/about/).

<|{value}|slider|on_change=on_slider|> <|Push|button|on_action=on_push|>

""")

def on_push(state):
    ...

def on_slider(state):
    if state.value == 100:
        notify(state, "success", "Taipy is running!")

def on_change(state, var_name:str, var_value):
    ...


if __name__ == "__main__":
    gui = Gui(single_page)
    gui.run()
