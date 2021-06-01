from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.compute import ComputeManagementClient

SUBSCRIPTION_ID = 'bed04b49-bcf7-4326-a7d7-106cb38f5bde'
GROUP_NAME = 'testvm_machine1_res'
LOCATION = 'germanywestcentral'
VM_NAME = 'testvm1'

def get_credentials():
    credentials = ServicePrincipalCredentials(
        client_id = 'application-id',
        secret = 'authentication-key',
        tenant = 'tenant-id'
    )
    return credentials

credentials = get_credentials()


#print("Hello")