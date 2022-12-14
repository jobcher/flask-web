"""
@Time   :2022-12-14
@Author :jobcher
@File   :http.py
"""
import requests


class HTTP:
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text
