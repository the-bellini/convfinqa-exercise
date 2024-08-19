from convfinqa.utils import chat_completion


def generate_summary(data: dict) -> dict:
    """
    Generates a brief summary of financial information based on pre and post text data.
    """
    # Define prompts
    pre_post_text = f"pre_text: {data['pre_text']} post_text: {data['post_text']}"
    system_prompt = """
    You are an expert at summarising financial information. 
    Include any dates and numerical figures in the document. 
    Return a brief summary and only the summary. Do not hallucinate."""

    return {
        "summary": chat_completion(
            system_prompt=system_prompt, user_prompt=pre_post_text
        )
    }
