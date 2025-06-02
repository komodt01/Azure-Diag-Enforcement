
# Teardown Instructions

1. Delete Logic App:
   ```bash
   az logic workflow delete --name alert-on-noncompliant-resource --resource-group diag-enforce-rg
   ```

2. Delete Policy Assignment:
   ```bash
   az policy assignment delete --name diag-enforce-policy
   ```

3. Delete Resource Group:
   ```bash
   az group delete --name diag-enforce-rg --yes
   ```
