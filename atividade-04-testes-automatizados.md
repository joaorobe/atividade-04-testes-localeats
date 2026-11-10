# Atividade 4 — Testes Automatizados do LocalEats

**Unidade Curricular:** Qualidade de Software  
**Projeto:** LocalEats  
**Integrantes:** Joao Robe e Octavio Hellwig  

## Objetivo e escopo

Esta entrega implementa duas regras de negócio em Python, testa os limites e
valores inválidos dessas regras e automatiza dois fluxos observados na tela de
login do LocalEats com Playwright.

As regras selecionadas são: valor mínimo de R$ 30,00 por pedido e quantidade
válida de 1 a 10 itens.

Os testes funcionais acessam
<https://local-eats-unisenac.vercel.app/static/login.html>. O primeiro alterna
para o formulário de cadastro; o segundo tenta enviar o formulário de login
vazio e verifica a validação nativa dos campos obrigatórios.

## Estrutura

```text
atividade-04/
├── atividade-04-testes-automatizados.md
├── relatorio-pytest.txt
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── regras_localeats.py
└── tests/
    ├── __init__.py
    ├── test_localeats.py
    └── test_regras_localeats.py
```

## Identificação dos testes

| ID | Tipo | Comportamento verificado | Arquivo e função |
|---|---|---|---|---|
| TU01 | Unitário | Pedido exatamente no mínimo (R$ 30,00) é aprovado | `tests/test_regras_localeats.py::test_pedido_exatamente_no_valor_minimo_e_aprovado` |
| TU02 | Unitário | Pedido abaixo do mínimo não é aprovado | `tests/test_regras_localeats.py::test_pedido_abaixo_do_valor_minimo_nao_e_aprovado` |
| TU03 | Unitário | Valor de pedido negativo gera `ValueError` | `tests/test_regras_localeats.py::test_pedido_com_valor_negativo_gera_value_error` |
| TU04 | Unitário | Quantidade máxima (10) é válida | `tests/test_regras_localeats.py::test_quantidade_maxima_de_itens_e_valida` |
| TU05 | Unitário | Quantidade acima do limite não é válida | `tests/test_regras_localeats.py::test_quantidade_acima_do_limite_nao_e_valida` |
| TU06 | Unitário | Quantidade negativa gera `ValueError` | `tests/test_regras_localeats.py::test_quantidade_negativa_gera_value_error` |
| TU07 | Unitário | Quantidade zero não é válida | `tests/test_regras_localeats.py::test_quantidade_zero_nao_e_valida` |
| TF01 | Funcional | Alternar para cadastro e verificar os campos exibidos | `tests/test_localeats.py::test_aba_criar_conta_apresenta_campos_de_cadastro` |
| TF02 | Funcional | Impedir envio do login vazio por campo obrigatório | `tests/test_localeats.py::test_login_vazio_bloqueia_envio_por_campo_obrigatorio` |

O caso de quantidade zero também é coberto por
`test_quantidade_zero_nao_e_valida`, como verificação adicional do limite
inferior definido no enunciado.

## Implementação das regras

Em `src/regras_localeats.py`:

- `pedido_atingiu_valor_minimo(valor_pedido)` retorna `True` a partir de
  R$ 30,00, `False` abaixo desse valor e lança `ValueError` para valores
  negativos.
- `quantidade_itens_valida(quantidade)` retorna `True` de 1 a 10, `False`
  para zero ou acima de 10 e lança `ValueError` para valores negativos.

## TDD

### TDD — valor mínimo do pedido

**Regra escolhida:** verificar se o pedido atingiu R$ 30,00.

**Primeiro teste escrito:** pedido de exatamente R$ 30,00 deve ser aprovado.

**Por que o teste falhou inicialmente:** antes da implementação, a função
estava ausente; após criar o módulo com a implementação pendente, a execução
falhou com `NotImplementedError`.

**Implementação mínima realizada:** rejeitar valores negativos com
`ValueError` e retornar se o valor é maior ou igual a 30.

**Segundo teste escrito:** pedido abaixo do mínimo deve retornar `False`.
Também foi testado o valor negativo para cobrir a exceção especificada.

**Melhoria ou refatoração realizada:** a regra ficou concentrada em uma função
curta, com mensagem explícita na exceção e anotação de tipo.

**Explicação individual — TU01:** o teste usa exatamente o limite de R$ 30,00
para verificar que a comparação inclui o valor mínimo (`>= 30`), e não apenas
valores maiores que ele.

### TDD — quantidade de itens

**Regra escolhida:** validar quantidade de itens entre 1 e 10.

**Primeiro teste escrito:** quantidade 10 deve ser válida.

**Por que o teste falhou inicialmente:** antes da implementação, a função
estava ausente; após criar o módulo com a implementação pendente, a execução
falhou com `NotImplementedError`.

**Implementação mínima realizada:** rejeitar quantidades negativas com
`ValueError` e retornar se o valor está no intervalo inclusivo de 1 a 10.

**Segundo teste escrito:** quantidade 11 deve retornar `False`. Também foram
cobertos zero e quantidade negativa, incluindo a exceção prevista.

**Melhoria ou refatoração realizada:** a validação de intervalo foi expressa
diretamente como `1 <= quantidade <= 10`, mantendo a regra simples de ler.

**Explicação individual — TU04:** o teste verifica o maior valor permitido,
10. O teste comprova que o limite superior é inclusivo; o caso seguinte,
11, confirma que valores fora do intervalo são rejeitados.

## Testes funcionais com Playwright

Todos os testes funcionais usam locators acessíveis do Playwright, realizam
interação na interface e verificam resultados observáveis:

- **TF01:** abre a tela de login, verifica título e texto de boas-vindas, clica
  em **Criar Conta** e verifica o campo de nome e o botão **Registrar**.
- **TF02:** abre a tela de login, verifica os campos de e-mail e senha, tenta
  enviar o formulário vazio e verifica que a URL não mudou e que o campo de
  e-mail continua inválido por estar vazio.

Não são usadas esperas fixas (`time.sleep`). Os testes dependem de acesso ao
site publicado e do Chromium instalado pelo Playwright.

## Dependências e execução

Com Python instalado, na pasta `atividades/atividade-04`, instale as
dependências e o navegador:

```powershell
python -m pip install -r requirements.txt
python -m playwright install chromium
```

Execute os testes e atualize o relatório:

```powershell
python -m pytest -v | Tee-Object -FilePath relatorio-pytest.txt
```

O relatório incluído nesta entrega foi gerado pela execução acima. Os testes
unitários não dependem da rede; os testes funcionais precisam que o site esteja
acessível.

## Uso de inteligência artificial

**Ferramenta utilizada:** assistente de IA integrado ao VS Code.

**Como a ferramenta foi utilizada:** apoio para organizar os arquivos e validar os testes unitários e funcionais com
Playwright.
