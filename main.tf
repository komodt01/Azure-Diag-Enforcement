
provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "diagnostics" {
  name     = "diag-enforce-rg"
  location = "East US"
}
