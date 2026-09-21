# Technologies and Control Components

## Azure Policy

**Purpose:** Evaluate Azure resources against defined configuration requirements.

**Used in this project:**  
The custom policy uses `auditIfNotExists` to evaluate whether diagnostic settings with logging enabled exist for Azure resource groups.

This is an audit control. The policy identifies noncompliance but does not automatically remediate the resource.

## Azure Monitor SDK for Python

**Purpose:** Programmatically inspect Azure monitoring configuration.

**Used in this project:**  
`validate_sdk.py` uses `DefaultAzureCredential` and `MonitorManagementClient` to retrieve and display diagnostic settings associated with a specified Azure resource.

The script provides configuration visibility; it is not a complete compliance-validation or remediation engine.

## Azure Logic Apps

**Purpose:** Provide workflow automation that can support alerting, escalation, and integration with operational processes.

**Used in this project:**  
`logic_app_template.json` defines the Logic App workflow resource `alert-on-noncompliant-resource`.

The current template does not contain implemented triggers or actions. It represents a starting point for a future noncompliance notification workflow rather than a completed alerting capability.

## Terraform

**Purpose:** Provide repeatable infrastructure provisioning through Infrastructure as Code.

**Used in this project:**  
`main.tf` configures the AzureRM provider and creates the resource group used by the project.

The repository does not contain Terraform deployment of the policy, Logic App, diagnostic settings, or a broader monitoring environment.

## Security Architecture Relationship

These components represent different parts of a potential diagnostic-governance control:

**Terraform → Supporting infrastructure**

**Azure Policy → Configuration evaluation**

**Azure SDK → Programmatic inspection**

**Logic Apps → Potential workflow and escalation integration**

A production implementation would require these capabilities to be integrated with defined policy scope, identity and permissions, remediation, exception governance, telemetry validation, and operational ownership.
