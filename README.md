# Azure Log Automation Terraform Lab

This project provisions a secure log monitoring environment in Microsoft Azure using Terraform. Key infrastructure components include a Log Analytics Workspace, NSG rules, subnet associations, public IP allocation, and a Linux VM for centralized diagnostics and data collection.

## ✅ Successfully Implemented
- Log Analytics Workspace
- Public IP address for VM
- Subnet and NSG creation
- NSG rules for SSH access
- Diagnostic settings for analytics and rule collection
- Data source configuration for existing NSG

## 🚀 Business Value
This lab demonstrates automation of Azure security and monitoring infrastructure, ensuring consistent, auditable deployments suitable for production environments. This aligns with enterprise IaC strategies and helps streamline DevSecOps pipelines.

## 📁 Files Included
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
