<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "10d8cb07ad0d2ee6705439d4e382ecc9",
  "translation_date": "2025-05-06T18:15:52+00:00",
  "source_file": "getting_started/set-up-resources/set-up-azure-openai.md",
  "language_code": "ru"
}
-->
# Настройка Azure OpenAI для перевода языков

## Создание ресурса Azure OpenAI в Azure AI Foundry

Чтобы настроить Azure OpenAI в Azure AI Foundry, выполните следующие шаги:

### Создание хаба

1. Войдите в [портал Azure AI Foundry](https://ai.azure.com): Убедитесь, что вы вошли в систему с вашей учетной записью Azure.

2. Перейдите в Центр управления: На главной странице выберите «Management Center» в левом меню.

3. Создайте новый хаб: Нажмите «+ New hub» и введите необходимые данные, такие как Подписка, Группа ресурсов и Название хаба. Рекомендуем развернуть хаб в регионе East US, так как этот регион поддерживает Cognitive vision и модели GPT.

4. Проверьте данные и создайте: Проверьте введённые данные и нажмите «Create» для создания хаба.

### Создание проекта

1. Перейдите на главную страницу: Если вы не на главной странице, выберите «Azure AI Foundry» в верхнем левом углу, чтобы вернуться на главную.

2. Создайте проект: Нажмите «+ Create project» и введите название проекта.

3. Выберите хаб: Если у вас несколько хабов, выберите нужный. Если хотите создать новый хаб, это можно сделать на этом шаге.

4. Настройте проект: Следуйте подсказкам для настройки проекта в соответствии с вашими требованиями.

5. Создайте проект: Нажмите «Create» для завершения создания.

### Развертывание модели и конечной точки для модели OpenAI

1. Войдите в [портал Azure AI Foundry](https://ai.azure.com): Убедитесь, что вы вошли с подпиской Azure, в которой есть ваш ресурс Azure OpenAI Service.

2. Перейдите в раздел Models and Endpoints: На главной странице Azure AI Foundry найдите плитку с надписью «Model and Endpoints» в левом меню и выберите «Let's go.» или перейдите напрямую в этот раздел.

3. Если у вас ещё нет развернутой модели GPT, выберите «deploy model»: выберите модель GPT, рекомендуем GPT-4o, GPT-4o-mini или o3-mini.

4. Доступ к вашим ресурсам: Вы увидите существующие ресурсы Azure OpenAI Service. Если у вас несколько ресурсов, используйте селектор для выбора нужного.

Для более подробных инструкций обратитесь к официальной документации Azure AI Foundry.

[Как создать проект](https://learn.microsoft.com/azure/ai-studio/how-to/create-project)

[Как создать ресурсы](https://learn.microsoft.com/azure/ai-studio/how-to/create-azure-ai-resource)

[Как использовать модель OpenAI в AI Foundry](https://learn.microsoft.com/azure/ai-studio/ai-services/how-to/connect-azure-openai)

[Сервисы OpenAI в Azure AI Foundry](https://learn.microsoft.com/azure/ai-studio/azure-openai-in-ai-studio)

**Отказ от ответственности**:  
Этот документ был переведен с помощью AI-сервиса перевода [Co-op Translator](https://github.com/Azure/co-op-translator). Несмотря на наши усилия по обеспечению точности, просим учитывать, что автоматический перевод может содержать ошибки или неточности. Оригинальный документ на исходном языке следует считать авторитетным источником. Для получения критически важной информации рекомендуется обращаться к профессиональному человеческому переводу. Мы не несем ответственности за любые недоразумения или неправильные толкования, возникшие в результате использования данного перевода.