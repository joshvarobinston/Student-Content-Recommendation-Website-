import os

BASE_DIR = os.getcwd()

structure = {
    "student_content_recommender": [
        "__init__.py",
        "settings.py",
        "urls.py",
        "asgi.py",
        "wsgi.py",
    ],
    "api": [
        "__init__.py",
        "admin.py",
        "apps.py",
        "models.py",
        "serializers.py",
        "permissions.py",
        "urls.py",
    ],
    "api/views": [
        "__init__.py",
        "auth.py",
        "content.py",
        "engagement.py",
        "user.py",
    ],
}

def create_structure():
    for folder, files in structure.items():
        folder_path = os.path.join(BASE_DIR, folder)
        os.makedirs(folder_path, exist_ok=True)

        for file in files:
            file_path = os.path.join(folder_path, file)
            if not os.path.exists(file_path):
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write("")
                print(f"Created: {file_path}")
            else:
                print(f"Exists:  {file_path}")

if __name__ == "__main__":
    create_structure()
    print("\n✅ Backend folder & file structure created successfully.")
