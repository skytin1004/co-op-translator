<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "9b1b247a8d0f1736459e0e9ede0d9c92",
  "translation_date": "2025-06-12T11:43:32+00:00",
  "source_file": "getting_started/markdown-only-mode.md",
  "language_code": "bg"
}
-->
# Използване на режим само с Markdown

## Въведение
Режимът само с Markdown е предназначен да превежда само Markdown съдържанието на вашия проект. Този режим пропуска процеса на превод на изображения и се фокусира единствено върху текстовото съдържание, което го прави идеален за ситуации, в които преводът на изображения не е необходим или съответните променливи на средата за Computer Vision не са настроени.

## Кога да се използва
- Когато променливите на средата, свързани с Computer Vision, не са конфигурирани.
- Когато искате да преведете само текстовото съдържание, без да обновявате връзките към изображения.
- Когато е изрично посочено от потребителя чрез командния ред с опцията `-md`.

## Как да активирате
За да активирате режим само с Markdown, използвайте опцията `-md` в командата си. Например:
```
translate -l "ko" -md
```

Или ако променливите на средата, свързани с Computer Vision, не са конфигурирани. Изпълнението на `translate -l "ko"` автоматично ще превключи към режим само с Markdown.

```
translate -l "ko"
```

Тази команда превежда Markdown съдържанието на корейски и обновява връзките към изображенията към техните оригинални пътища, вместо да ги променя към преведени пътища.

## Поведение
В режим само с Markdown:
- Процесът на превод пропуска стъпката за превод на изображения.
- Връзките към изображения в Markdown остават непроменени и сочат към оригиналните си пътища.

## Примери
### Преди
```markdown
![Image](../../../translated_images/image.aa98bae4d78871bb3b23ac9f938ff86539da4cd6fb4c52dafedc4665135c3d61.bg.png)
```
### След използване на режим само с Markdown
```markdown
![Image](../../../translated_images/image.fc8708ffe1e1ca12c38822b1a382726da4b232025d1daa8a50ab75c8635d0c4a.bg.png)
```

## Отстраняване на проблеми
- Уверете се, че опцията `-md` е правилно зададена в командата.
- Проверете дали няма променливи на средата за Computer Vision, които пречат на процеса.

## Заключение
Режимът само с Markdown предлага опростен начин за превод на текстово съдържание без промяна на връзките към изображения. Той е особено полезен, когато преводът на изображения не е необходим или когато работите в среди без настройка за Computer Vision.

**Отказ от отговорност**:  
Този документ е преведен с помощта на AI преводаческа услуга [Co-op Translator](https://github.com/Azure/co-op-translator). Въпреки че се стремим към точност, моля, имайте предвид, че автоматизираните преводи могат да съдържат грешки или неточности. Оригиналният документ на неговия роден език трябва да се счита за авторитетен източник. За критична информация се препоръчва професионален човешки превод. Ние не носим отговорност за никакви недоразумения или неправилни тълкувания, произтичащи от използването на този превод.