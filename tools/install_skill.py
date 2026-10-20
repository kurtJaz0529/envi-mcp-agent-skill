"""Install this skill locally, preserving an existing copy before updating it."""
import argparse
import hashlib
import json
import os
import shutil
from datetime import datetime, timezone
from pathlib import Path


def install(source, destination, dry_run=False):
    source = source.resolve()
    destination = destination.resolve()
    if not (source / 'SKILL.md').is_file():
        raise ValueError('Source does not contain SKILL.md')
    if destination == source or source in destination.parents or destination in source.parents:
        raise ValueError('Source and destination must be separate, non-nested directories')
    files = sorted(p for p in source.rglob('*') if p.is_file())
    if any(p.is_symlink() for p in source.rglob('*')):
        raise ValueError('Skill source must not contain symbolic links')
    if destination.exists() and not destination.is_dir():
        raise ValueError('Destination exists and is not a directory')
    result = {'source': str(source), 'destination': str(destination),
              'files': len(files), 'dry_run': dry_run, 'backup': None}
    if dry_run:
        return result
    if destination.exists():
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
        backup = destination.parent.parent / 'backups' / 'skills' / (destination.name + '-' + stamp)
        backup.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(destination, backup)
        result['backup'] = str(backup)
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination, dirs_exist_ok=True)
    for file in files:
        installed = destination / file.relative_to(source)
        if hashlib.sha256(file.read_bytes()).digest() != hashlib.sha256(installed.read_bytes()).digest():
            raise RuntimeError('Installed file hash mismatch: ' + str(installed))
    result['verified'] = True
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    default_source = Path(__file__).resolve().parents[1] / 'skills' / 'envi-workflows'
    codex_root = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    parser.add_argument('--source', type=Path, default=default_source)
    parser.add_argument('--destination', type=Path, default=codex_root / 'skills' / 'envi-workflows')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    print(json.dumps(install(args.source, args.destination, args.dry_run), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
