# Luo *.env* -tiedosto juurikansioon

Tässä ohjeessa opastamme sinua määrittämään ympäristömuuttujasi Azure-palveluille käyttäen *.env* -tiedostoa. Ympäristömuuttujat antavat sinun hallita turvallisesti arkaluontoisia tunnistetietoja, kuten API-avaimia, ilman että ne kovakoodataan koodipohjaasi.

> [!IMPORTANT]
> - Vain yksi kielimallipalvelu (Azure OpenAI tai OpenAI) tarvitsee olla määritettynä. Täytä ympäristömuuttujat haluamallesi palvelulle. Jos ympäristömuuttujat useammalle kielimallille on asetettu, co-op translator valitsee niistä yhden prioriteetin perusteella.
> - Jos Computer Visionin ympäristömuuttujia ei ole asetettu, kääntäjä vaihtaa automaattisesti [vain Markdown -tilaan](./markdown-only-mode.md).

> [!NOTE]
> Tämä ohje keskittyy pääasiassa Azure-palveluihin, mutta voit valita minkä tahansa tuetun kielimallin [tuettujen mallien ja palveluiden listalta](../README.md#-supported-models-and-services).

## Luo *.env* -tiedosto

Projektisi juurikansioon luo tiedosto nimeltä *.env*. Tämä tiedosto tallentaa kaikki ympäristömuuttujasi yksinkertaisessa muodossa.

> [!WARNING]
> Älä tallenna *.env* -tiedostoa versiohallintajärjestelmiin kuten Git. Lisää *.env* .gitignore -tiedostoosi estääksesi vahingossa tehdyt commitit.

1. Siirry projektisi juurikansioon.

1. Luo *.env* -tiedosto projektisi juurikansioon.

1. Avaa *.env* -tiedosto ja liitä seuraava mallipohja:

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
> Jos haluat löytää API-avaimesi ja päätepisteesi, voit katsoa [set-up-azure-ai.md](../set-up-azure-ai.md).

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Vastuuvapauslauseke**:
Tämä asiakirja on käännetty käyttämällä tekoälypohjaista käännöspalvelua [Co-op Translator](https://github.com/Azure/co-op-translator). Vaikka pyrimme tarkkuuteen, ota huomioon, että automaattikäännöksissä saattaa esiintyä virheitä tai epätarkkuuksia. Alkuperäistä asiakirjaa sen alkuperäiskielellä tulisi pitää virallisena lähteenä. Tärkeiden tietojen osalta suositellaan ammattilaisten tekemää ihmiskäännöstä. Emme ole vastuussa mistään väärinymmärryksistä tai virhetulkintojen seurauksista, jotka johtuvat tämän käännöksen käytöstä.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->