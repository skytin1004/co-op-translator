# Luo *.env*-tiedosto juurihakemistoon

Tässä opetusohjelmassa ohjaamme sinua ympäristömuuttujien määrittämisessä Azure-palveluille käyttäen *.env*-tiedostoa. Ympäristömuuttujat mahdollistavat arkaluontoisten tunnistetietojen, kuten API-avaimien, turvallisen hallinnan ilman, että ne kovakoodataan koodipohjaasi.

> [!IMPORTANT]
> - Tarvitaan vain yhden kielimallipalvelun (Azure OpenAI tai OpenAI) konfigurointi. Täytä ympäristömuuttujat haluamallesi palvelulle. Jos useamman kielimallin ympäristömuuttujat on asetettu, co-op translator valitsee yhden prioriteetin perusteella.
> - Jos Computer Vision -ympäristömuuttujia ei ole asetettu, kääntäjä vaihtaa automaattisesti [vain Markdown -tilaan](./markdown-only-mode.md).

> [!NOTE]
> Tämä ohje keskittyy pääasiassa Azure-palveluihin, mutta voit valita minkä tahansa tuetun kielimallin [tuettujen mallien ja palveluiden listasta](../README.md#-supported-models-and-services).

## Luo *.env*-tiedosto

Projektisi juurihakemistoon luo tiedosto nimeltä *.env*. Tämä tiedosto tallentaa kaikki ympäristömuuttujasi yksinkertaisessa muodossa.

> [!WARNING]
> Älä kommitoi *.env*-tiedostoa versionhallintajärjestelmiin kuten Gitiin. Lisää *.env* .gitignore-tiedostoosi estääksesi vahingossa tapahtuvat commitit.

1. Siirry projektisi juurihakemistoon.

1. Luo *.env*-tiedosto projektisi juurihakemistoon.

1. Avaa *.env*-tiedosto ja liitä seuraava pohja:

    ```plaintext
    # Azure Credentials
    AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key"
    AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint"

    # Optional fallback set example (index 1)
    AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
    AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1"

    # Azure OpenAI Credentials
    AZURE_OPENAI_API_KEY="your_azure_openai_api_key"
    AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint"
    AZURE_OPENAI_MODEL_NAME="your_model_name"
    AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name"
    AZURE_OPENAI_API_VERSION="your_api_version"

    # Optional fallback sets: duplicate the full AZURE_OPENAI_* set with suffix _1/_2 (same index for all variables)

    # OpenAI Credentials
    OPENAI_API_KEY="your_openai_api_key"
    OPENAI_ORG_ID="your_openai_org_id"
    OPENAI_CHAT_MODEL_ID="your_chat_model_id(ex. gpt-4o)"
    OPENAI_BASE_URL="https://api.openai.com/v1 (If you don't have a custom base URL, you can delete this lin, then it will use the default base URL)"

    # Optional fallback sets: duplicate the full OPENAI_* set with suffix _1/_2 (same index for all variables)
    ```

> [!NOTE]
> Jos haluat löytää API-avaimesi ja päätepisteesi, voit katsoa ohjetta [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:  
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, otathan huomioon, että automaattiset käännökset voivat sisältää virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää ensisijaisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattimaista ihmiskäännöstä. Emme ole vastuussa tämän käännöksen käytöstä johtuvista väärinymmärryksistä tai tulkinnoista.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->