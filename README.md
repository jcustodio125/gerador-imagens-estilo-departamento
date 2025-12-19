# Image Color Transformer – Ensiene Style

Este projeto é um script em **Python** para processamento em imagens, inspirado no estilo visual utilizado pelo **DEPARTAMENTO ®**.

O script converte imagens comuns em composições **binárias de alto contraste**, substituindo pixels claros por **branco** e pixels escuros por um **azul**.

---

## 📌 O que este código faz?

1. Lê todas as imagens de uma pasta de entrada (`input`)
2. Converte cada imagem para **escala de cinza**
3. Analisa a imagem **pixel a pixel**
4. Aplica um **threshold (limiar)** para separar claro e escuro
5. Gera uma nova imagem RGB onde:
   - Pixels acima do limiar → **branco**
   - Pixels abaixo do limiar → **azul**
6. Salva o resultado na pasta `output`

---

## 🧱 Estrutura do projeto

```
project/
│
├── input/          # Coloque aqui as imagens originais
├── output/         # As imagens processadas serão salvas aqui
├── main.py         # Script principal
└── README.md
```

---

## 🚀 Como usar:

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/ainda-nao-criado.git
```

---

### 2️⃣ Criar e ativar uma virtual environment (venv)

#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS
```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar as dependências

```bash
pip install pillow numpy
```

---

### 4️⃣ Adicionar as imagens

Coloque todas as imagens que deseja processar dentro da pasta:

```
input/
```

Formatos suportados:
- `.jpg`
- `.jpeg`
- `.png`
- `.webp`

---

### 5️⃣ Rodar o script

```bash
python main.py
```

---

### 6️⃣ Resultado

As imagens processadas aparecerão automaticamente na pasta:

```
output/
```

Cada imagem mantém o nome original.

---

## 🎛️ Configurações importantes

No início do código você pode ajustar:

```python
BLUE = (2, 42, 254)     # Azul (#022AFE)
WHITE = (255, 255, 255)
THRESHOLD = 125        # Ajuste fino do contraste
```

- **THRESHOLD menor** → mais áreas viram branco
- **THRESHOLD maior** → mais áreas viram azul

---

## 🎨 Inspiração visual

Este projeto é inspirado no estilo visual utilizado pelo **DEPARTAMENTO ®**:

📸 Instagram do DEPARTAMENTO ®:
👉 https://www.instagram.com/departamento____/

---

## 🧠 Tecnologias usadas

- Python 3
- Pillow (PIL)
- NumPy
