# checksum

A program that takes as input two directories and:

- finds pairs of matching files by name,

- for each pair, computes checksum for each file, and then compares the checksums for each pair

- reports pairs of files whose checksums do no match

## usage

```
usage: verify_checksums.py [-h] dir1 dir2

positional arguments:
  dir1
  dir2

options:
  -h, --help  show this help message and exit
```

Create a virtual environment and install requirements in `requirements.txt`:

```
pip install -r requirements.txt
```

## examples

Two equivalent directories:

```
python verify_checksums.py test_data/dir_a test_data/dir_b
```

Two directories with 1 matching file, 1 different file:

```
python verify_checksums.py test_data/dir_a test_data/dir_c
```
