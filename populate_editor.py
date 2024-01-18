import json
import requests

def post_data(data):
    url = 'http://localhost:8000/editor/'
    headers = {'Content-Type': 'application/json'}

    response = requests.post(url, data=json.dumps(data), headers=headers)
    try:
        response.raise_for_status()
        # print(f"POST request successful for data: {data}")
    except requests.exceptions.RequestException as e:
        print(f"Error making POST request for {data[0]['oeuvre_num_livres']}, traceback:\n {response.text}")
        # raise e

def main():
    file_path = '../final_full.json'

    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            if isinstance(json_data, list):
                skip = 6000
                for index, element in enumerate(json_data[skip::]):
                    if int(element["oeuvre_num_livres"]) in (8077, 8094, 8105, 8118, 8129, 8130, 8131, 8132,):
                        # print(f"{index+skip=}")
                        post_data([element])
            else:
                print("The JSON file should contain an array of elements.")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON in {file_path}")

if __name__ == "__main__":
    main()
