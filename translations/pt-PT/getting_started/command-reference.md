# Referência de comandos

A CLI do **Co-op Translator** oferece várias opções para personalizar o processo de tradução:

Comando                                      | Descrição
---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
translate -l "language_codes"                | Traduz o seu projeto para as línguas especificadas. Exemplo: translate -l "es fr de" traduz para Espanhol, Francês e Alemão. Use translate -l "all" para traduzir para todas as línguas suportadas.
translate -l "language_codes" -u             | Atualiza as traduções eliminando as existentes e recriando-as. Aviso: Isto irá eliminar todas as traduções atuais para as línguas especificadas.
translate -l "language_codes" -img           | Traduz apenas ficheiros de imagem.
translate -l "language_codes" -md            | Traduz apenas ficheiros Markdown.
translate -l "language_codes" -nb            | Traduz apenas ficheiros Jupyter notebook (.ipynb).
translate -l "language_codes" --fix          | Retraduz ficheiros com pontuações de confiança baixas com base nos resultados de avaliação anteriores.
translate -l "language_codes" -d              | Ativa o modo de depuração para registos detalhados.
translate -l "language_codes" --save-logs, -s | Guarda registos ao nível DEBUG em ficheiros em <root_dir>/logs/ (o console mantém-se controlado por -d)
translate -l "language_codes" -r "root_dir"  | Especifica o diretório raiz do projeto
translate -l "language_codes" -f              | Utiliza modo rápido para tradução de imagens (até 3x mais rápido a desenhar, com ligeira perda de qualidade e alinhamento).
translate -l "language_codes" -y              | Confirma automaticamente todos os prompts (útil para pipelines CI/CD)
translate -l "language_codes" --add-disclaimer/--no-disclaimer | Ativa ou desativa a adição de uma secção de aviso de tradução automática a markdowns e notebooks traduzidos (padrão: ativado).
translate -l "language_codes" --repo-url "https://github.com/org/repo.git" | Personaliza o aviso da secção de idiomas no README (retracção parcial) com a URL do seu repositório.
translate -l "language_codes" --help          | detalhes de ajuda dentro da CLI mostrando comandos disponíveis
evaluate -l "language_code"                  | Avalia a qualidade da tradução para uma língua específica e fornece pontuações de confiança
evaluate -l "language_code" -c 0.8           | Avalia traduções com limiar de confiança personalizado
evaluate -l "language_code" -f               | Modo de avaliação rápida (apenas baseado em regras, sem LLM)
evaluate -l "language_code" -D               | Modo de avaliação profunda (apenas baseado em LLM, mais rigoroso mas mais lento)
evaluate -l "language_code" --save-logs, -s  | Guarda registos ao nível DEBUG em ficheiros em <root_dir>/logs/
migrate-links -l "language_codes"             | Reprocessa ficheiros Markdown traduzidos para atualizar links para notebooks (.ipynb). Prefere notebooks traduzidos quando disponíveis; caso contrário pode recorrer aos notebooks originais.
migrate-links -l "language_codes" -r          | Especifica o diretório raiz do projeto (padrão: diretório atual).
migrate-links -l "language_codes" --dry-run   | Mostra quais ficheiros seriam alterados sem efetuar alterações.
migrate-links -l "language_codes" --no-fallback-to-original | Não reescreve links para notebooks originais quando faltar o equivalente traduzido (atualiza apenas quando existe tradução).
migrate-links -l "language_codes" -d          | Ativa o modo de depuração para registos detalhados.
migrate-links -l "language_codes" --save-logs, -s | Guarda registos ao nível DEBUG em ficheiros em <root_dir>/logs/
migrate-links -l "all" -y                      | Processa todas as línguas e confirma automaticamente o alerta.

## Exemplos de utilização

  1. Comportamento padrão (adiciona novas traduções sem eliminar as existentes):   translate -l "ko"    translate -l "es fr de" -r "./my_project"

  2. Adiciona apenas novas traduções de imagens em coreano (não elimina traduções existentes):    translate -l "ko" -img

  3. Atualiza todas as traduções em coreano (Aviso: isto elimina todas as traduções coreanas existentes antes de retraduzir):    translate -l "ko" -u

  4. Atualiza apenas imagens coreanas (Aviso: isto elimina todas as imagens coreanas existentes antes de retraduzir):    translate -l "ko" -img -u

  5. Adiciona novas traduções markdown para coreano sem afetar outras traduções:    translate -l "ko" -md

  6. Corrige traduções com baixa confiança baseando-se em resultados de avaliação anteriores: translate -l "ko" --fix

  7. Corrige traduções com baixa confiança apenas para ficheiros específicos (markdown): translate -l "ko" --fix -md

  8. Corrige traduções com baixa confiança apenas para ficheiros específicos (imagens): translate -l "ko" --fix -img

  9. Utiliza o modo rápido para tradução de imagens:    translate -l "ko" -img -f

  10. Corrige traduções com baixa confiança com limiar personalizado: translate -l "ko" --fix -c 0.8

  11. Exemplo de modo de depuração: - translate -l "ko" -d: Ativa registos de depuração.
  12. Guarda registos para ficheiros: translate -l "ko" -s
  13. DEBUG no console e em ficheiros: translate -l "ko" -d -s
  14. Traduzir sem adicionar avisos de tradução automática às saídas: translate -l "ko" --no-disclaimer

  15. Migrar links de notebooks para traduções coreanas (atualiza links para notebooks traduzidos quando disponíveis):    migrate-links -l "ko"

  15. Migrar links com execução apenas simulada (sem gravação em ficheiros):    migrate-links -l "ko" --dry-run

  16. Atualiza links apenas quando notebooks traduzidos existirem (não recorre a originais):    migrate-links -l "ko" --no-fallback-to-original

  17. Processa todas as línguas com pedido de confirmação:    migrate-links -l "all"

  18. Processa todas as línguas e confirma automaticamente:    migrate-links -l "all" -y
  19. Guarda registos em ficheiros para migrate-links:    migrate-links -l "ko ja" -s

  20. Personaliza o aviso de idiomas no README com a URL do seu repositório:
      translate -l "ko" --repo-url "https://github.com/org/repo.git"

### Exemplos de Avaliação

> [!WARNING]  
> **Funcionalidade Beta**: A funcionalidade de avaliação encontra-se atualmente em beta. Esta funcionalidade foi lançada para avaliar documentos traduzidos, sendo os métodos de avaliação e a implementação detalhada ainda em desenvolvimento e sujeitos a alterações.

  1. Avaliar traduções coreanas: evaluate -l "ko"

  2. Avaliar com limiar de confiança personalizado: evaluate -l "ko" -c 0.8

  3. Avaliação rápida (apenas baseada em regras): evaluate -l "ko" -f

  4. Avaliação profunda (apenas baseada em LLM): evaluate -l "ko" -D

---

<!-- CO-OP TRANSLATOR DISCLAIMER START -->
**Aviso Legal**:
Este documento foi traduzido utilizando o serviço de tradução automática [Co-op Translator](https://github.com/Azure/co-op-translator). Embora nos esforcemos por garantir a precisão, tenha em atenção que traduções automáticas podem conter erros ou imprecisões. O documento original na sua língua nativa deve ser considerado a fonte autoritária. Para informações críticas, recomenda-se tradução profissional humana. Não nos responsabilizamos por quaisquer mal-entendidos ou interpretações incorretas decorrentes da utilização desta tradução.
<!-- CO-OP TRANSLATOR DISCLAIMER END -->