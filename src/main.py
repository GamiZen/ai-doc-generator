from fastapi import FastAPI
import os

app = FastAPI()

# Define the project directory (root folder)
PROJECT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

@app.get("/")
def read_root():
    return {"message": "AI Documentation Generator is running!"}

@app.get("/list-files")
def list_project_files():
    """
    Lists all files and directories in the project.
    """
    file_structure = {}

    for root, dirs, files in os.walk(PROJECT_DIR):
        relative_root = os.path.relpath(root, PROJECT_DIR)
        file_structure[relative_root] = {
            "folders": dirs,
            "files": files
        }

    return file_structure
