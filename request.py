import requests
import json  # Added back for "pretty printing"

url = "https://api.gbif.org/v1/species/search"
params = {
    "datasetKey": "d7dddbf4-2cf0-4f39-9b2a-bb099caae36c",
    "q": "kangaroo"
}

search_keyword = "kangaroo"

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    filtered_results = []

    for record in data.get('results', []):
        sci_name = record.get("scientificName", "")
        v_list = record.get('vernacularNames', [])
        v_names_text = [v.get('vernacularName', '').lower() for v in v_list]
        
        found_in_sci = search_keyword.lower() in sci_name.lower()
        found_in_vernacular = any(search_keyword.lower() in vn for vn in v_names_text)

        if found_in_sci or found_in_vernacular:
            animal_info = {
                "scientificName": sci_name,
                "authorship": record.get("authorship"),
                "kingdom": record.get("kingdom"),
                "habitats": record.get("habitats", []),
                "threatStatuses": record.get("threatStatuses", []),
                "vernacularName": v_names_text[0] if v_names_text else "N/A"
            }
            filtered_results.append(animal_info)

    # Using json.dumps with indent=4 makes the terminal output much easier to read
    print(f"Found {len(filtered_results)} matches:\n")
    print(json.dumps(filtered_results, indent=4))

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")