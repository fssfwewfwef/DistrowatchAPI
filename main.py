from api.distrowatch import Distrowatch
from api.periods import PeriodType
import asyncio


async def main():
    distrowatch = Distrowatch()
    print(await distrowatch.get_top_of_distributions(10, PeriodType.LAST_MONTH))


if __name__ == "__main__":
    asyncio.run(main())
