import requests
import json

search_term = "kangaroo"
dataset_key = "d7dddbf4-2cf0-4f39-9b2a-bb099caae36c"

def get_species_images(taxon_key):
    """Fetches real-world occurrence photos for a specific taxon key."""
    occ_url = "https://api.gbif.org/v1/occurrence/search"
    occ_params = {
        "taxonKey": taxon_key,
        "mediaType": "StillImage",
        "limit": 3
    }
    try:
        occ_res = requests.get(occ_url, params=occ_params).json()
        photo_list = []
        for occ in occ_res.get('results', []):
            for media in occ.get('media', []):
                if media.get('type') == 'StillImage':
                    photo_list.append({
                        "url": media.get('identifier'),
                        "license": media.get('license'),
                    })
        return photo_list
    except Exception:
        return []

def get_safe_vernacular(record):
    """Safely extracts the first vernacular name or returns N/A."""
    v_names = record.get('vernacularNames', [])
    if isinstance(v_names, list) and len(v_names) > 0:
        return v_names[0].get('vernacularName', 'N/A')
    return "N/A"

def get_animal_data():
    species_url = "https://api.gbif.org/v1/species/search"
    species_params = {"datasetKey": dataset_key, "q": search_term}
    
    try:
        species_res = requests.get(species_url, params=species_params)
        species_res.raise_for_status()
        species_data = species_res.json()
        
        final_results = []

        for item in species_data.get('results', []):
            key = item.get('key')
            vernacular_name = get_safe_vernacular(item)
            
            # Constructing the exact dictionary from your requirement
            extracted_item = {
                'scientificName': item.get('scientificName', ''),
                'authorship': item.get('authorship', ''),
                'kingdom': item.get('kingdom', ''),
                'habitats': item.get('habitats', []),
                'threatStatuses': item.get('threatStatuses', []),
                'extinct': item.get('extinct', False), # Defaulted to False (boolean)
                'vernacularName': vernacular_name,
                'images': get_species_images(key)
            }
            
            # Optional: Only add if there are images, or remove this check to see everything
            if extracted_item['images']:
                final_results.append(extracted_item)

        return final_results

    except Exception as e:
        return {"error": str(e)}

# Execute and display
if __name__ == "__main__":
    data = get_animal_data()
    print(json.dumps(data, indent=4))