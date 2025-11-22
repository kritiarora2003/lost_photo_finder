
# 🖼️ Lost Photo Finder

> *Find your lost or duplicate photos instantly using intelligent image similarity search.*

---

## 🚀 Overview

**Lost Photo Finder** is an intelligent image search and recovery tool that helps users locate missing, duplicate, or similar images within large local directories.
It uses **deep learning–based feature extraction** (via models like ResNet or VGG) and **cosine similarity** to match photos based on visual content — not just filenames or metadata.

This makes it ideal for:

* Reorganizing messy photo collections
* Recovering duplicates with different names or sizes
* Detecting similar images (e.g., resized, cropped, or filtered versions)

---

## 🧠 How It Works

1. **Feature Extraction:**
   Each image is converted into a vector using a pre-trained CNN model (e.g., ResNet50).

2. **Embedding Storage:**
   The vectors are saved in a local database (NumPy or pickle format).

3. **Query Search:**
   When a new image is uploaded, the system computes its embedding and finds the top-k most similar images using **cosine similarity**.

4. **Visualization:**
   The matched images are displayed with similarity scores.

---


## 💡 Example Usage

// will add later
---

## 🧮 Algorithm Details

Similarity is computed using **cosine similarity** between embeddings:

[
\text{similarity}(A, B) = \frac{A \cdot B}{||A|| \times ||B||}
]

Where A and B are feature vectors from the CNN model.
A higher score → greater visual similarity.

---

## 🧰 Installation

```bash
git clone https://github.com/<your-username>/lost-photo-finder.git
cd lost-photo-finder
```

---


## 📜 License

This project is licensed under the **MIT License** — feel free to modify and use with attribution.

