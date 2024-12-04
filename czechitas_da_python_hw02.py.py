import json


def remove_empty_string(value):
    """This function replaces empty string within a list for an empty list"""
    if value == ['']:
        return []
    else:
        return value


with open("netflix_titles.tsv", mode="r", encoding="utf-8") as tsvfile:
    tsvreader = tsvfile.readlines()

column_index = {}
selected_columns = ["PRIMARYTITLE", "DIRECTOR", "CAST", "GENRES", "STARTYEAR"]
for column in selected_columns:
    index_value = tsvreader[0].split('\t').index(column)
    column_index[column] = index_value

titles = []
for row in tsvreader[1:]:
    split_row = row.split('\t')
    selected_cells = {}
    selected_cells["title"] = split_row[column_index["PRIMARYTITLE"]]
    selected_cells["directors"] = remove_empty_string(
        split_row[column_index["DIRECTOR"]].split(", "))
    selected_cells["cast"] = remove_empty_string(
        split_row[column_index["CAST"]].split(", "))
    selected_cells["genres"] = split_row[column_index["GENRES"]].split(",")
    selected_cells["decade"] = int(
        (split_row[column_index["STARTYEAR"]])[0:-1] + '0')
    titles.append(selected_cells)

with open("hw02_output.json", mode="w", encoding="utf-8") as output_file:
    json.dump(titles,
              output_file, indent=4, ensure_ascii=False)
