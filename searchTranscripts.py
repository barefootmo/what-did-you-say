import os
import json
searchTerm = input("Enter search term: ")
path = "C://users/moult/documents/making gold/audio/_transcriptions"
for filename in os.listdir(path):
    if filename.lower().endswith(('.json')):
        f = os.path.join(path, filename)
        with open(f) as json_file:
            data = json.load(json_file)
            data = data['text']
            if searchTerm in data:
                print(filename)
        json_file.close()
    else:
        print('skipping: ', filename)
