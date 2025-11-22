import json
import faiss
import torch
from PIL import Image
from sentence_transformers import SentenceTransformer
from scan import scan_images

MODEL_NAME = "sentence-transformers/clip-ViT-L-14"

def embed_images(image_paths):
    print("Loading model...")
    model = SentenceTransformer(MODEL_NAME)

    embeddings = []
    metadata = []

    for path in image_paths:
        try:
            img = Image.open(path).convert("RGB")
            emb = model.encode(img)
            embeddings.append(emb)
            metadata.append(path)
        except Exception as e:
            print("Failed:", path, e)

    embeddings = torch.tensor(embeddings).numpy()
    d = embeddings.shape[1]

    index = faiss.IndexFlatL2(d)
    index.add(embeddings)
    faiss.write_index(index, "embeddings/index.faiss")

    with open("embeddings/metadata.json", "w") as f:
        json.dump(metadata, f, indent=2)

    print(f"Indexed {len(metadata)} images")

if __name__ == "__main__":
    imgs = scan_images("data/images")
    print(f"Found {len(imgs)} images. Embedding now...")
    embed_images(imgs)
