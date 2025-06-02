
from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient
import os

subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
credentials = DefaultAzureCredential()
client = MonitorManagementClient(credentials, subscription_id)

resource_id = "/subscriptions/<sub-id>/resourceGroups/<rg-name>"
settings = client.diagnostic_settings.list(resource_id)
for s in settings.value:
    print(f"Diagnostic Setting: {s.name}")
