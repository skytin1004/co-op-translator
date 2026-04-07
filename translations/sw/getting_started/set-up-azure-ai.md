# Weka Azure AI kwa Co-op Translator (Azure OpneAI & Azure AI Vision)

Mwongozo huu utakuelekeza jinsi ya kuweka Azure OpenAI kwa tafsiri ya lugha na Azure Computer Vision kwa uchambuzi wa maudhui ya picha (ambayo inaweza kutumika kwa tafsiri za picha) ndani ya Azure AI Foundry.

**Mahitaji ya awali:**
- Akaunti ya Azure yenye usajili hai.
- Ruhusa za kutosha za kuunda rasilimali na upangaji ndani ya usajili wako wa Azure.

## Unda Mradi wa Azure AI

Utaanza kwa kuunda Mradi wa Azure AI, ambao hutumika kama mahali pa kuuza kudhibiti rasilimali zako za AI.

1. Tembelea [https://ai.azure.com](https://ai.azure.com) na jinasisha kwa akaunti yako ya Azure.

1. Chagua **+Create** kuunda mradi mpya.

1. Fanya shughuli zifuatazo:
   - Weka **Jina la Mradi** (mfano, `CoopTranslator-Project`).
   - Chagua **AI hub**  (mfano, `CoopTranslator-Hub`) (Unda mpya ikiwa inahitajika).

1. Bonyeza "**Review and Create**" kuanzisha mradi wako. Utaongozwa kwenye ukurasa wa muhtasari wa mradi wako.

## Weka Azure OpenAI kwa Tafsiri ya Lugha

Ndani ya mradi wako, utaweka mfano wa Azure OpenAI kama sehemu ya nyuma kwa tafsiri ya maandishi.

### Nenda kwa Mradi Wako

Kama bado hauko hapo, fungua mradi ulioanzisha mpya (mfano, `CoopTranslator-Project`) katika Azure AI Foundry.

### Weka Mfano wa OpenAI

1. Kutoka kwenye menyu ya kushoto ya mradi wako, chini ya "My assets", chagua "**Models + endpoints**".

1. Chagua **+ Deploy model**.

1. Chagua **Deploy Base Model**.

1. Utaonyeshwa orodha ya mifano iliyopo. Chuja au tafuta mfano wa GPT unaofaa. Tunapendekeza `gpt-4o`.

1. Chagua mfano unaotaka na bonyeza **Confirm**.

1. Chagua **Deploy**.

### Usanidi wa Azure OpenAI

Mara baada ya kuwekwa, unaweza kuchagua upangaji kutoka ukurasa wa "**Models + endpoints**" ili kupata **REST endpoint URL**, **Key**, **Deployment name**, **Model name** na **API version**. Hizi zitahitajika kuunganisha mfano wa tafsiri ndani ya programu yako.

> [!NOTE]
> Unaweza kuchagua matoleo ya API kutoka kwenye ukurasa wa [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) kulingana na mahitaji yako. Fahamu kuwa **API version** ni tofauti na **Model version** inayoonekana kwenye ukurasa wa **Models + endpoints** katika Azure AI Foundry.

## Weka Azure Computer Vision kwa Tafsiri ya Picha

Ili kuwezesha tafsiri ya maandishi yaliyomo kwenye picha, unahitaji kupata API Key na Endpoint ya Azure AI Service.

1. Nenda kwenye Mradi wako wa Azure AI (mfano, `CoopTranslator-Project`). Hakikisha uko kwenye ukurasa wa muhtasari wa mradi.

### Usanidi wa Azure AI Service

Pata API Key na Endpoint kutoka tabo ya Azure AI Service.

1. Nenda katika Mradi wako wa Azure AI (mfano, `CoopTranslator-Project`). Hakikisha uko kwenye ukurasa wa muhtasari wa mradi.

1. Pata **API Key** na **Endpoint** kutoka tabo ya Azure AI Service.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

Muunganisho huu unafanya huduma za rasilimali husika za Azure AI Services (pamoja na uchambuzi wa picha) zipatikane kwa mradi wako wa AI Foundry. Baadaye unaweza kutumia muunganisho huu katika daftari zako au programu za kutoa maandishi kutoka kwa picha, ambayo yanaweza kutumwa kwa mfano wa Azure OpenAI kwa tafsiri.

## Kuhakiki Nyaraka Zako

Kwa sasa, unapaswa kuwa umekusanya yafuatayo:

**Kwa Azure OpenAI (Tafsiri ya Maandishi):**
- Azure OpenAI Endpoint
- Azure OpenAI API Key
- Jina la Mfano wa Azure OpenAI (mfano, `gpt-4o`)
- Jina la Upangaji wa Azure OpenAI (mfano, `cooptranslator-gpt4o`)
- Toleo la Azure OpenAI API

**Kwa Azure AI Services (Kutoa Maandishi ya Picha kupitia Vision):**
- Azure AI Service Endpoint
- Azure AI Service API Key

### Mfano: Usanidi wa Kigezo cha Mazingira (Mapitio)

Baadaye, unapoanza kujenga programu yako, huenda ulaisanidi kwa kutumia nyaraka hizi ulizokusanya. Kwa mfano, unaweza kuweka kama vigezo vya mazingira kama vifuatavyo:

```bash
# Vyeti vya Huduma ya Azure AI (Vinahitajika kwa tafsiri ya picha)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # kwa mfano, 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# Msets fallback ya hiari: rudia vigezo na kiambatisho _1/_2 (nambari hiyo hiyo kwa vigezo vyote katika seti)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Vyeti vya Azure OpenAI (Vinahitajika kwa tafsiri ya maandishi)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # kwa mfano, 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # kwa mfano, gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # kwa mfano, cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # kwa mfano, 2024-12-01-preview

# Msets fallback ya hiari: rudia seti kamili ya AZURE_OPENAI_* na kiambatisho _1/_2 (nambari hiyo hiyo kwa vigezo vyote)
```

---

### Kusoma Zaidi

- [Jinsi ya Kuunda mradi katika Azure AI Foundry](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Jinsi ya Kuunda rasilimali za Azure AI](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Jinsi ya Kuweka mifano ya OpenAI katika Azure AI Foundry](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Kiasi cha majibu**:  
Hati hii imefasiriwa kwa kutumia huduma ya tafsiri ya AI [Co-op Translator](https://github.com/Azure/co-op-translator). Wakati tunajitahidi kwa usahihi, tafadhali fahamu kwamba tafsiri za kiotomatiki zinaweza kuwa na makosa au ukosefu wa usahihi. Hati asili katika lugha yake ya asili inapaswa kuzingatiwa kama chanzo cha mamlaka. Kwa habari muhimu, tafsiri ya kitaalamu ya mtu inashauriwa. Hatuna wajibu kwa uelewa au tafsiri potofu zinazotokana na matumizi ya tafsiri hii.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->