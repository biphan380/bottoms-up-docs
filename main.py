import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))

from llama_docs_bot.markdown_docs_reader import MarkdownDocsReader
from llama_index import SimpleDirectoryReader

# use the custom MarkdownDocsReader
def load_markdown_docs(filepath):
    """Load markdown docs from a directory, excluding all other file types."""
    loader = SimpleDirectoryReader(
        input_dir=filepath, 
        exclude=["*.rst", "*.ipynb", "*.py", "*.bat", "*.txt", "*.png", "*.jpg", "*.jpeg", "*.csv", "*.html", "*.js", "*.css", "*.pdf", "*.json"],
        file_extractor={".md": MarkdownDocsReader()},
        recursive=True
    )

    return loader.load_data()

# load our documents from each folder.
# we keep them seperate for now, in order to create seperate indexes later
getting_started_docs = load_markdown_docs("docs/getting_started")
community_docs = load_markdown_docs("docs/community")
data_docs = load_markdown_docs("docs/core_modules/data_modules")
agent_docs = load_markdown_docs("docs/core_modules/agent_modules")
model_docs = load_markdown_docs("docs/core_modules/model_modules")
query_docs = load_markdown_docs("docs/core_modules/query_modules")
supporting_docs = load_markdown_docs("docs/core_modules/supporting_modules")
tutorials_docs = load_markdown_docs("docs/end_to_end_tutorials")
contributing_docs = load_markdown_docs("docs/development")

from llama_index.schema import MetadataMode

print(getting_started_docs)