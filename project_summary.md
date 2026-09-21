# Project Summary – Azure Diagnostic Enforcement

## Business Problem

Security monitoring depends on Azure resources producing the telemetry required for investigation, incident response, and audit.

As cloud environments grow, manually maintained diagnostic settings can become inconsistent or be removed over time, creating security visibility gaps.

## Project Objective

This project explores how diagnostic configuration can be evaluated through policy and programmatic inspection rather than relying entirely on manual review.

The proof-of-concept focuses on the foundation of a broader diagnostic-governance control.

## Implemented Components

The repository includes:

- A custom Azure Policy using `auditIfNotExists` to identify resource groups without the expected diagnostic logging configuration
- A Python script using the Azure Monitor SDK to enumerate diagnostic settings for a specified Azure resource
- A Logic App resource template representing a starting point for a future noncompliance workflow
- Terraform configuration for the Azure resource group supporting the project

The current implementation provides configuration evaluation and inspection. It does not implement automatic remediation or a completed Logic App alerting workflow.

## Security Architecture Value

The project demonstrates an important distinction between configuring logging and governing logging as a security control.

An enterprise implementation would need to address:

- Continuous compliance evaluation
- Configuration drift
- Least-privilege remediation
- Failed-remediation handling
- Exception governance
- Audit evidence
- Telemetry-health validation
- Operational ownership

The broader architecture is documented in the accompanying technical case study.

## Outcome

The project demonstrates a proof-of-concept for evaluating Azure diagnostic configuration and establishes the architectural foundation for a more comprehensive diagnostic-enforcement capability.

The primary security objective is **telemetry assurance**: reducing the risk that resources operate without the logging required for security monitoring and investigation.
