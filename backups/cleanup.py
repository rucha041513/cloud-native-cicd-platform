import os
import shutil
import subprocess
from pathlib import Path

print("Cleaning unused Docker images...")

subprocess.run(
    ["docker", "image", "prune", "-f"],
    check=False
)

print("Removing old logs...")

log_folder = Path("../logs")

if log_folder.exists():
    for file in log_folder.glob("*.log"):
        try:
            file.unlink()
            print(f"Deleted {file.name}")
        except Exception as e:
            print(e)

print("Removing temp files...")

temp_folder = Path("../temp")

if temp_folder.exists():
    shutil.rmtree(temp_folder)
    print("Temp folder deleted")

print("Cleanup completed.")