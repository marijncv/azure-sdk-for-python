# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from azure.identity import DefaultAzureCredential
from azure.mgmt.logic import LogicManagementClient

"""
# PREREQUISITES
    pip install azure-identity
    pip install azure-mgmt-logic
# USAGE
    python create_or_update_a_workflow.py

    Before run the sample, please set the values of the client ID, tenant ID and client secret
    of the AAD application as environment variables: AZURE_CLIENT_ID, AZURE_TENANT_ID,
    AZURE_CLIENT_SECRET. For more info about how to get the value, please see:
    https://docs.microsoft.com/azure/active-directory/develop/howto-create-service-principal-portal
"""


def main():
    client = LogicManagementClient(
        credential=DefaultAzureCredential(),
        subscription_id="34adfa4f-cedf-4dc0-ba29-b6d1a69ab345",
    )

    response = client.workflows.create_or_update(
        resource_group_name="test-resource-group",
        workflow_name="test-workflow",
        workflow={
            "location": "brazilsouth",
            "properties": {
                "definition": {
                    "$schema": "https://schema.management.azure.com/providers/Microsoft.Logic/schemas/2016-06-01/workflowdefinition.json#",
                    "actions": {
                        "Find_pet_by_ID": {
                            "inputs": {
                                "host": {
                                    "connection": {
                                        "name": "@parameters('$connections')['test-custom-connector']['connectionId']"
                                    }
                                },
                                "method": "get",
                                "path": "/pet/@{encodeURIComponent('1')}",
                            },
                            "runAfter": {},
                            "type": "ApiConnection",
                        }
                    },
                    "contentVersion": "1.0.0.0",
                    "outputs": {},
                    "parameters": {"$connections": {"defaultValue": {}, "type": "Object"}},
                    "triggers": {"manual": {"inputs": {"schema": {}}, "kind": "Http", "type": "Request"}},
                },
                "integrationAccount": {
                    "id": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/test-resource-group/providers/Microsoft.Logic/integrationAccounts/test-integration-account"
                },
                "parameters": {
                    "$connections": {
                        "value": {
                            "test-custom-connector": {
                                "connectionId": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/resourceGroups/test-resource-group/providers/Microsoft.Web/connections/test-custom-connector",
                                "connectionName": "test-custom-connector",
                                "id": "/subscriptions/34adfa4f-cedf-4dc0-ba29-b6d1a69ab345/providers/Microsoft.Web/locations/brazilsouth/managedApis/test-custom-connector",
                            }
                        }
                    }
                },
            },
            "tags": {},
        },
    )
    print(response)


# x-ms-original-file: specification/logic/resource-manager/Microsoft.Logic/stable/2019-05-01/examples/Workflows_CreateOrUpdate.json
if __name__ == "__main__":
    main()
