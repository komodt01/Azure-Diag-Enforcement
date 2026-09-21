# Teardown

## Terraform-Deployed Resources

The Terraform configuration in this repository creates the project resource group.

To remove resources managed by the current Terraform configuration, run:

```bash
terraform destroy
```

Review the Terraform plan before confirming the destroy operation.

## Manually Deployed Resources

The repository also contains Azure Policy and Logic App artifacts that can be used independently of the Terraform configuration.

If these artifacts were manually deployed during testing, remove those resources using the same Azure management method used to create them.

Examples may include:

- Azure Policy definitions or assignments created during testing
- Logic App workflows created from the provided template
- Other diagnostic or monitoring configuration created outside Terraform

Verify that a resource is associated with this lab before deleting it.

## Cleanup Validation

After teardown, confirm that:

- Terraform-managed resources have been removed
- Manually created test resources have been removed where appropriate
- No test policy assignments remain active
- No unnecessary project resources continue generating Azure costs

Production or shared security controls should never be removed as part of lab cleanup without confirming ownership, scope, and change approval.
