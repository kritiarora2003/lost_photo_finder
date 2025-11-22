import json
import faiss
from sentence_transformers import SentenceTransformer

MODEL_NAME = "sentence-transformers/clip-ViT-L-14"

def search(query, k=5):
    model = SentenceTransformer(MODEL_NAME)

    q_emb = model.encode(query).reshape(1, -1).astype("float32")
    index = faiss.read_index("embeddings/index.faiss")

    with open("embeddings/metadata.json") as f:
        metadata = json.load(f)

    distances, indices = index.search(q_emb, k)

    results = [metadata[i] for i in indices[0]]
    return results

if __name__ == "__main__":
    print(search("two people", 5))
