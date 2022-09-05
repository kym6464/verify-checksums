import argparse
import hashlib
from pathlib import Path
from prettytable import PrettyTable
from tqdm import tqdm

def directory_or_file(s: str) -> Path:
    path = Path(s)
    if not path.exists():
        raise ValueError
    return path

parser = argparse.ArgumentParser()
parser.add_argument('path1', type=directory_or_file)
parser.add_argument('path2', type=directory_or_file)
args = parser.parse_args()

path1 = args.path1
path2 = args.path1

files1 = [f for f in path1.iterdir() if f.is_file()] if path1.is_dir() else [path1]
files2 = [f for f in path2.iterdir() if f.is_file()] if path2.is_dir() else [path2]

file_pairs = []
for f1 in files1:
    for f2 in files2:
        if f1.name == f2.name:
            file_pairs.append((f1, f2))

def get_md5_sum(file: Path) -> str:
    with file.open('rb') as f:
        data = f.read()
        return hashlib.md5(data).hexdigest()

table = PrettyTable(['index', 'directory', 'name', 'md5_checksum'])
for i, (f1, f2) in enumerate(tqdm(file_pairs, desc='Computing checksums...')):
    f1_checksum = get_md5_sum(f1)
    f2_checksum = get_md5_sum(f2)
    if f1_checksum != f2_checksum:
        table.add_rows([
            [i, f1.parent, f1.name, f1_checksum],
            [i, f2.parent, f2.name, f2_checksum],
            [''] * 4
        ])

print(table)
