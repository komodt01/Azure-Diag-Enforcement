# Azure Security Logging & Diagnostic Automation

This project demonstrates the use of Terraform to provision Azure infrastructure for centralized security logging, diagnostic collection, and alerting.

The environment includes a Log Analytics Workspace, network security controls, diagnostic settings, a Linux virtual machine, and a Logic App template for alerting workflows. The project explores how infrastructure automation can make security telemetry configuration more consistent and repeatable rather than relying entirely on manual configuration.

## Problem Being Addressed

Cloud monitoring depends on resources being configured to produce and forward the telemetry security and operational teams need.

As Azure environments grow, manually configuring diagnostic settings and supporting monitoring infrastructure can lead to inconsistent configurations and visibility gaps.

This project explores how Terraform can be used to establish the underlying logging and monitoring infrastructure consistently and how those technical controls could support a broader diagnostic-enforcement model in an enterprise environment.

## What I Implemented

- Log Analytics Workspace for centralized log collection
- Linux virtual machine and network interface
- Public IP configuration
- Subnet and Network Security Group configuration
- NSG rules controlling SSH access
- Diagnostic settings for analytics and rule collection
- Terraform data source referencing an existing NSG
- Logic App template for alerting workflows
- Supporting architecture, security requirements, risk, and design documentation

## Architecture Focus

The project focuses on the path from Azure infrastructure through diagnostic configuration and centralized telemetry collection.

At a high level:

**Azure Resources → Diagnostic Settings → Log Analytics → Monitoring / Alerting**

The Terraform configuration provides a repeatable way to deploy the supporting infrastructure and diagnostic configuration.

The project also led to a broader architectural question: how should an enterprise ensure that required diagnostic settings remain consistently applied as resources are added or changed?

That question is explored separately in the technical architecture case study.

## Security Considerations

The project considers:

- Consistent diagnostic configuration
- Centralized security and operational telemetry
- Network access controls
- Infrastructure-as-Code repeatability
- Monitoring and alerting
- Configuration visibility
- Security requirements and risk documentation

A production implementation would require additional consideration of policy-based enforcement, least-privilege administration, exception management, telemetry validation, cost, and ongoing compliance monitoring.

## Technical Architecture Case Study

The accompanying technical case study expands the project beyond the lab implementation and examines how I would approach diagnostic enforcement in an enterprise Azure environment.

It covers:

- Continuous compliance evaluation
- Configuration drift
- Automated remediation
- Failed-remediation handling
- Identity and trust
- Exceptions and change management
- Audit evidence
- Production rollout considerations

**[Azure Diagnostic Enforcement – Technical Architecture Case Study](./Azure_Diagnostic_Enforcement_Technical_Case_Study.md)**

The case study distinguishes between controls implemented in this project and additional controls I would evaluate for a production environment.

## Repository Contents

- `main.tf` – Core infrastructure
- `vm.tf` – Virtual machine and NIC configuration
- `logicapp.tf` – Logic App template deployment for alerting workflows
- `project_summary.md` – Business problem and solution context
- `design_overview.md` – Architecture and design considerations
- `security_requirements.md` – Security expectations and controls
- `risks_and_mitigations.md` – Identified risks and recommended mitigations
- `lessonslearned.md` – Observations and next steps
- `teardown.md` – Cleanup guide
- `architecture.png` – Visual overview of the environment

## Architecture Artifacts

- [Design Overview](./design_overview.md)
- [Security Requirements](./security_requirements.md)
- [Risks & Mitigations](./risks_and_mitigations.md)
