import json


def update_description():
    """
    Update description from about.md
    """
    # Open and read the about markdown file
    with open('./data/about.md', 'r') as file:
        description = file.read()

    # Load existing data from the JSON file
    with open('./data/dataset-metadata.json', 'r') as file:
        data = json.load(file)

    data["description"] = description

    with open('./data/dataset-metadata.json', 'w') as file:
        json.dump(data, file, indent=4)
