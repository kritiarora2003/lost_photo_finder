import os

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".heic"}

def scan_images(folder):
    files = []
    for root, dirs, names in os.walk(folder):
        for n in names:
            ext = os.path.splitext(n.lower())[1]
            if ext in IMAGE_EXTS:
                files.append(os.path.join(root, n))
    return files

if __name__ == "__main__":
    folder = "data/images"
    imgs = scan_images(folder)
    print(f"Found {len(imgs)} images.")
