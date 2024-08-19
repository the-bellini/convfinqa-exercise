from convfinqa.utils import predict_entities

from .utils.semantic_chunking import chunker
from .utils.summarise import generate_summary


def execute_document_processing(data: dict) -> str:
    """
    Processes a financial document and returns the result as a JSON string.

    Args:
        data (dict): A dictionary containing pre-text, post-text, and annotation details.

    Returns:
        str: A JSON string containing the processed pre-text, post-text, amount table, summary, and entity chunks.
    """
    pre_text = data["pre_text"]
    post_text = data["post_text"]
    amt_table = data["annotation"]["amt_table"]
    summary = generate_summary(data=data)
    entity_chunks = [
        {"labels": predict_entities(chunk), "chunk": chunk}
        for chunk in chunker(document=f"{pre_text} \n{post_text}")
    ]

    # Construct the output as a dictionary
    return {
        "pre_text": pre_text,
        "post_text": post_text,
        "amt_table": amt_table,
        "summary": summary,
        "entity_chunks": entity_chunks,
    }
