import json
import requests

def post_data(data):
    url = 'http://scd.prefi.tech/edit_one/'
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    try:
        response.raise_for_status()
        print(f"POST request successful {response.status_code=} for oeuvre {data['oeuvre_num_livres']}")
    except requests.exceptions.RequestException as e:
        print(f"Error making POST request for {data['oeuvre_num_livres']}, traceback:\n {response.text}")
        # raise e

def main():
    file_path = '../final_full.json'

    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            if isinstance(json_data, list):
                skip = 0
                for index, element in enumerate(json_data[skip::]):
                    # print(f"{index+skip=}")
                    post_data(element)
            else:
                print("The JSON file should contain an array of elements.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {file_path}")

if __name__ == "__main__":
    main()
