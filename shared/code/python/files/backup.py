import pathlib
import shutil


home = pathlib.Path.home()
formations_dir = home / "formations"
backup_dir = home / "backup-formations"
old_backup_dir = home / "backup-formations-old"

if backup_dir.exists():
    shutil.move(backup_dir, old_backup_dir)

shutil.copytree(formations_dir, backup_dir)

if old_backup_dir.exists():
    shutil.rmtree(old_backup_dir)
