# Import required libraries
from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings


def chunker(
    document=str,
) -> None:
    """
    Chunks a document into smaller pieces using semantic chunking.

    This function uses the `OpenAIEncoder` to encode the document and then
    applies a `RollingWindowSplitter` to break the document into semantically
    meaningful chunks. Each chunk is returned as a dictionary with the chunk
    content.

    Args:
        document (str): The document to be chunked.

    Returns:
        list[dict]: A list of dictionaries, each containing a chunk of the
        document. The content of each chunk is stored in the "content" key.
    """
    text_splitter = SemanticChunker(OpenAIEmbeddings())
    docs = text_splitter.create_documents([document])
    return [doc.page_content for doc in docs]
