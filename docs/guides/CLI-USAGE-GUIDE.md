# CLI Usage Guide

## Objetivo

A CLI oficial do DPF facilita a inicialização e a manutenção de projetos documentados segundo a metodologia, sem substituir a documentação como fonte da verdade.

## Requisitos

- Python 3.11 ou superior;
- projeto local ou diretório vazio para inicialização;
- sem dependência de rede.

## Instalação local

Modo de desenvolvimento:

```bash
./dpf --help
python -m dpf_cli --help
```

Instalação local editável:

```bash
pip install -e . --no-build-isolation
```

Launcher local sem instalação:

```bash
./dpf version
```

Após a instalação editável, o comando `dpf` fica disponível no ambiente Python local quando `setuptools` estiver disponível no ambiente de build.

## Início rápido

Inicializar um projeto:

```bash
./dpf init --path ./meu-projeto --name "Meu Projeto" --context MPRJ
```

Validar:

```bash
./dpf validate ./meu-projeto
```

Ver status:

```bash
./dpf status --path ./meu-projeto
```

Criar Feature:

```bash
./dpf feature create --path ./meu-projeto --epic EPC-MPRJ-0001 --title "Autenticação"
```

Criar Task:

```bash
./dpf task create --path ./meu-projeto --feature FEAT-MPRJ-0001 --title "Definir fluxo"
```

Criar decisão:

```bash
./dpf decision create --path ./meu-projeto --title "Separar autenticação de cadastro"
```

Preparar release:

```bash
./dpf release prepare --path ./meu-projeto --title "Release inicial" --version 1.0.0 --feature FEAT-MPRJ-0001
```

## Códigos de saída

- `0`: comando concluído com sucesso;
- `1`: erro de validação, conflito, inconsistência ou operação bloqueada;
- `2`: uso incorreto do comando.

## Segurança

A CLI:

- não faz commit;
- não faz push;
- não acessa rede;
- não executa código do projeto;
- não sobrescreve arquivos silenciosamente;
- rejeita caminhos inseguros baseados em symlink direto.

## Limitações do MVP

- não cria Capability nem Epic automaticamente;
- `feature create` exige Epic existente;
- `task create` exige Feature existente;
- usa a biblioteca oficial materializada em `templates/` como base canônica para os principais artefatos do MVP;
- não implementa ainda edição interativa avançada;
- não corrige inconsistências existentes no projeto.

## Solução de problemas

`manifest-not-found`:
- o caminho informado não contém projeto DPF inicializado.

`Epic inexistente`:
- a Epic informada não foi encontrada no projeto.

`Feature inexistente`:
- a Feature informada não foi encontrada no projeto.

`Features incompatíveis para release`:
- a release tentou incluir Feature em estado não liberável no MVP.
