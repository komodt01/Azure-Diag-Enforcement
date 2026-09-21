# Azure Diagnostic Enforcement – Security Logging Governance

## Overview

This project explores how Azure diagnostic logging can be treated as a governed security control rather than a configuration task left to individual resource owners.

The repository contains a small proof-of-concept for evaluating diagnostic configuration using Azure Policy and the Azure SDK, along with a Logic App workflow template and Terraform used to establish the supporting Azure resource group.

The implementation is intentionally limited. A separate technical architecture case study extends the lab into the security, governance, failure-handling, and production considerations that would be required for enterprise diagnostic enforcement.

## Security Problem

Security monitoring depends on the availability of reliable telemetry.

As an Azure environment grows, diagnostic settings can become inconsistent. Resources may be deployed without required logging, existing settings may be changed, or administrators may configure different destinations and logging categories.

The resulting risk is a security visibility gap: during an investigation or incident, the organization may discover that required telemetry was never collected.

The architectural problem is therefore not simply:

**Are diagnostic settings enabled?**

It is:

**Can the organization establish and continuously verify that required Azure resources have the expected diagnostic configuration and that deviations are identified and governed?**

## What I Implemented

The repository contains the following proof-of-concept components:

- Terraform configuration for an Azure resource group used by the project
- Custom Azure Policy using `auditIfNotExists` to evaluate whether diagnostic settings with logging enabled exist for resource groups
- Python validation script using `DefaultAzureCredential` and the Azure Monitor SDK to enumerate diagnostic settings for a specified resource
- Logic App ARM template defining the workflow resource used as the starting point for a noncompliance-alerting workflow
- Compliance and technology documentation
- Teardown guidance
- Technical architecture case study examining how the control would need to evolve for enterprise use

The Azure Policy in this repository is an **audit control**. It identifies the absence of the expected diagnostic configuration; it does not automatically remediate noncompliant resources.

The Logic App definition is also a **template**. Its trigger and action workflow is not implemented in the current repository.

## Control Concept

The lab demonstrates the beginning of a diagnostic-governance control:

**Azure Resource → Policy Evaluation → Compliance Status**

The Python SDK provides an additional way to inspect the diagnostic settings associated with a resource:

**Azure Resource → Azure Monitor SDK → Diagnostic Settings**

Together, these artifacts explore how diagnostic configuration can be evaluated programmatically instead of depending entirely on manual review.

## Security Architecture Perspective

The larger security concern is telemetry assurance.

A production diagnostic-enforcement architecture needs to consider several separate questions:

- Which resources are required to produce security telemetry?
- What diagnostic categories are required for each resource type?
- Where must that telemetry be sent?
- Who can change the logging requirement or destination?
- How is configuration drift identified?
- What happens when remediation fails?
- How are legitimate exceptions approved and reviewed?
- How can compliance be demonstrated to security governance and audit teams?
- How does the organization know telemetry is actually arriving?

The last question creates an important architectural distinction:

**Configuration compliance does not necessarily prove successful telemetry delivery.**

A resource may have the expected diagnostic configuration while telemetry is still unavailable because of another failure in the monitoring path.

For that reason, I would treat configuration enforcement and telemetry-health monitoring as complementary controls in a production architecture.

## Implemented Lab vs. Production Architecture

### Implemented in This Repository

- Azure resource group deployment through Terraform
- Azure Policy definition using `auditIfNotExists`
- Programmatic inspection of diagnostic settings through the Azure SDK
- Logic App workflow resource template
- Supporting security and compliance documentation

### Production Capabilities I Would Evaluate

A production implementation would require additional controls and design decisions, including:

- Policy assignment at the appropriate management-group, subscription, resource-group, or resource scope
- Resource-specific diagnostic requirements
- Automated remediation where the configuration is predictable and safe to enforce
- Managed identity and least-privilege permissions for remediation
- Monitoring for failed remediation
- Configuration-drift detection
- Exception ownership, justification, expiration, and review
- Validation that expected telemetry continues to arrive
- Controlled rollout and rollback of policy changes
- Audit evidence for policy changes, exemptions, compliance, and remediation
- Logging-volume and retention cost management
- Defined operational ownership for ongoing compliance

These are architectural recommendations and are not presented as capabilities implemented by this lab.

## Failure and Risk Considerations

Diagnostic enforcement should not silently fail.

A production control should distinguish between several conditions:

**Compliant → Required configuration exists**

**Noncompliant → Required configuration is missing or incorrect**

**Remediation Failed → Control attempted correction but could not restore compliance**

**Exception → Noncompliance has been explicitly reviewed and accepted for a defined scope and period**

**Telemetry Gap → Configuration appears correct, but expected telemetry is not being received**

These states have different operational and security implications and should not be treated as equivalent.

## Architecture Tradeoffs

### Audit vs. Automatic Remediation

The repository uses `auditIfNotExists`, which provides visibility without modifying resources.

Automatic remediation could reduce the amount of time a resource remains outside the logging standard, but it also increases the potential blast radius of an incorrect policy. Production use would require testing, scope control, appropriate permissions, and rollback planning.

### Standardization vs. Resource-Specific Logging

A common logging requirement improves governance, but Azure resource types expose different diagnostic categories.

A production standard should define the security requirement consistently while allowing the implementation to reflect the telemetry capabilities of each resource type.

### Security Visibility vs. Cost

Collecting more telemetry is not automatically better security.

Diagnostic requirements should be based on defined security, operational, audit, or regulatory needs because unnecessary telemetry increases ingestion and retention costs and may add monitoring noise.

## Technical Architecture Case Study

The technical case study extends the proof-of-concept into an enterprise diagnostic-enforcement architecture.

It examines:

- Continuous policy evaluation
- Configuration drift
- Automated remediation
- Failed-remediation handling
- Identity and trust boundaries
- Exception governance
- Audit evidence
- Telemetry validation
- Production rollout
- Architecture decisions and tradeoffs

[Azure Diagnostic Enforcement – Technical Architecture Case Study](./Azure_Diagnostic_Enforcement_Technical_Case_Study.md)

## Repository Contents

- `README.md` – Project overview and security architecture context
- `Azure_Diagnostic_Enforcement_Technical_Case_Study.md` – Enterprise architecture analysis
- `main.tf` – Terraform configuration for the project resource group
- `policy.json` – Custom Azure Policy for auditing diagnostic settings
- `validate_sdk.py` – Azure SDK diagnostic-setting inspection
- `logic_app_template.json` – Logic App workflow resource template
- `project_summary.md` – Original project summary
- `technologies.md` – Technology overview
- `compliance_mapping.md` – Security-framework references
- `teardown.md` – Cleanup guidance

## Key Takeaway

The value of diagnostic enforcement is not simply enabling logging.

The security objective is to establish confidence that required telemetry controls are consistently applied, deviations are visible, failures have an owner and response path, and exceptions are governed.

This proof-of-concept demonstrates the underlying control idea. The accompanying architecture case study addresses what would have to change before that idea could be treated as an enterprise security control.
