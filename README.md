# Complex Parser

Complex Parser is a powerful Python package designed to streamline the process of data extraction from JSON-like structures while also enriching the extracted data with synonym retrieval capabilities. Whether you're working with complex nested JSON data or simple dictionaries, this package provides a flexible and intuitive solution for extracting specific data elements based on user-defined format keys, all while expanding the semantic richness of your data through synonym retrieval.

## Features

### Data Extraction
- **Structured Data Extraction:** Extract specific data elements from nested JSON-like structures based on user-specified format keys.
- **Customizable Format Keys:** Define format keys to precisely target the data elements you need, making it adaptable to a wide range of data structures.
- **Efficient Data Parsing:** Utilizes efficient algorithms to parse through the data and extract relevant information with minimal computational overhead.

### Synonym Retrieval
- **Semantic Enrichment:** Enhance the semantic richness of your data by retrieving synonyms for key terms using both WordNet and custom synonym lists.
- **Flexible Synonym Loading:** Load additional synonyms from custom lists to expand the synonym pool for specific terms, allowing for fine-tuned control over synonym retrieval.

### Ease of Use
- **Simple Integration:** Integrate seamlessly into your Python projects with an intuitive interface and straightforward usage.
- **Comprehensive Documentation:** Detailed documentation and examples provided for easy reference and quick integration into your projects.

## Installation

You can install Json Data Extractor Synonymizer via pip:

```bash
pip install json-data-extractor-synonymizer
```

## Usage: 

Here's a simple example demonstrating how to use the package

```python
from complex_parser import extract_data

# Example data
data = {
    "people":[
        {
            "name": "John",
            "age": 30,
            "address": {
                "road": "123 Main St",
                "city": "Anytown"
            }
        }, 
        {
            "name": "Joshua",
            "age": 3100,
            "address": {
                "road": "657 Loud St",
                "city": "Basictown",
                "landmark": "Town Square"
            }
        }, 
        {
            "name": "John",
            "age": 30,
            "location": {
                "road": "8474 Main St",
                "city": "None"
            }
        }, 
        {
            "fullname": "Job",
            "age": 27,
            "destination": {
                "road": "8474 John's St",
                "city": "London"
            }
        }, 
        {
            "unknown": "Job",
            "age": 27,
            "destination": {
                "road": "8474 John's St",
                "city": "London"
            }
        }
    ]
}
format_keys = ["name", "address"]
load_lists= {
    "address":[
        "location"
    ], 
    "name": [
        "fullname"
    ]
}
# Extract data with specified format keys
extracted_data = extract_data(data=data, format_keys=format_keys,load_lists=load_lists)
print(extracted_data)
```

results: 

```bash
[{'name': 'John', 'age': 30, 'address': {'road': '123 Main St', 'city': 'Anytown'}}, {'name': 'Joshua', 'age': 3100, 'address': {'road': '657 Loud St', 'city': 'Basictown', 'landmark': 'Town Square'}}, {'name': 'John', 'age': 30, 'location': {'road': '8474 Main St', 'city': 'None'}}, {'fullname': 'Job', 'age': 27, 'destination': {'road': "8474 John's St", 'city': 'London'}}]
```

## License: 
This project is licensed under the Mozilla Public License Version 2.0 - see the [LICENSE](./LICENSE) file for details.

## Contributing
Contributions are welcome! Please feel free to submit bug reports, feature requests, or pull requests on the GitHub repository.
