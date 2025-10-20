import os
import shutil 
import datetime
import platform
import subprocess
from pathlib import Path

def backup_files(source: str, destination: str):
    today = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = Path(destination) / f"backup_{today}"
    
    if not Path(source).exists():
        print(f"source directory not found: {source}")
        return ""
    
    Path(destination).mkdir(parents=True, exist_ok=True)

    try:
        shutil.make_archive(str(backup_name), 'gztar', root_dir=source)
        final_backup = f"{backup_name}.tar.gz"
        print(f"backup created successfully: {final_backup}")
        return final_backup
    except Exception as e:
        print(f"Backup failed due to error: {e}")
        return ""
    
def check_disk_space():
    print("\n checking disk space")
    try:
        subprocess.run(["df", "-h"], check=True)
    except Exception as e:
        print(f"could not check disk space {e}")

def check_cpu_load():
    print("\n checking cpu load")
    try:
        subprocess.run(["uptime"], check=True)
    except Exception as e:
        print(f"could not check cpu load: {e}")

def main():
    source_dir = input("Enter the source directory path. ").strip()
    destination_dir = input("Enter the destination directory path. ").strip()

    print("\n running systems health checks")
    check_disk_space()
    check_cpu_load()

    print("\n starting backup process")
    backup_files(source_dir, destination_dir)

    print("\n automation completed")

if __name__ == "__main__":
    main()
