---
title: Tworzenie definicji usługi za pomocą kodu Terraform
description: Dowiedz się, jak wdrożyć definicję usługi platformy Azure Container Apps ze źródła kodu za pomocą szablonów Terraform.
ms.topic: tutorial
ms.date: 08/02/2023
---

# Tworzenie definicji usługi za pomocą kodu Terraform

W tym artykule dowiesz się, jak wdrożyć definicję usługi platformy Azure Container Apps przy użyciu kodu Terraform.

[!INCLUDE [prerequisites-note](../../includes/prerequisites-aca.md)]

## Zarządzanie zasobem definicji usługi

W tej sekcji omówimy konfigurację i parametry, które musisz określić w module definicji usługi zaznaczonym w poniższym przykładowym pliku Terraform.

```hcl:title=main.tf
resource "azurerm_container_app_revision" "example" {
  name                   = "example"
  container_app_name     = azurerm_container_app.example.name
  resource_group_name    = azurerm_resource_group.example.name
  revision_mode          = "Single"
  image                  = "mcr.microsoft.com/apps/sample:latest"
  cpu                    = 0.25
  memory_in_gb           = 0.5
}
```

W powyższym przykładzie:

- `name` — nazwa definicji usługi.
- `container_app_name` — odniesienie do nazwy kontenera aplikacji.
- `resource_group_name` — grupa zasobów zawierająca kontener aplikacji.
- `revision_mode` — tryb rewizji (np. Single lub Multiple).
- `image` — obraz kontenera do wdrożenia.
- `cpu` — przydzielone CPU dla kontenera.
- `memory_in_gb` — przydzielona pamięć RAM w GB.

## Przykładowy kod Terraform

Poniżej znajduje się kompletny przykład pliku Terraform, pokazujący definicję aplikacji kontenerowej wraz z jej rewizją.

```hcl
# Definicja grupy zasobów
resource "azurerm_resource_group" "example" {
  name     = "example-rg"
  location = "East US"
}

# Kontener aplikacji
resource "azurerm_container_app" "example" {
  name                = "example-container-app"
  resource_group_name = azurerm_resource_group.example.name
  location            = azurerm_resource_group.example.location
  environment_id      = azurerm_container_app_environment.example.id
}

# Rewizja kontenera aplikacji
resource "azurerm_container_app_revision" "example" {
  name                   = "example-revision"
  container_app_name     = azurerm_container_app.example.name
  resource_group_name    = azurerm_resource_group.example.name
  revision_mode          = "Single"
  image                  = "mcr.microsoft.com/apps/sample:latest"
  cpu                    = 0.5
  memory_in_gb           = 1.0
}
```

Powyższy kod pokazuje, jak definiować poszczególne zasoby potrzebne do wdrożenia platformy Azure Container Apps oraz jej rewizji.

## Dalsze kroki

Po wdrożeniu definicji usługi za pomocą Terraform, możesz użyć [przewodnika Azure Container Apps](https://learn.microsoft.com/azure/container-apps/) aby:

- Skonfigurować ruch i skalowanie
- Monitorować działanie aplikacji
- Aktualizować definicje usługi

Zapoznaj się także z [oficjalną dokumentacją Terraform dla Azure Container Apps](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/container_app) dla szczegółowych informacji o dostępnych właściwościach zasobów i opcjach konfiguracyjnych.

[!TIP]
Aby uprościć zarządzanie wersjami i środowiskami, warto rozważyć użycie modułów Terraform oraz zarządzanie stanem za pomocą zdalnego backendu (np. Azure Storage).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Zastrzeżenie**:  
Niniejszy dokument został przetłumaczony przy użyciu usługi tłumaczeń AI [Co-op Translator](https://github.com/Azure/co-op-translator). Chociaż dążymy do dokładności, prosimy pamiętać, że automatyczne tłumaczenia mogą zawierać błędy lub niedokładności. Oryginalny dokument w języku źródłowym powinien być uznawany za autorytatywne źródło. W przypadku istotnych informacji zaleca się skorzystanie z profesjonalnego tłumaczenia wykonanego przez człowieka. Nie ponosimy odpowiedzialności za wszelkie nieporozumienia lub błędne interpretacje wynikające z korzystania z tego tłumaczenia.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->