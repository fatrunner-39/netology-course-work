import requests
import os
from tqdm import tqdm



# folder = os.chdir(r"C:\Users\alexa_000\PycharmProjects\course_project_python_first\avatars")
# files_list = os.listdir(path=folder)
# print(files_list)



from pprint import pprint


TOKEN = 'AQAAAAAcaxtmAADLW_LZp6a8bkgOu44HZeA7HsY'


class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def create_folder(self, name):
        folder_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {
            "path": name
        }
        folder = requests.put(folder_url, headers=headers, params=params)
        return name

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    ya = YaUploader(token=TOKEN)
    folder = os.chdir(os.getcwd() + "\\" + "None")
    files_list = os.listdir(path=folder)
    print(files_list)
    ya.create_folder('None')
    for file in tqdm(files_list[-1:-6:-1]):
        ya.upload_file_to_disk(f"None/{file}", file)


