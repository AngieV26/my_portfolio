import json
import re


def text_edit(text):
    return re.sub(r"[ \n]", "", text)


with open("alice.txt", mode="r", encoding="utf-8") as input_file:
    text = input_file.read().lower()

edited_text = text_edit(text)
unique_characters = set(edited_text)
unique_characters_count = dict()
for character in unique_characters:
    unique_characters_count[character] = text.count(character)

unique_characters_count_sorted = dict(sorted(unique_characters_count.items()))

with open("hw01_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(unique_characters_count_sorted,
              output_file, indent=4, ensure_ascii=False)
