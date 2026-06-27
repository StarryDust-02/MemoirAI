from pathlib import Path

from extract import extract_memoir_json
from latex import compile_memoir_pdf


LMSTUDIO_CONVERSATIONS = (
    Path.home()
    / ".lmstudio"
    / "conversations"
)


def main():

    filename = input("Conversation file: ").strip()

    if not filename.endswith(".json"):
        filename += ".json"
    elif not filename.endswith(".conversation.json"):
        filename += ".conversation.json"

    conversation_path = LMSTUDIO_CONVERSATIONS / filename

    try:
        memoir = extract_memoir_json(conversation_path)

        # Debug use
        # print(memoir)
        
        compile_memoir_pdf(memoir)
        print("Memoir PDF generated successfully.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
