from netlab.sync_client import SyncClient
from netlab.enums import HDRSeverity
import datetime

SOURCE_POD_ID = 100
CLONE_POD_BASE_ID = 121
COUNT = 30
CLONE_DATASTORE = "H23_LOCAL_SSD_CLONE"
CLONE_POD_NAME = "H23_PT8_P"
CLONE_ROLE = "NORMAL"
CLONE_VH_ID = 12


start = datetime.datetime.now()
print(f"Current time: {start}")
client = SyncClient()
for pod in range(CLONE_POD_BASE_ID, (CLONE_POD_BASE_ID+COUNT)):
    print('{} - Starting pod clone id: \t{}'.format(datetime.datetime.now(), pod))
    result = client.pod_clone_task(source_pod_id=SOURCE_POD_ID,
                                   clone_pod_id=pod,
                                   severity_level=HDRSeverity.INFO,
                                   clone_pod_name=CLONE_POD_NAME + str(pod),
                                   pc_clone_specs=[
                                       {"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                       {"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                       #{"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                       #{"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                       #{"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                       #{"clone_datastore": CLONE_DATASTORE, "clone_vh_id": CLONE_VH_ID, "clone_role": CLONE_ROLE},
                                    ])
    print("{} - Pod Clone Result: \t{}".format(datetime.datetime.now(), result['status']))
    state_output = client.pod_state_change(pod_id=pod, state="ONLINE")
    print("{} - Brought Pod {} Online: \t".format(datetime.datetime.now(), str(pod), state_output))

finaltime = datetime.datetime.now() - start
print(f"Script took {finaltime} seconds to complete.")
