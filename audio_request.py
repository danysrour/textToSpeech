import requests


class AudioRequest:
    def __init__(self, url, querystring, headers):
        self.url = url
        self.querystring = querystring
        self.headers = headers

    def request_audio_data(self):
        response = requests.get(self.url, headers=self.headers, params=self.querystring)
        response.raise_for_status()
        return response.content
