import os
import shutil

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def delete_pycache_dirs(root=PROJECT_ROOT):
    for dirpath, dirnames, filenames in os.walk(root):
        if '__pycache__' in dirnames:
            pycache_path = os.path.join(dirpath, '__pycache__')
            try:
                shutil.rmtree(pycache_path)
                print(f"Deleted: {pycache_path}")
            except Exception as e:
                print(f"Failed to delete {pycache_path}: {e}")

if __name__ == "__main__":
    delete_pycache_dirs() 