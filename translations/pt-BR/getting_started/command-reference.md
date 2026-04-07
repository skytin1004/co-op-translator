# Referência de comandos

A CLI do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                       | Descrição
----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                 | Traduz seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para Espanhol, Francês e Alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "language_codes" -u              | Atualiza traduções excluindo as existentes e recriando-as. Aviso: Isso excluirá todas as traduções atuais para os idiomas especificados.
translate -l "language_codes" -img            | Traduz apenas arquivos de imagem.
translate -l "language_codes" -md             | Traduz apenas arquivos Markdown.
translate -l "language_codes" -nb             | Traduz apenas arquivos de notebook Jupyter (.ipynb).
translate -l "language_codes" --fix           | Retraduz arquivos com pontuações de confiança baixas com base em resultados de avaliação anteriores.
translate -l "language_codes" -d              | Habilita modo de depuração para logs detalhados.
translate -l "language_codes" --save-logs, -s | Salva logs em nível DEBUG em arquivos sob <root_dir>/logs/ (o console permanece controlado por -d)
translate -l "language_codes" -r "root_dir"   | Especifica o diretório raiz do projeto
translate -l "language_codes" -f              | Usa modo rápido para tradução de imagens (até 3x mais rápido para plotagem com pequena perda na qualidade e alinhamento).
translate -l "language_codes" -y              | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Habilita ou desabilita a adição de uma seção de aviso de tradução automática em markdown e notebooks traduzidos (padrão: habilitado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza o aviso da seção de idiomas no README (checkout esparso) com a URL do seu repositório.
translate -l "language_codes" --help          | detalhes de ajuda dentro da CLI mostrando comandos disponíveis
evaluate -l "language_code"                  | Avalia a qualidade da tradução para um idioma específico e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8           | Avalia traduções com limite de confiança personalizado
evaluate -l "language_code" -f               | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "language_code" -D               | Modo de avaliação profunda (apenas baseado em LLM, mais completo porém mais lento)
evaluate -l "language_code" --save-logs, -s  | Salva logs em nível DEBUG em arquivos sob <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa arquivos Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode recorrer aos notebooks originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais arquivos seriam alterados sem salvar as alterações.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando equivalentes traduzidos não existem (atualiza somente quando traduzidos existem).
migrate-links -l "language_codes" -d          | Habilita modo de depuração para logs detalhados.
migrate-links -l "language_codes" --save-logs, -s | Salva logs em nível DEBUG em arquivos sob <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de uso

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (nenhuma tradução existente é excluída):    translate -l "ko" -img

  3. Atualiza todas as traduções coreanas (Aviso: Isso apaga todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas as imagens coreanas (Aviso: Isso apaga todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em resultados de avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança apenas para arquivos específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança apenas para arquivos específicos (imagens): translate -l "ko" --fix -img

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limite personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo modo depuração: - translate -l "ko" -d: Habilita log de depuração.
  12. Salvar logs em arquivos: translate -l "ko" -s
  13. DEBUG no console e em arquivo: translate -l "ko" -d -s
  14. Traduzir sem adicionar avisos de tradução automática nas saídas: translate -l "ko" --no-disclaimer

  15. Migrar links de notebooks para traduções coreanas (atualizar links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migrar links com dry-run (sem gravar mudanças):    migrate-links -l "ko" --dry-run

  16. Atualizar links somente quando notebooks traduzidos existirem (não recorrer aos originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processar todos os idiomas com prompt de confirmação:    migrate-links -l "all"

  18. Processar todos os idiomas e confirmar automaticamente:    migrate-links -l "all" -y
  19. Salvar logs em arquivos para migrate-links:    migrate-links -l "ko ja" -s

  20. Personalizar aviso da seção de idiomas no README com a URL do seu repositório:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemplos de avaliação

> [!WARNING]  
> **Recurso Beta**: A funcionalidade de avaliação está atualmente em beta. Este recurso foi lançado para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e sujeitos a alterações.

  1. Avaliar traduções coreanas: evaluate -l "ko"

  2. Avaliar com limite de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido usando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos pela precisão, esteja ciente de que traduções automáticas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se a tradução profissional feita por um humano. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->