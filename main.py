import asyncio
from pprint import pprint
from netlab.async_client import NetlabClient


async def main():
    async with NetlabClient() as connection:
        info = await connection.system_status_get()
        pprint(info)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())