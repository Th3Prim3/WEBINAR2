import asyncio

from netlab.async_client import NetlabClient, NetlabConnection
from netlab import enums

SOURCE_POD_ID = 100
POD_NAME_TEMPLATE = 'example_pod_{}'
POD_RANGE = range(150, 159)


async def clone_pod(client: NetlabConnection, pod_number: int):
    pod_name = POD_NAME_TEMPLATE.format(pod_number)

    await client.pod_clone_task(
        source_pod_id=SOURCE_POD_ID,
        clone_pod_id=pod_number,
        clone_pod_name=pod_name,
        pc_clone_specs=[{
            "source_snapshot": "GOLDEN_MASTER",
            "clone_snapshot": "GOLDEN_MASTER",
            },{
            "source_snapshot": "GOLDEN_MASTER",
            "clone_snapshot": "GOLDEN_MASTER",
            },
            ])
    await client.pod_state_change(pod_id=pod_number, state=enums.PodState.ONLINE)

    return pod_name


async def main():
    async with NetlabClient() as client:
        for pod_task in asyncio.as_completed([
            clone_pod(client, i) for i in POD_RANGE
        ]):
            pod_name = await pod_task

            print(f'Cloned pod: {pod_name}')


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
