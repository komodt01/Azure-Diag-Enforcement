import os

from azure.identity import DefaultAzureCredential
from azure.mgmt.monitor import MonitorManagementClient


def list_diagnostic_settings(subscription_id, resource_id):
    """List diagnostic settings configured for an Azure resource."""

    credential = DefaultAzureCredential()
    monitor_client = MonitorManagementClient(credential, subscription_id)

    settings = monitor_client.diagnostic_settings.list(resource_id)

    if not settings.value:
        print("No diagnostic settings found.")
        return

    print("Diagnostic settings found:")

    for setting in settings.value:
        print(f"- {setting.name}")


if __name__ == "__main__":
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    resource_id = os.environ.get("AZURE_RESOURCE_ID")

    if not subscription_id:
        raise ValueError(
            "AZURE_SUBSCRIPTION_ID environment variable is required."
        )

    if not resource_id:
        raise ValueError(
            "AZURE_RESOURCE_ID environment variable is required."
        )

    list_diagnostic_settings(subscription_id, resource_id)
