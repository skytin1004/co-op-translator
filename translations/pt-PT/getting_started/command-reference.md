# Command reference

The **Co-op Translator** CLI oferece várias opções para personalizar o processo de tradução:

Command                                       | Description
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduza o seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para Espanhol, Francês e Alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "language_codes" -u              | Atualiza as traduções eliminando as existentes e recriando-as. Aviso: Isto vai eliminar todas as traduções atuais para os idiomas especificados.
translate -l "language_codes" -img            | Traduz apenas ficheiros de imagem.
translate -l "language_codes" -md             | Traduz apenas ficheiros Markdown.
translate -l "language_codes" -nb             | Traduz apenas ficheiros Jupyter notebook (.ipynb).
translate -l "language_codes" --fix           | Retraduz ficheiros com pontuações de confiança baixas com base nos resultados de avaliação anteriores.
translate -l "language_codes" -d              | Ativa o modo debug para registos detalhados.
translate -l "language_codes" --save-logs, -s | Guarda registos a nível DEBUG em ficheiros sob <root_dir>/logs/ (o console mantém-se controlado por -d)
translate -l "language_codes" -r "root_dir"   | Especifica o diretório raiz do projeto
translate -l "language_codes" -f              | Usa modo rápido para a tradução de imagens (até 3x mais rápido a desenhar com ligeira perda na qualidade e alinhamento).
translate -l "language_codes" -y              | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ativa ou desativa a adição de uma secção de aviso de tradução automática a markdown e notebooks traduzidos (padrão: ativado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza o aviso da secção de idiomas do README (sparse checkout) com a URL do seu repositório.
translate -l "language_codes" --help          | mostrar detalhes de ajuda na CLI com os comandos disponíveis
evaluate -l "language_code"                  | Avalia a qualidade da tradução para um idioma específico e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8           | Avalia traduções com um limiar de confiança personalizado
evaluate -l "language_code" -f               | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "language_code" -D               | Modo de avaliação aprofundada (apenas baseado em LLM, mais rigoroso mas mais lento)
evaluate -l "language_code" --save-logs, -s  | Guarda registos a nível DEBUG em ficheiros sob <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa ficheiros Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário pode recorrer aos notebooks originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais ficheiros seriam alterados sem efetuar alterações.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando não existem pares traduzidos (atualiza apenas quando a tradução existe).
migrate-links -l "language_codes" -d          | Ativa modo debug para registos detalhados.
migrate-links -l "language_codes" --save-logs, -s | Guarda registos a nível DEBUG em ficheiros sob <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de utilização

  1. Comportamento por defeito (adicionar novas traduções sem eliminar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adicionar apenas novas traduções de imagem em coreano (não serão eliminadas traduções existentes):    translate -l "ko" -img

  3. Atualizar todas as traduções em coreano (Aviso: Isto elimina todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualizar apenas imagens em coreano (Aviso: Isto elimina todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adicionar novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrigir traduções com baixa confiança com base em avaliações anteriores: translate -l "ko" --fix

  7. Corrigir traduções com baixa confiança para ficheiros específicos somente (markdown): translate -l "ko" --fix -md

  8. Corrigir traduções com baixa confiança para ficheiros específicos somente (imagens): translate -l "ko" --fix -img

  9. Usar modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrigir traduções com baixa confiança com limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo debug: - translate -l "ko" -d: Ativa registos debug.
  12. Guardar registos em ficheiros: translate -l "ko" -s
  13. DEBUG no console e no ficheiro: translate -l "ko" -d -s
  14. Traduzir sem adicionar avisos de tradução automática nos outputs: translate -l "ko" --no-disclaimer

  15. Migrar links de notebooks para traduções coreanas (atualizar links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migrar links com execução simulada (sem escrever ficheiros):    migrate-links -l "ko" --dry-run

  16. Atualizar links apenas quando existirem notebooks traduzidos (não usar versões originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processar todos os idiomas com pedido de confirmação:    migrate-links -l "all"

  18. Processar todos os idiomas e confirmar automaticamente:    migrate-links -l "all" -y
  19. Guardar registos em ficheiros para migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizar aviso da secção de idiomas do README com a URL do seu repositório:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemplos de Avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação encontra-se atualmente em beta. Esta funcionalidade foi lançada para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e sujeitos a alterações.

  1. Avaliar traduções em coreano: evaluate -l "ko"

  2. Avaliar com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação aprofundada (apenas LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, por favor, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se a tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações erradas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->