# Referência de comandos

A CLI do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                      | Descrição
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Traduz seu projeto para os idiomas especificados. Exemplo: translate -l "es fr de" traduz para espanhol, francês e alemão. Use translate -l "all" para traduzir para todos os idiomas suportados.
translate -l "language_codes" -u             | Atualiza traduções excluindo as existentes e recriando-as. Aviso: Isso excluirá todas as traduções atuais para os idiomas especificados.
translate -l "language_codes" -img           | Traduz apenas arquivos de imagem.
translate -l "language_codes" -md            | Traduz apenas arquivos Markdown.
translate -l "language_codes" -nb            | Traduz apenas arquivos de notebook Jupyter (.ipynb).
translate -l "language_codes" --fix          | Retraduz arquivos com baixa pontuação de confiança com base em resultados de avaliação anteriores.
translate -l "language_codes" -d             | Habilita modo de depuração para registros detalhados.
translate -l "language_codes" --save-logs, -s| Salva logs de nível DEBUG em arquivos sob <root_dir>/logs/ (o console permanece controlado por -d)
translate -l "language_codes" -r "root_dir"  | Especifica o diretório raiz do projeto
translate -l "language_codes" -f             | Usa modo rápido para tradução de imagens (até 3x mais rápido na geração, com leve perda na qualidade e alinhamento).
translate -l "language_codes" -y             | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ativa ou desativa a adição de uma seção de aviso de tradução automática a markdowns e notebooks traduzidos (padrão: ativado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza o aviso da seção de idiomas do README (checkout esparso) com a URL do seu repositório.
translate -l "language_codes" --help         | Detalhes de ajuda dentro da CLI mostrando os comandos disponíveis
evaluate -l "language_code"                  | Avalia a qualidade da tradução para um idioma específico e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8           | Avalia traduções com limite personalizado de confiança
evaluate -l "language_code" -f               | Modo de avaliação rápida (somente baseado em regras, sem LLM)
evaluate -l "language_code" -D               | Modo de avaliação profunda (baseado em LLM, mais completo porém mais lento)
evaluate -l "language_code" --save-logs, -s  | Salva logs de nível DEBUG em arquivos sob <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa arquivos Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário, pode usar notebooks originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais arquivos seriam alterados sem fazer gravações.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando traduções estiverem faltando (atualiza somente quando tradução existe).
migrate-links -l "language_codes" -d          | Habilita modo de depuração para registros detalhados.
migrate-links -l "language_codes" --save-logs, -s | Salva logs de nível DEBUG em arquivos sob <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todos os idiomas e confirma automaticamente o aviso.

## Exemplos de uso

  1. Comportamento padrão (adiciona novas traduções sem apagar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não apaga traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Aviso: Isto apaga todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens coreanas (Aviso: Isto apaga todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança com base em resultados de avaliações anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança para arquivos específicos apenas (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança para arquivos específicos apenas (imagens): translate -l "ko" --fix -img

  9. Usa modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limite personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo modo depuração: - translate -l "ko" -d: Habilita registro de debug.
  12. Salva logs em arquivos: translate -l "ko" -s
  13. DEBUG no console e DEBUG em arquivo: translate -l "ko" -d -s
  14. Traduz sem adicionar avisos de tradução automática nas saídas: translate -l "ko" --no-disclaimer

  15. Migra links de notebooks para traduções coreanas (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migra links com dry-run (sem gravação de arquivos):    migrate-links -l "ko" --dry-run

  16. Atualiza links somente quando notebooks traduzidos existirem (não volta aos originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todos os idiomas com prompt de confirmação:    migrate-links -l "all"

  18. Processa todos os idiomas e confirma automaticamente:    migrate-links -l "all" -y
  19. Salva logs em arquivos para migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliza aviso de idiomas do README com a URL do seu repositório:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemplos de Avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação está atualmente em beta. Este recurso foi lançado para avaliar documentos traduzidos, e os métodos de avaliação e implementação detalhada ainda estão em desenvolvimento e sujeitos a alterações.

  1. Avaliar traduções em coreano: evaluate -l "ko"

  2. Avaliar com limite personalizado de confiança: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (somente baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseado em LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:  
Este documento foi traduzido utilizando o serviço de tradução por IA [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos para garantir a precisão, esteja ciente de que traduções automatizadas podem conter erros ou imprecisões. O documento original em seu idioma nativo deve ser considerado a fonte autorizada. Para informações críticas, recomenda-se tradução profissional feita por humanos. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações equivocadas decorrentes do uso desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->