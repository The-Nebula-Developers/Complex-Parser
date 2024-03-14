import json
from fuzzywuzzy import fuzz
from nltk.corpus import wordnet

def extract_data(data: dict, format_keys: list, load_lists: dict) -> list:
    '''
    Extracts data from a JSON-like structure based on specified format keys.

    Parameters:
        data (dict): The JSON-like data structure to extract data from.
        format_keys (list): A list of keys representing the desired format.
        load_lists (list): A list containing additional words to load for synonyms.

    Returns:
        list: A list containing extracted data matching the specified format.

    Raises:
        This function does not explicitly raise any exceptions, but may encounter
        errors during execution due to malformed input or other issues.

    Example:
        data = {
            "name": "John",
            "age": 30,
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            },
            "contacts": [
                {"type": "email", "value": "john@example.com"},
                {"type": "phone", "value": "555-1234"}
            ]
        }
        format_keys = ["name", "address"]
        load_lists = ["street", "city"]
        extracted = extract_data(data, format_keys, load_lists)
        print(extracted)
        # Output: [{'name': 'John', 'address': {'street': '123 Main St', 'city': 'Anytown'}}]
    '''
    try:
        extracted_data = []
        if isinstance(data, dict):
            matches = {key: False for key in format_keys}
            for key in data.keys():
                for format_key in format_keys:
                    synonyms = get_synonyms(word=format_key, load_lists=load_lists)
                    if fuzz.token_sort_ratio(format_key, key) >= 70:
                        matches[format_key] = True
                    else:
                        for synonym in synonyms:
                            if fuzz.token_sort_ratio(synonym, key) >= 70:
                                matches[format_key] = True
                                break
            if all(matches.values()):
                extracted_data.append(data)
            for value in data.values():
                extracted_data.extend(extract_data(value, format_keys, load_lists))
        elif isinstance(data, list):
            for item in data:
                extracted_data.extend(extract_data(item, format_keys, load_lists))
        return extracted_data
    except Exception as e:
        print(f"[-] An Error has Occurred - {e}")

def get_synonyms(word: str, load_lists: dict) -> list:
    '''
    Retrieves synonyms for a given word, including additional synonyms loaded from custom lists.

    Parameters:
        word (str): The word to find synonyms for.
        load_lists (list): A list containing additional synonyms to load for specific words.

    Returns:
        list: A list containing synonyms for the input word.

    Raises:
        This function does not explicitly raise any exceptions, but may encounter
        errors during execution due to issues with wordnet or malformed input.

    Example:
        word = "happy"
        load_lists = {"happy": ["joyful", "cheerful"]}
        synonyms = get_synonyms(word, load_lists)
        print(synonyms)
        # Output: ['happy', 'felicitous', 'glad', 'well-chosen', 'joyful', 'cheerful']
    '''
    try:
        synonyms = set()
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                synonyms.add(lemma.name())
        synonym_list = list(synonyms)
        for key in load_lists:
            if key.lower() == word.lower():
                synonym_list.extend(load_lists[key])
        return synonym_list
    except Exception as e:
        print(f"[-] An Error has Occurred - {e}")