from email.mime import text
from unicodedata import category

from fastapi import FastAPI
from pydantic import BaseModel
from chromadb import Client

app = FastAPI()

# Chroma DB
client = Client()

collection = client.create_collection(name="quotes")

# Load quotes from the file and add them to the collection
# The file should have the format: text|author|category
with open("quotes.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for i, line in enumerate(lines):
        text, author, category = line.strip().split("|")
        # Add the quote to the Chroma DB collection
        # Each quote is stored as a document with metadata for the author and category
        # The document ID is generated using uuid4 to ensure uniqueness
        # The collection.add() method takes a list of documents, a list of metadata dictionaries, and a list of IDs.
        # The documents are the quote texts, the metadata includes the author and category, and the IDs are unique identifiers for each quote.
        # This allows us to efficiently store and retrieve quotes based on their content and metadata.
        # The quotes are stored in the collection with their associated metadata, which can be used for querying and filtering later on.
        collection.add(
        documents=[text],
        metadatas=[{"author": author, "category": category}],
        ids=[f"id_{i}"]
)


@app.get("/quotes", response_model=list[str])
def get_quote(quote_context: str) -> list[str]:
    context = quote_context.split(",")
    
    # Query the collection for quotes that match the context
    # The query_texts parameter is set to the context, which is a list of strings that we want to match against the quote texts in the collection.
    # The n_results parameter is set to 5, which means we want to retrieve the
    # top 5 matching quotes from the collection.
    quote = collection.query(
    query_texts=context,
    n_results=5,
    )
    return quote["documents"][0]