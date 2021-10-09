import requests
import json
from pprint import pprint
from tqdm import tqdm
import os
from api_vk import ApiVk
from ya_disk import YaUploader

id = '62486308'
TOKEN = ''


def send_photos_to_ya_disk(user, password):
    api_vk = ApiVk(user)
    api_vk.get_profile_photos()

    ya = YaUploader(token=password)
    folder = os.chdir(os.getcwd() + "\\" + str(user))
    files_list = os.listdir(path=folder)
    fold = ya.create_folder(str(user))
    for file in tqdm(files_list[-1:-6:-1]):
        ya.upload_file_to_disk(f"{fold}/{file}", file)

if __name__ == '__main__':
    send_photos_to_ya_disk(id, TOKEN)
