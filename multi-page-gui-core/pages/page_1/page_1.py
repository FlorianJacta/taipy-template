from taipy.gui import Markdown
import pandas as pd

scenario = None
results = None

def show_results(state):
    state.results = state.scenario.predictions.read()

page_1_md = Markdown("pages/page_1/page_1.md")