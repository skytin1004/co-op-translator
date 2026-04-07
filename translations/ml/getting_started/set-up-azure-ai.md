# Co-op Translator ന് Azure AI സജ്ജമാക്കുക (Azure OpneAI & Azure AI Vision)

ഭാഷ പരിഭാഷക്കായി Azure OpenAI സ്ഥാപിക്കുന്നതിനും ചിത്രകണ്ടന്റ് വിശകലനത്തിനായി Azure Computer Vision (പിന്നീട് ചിത്രാധിഷ്ഠിത പരിഭാഷക്ക് ഉപയോഗിക്കാവുന്നതാണ്) Azure AI Foundryയിലുള്ളത് സജ്ജമാക്കുന്നതിനുള്ള മാർഗ്ഗനിർദ്ദേശം.

**അടിസ്ഥാന സാഹചര്യം:**
- സജീവമായ സബ്സ്ക്രിപ്ഷൻ ഉള്ള ഒരു Azure അക്കൗണ്ട്.
- നിങ്ങളുടെ Azure സബ്സ്ക്രിപ്ഷനിൽ റിസോഴ്‌സുകളും ഡിപ്പ്ലോയ്‌മെന്റുകളും സൃഷ്‌ടിക്കാൻ മതിയായ അനുമതികൾ.

## Azure AI പ്രോജക്റ്റ് സൃഷ്‌ടിക്കുക

നിങ്ങൾ AI റിസോഴ്‌സുകൾ നിയന്ത്രിക്കുന്ന കേന്ദ്രസ്ഥലമായി പ്രവർത്തിക്കുന്ന Azure AI പ്രോജക്റ്റ് സൃഷ്‌ടിക്കുന്നത് ആരംഭിക്കും.

1. [https://ai.azure.com](https://ai.azure.com) സന്ദർശിച്ച് നിങ്ങളുടെ Azure അക്കൗണ്ടിൽ സൈൻ ഇൻ ചെയ്യുക.

1. പുതിയ പ്രോജക്റ്റ് സൃഷ്‌ടിക്കാൻ **+Create** തിരഞ്ഞെടുക്കുക.

1. ചുവടെയുള്ള പ്രവർത്തനങ്ങൾ ചെയ്യുക:
   - **Project name** നൽകുക (ഉദാ., `CoopTranslator-Project`).
   - **AI hub** തിരഞ്ഞെടുക്കുക (ഉദാ., `CoopTranslator-Hub`) (ആവശ്യമെങ്കിൽ പുതിയതായി സൃഷ്‌ടിക്കുക).

1. പ്രോജക്റ്റ് ക്രമീകരിക്കാൻ "**Review and Create**" ക്ലിക്കുചെയ്യുക. ഇത് നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ അവലോകന പേജിലേക്ക് നിങ്ങളെ കൊണ്ടുപോകും.

## ഭാഷ പരിഭാഷയ്ക്കായി Azure OpenAI സജ്ജമാക്കുക

നിങ്ങളുടെ പ്രോജക്റ്റിനുള്ളിൽ, ടെക്‌സ്‌റ്റ് പരിഭാഷയ്ക്കായുള്ള ബാക്ക്‌എൻഡ് ആയി സേവനം നൽകാൻ Azure OpenAI മോഡൽ ഡിപ്പ്ലോയ് ചെയ്യണം.

### നിങ്ങളുടെ പ്രോജക്റ്റിലേക്ക് നവിഗേറ്റ് ചെയ്യുക

ഇപ്പോൾ വരെ എത്താതെ എങ്കിൽ, നിങ്ങളുടെ പുതിയ സൃഷ്‌ടിച്ച (ഉദാ., `CoopTranslator-Project`) പ്രോജക്റ്റ് Azure AI Foundryയിൽ തുറക്കുക.

### OpenAI മോഡൽ ഡിപ്പ്ലോയ് ചെയ്യുക

1. നിങ്ങളുടെ പ്രോജക്റ്റിന്റെ ഇടതു മെനുവിൽ, "My assets" താഴെ "**Models + endpoints**" തിരഞ്ഞെടുക്കുക.

1. **+ Deploy model** തിരഞ്ഞെടുക്കുക.

1. **Deploy Base Model** തിരഞ്ഞെടുക്കുക.

1. ലഭ്യമായ മോഡലുകളുടെ പട്ടിക നിങ്ങൾക്ക് കാണിക്കപ്പെടും. യോഗ്യമായ GPT മോഡൽ ഫിൽറ്റർ ചെയ്യുകയോ തിരയുകയോ ചെയ്യുക. ഞങ്ങൾ `gpt-4o` ശുപാർശ ചെയ്യുന്നു.

1. നിങ്ങളുടെ ഇഷ്ട മോഡൽ തിരഞ്ഞെടുക്കുകയും **Confirm** ക്ലിക്കുചെയ്യുകയും ചെയ്യുക.

1. **Deploy** തിരഞ്ഞെടുക്കുക.

### Azure OpenAI കോൺഫിഗറേഷൻ

ഡിപ്പ്ലോയ് ചെയ്തശേഷം, "**Models + endpoints**" പേജിൽ നിന്നും ഡിപ്പ്ലോയ്‌മെന്റ് തിരഞ്ഞെടുക്കുന്നതിലൂടെ അതിന്റെ **REST endpoint URL**, **Key**, **Deployment name**, **Model name** എന്നിവ ലഭിക്കും. ഈവെല്ലാം പരിഭാഷ മോഡൽ നിങ്ങളുടെ അപ്ലിക്കേഷൻ ഇന്റഗ്രേറ്റ് ചെയ്യാൻ ആവശ്യമാണ്.

> [!NOTE]
> ആവശ്യാനുസരിച്ച് API പതിപ്പുകൾ തിരഞ്ഞെടുക്കാൻ നിങ്ങൾക്ക് [API version deprecation](https://learn.microsoft.com/azure/ai-services/openai/api-version-deprecation) പേജ് സന്ദർശിക്കാം. **API version** Azure AI Foundryയിലെ "**Models + endpoints**" പേജിൽ കാണുന്നതുപോലെ **Model version** ൽ നിന്നും വ്യത്യസ്തമാണ് എന്ന കാര്യം ശ്രദ്ധിക്കുക.

## ചിത്ര പരിഭാഷക്കായി Azure Computer Vision സജ്ജമാക്കുക

ചിത്രങ്ങളിൽ ഉള്ള ടെക്‌സ്‌റ്റ് പരിഭാഷക്കായി Azure AI Service API കീയും എന്റ്പോയിന്റും കണ്ടെത്തേണ്ടതാണ്.

1. നിങ്ങളുടെ Azure AI പ്രോജക്റ്റിലേക്ക് (ഉദാ., `CoopTranslator-Project`) പോയി പ്രോജക്റ്റ് അവലോകന പേജിലാണ് എന്ന് ഉറപ്പാക്കുക.

### Azure AI Service കോൺഫിഗറേഷൻ

Azure AI Service ൽ നിന്നും API കീയും എന്റ്പോയിന്റും കണ്ടുകൂട്ടുക.

1. നിങ്ങളുടെ Azure AI പ്രോജക്റ്റിലേക്ക് (ഉദാ., `CoopTranslator-Project`) പോയി പ്രോജക്റ്റ് അവലോകന പേജിലാണ് എന്ന് ഉറപ്പാക്കുക.

1. Azure AI Service ടാബിൽ നിന്നു **API Key** യും **Endpoint** യും കണ്ടെത്തുക.

    ![Find API Key and Endpoint](../../../getting_started/imgs/find-azure-ai-info.png)

ഈ ബന്ധം കണക്റ്റുചെയ്‌ത Azure AI Services റിസോഴ്‌സ് (ചിത്ര വിശകലനം ഉൾപ്പെടെ) നിങ്ങളുടെ AI Foundry പ്രോജക്റ്റിന് ഉപയോഗിക്കാൻ ലഭ്യമാക്കുന്നു. ഇതിലൂടെ നോട്ട്ബുക്കുകളിലും അപ്ലിക്കേഷനുകളിലും ചിത്രങ്ങളിൽ നിന്നുള്ള ടെക്‌സ്‌റ്റ് എക്സ്ട്രാക്റ്റ് ചെയ്യാനാകും, തുടർന്ന് അത് Azure OpenAI മോഡലിലേക്ക് പരിഭാഷക്കായി അയയ്ക്കാം.

## നിങ്ങളുടെ ക്രെഡൻഷ്യലുകൾ സംയോജിപ്പിക്കൽ

ഇപ്പോൾ വരെ, നിങ്ങൾ താഴെ പറയുന്നതുകൾ ശേഖരിച്ചിരിക്കണം:

**Azure OpenAI (ടെക്‌സ്‌റ്റ് പരിഭാഷ) varten:**
- Azure OpenAI എന്റ്പോയിന്റ്
- Azure OpenAI API കീ
- Azure OpenAI മോഡൽ നാമം (ഉദാ., `gpt-4o`)
- Azure OpenAI ഡിപ്പ്ലോയ്‌മെന്റ് നാമം (ഉദാ., `cooptranslator-gpt4o`)
- Azure OpenAI API പതിപ്പ്

**Azure AI Services (Vision വഴി ചിത്രം ടെക്‌സ്‌റ്റ് എക്സ്ട്രാക്ഷൻ) varten:**
- Azure AI Service Endpoint
- Azure AI Service API കീ

### ഉദാഹരണം: എൻവയോൺമെന്റ് വെറിയബിൾ കോൺഫിഗറേഷൻ (പ്രിവ്യു)

നിങ്ങളുടെ അപ്ലിക്കേഷൻ നിർമ്മിക്കുമ്പോൾ, നിങ്ങളുള്ള ഈ ശേഖരിച്ച ക്രെഡൻഷ്യലുകൾ ഉപയോഗിച്ച് കോൺഫിഗർ ചെയ്യാൻ സാദ്ധ്യതയുണ്ട്. ഉദാഹരണത്തിന്, ഇവയെ എൻവയോൺമെന്റ് വെറിയബിൾസ് ആയി ഇതുപോലെ സജ്ജമാക്കാം:

```bash
# Azure AI സേവിസ് ക്രെഡൻഷ്യലുകൾ (ഇമേജ് തർജ്ജമയ്ക്കായി ആവശ്യമാണ്)
AZURE_AI_SERVICE_API_KEY="your_azure_ai_service_api_key" # ഉദാ., 21xasd...
AZURE_AI_SERVICE_ENDPOINT="https://your_azure_ai_service_endpoint.cognitiveservices.azure.com/"

# ഓപ്ഷണൽ ഫാൽബാക്ക് സെറ്റുകൾ: _1/_2 എന്ന സഫിക്‌സ് ഉപയോഗിച്ച് ഡ്യൂപ്ലിക്കറ്റ് വേരിയബിളുകൾ (സെറ്റിലുള്ള എല്ലാ വേരിയബിളുകൾക്കും ഒരേ ഇൻഡക്സ്)
AZURE_AI_SERVICE_API_KEY_1="your_azure_ai_service_api_key_1"
AZURE_AI_SERVICE_ENDPOINT_1="https://your_azure_ai_service_endpoint_1.cognitiveservices.azure.com/"

# Azure OpenAI ക്രെഡൻഷ്യലുകൾ (ടെക്സ്റ്റ് തർജ്ജമയ്ക്ക് ആവശ്യമാണ്)
AZURE_OPENAI_API_KEY="your_azure_openai_api_key" # ഉദാ., 21xasd...
AZURE_OPENAI_ENDPOINT="https://your_azure_openai_endpoint.openai.azure.com/"
AZURE_OPENAI_MODEL_NAME="your_model_name" # ഉദാ., gpt-4o
AZURE_OPENAI_CHAT_DEPLOYMENT_NAME="your_deployment_name" # ഉദാ., cooptranslator-gpt4o
AZURE_OPENAI_API_VERSION="your_api_version" # ഉദാ., 2024-12-01-preview

# ഓപ്ഷണൽ ഫാൾബാക്ക് സെറ്റുകൾ: സഫിക്‌സ് _1/_2 ഉപയോഗിച്ച് പൂർണ്ണ AZURE_OPENAI_* സെറ്റ് ഡ്യൂപ്ലിക്കേറ്റ് ചെയ്യുക (എല്ലാ വേരിയബിളുകൾക്കും ഒരേ ഇൻഡക്സ്)
```

---

### കൂടുതൽ വായന

- [Azure AI Foundryയിൽ പ്രോജക്റ്റ് സൃഷ്‌ടിക്കുന്നതിനുള്ള മാർഗ്ഗനിർദ്ദേശം](https://learn.microsoft.com/azure/ai-foundry/how-to/create-projects?tabs=ai-studio)
- [Azure AI റിസോഴ്‌സുകൾ സൃഷ്‌ടിക്കുന്നതിനുള്ള മാർഗ്ഗനിർദ്ദേശം](https://learn.microsoft.com/azure/ai-foundry/how-to/create-azure-ai-resource?tabs=portal)
- [Azure AI Foundryയിൽ OpenAI മോഡലുകൾ ഡിപ്പ്ലോയ് ചെയ്യുന്ന വിധം](https://learn.microsoft.com/en-us/azure/ai-foundry/how-to/deploy-models-openai)

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**വിഷയമുക്തി**:  
ഈ രേഖ AI പരിഭാഷാ സേവനം [Co-op Translator](https://github.com/Azure/co-op-translator) ഉപയോഗിച്ച് തർജ്ജുമ ചെയ്തതാണ്. നാം കൃത്യത ഉറപ്പു വരുത്താൻ ശ്രമിച്ചിരുന്നെങ്കിലും, ഓട്ടോമേറ്റഡ് പരിഭാഷകളിൽ പിഴവുകൾ അല്ലെങ്കിൽ അസമർത്ഥതകൾ ഉണ്ടാകാമെന്ന് ദയവായി ശ്രദ്ധിക്കുക. സോഴ്‌സ് ഭാഷയിൽ ഉള്ള അസൽ രേഖയെ അധികാരമുള്ള സ്രോതസ്സായി പരിഗണിക്കണമെന്നും നിർബന്ധം. അത്യാവശ്യ വിവരങ്ങൾക്ക് പ്രൊഫഷണൽ മാനുവൽ പരിഭാഷ നിർദ്ദേശിക്കുന്നു. ഈ പരിഭാഷ ഉപയോഗിച്ചതിനാൽ വന്ന ഏതെങ്കിലും തെറ്റി വ്യാഖ്യാനങ്ങൾക്കും തെറ്റിദ്ധാരണകൾക്കും ഞങ്ങൾ ഉത്തരവാദികൾ അല്ല.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->