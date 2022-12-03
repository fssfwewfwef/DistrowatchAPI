import re

import aiohttp
from bs4 import BeautifulSoup
from .periods import PeriodType
from .requestable import Requestable


class Distributive:
    def __init__(self, name: str, points: int, is_increase: bool = False):
        self.name = name
        self.points = points
        self.is_increase = is_increase

    def __str__(self):
        return f"{self.name} ({self.points} {'+' if self.is_increase else '-'})"

    def __repr__(self):
        return self.__str__()


class Distrowatch(Requestable):
    def __init__(self):
        super().__init__("https://distrowatch.com")

    async def get_top_of_distributions(self, count: int = 10, period: str | PeriodType = PeriodType.LAST_WEEK):
        if isinstance(period, PeriodType):
            period = period.value
        top = await self.make_request(f"index.php", parameters={"dataspan": str(period)})
        table = BeautifulSoup(top, "html.parser").find(attrs={"class": "News", "style": "direction: ltr"})
        points = table.find_all(attrs={"class": "phr3"}, limit=count)
        names = table.find_all(attrs={"class": "phr2"}, limit=count)

        distributions = []

        for i in range(count):
            name = names[i].a.get_text()
            rating = int(re.match(r".*: (.*)", points[i]["title"]).groups()[0])
            is_increase = points[i].img["alt"] == ">"
            distributions.append(Distributive(name, rating, is_increase))

        return distributions


def get_session() -> aiohttp.ClientSession:
    return aiohttp.ClientSession()
