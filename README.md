# checksum

A program that takes as input two paths (directory or file) and:

- matches files by name,

- compares MD5 checksum for each pair of files

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
%python verify_checksums.py "test_data/dir_a" "test_data/dir_b"
Comparing 2 file pair(s)...
+-------+-----------------+------------+
| index |    directory    |    name    |
+-------+-----------------+------------+
|   0   | test_data/dir_a | file_a.txt |
|   0   | test_data/dir_b | file_a.txt |
|       |                 |            |
|   1   | test_data/dir_a | file_b.txt |
|   1   | test_data/dir_b | file_b.txt |
+-------+-----------------+------------+
computing checksums...: 100%|██████████████| 4/4 [00:00<00:00, 9592.46it/s]
all file pair checksums match

```

Two directories with 1 matching file pair, and 2 different file pairs:

```
% python verify_checksums.py "./test_data/dir_a" "./test_data/dir_d"
Comparing 3 file pair(s)...
+-------+-----------------+------------+
| index |    directory    |    name    |
+-------+-----------------+------------+
|   0   | test_data/dir_a | file_a.txt |
|   0   | test_data/dir_d | file_a.txt |
|       |                 |            |
|   1   | test_data/dir_a | file_b.txt |
|   1   | test_data/dir_d | file_b.txt |
|       |                 |            |
|   2   | test_data/dir_a | file_c.txt |
|   2   | test_data/dir_d | file_c.txt |
+-------+-----------------+------------+
computing checksums...: 100%|███████████| 6/6 [00:00<00:00, 16448.25it/s]
Found 2 file pair(s) with mismatched checksums...
+-------+-----------------+------------+----------------------------------+
| index |    directory    |    name    |           md5_checksum           |
+-------+-----------------+------------+----------------------------------+
|   0   | test_data/dir_a | file_a.txt | 0cc175b9c0f1b6a831c399e269772661 |
|   0   | test_data/dir_d | file_a.txt | 00e436c5a03970a560ec86b239f15098 |
|       |                 |            |                                  |
|   2   | test_data/dir_a | file_c.txt | 4a8a08f09d37b73795649038408b5f33 |
|   2   | test_data/dir_d | file_c.txt | df5591d19e584590bbd831740178a493 |
+-------+-----------------+------------+----------------------------------+
```
