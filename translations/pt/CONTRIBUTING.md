<!--
CO_OP_TRANSLATOR_METADATA:
{
  "original_hash": "1ae2159f900e7d5d596bb00bcba4c999",
  "translation_date": "2025-10-22T13:42:22+00:00",
  "source_file": "CONTRIBUTING.md",
  "language_code": "pt"
}
-->
# Contribuir para o Co-op Translator

Este projeto aceita contribuições e sugestões. A maioria das contribuições exige que concordes com um
Acordo de Licença de Contribuidor (CLA), declarando que tens o direito de, e realmente concedes,
os direitos para usarmos a tua contribuição. Para mais detalhes, visita https://cla.opensource.microsoft.com.

Quando submeteres um pull request, um bot do CLA irá automaticamente determinar se precisas de fornecer
um CLA e irá marcar o PR de forma apropriada (por exemplo, verificação de estado, comentário). Basta seguir as instruções
fornecidas pelo bot. Só precisas de fazer isto uma vez para todos os repositórios que usam o nosso CLA.

## Configuração do ambiente de desenvolvimento

Para configurar o ambiente de desenvolvimento deste projeto, recomendamos usar o Poetry para gerir as dependências. Usamos o `pyproject.toml` para gerir as dependências do projeto, por isso, para instalar dependências, deves usar o Poetry.

### Criar um ambiente virtual

#### Usando pip

```bash
python -m venv .venv
```

#### Usando Poetry

```bash
poetry init
```

### Ativar o ambiente virtual

#### Para pip e Poetry

- Windows:

    ```bash
    .venv\Scripts\activate.bat
    ```

- Mac/Linux:

    ```bash
    source .venv/bin/activate
    ```

#### Usando Poetry

```bash
poetry shell
```

### Instalar o pacote e as dependências necessárias

#### Usando Poetry (a partir do pyproject.toml)

```bash
poetry install
```

### Testes manuais

Antes de submeteres um PR, é importante testar a funcionalidade de tradução com documentação real:

1. Cria uma pasta de teste na raiz do projeto:
    ```bash
    mkdir test_docs
    ```

2. Copia alguma documentação em markdown e imagens que queiras traduzir para a pasta de teste. Por exemplo:
    ```bash
    cp /path/to/your/docs/*.md test_docs/
    cp /path/to/your/images/*.png test_docs/
    ```

3. Instala o pacote localmente:
    ```bash
    pip install -e .
    ```

4. Executa o Co-op Translator nos teus documentos de teste:
    ```bash
    python -m co_op_translator --language-codes ko --root-dir test_docs
    ```

5. Verifica os ficheiros traduzidos em `test_docs/translations` e `test_docs/translated_images` para confirmar:
   - A qualidade da tradução
   - Se os comentários de metadados estão corretos
   - Se a estrutura original do markdown foi preservada
   - Se os links e imagens funcionam corretamente

Este teste manual ajuda a garantir que as tuas alterações funcionam bem em cenários reais.

### Variáveis de ambiente

1. Cria um ficheiro `.env` na raiz do projeto copiando o ficheiro `.env.template` fornecido.
1. Preenche as variáveis de ambiente conforme indicado.

> [!TIP]
>
> ### Opções adicionais para o ambiente de desenvolvimento
>
> Além de executar o projeto localmente, podes também usar o GitHub Codespaces ou os Dev Containers do VS Code como alternativa para configurar o ambiente de desenvolvimento.
>
> #### GitHub Codespaces
>
> Podes executar estes exemplos virtualmente usando o GitHub Codespaces, sem necessidade de configurações ou instalações adicionais.
>
> O botão irá abrir uma instância do VS Code baseada na web no teu navegador:
>
> 1. Abre o template (pode demorar alguns minutos):
>
>     <a href="https://codespaces.new/azure/co-op-translator"><img src="https://github.com/codespaces/badge.svg" alt="Abrir no GitHub Codespaces"></a>
>
> #### Executar localmente com VS Code Dev Containers
>
> ⚠️ Esta opção só funciona se o teu Docker Desktop tiver pelo menos 16 GB de RAM alocados. Se tiveres menos de 16 GB de RAM, podes experimentar a opção [GitHub Codespaces](../..) ou [configurar localmente](../..).
>
> Uma opção relacionada são os Dev Containers do VS Code, que abrem o projeto no teu VS Code local usando a extensão [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):
>
> 1. Inicia o Docker Desktop (instala se ainda não estiver instalado)
> 2. Abre o projeto:
>
>    <a href="https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure/co-op-translator"><img src="https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode" alt="Abrir em Dev Containers"></a>


### Estilo de código

Usamos o [Black](https://github.com/psf/black) como formatador de código Python para manter um estilo consistente em todo o projeto. O Black é um formatador rigoroso que reformata automaticamente o código Python para seguir o estilo definido por ele.

#### Configuração

A configuração do Black está especificada no nosso `pyproject.toml`:

```toml
[tool.black]
line-length = 88
target-version = ['py310']
include = '\.pyi?$'
```

#### Instalar o Black

Podes instalar o Black usando o Poetry (recomendado) ou pip:

##### Usando Poetry

O Black é instalado automaticamente quando configuras o ambiente de desenvolvimento:
```bash
poetry install
```

##### Usando pip

Se usares pip, podes instalar o Black diretamente:
```bash
pip install black
```

#### Usar o Black

##### Com Poetry

1. Formata todos os ficheiros Python do projeto:
    ```bash
    poetry run black .
    ```

2. Formata um ficheiro ou pasta específica:
    ```bash
    poetry run black path/to/file_or_directory
    ```

##### Com pip

1. Formata todos os ficheiros Python do projeto:
    ```bash
    black .
    ```

2. Formata um ficheiro ou pasta específica:
    ```bash
    black path/to/file_or_directory
    ```

> [!TIP]
> Recomendamos que configures o teu editor para formatar automaticamente o código com o Black ao guardar. A maioria dos editores modernos suporta isto através de extensões ou plugins.

## Executar o Co-op Translator

Para executar o Co-op Translator usando o Poetry no teu ambiente, segue estes passos:

1. Navega até à pasta onde queres fazer testes de tradução ou cria uma pasta temporária para testes.

2. Executa o seguinte comando. Substitui `-l ko` pelo código da língua para a qual queres traduzir. O parâmetro `-d` ativa o modo de depuração.

    ```bash
    poetry run co-op-translator translate -l ko -d
    ```

> [!NOTE]
> Garante que o ambiente do Poetry está ativado (poetry shell) antes de executar o comando.

## Contribuir com um novo idioma

Aceitamos contribuições que adicionem suporte a novos idiomas. Antes de abrires um PR, completa os passos abaixo para facilitar a revisão.

1. Adiciona o idioma ao mapeamento de fontes
   - Edita `src/co_op_translator/fonts/font_language_mappings.yml`
   - Adiciona uma entrada com:
     - `code`: Código de idioma tipo ISO (exemplo: `vi`)
     - `name`: Nome legível para humanos
     - `font`: Uma fonte incluída em `src/co_op_translator/fonts/` que suporte o alfabeto
     - `rtl`: `true` se for escrita da direita para a esquerda, caso contrário `false`

2. Inclui os ficheiros de fonte necessários (se aplicável)
   - Se for necessária uma nova fonte, verifica a compatibilidade da licença para distribuição open source
   - Adiciona o ficheiro da fonte em `src/co_op_translator/fonts/`

3. Verificação local
   - Executa traduções para uma pequena amostra (Markdown, imagens e notebooks conforme necessário)
   - Verifica se o resultado é apresentado corretamente, incluindo fontes e layout RTL se aplicável

4. Atualiza a documentação
   - Garante que o idioma aparece em `getting_started/supported-languages.md`
   - Não é necessário alterar o `README_languages_template.md`; este é gerado a partir da lista de idiomas suportados

5. Abre um PR
   - Descreve o idioma adicionado e quaisquer considerações sobre fontes/licenciamento
   - Anexa capturas de ecrã dos resultados renderizados, se possível

Exemplo de entrada YAML:

```yaml
new_lang(code):
  name: "New Language"
  font: "NotoSans-Medium.ttf"
  rtl: false
```

### Testar o novo idioma

Podes testar o novo idioma executando o seguinte comando:

```bash
# Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
# Install the development package
pip install -e .
# Run the translation
translate -l "new_lang"
```

## Mantenedores

### Mensagem de commit e estratégia de merge

Para garantir consistência e clareza no histórico de commits do projeto, seguimos um formato específico para a **mensagem final de commit** ao usar a estratégia **Squash and Merge**.

Quando um pull request (PR) é integrado, os commits individuais são agrupados num único commit. A mensagem final de commit deve seguir o formato abaixo para manter um histórico limpo e consistente.

#### Formato da mensagem de commit (para squash and merge)

Usamos o seguinte formato para mensagens de commit:

```bash
<type>: <description> (#<PR number>)
```

- **type**: Especifica a categoria do commit. Usamos os seguintes tipos:
  - `Docs`: Para atualizações de documentação.
  - `Build`: Para alterações relacionadas com o sistema de build ou dependências, incluindo atualizações de ficheiros de configuração, workflows de CI ou Dockerfile.
  - `Core`: Para modificações na funcionalidade principal do projeto, especialmente nos ficheiros em `src/co_op_translator/core`.

- **description**: Um resumo conciso da alteração.
- **PR number**: O número do pull request associado ao commit.

**Exemplos**:

- `Docs: Atualizar instruções de instalação para maior clareza (#50)`
- `Core: Melhorar o tratamento da tradução de imagens (#60)`

> [!NOTE]
> Atualmente, os prefixos **`Docs`**, **`Core`** e **`Build`** são adicionados automaticamente aos títulos dos PRs com base nas etiquetas aplicadas ao código fonte modificado. Desde que a etiqueta correta seja aplicada, normalmente não precisas de atualizar manualmente o título do PR. Só tens de verificar se está tudo correto e se o prefixo foi gerado adequadamente.

#### Estratégia de merge

Usamos **Squash and Merge** como estratégia padrão para pull requests. Esta estratégia garante que as mensagens de commit seguem o nosso formato, mesmo que os commits individuais não o façam.

**Razões**:

- Um histórico de projeto limpo e linear.
- Consistência nas mensagens de commit.
- Menos ruído de commits menores (ex: "corrigir erro ortográfico").

Ao fazer merge, garante que a mensagem final de commit segue o formato descrito acima.

**Exemplo de Squash and Merge**
Se um PR contiver os seguintes commits:

- `corrigir erro ortográfico`
- `atualizar README`
- `ajustar formatação`

Devem ser agrupados em:
`Docs: Melhorar clareza e formatação da documentação (#65)`

---

**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original, na sua língua nativa, deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas resultantes do uso desta tradução.