import requests
import json
from pprint import pprint
import os
from tqdm import tqdm




class ApiVk:

    def __init__(self, id=None, token='c9d46cd2f0ec7c9aba23d1fc77a132c7c4532f19bacc8bbd22973e0de7f5381a4e5a5ebb9f00c438825a5'):
        self.id = id,
        self.token = token

    def get_params(self):
        return {
            'user_id': self.id,
            'access_token': self.token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': '1',
            # 'photo_sizes': '0',
        }

    def get_profile_photos(self):
        URL = 'https://api.vk.com/method/photos.get'
        res = requests.get(URL, params=self.get_params())
        photos = res.json()['response']['items']
        photo_list = []
        likes = []
        folder_name = str(self.id).strip("(',)")
        os.mkdir(os.getcwd() + "/" + folder_name)
        for photo in tqdm(photos):
            sizes = []
            for obj in photo['sizes']:
                size = obj['height'] * obj['width']
                sizes.append(size)
            pos = sizes.index(max(sizes))
            likes_num = photo['likes']['count']
            if likes_num not in likes:
                likes.append(likes_num)
                with open(f'{folder_name}/{likes_num}.jpg', 'wb') as f:
                    f.write(requests.get(photo['sizes'][pos]['url']).content)
                photo_list.append({'file_name': f'{likes_num}.jpg',
                                   'size': photo['sizes'][pos]['type']})
            else:
                likes.append(str(likes_num) + '_' + str(photo['date']))
                with open(f'{folder_name}/{likes_num}_{photo["date"]}.jpg', 'wb') as f:
                    f.write(requests.get(photo['sizes'][pos]['url']).content)
                    photo_list.append({'file_name': f'{likes_num}_{photo["date"]}.jpg',
                                       'size': photo['sizes'][pos]['type']})
        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(photo_list, file, ensure_ascii=False, indent=4)
        return 'Загрузка завершена'

if __name__ == '__main__':
    api_vk = ApiVk()
    pprint(api_vk.get_profile_photos())