from taipy.gui import Markdown

import pandas as pd

path = None
data = None

def drop_csv(state):
    state.data = pd.read_csv(state.path)

page_2_md = Markdown("pages/page_2/page_2.md")