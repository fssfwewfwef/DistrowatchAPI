from abc import ABC

import aiohttp
from aiohttp import ClientSession, ClientTimeout
from json import loads

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9 "
    ,
    "Accept-Encoding": "gzip, deflate, br"
    ,
    "Accept-Language": "ru,en;q=0.9"
    ,
    "Cache-Control": "max-age=0"
    ,
    "Connection": "keep-alive"
    ,
    "Host": "distrowatch.com"
    ,
    "Sec-Fetch-Dest": "document"
    ,
    "Sec-Fetch-Mode": "navigate"
    ,
    "Sec-Fetch-Site": "none"
    ,
    "Sec-Fetch-User": "?1"
    ,
    "Upgrade-Insecure-Requests": "1"
    ,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.0.2419 Yowser/2.5 Safari/537.36"
    ,
    "sec-ch-ua": '"Chromium";v="106", "Yandex";v="22", "Not;A=Brand";v="99"'
    ,
    "sec-ch-ua-mobile": "?0"
    ,
    "sec-ch-ua-platform": "Windows"
}


class Requestable(ABC):
    def __init__(self, url: str):
        self.url = url

    async def make_request(self, request: str, method: str = "GET", parameters: dict[str, str | int] = None) -> str:

        parameters_without_null = {}

        if parameters is None:
            parameters = {}

        url = f"{self.url}/{request}"

        for parameter in parameters:
            value = parameters[parameter]
            if value is not None:
                parameters_without_null[parameter] = value

        async with ClientSession(headers=HEADERS) as session:
            async with session.request(url=url, method=method, params=parameters_without_null, ) as response:
                print(response.url)
                return await response.text()
