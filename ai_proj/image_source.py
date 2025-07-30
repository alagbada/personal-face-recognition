import requests


path = "/home/user/Downloads/ai_proj/data/train/others"

for i in range(920):
    url = "https://picsum.photos/160/160/?random"
    response = requests.get(url)
    if response.status_code == 200:
        file_name = 'not_temitope_{}.jpg'.format(i)
        file_path = path + "/" + file_name
        with open(file_path, 'wb') as f:
            print("saving: " + file_name)
            f.write(response.content)