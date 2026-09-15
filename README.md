# Calculadora em Python

Uma calculadora simples desenvolvida em Python, com duas versões:

- **`calculadora.py`** — versão de linha de comando (terminal).
- **`calculadora_app.py`** — versão com interface gráfica, feita com `tkinter`.

Projeto criado como estudo de:
- Funções e organização de código
- Tratamento de erros (`try/except`)
- Programação orientada a objetos (classes)
- Interfaces gráficas com `tkinter`

## 🚀 Como executar

Pré-requisito: Python 3 instalado ([python.org](https://www.python.org/downloads/)).

### Versão terminal
```bash
python calculadora.py
```

### Versão com interface gráfica
```bash
python calculadora_app.py
```

## 🖼️ Funcionalidades

- Soma, subtração, multiplicação e divisão
- Validação de números inválidos
- Proteção contra divisão por zero
- Interface com botões (versão gráfica)

## 📦 Gerando um executável (opcional)

Para transformar a versão gráfica em um aplicativo executável (sem precisar de Python instalado), use o [PyInstaller](https://pyinstaller.org/):

```bash
pip install pyinstaller
pyinstaller --onefile --windowed calculadora_app.py
```

O executável será gerado na pasta `dist/`.

## 🛠️ Tecnologias

- Python 3
- Tkinter (interface gráfica)

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para usar, estudar e modificar.
