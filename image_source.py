import requests


path = "put-the-right-path-here/data/train/class1"

for i in range(920):
    url = "https://picsum.photos/160/160/?random"
    response = requests.get(url)
    if response.status_code == 200:
        file_name = 'not_class_{}.jpg'.format(i)
        file_path = path + "/" + file_name
        with open(file_path, 'wb') as f:
            print("saving: " + file_name)
            f.write(response.content)