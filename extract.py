import json
import re


def extract_memoir_json(conversation_path):
    with open(conversation_path, "r", encoding="utf-8") as f:
        conversation = json.load(f)

    messages = conversation.get("messages", [])

    candidates = []

    for message in messages:

        selected = message.get("currentlySelected", 0)
        versions = message.get("versions", [])

        if selected >= len(versions):
            continue

        version = versions[selected]

        if version.get("role") != "assistant":
            continue

        for step in version.get("steps", []):
            if step.get("type") != "contentBlock":
                continue

            for content in step.get("content", []):
                if content.get("type") != "text":
                    continue

                text = content.get("text", "")

                match = re.search(
                    r"```json\s*(.*?)\s*```",
                    text,
                    flags=re.DOTALL
                )

                if match is None:
                    continue

                memoir = json.loads(match.group(1))

                if "entries" not in memoir:
                    raise ValueError("Memoir JSON missing 'entries' field.")

                candidates.append(memoir)

    if candidates:
        return candidates[-1]

    raise ValueError("No memoir JSON code block found.")
