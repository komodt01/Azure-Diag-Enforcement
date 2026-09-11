# Azure Diagnostic Enforcement: Technical Architecture Case Study

## Executive Summary

This case study examines how I would address inconsistent diagnostic logging across an Azure environment. The security problem is not simply whether a centralized logging platform exists. The problem is whether the organization can rely on in-scope Azure resources to produce required telemetry and send it to the approved destination consistently over time.

For this scenario, I use policy-based diagnostic enforcement rather than relying on resource owners to configure logging manually. The control model evaluates resources for required diagnostic settings, identifies noncompliance, supports remediation, and continues evaluating resources after deployment so configuration drift can be detected.

The architecture improves the consistency and availability of telemetry used for security monitoring, investigation, incident response, and audit. It does not guarantee that security incidents will be detected; detection logic and SOC processes are separate layers.

## Business Problem

As Azure adoption grows, diagnostic settings can become inconsistent across subscriptions, resource types, and application teams. A resource may be deployed without required logging, or a previously compliant configuration may later be changed or removed.

That creates a security visibility problem. During an incident, the organization may discover that the telemetry needed to understand what happened was never collected. Manual configuration also becomes increasingly unreliable as the number of resources grows.

The architectural question for this case study is:

**How can an organization ensure that in-scope Azure resources continue to meet its diagnostic logging requirements without depending on individual administrators to configure and maintain those settings manually?**

## Assumptions

- The organization has already selected an approved centralized logging destination. This case study focuses on enforcing telemetry collection rather than designing the enterprise SIEM/logging platform itself.
- The organization has defined which Azure resources are in scope for diagnostic enforcement.
- Security and operational teams have established minimum telemetry requirements appropriate to the resource types being governed.
- Existing Azure identity and access management capabilities are available for administrative separation and least-privilege access.

## Scope and Boundaries

### In Scope

- Azure resources subject to organizational diagnostic logging requirements.
- Defining and evaluating required diagnostic settings.
- Detecting missing or changed diagnostic configurations.
- Policy-based enforcement and remediation of noncompliant resources.
- Delivery of required telemetry to the approved centralized destination.
- Continuous compliance evaluation after deployment.
- Access control for policy administration, diagnostic configuration, and exemptions.
- Failed-remediation handling, exceptions, and audit evidence.

### Out of Scope

- Design of the enterprise Log Analytics or SIEM platform.
- Detailed SIEM detection-rule engineering and threat hunting.
- Application-level logging design.
- Cross-cloud logging architecture.
- High-availability or redundancy design for the logging platform.
- Full incident-response workflow after a security event is detected.
- Detailed enterprise log-retention architecture.

## Security and Operational Requirements

The control needs to provide more than an initial configuration check. For this scenario, I would require that:

- In-scope Azure resources have the required diagnostic logging configuration.
- Required telemetry is directed to the approved centralized logging destination.
- Resources missing required settings can be identified.
- Changes that remove or weaken required diagnostic settings can be detected.
- Existing resources as well as newly deployed resources are evaluated.
- Noncompliant resources have a defined remediation or escalation path.
- Failed remediation is visible rather than silently leaving a resource unmonitored.
- Access to policy, diagnostic settings, remediation permissions, and exemptions follows least privilege.
- Compliance status, exceptions, and privileged changes can be demonstrated for governance and audit purposes.

## Architecture and Control Flow

I would treat diagnostic enforcement as a continuous control rather than a deployment checklist.

The control flow is:

**Resource deployed or already exists -> Policy evaluation -> Compliance decision -> Remediation if required -> Re-evaluation -> Telemetry sent to approved destination -> Ongoing compliance evaluation**

### 1. Resource Evaluation

An in-scope Azure resource is evaluated against the organization's diagnostic requirement. The question is not merely whether diagnostics are enabled, but whether the required configuration exists for that resource and points to the approved destination.

### 2. Compliance Decision

A resource that meets the required configuration is considered compliant.

A resource with missing or incorrect required diagnostic settings is considered noncompliant and enters the remediation path.

### 3. Enforcement and Remediation

For predictable configurations, I would favor automated remediation rather than relying only on an alert that asks an administrator to correct the resource manually.

The progression is:

**Detect -> Evaluate -> Remediate -> Re-evaluate**

If remediation succeeds, the resource returns to compliance. If remediation fails, the failure becomes an operational event requiring investigation.

### 4. Telemetry Delivery

Once the required configuration is present, the resource sends the required telemetry to the organization's approved centralized logging destination.

This case study stops at successful telemetry delivery. Detection engineering, correlation, threat hunting, and SOC response occur downstream and are intentionally outside the scope of this architecture.

### 5. Continuous Evaluation and Drift

The control must continue operating after deployment. If a required diagnostic setting is later changed or removed, the resource can move from compliant to noncompliant and enter the remediation process again.

This is why I would use policy-based enforcement rather than relying on deployment documentation or individual resource owners to maintain the setting manually.

## Identity and Trust

I would separate workload administration from security-control administration and security-monitoring access.

**Security Architecture / Governance** defines the logging requirement and control intent.

**Cloud / Platform Administration** implements and maintains the enforcement mechanism and supporting platform configuration.

**Resource / Application Owners** administer their workloads but should not automatically receive authority to weaken organization-wide diagnostic requirements or alter the approved centralized destination.

**Security Operations** primarily consumes the resulting telemetry and compliance information. Broad workload-administration privileges are not required simply to investigate security events.

Where automated remediation uses a managed identity, I would grant only the permissions required to create or correct the necessary diagnostic configuration. Broad subscription-level administrative rights would not be justified merely for convenience.

Changes to policy assignments, exemptions, diagnostic requirements, approved destinations, or remediation permissions should themselves be auditable.

The trust separation is:

**Workload administration != Security control administration != Security monitoring access**

## Noncompliance and Failure Handling

### Missing Diagnostic Settings

If required settings are missing, the resource is marked noncompliant and remediation is attempted where appropriate.

### Configuration Drift

If someone later changes or removes required diagnostic settings, continuous evaluation should identify the resource as noncompliant and return it to the remediation path.

### Failed Remediation

Remediation can fail because of permissions, unsupported configurations, policy errors, or other dependencies.

I would use the following progression:

**Noncompliant -> Remediation attempted -> Remediation failed -> Alert/escalation -> Platform or resource owner investigates -> Manual remediation or approved exception -> Compliance verified**

The architecture should not retry indefinitely without surfacing the failure.

### Telemetry Is Not Arriving

A resource can have the expected diagnostic configuration and still fail to produce or deliver expected telemetry.

This creates an important distinction:

**Configuration compliance does not necessarily prove successful telemetry delivery.**

In a production environment, I would evaluate a separate mechanism for detecting unexpected telemetry gaps. I would not treat a compliant policy result as proof that the monitoring pipeline is functioning end to end.

### Intentional Logging Change

If an administrator intentionally changes or disables required logging, policy evaluation should identify the resulting drift. The administrative change should also be attributable through Azure activity and audit records.

## Exceptions and Change Management

A legitimate exception should not result in weakening the control for unrelated resources.

For this scenario, an exception should be:

- Narrowly scoped.
- Assigned an owner.
- Supported by a business or technical justification.
- Accompanied by a compensating control where appropriate.
- Given an expiration or review date.
- Auditable.

Changes to the enforcement architecture can have a larger blast radius than changes to an individual workload. I would therefore treat changes to policy definitions or assignments, required diagnostic categories, approved destinations, remediation permissions, and exemptions as controlled changes.

A production change progression would be:

**Propose -> Assess impact -> Test in limited scope -> Approve -> Deploy -> Validate -> Monitor -> Roll back if necessary**

I would avoid treating patch management as part of this case study because it is not central to the diagnostic-enforcement problem.

## Monitoring, Evidence, and Auditability

I would look for evidence at three levels.

### Policy Compliance

The organization should be able to determine which evaluated resources are compliant, noncompliant, or exempt. This provides measurable evidence of control coverage rather than relying on a statement that resources are expected to have logging enabled.

### Remediation Evidence

For noncompliant resources, the organization should be able to determine whether remediation was initiated and whether it succeeded or failed.

The evidence chain is:

**Noncompliant -> Remediation initiated -> Succeeded or failed -> Re-evaluated**

### Telemetry Evidence

Policy compliance demonstrates that the expected configuration exists. It does not by itself demonstrate that useful telemetry continues to arrive.

In production, I would also want a way to identify unexpected telemetry absence so that a resource cannot appear healthy solely because its diagnostic configuration is technically correct.

For governance and audit purposes, the organization should be able to trace:

**Security requirement -> Policy assignment and scope -> Resource compliance -> Remediation history -> Approved exceptions -> Privileged changes**

## Business Risk and Impact

Inconsistent diagnostic logging creates an unknown security blind spot.

The primary risks include:

- **Incident response risk:** Security may not have the evidence required to reconstruct an event.
- **Compliance and audit risk:** The organization may be unable to demonstrate consistent application of required logging controls.
- **Operational risk:** Manual configuration depends on administrators remembering to configure each resource correctly.
- **Investigation cost:** Missing or inconsistent telemetry can increase the time required to investigate security and operational events.
- **Scale risk:** A manual process that appears workable for a small environment becomes increasingly unreliable as the Azure footprint grows.

The business value of the architecture is therefore not simply that diagnostics are enabled. It is that the organization has a repeatable, measurable control designed to reduce security visibility gaps as the environment grows.

## Production Considerations

The project demonstrates the control concept, but a production implementation would require additional decisions.

### Policy Scope

I would evaluate whether enforcement belongs at a management group, subscription, resource group, or more limited scope. The objective is sufficient coverage without creating unnecessary blast radius.

### Resource-Specific Requirements

Not every Azure resource exposes the same diagnostic categories. I would not assume that one universal configuration is appropriate for every resource type.

### Staged Rollout

I would validate policy changes against a limited non-production scope before expanding them broadly, especially when automatic remediation is involved.

### Telemetry Validation

I would evaluate monitoring for unexpected telemetry gaps so configuration compliance is not mistaken for end-to-end monitoring health.

### Least Privilege

Remediation identities should receive only the permissions required to perform their function. Changes to policies, exemptions, logging destinations, and remediation permissions should be auditable.

### Exception Lifecycle

Exceptions should remain scoped, owned, documented, and periodically reviewed rather than becoming permanent undocumented exclusions.

### Cost

Broad diagnostic enforcement can increase ingestion and retention volume. I would define required telemetry according to security, operational, and regulatory value rather than automatically enabling every available diagnostic category.

### Operational Ownership

The organization needs an owner for ongoing compliance review, failed remediation, exceptions, and policy changes. Enforcement should not be treated as a one-time deployment.

## Architecture Decisions and Tradeoffs

### Policy-Based Enforcement vs. Manual Configuration

I chose policy-based enforcement because the control needs to remain effective after deployment and identify configuration drift over time. Manual instructions may help teams deploy resources correctly, but they do not provide the same continuing assurance.

### Automatic Remediation vs. Alert Only

For configurations that are well understood and safe to apply consistently, automatic remediation reduces the period during which a resource remains outside the logging standard.

The tradeoff is blast radius. An incorrect remediation policy can affect many resources, which is why testing, scope control, and rollback planning matter.

### Required Telemetry vs. Collect Everything

I would not equate maximum log volume with maximum security. More telemetry increases cost and can add noise. The logging standard should identify telemetry that has a defined security, operational, audit, or regulatory purpose.

### Configuration Compliance vs. Operational Assurance

Policy compliance answers whether the expected configuration exists.

It does not fully answer whether telemetry is arriving and usable.

I would therefore treat policy compliance and telemetry-health monitoring as complementary controls rather than interchangeable evidence.

## What the Project Demonstrates

This project demonstrates my approach to treating diagnostic logging as a governed security control rather than a one-time configuration task.

The implemented Azure work provides the technical foundation for diagnostic enforcement and centralized telemetry. The case study extends that work into the architectural questions I would need to address in an enterprise environment: control scope, ownership, least privilege, configuration drift, remediation failure, exceptions, audit evidence, cost, and production rollout.

Where this case study discusses broader production controls that were not part of the lab implementation, I present them as production considerations rather than claiming they were implemented.

The architecture is intentionally focused on **telemetry assurance**. It improves the consistency and availability of the information that monitoring, investigation, and incident response depend on, but it does not claim to guarantee detection of security incidents.
