from taipy.gui import Gui, Markdown, notify
from taipy.config import Config 

from pages.root.root import *
from pages.page_1.page_1 import page_1_md
from pages.page_2.page_2 import page_2_md

Config.load("config/config.toml")

def on_change(state, var_name:str, var_value):
    ...


pages = {"/":"<|navbar|>",
         "page_1":page_1_md,
         "page_2":page_2_md}


if __name__ == "__main__":
    gui = Gui(pages=pages)
    gui.run()
