# Security Control Alignment

This project demonstrates technical concepts that can support broader security and compliance requirements. The mappings below represent areas of alignment and should not be interpreted as demonstrating compliance with an entire framework or control.

## NIST SP 800-53

### AU – Audit and Accountability

Diagnostic logging and centralized telemetry can support organizational requirements for generating, reviewing, and analyzing audit information.

The project specifically explores how required diagnostic configuration can be evaluated consistently rather than relying entirely on manual configuration.

## ISO/IEC 27001

### Logging and Monitoring

Consistent diagnostic configuration can support organizational logging and monitoring controls by improving the availability of security and operational telemetry.

Implementation of diagnostic settings alone does not satisfy the broader governance, monitoring, review, retention, and response requirements associated with an information security management system.

## CIS Microsoft Azure Foundations Benchmark

Azure diagnostic and monitoring recommendations generally emphasize maintaining appropriate logging and visibility across cloud resources.

This project demonstrates the control concept of evaluating whether expected diagnostic configuration exists.

Specific CIS benchmark mappings should be validated against the benchmark version adopted by the organization because recommendations and control numbering can change between releases.

## Architecture Perspective

Framework requirements define the security objective, while cloud-native services provide mechanisms for implementing portions of that objective.

For diagnostic governance, the broader control should consider:

**Security requirement → Technical policy → Compliance evaluation → Remediation or exception → Evidence → Ongoing monitoring**

The Azure artifacts in this repository demonstrate only part of that control lifecycle. Production compliance would depend on organizational scope, implementation, operating procedures, evidence, and ongoing control effectiveness.
