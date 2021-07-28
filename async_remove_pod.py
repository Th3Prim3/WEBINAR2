import asyncio
from netlab.async_client import NetlabClient, NetlabConnection
from netlab.enums import HDRSeverity
import datetime
import pprint


async def main():
    async with NetlabClient() as client:
        client: NetlabConnection

        start = datetime.datetime.now()
        print(f"Current time: {start}")

        START_POD_ID = 131
        FINAL_POD_ID = 139

        for pod in range(START_POD_ID, FINAL_POD_ID+1):
            print(f"Removing pod: {pod}")
            result = await client.pod_remove_task(pod_id=pod,
                                                  remove_vms="DISK",
                                                  severity_level=HDRSeverity.INFO,
                                                  )
            print("{} - Pod {} Remove Result: \t{}".format(datetime.datetime.now(), pod, result['status']))

        finaltime = datetime.datetime.now() - start

        print(f"Script took {finaltime} seconds to complete.")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())