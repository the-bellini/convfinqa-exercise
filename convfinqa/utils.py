"""
Functions that are used in document_processing and query_processing modules
"""

from openai import OpenAI

from gliner import GLiNER


client = OpenAI()

model = GLiNER.from_pretrained("urchade/gliner_mediumv2.1")


def chat_completion(system_prompt: str, user_prompt: str) -> str:
    """
    Generates a chat-based completion using specified system and user prompts.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return response.choices[0].message.content


def predict_entities(
    text: str,
    labels=[
        "Date",
        "Revenue",
        "Profit",
        "Percent",
        "Debt",
        "Cost",
        "Amount",
        "Fee",
        "Expense",
    ],
    threshold=0.5,
) -> list[dict]:
    """
    Predicts entities in the given text based on the specified labels and threshold.

    This function uses a model to predict entities within the input text. Each
    predicted entity is returned with its corresponding label.

    Args:
        text (str): The input text where entities are to be predicted.
        labels (list): A list of labels that the model should consider when predicting entities.
        threshold (float, optional): The confidence threshold for entity prediction.
                                      Defaults to 0.5.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary contains the text of the
                    predicted entity and its associated label.
    """

    entities = model.predict_entities(text, labels, threshold=threshold)

    # Display predicted entities and their labels
    entity_list = [entity["label"] for entity in entities]

    return entity_list
