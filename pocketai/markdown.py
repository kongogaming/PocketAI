from rich.markdown import Markdown

def render_markdown(text: str):
    """
    Convert markdown text into a Rich Markdown object.
    """
    return Markdown(text)