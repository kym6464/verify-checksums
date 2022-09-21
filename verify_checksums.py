import sys
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


def get_md5_sum(file: Path) -> str:
    with file.open('rb') as f:
        data = f.read()
    return hashlib.md5(data).hexdigest()


parser = argparse.ArgumentParser()
parser.add_argument('path1', type=directory_or_file)
parser.add_argument('path2', type=directory_or_file)
args = parser.parse_args()

path1 = args.path1
path2 = args.path2

files1 = [f for f in path1.iterdir() if f.is_file()] if path1.is_dir() else [path1]
files2 = [f for f in path2.iterdir() if f.is_file()] if path2.is_dir() else [path2]

file_pairs = []
for f1 in files1:
    for f2 in files2:
        if f1.name == f2.name:
            file_pairs.append((f1, f2))

if not file_pairs:
    print('no file pairs with matching names!')
    sys.exit()

print(f'Comparing {len(file_pairs)} file pair(s)...')
pair_table = PrettyTable(['index', 'directory', 'name'])
for i, (f1, f2) in enumerate(file_pairs):
    pair_table.add_rows([
        [i, f1.parent, f1.name],
        [i, f2.parent, f2.name],
    ])
    if i != len(file_pairs) - 1:
        pair_table.add_row([' '] * 3)
print(pair_table)

file_hash : dict[Path, str] = {}
files_to_hash = [f for pair in file_pairs for f in pair]
for fpath in tqdm(files_to_hash, desc='computing checksums...', ):
    file_hash[fpath] = get_md5_sum(fpath)

mismatch_pairs = []
for i, (f1, f2) in enumerate(file_pairs):
    f1_checksum = file_hash[f1]
    f2_checksum = file_hash[f2]
    if f1_checksum != f2_checksum:
        mismatch_pairs.append([i, f1, f2])

if not mismatch_pairs:
    print('all file pair checksums match')
    sys.exit()

table = PrettyTable(['index', 'directory', 'name', 'md5_checksum'])
for mismatch_idx, (pair_idx, f1, f2) in enumerate(mismatch_pairs):
    f1_checksum = file_hash[f1]
    f2_checksum = file_hash[f2]
    table.add_rows([
        [pair_idx, f1.parent, f1.name, f1_checksum],
        [pair_idx, f2.parent, f2.name, f2_checksum],
    ])
    if mismatch_idx != len(mismatch_pairs) - 1:
        table.add_row([''] * 4)
print(f'Found {len(mismatch_pairs)} file pair(s) with mismatched checksums...')
print(table)
