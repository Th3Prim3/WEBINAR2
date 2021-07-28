from netlab.sync_client import SyncClient
from netlab.enums import HDRSeverity
import datetime
import pprint
start = datetime.datetime.now()
print(f"Current time: {start}")

POD_ID = 150
START_POD_ID = 130
FINAL_POD_ID = 139


client = SyncClient()

accounts = client.user_account_list(com_id=12,
                                    acc_type='S',
                                    properties='acc_last_login')

pprint.pprint(accounts)



# for pod in range(START_POD_ID, FINAL_POD_ID+1):
#     print(f"Removing pod: {pod}")
#     result = client.pod_remove_task(pod_id=pod,
#                                     remove_vms="DISK",
#                                     severity_level=HDRSeverity.INFO,
#                                     )
#     print("{} - Pod {} Remove Result: \t{}".format(datetime.datetime.now(), pod, result['status']))
#
# finaltime = datetime.datetime.now() - start
#
#
#
# print(f"Script took {finaltime} seconds to complete.")
