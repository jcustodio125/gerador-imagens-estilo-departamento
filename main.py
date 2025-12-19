import os
from PIL import Image
import numpy as np

# CONFIG
INPUT_DIR = "input"
OUTPUT_DIR = "output"

BLUE = (2, 42, 254)   # #022AFE
WHITE = (255, 255, 255)
THRESHOLD = 125      # ajuste fino aqui

# Criar pasta output se não existir
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Extensões suportadas
EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

for filename in os.listdir(INPUT_DIR):
    if not filename.lower().endswith(EXTENSIONS):
        continue

    input_path = os.path.join(INPUT_DIR, filename)
    output_path = os.path.join(OUTPUT_DIR, filename)

    # Abrir imagem
    img = Image.open(input_path).convert("L")

    # Converter para array
    arr = np.array(img)

    # Threshold
    binary = arr > THRESHOLD

    # Criar imagem final RGB
    result = np.zeros((arr.shape[0], arr.shape[1], 3), dtype=np.uint8)
    result[binary] = WHITE
    result[~binary] = BLUE

    # Salvar
    Image.fromarray(result).save(output_path)

    print(f"Processada: {filename}")

print("✅ Todas as imagens foram processadas.")
