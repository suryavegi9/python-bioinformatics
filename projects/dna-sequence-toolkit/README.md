 # 🧬 DNA Sequence Toolkit

A lightweight Python toolkit for performing fundamental DNA sequence analysis from FASTA files.

**Version 1.0**

## 🔬 Overview

DNA Sequence Toolkit is a Python-based bioinformatics project for reading and analyzing DNA sequences.

The toolkit accepts DNA sequence data in **FASTA format**, validates the sequence, calculates basic sequence statistics, and supports motif searching.

The project was built to apply core Python programming concepts to biological sequence analysis while following good practices such as modular functions, input validation, automated testing, and version control.

## ✨ Features

The current version supports:

* ✅ FASTA file parsing
* ✅ DNA sequence validation
* ✅ Uppercase and lowercase sequence handling
* ✅ Sequence length calculation
* ✅ A/T/G/C nucleotide counting
* ✅ GC content calculation
* ✅ DNA motif searching
* ✅ Invalid sequence detection
* ✅ Empty-sequence handling
* ✅ Automated testing with `pytest`

## 🧬 Analysis Workflow

```text
FASTA File
    ↓
Read Sequence
    ↓
Validate DNA
    ↓
Calculate Sequence Length
    ↓
Count A / T / G / C
    ↓
Calculate GC Content
    ↓
Search for Motif
    ↓
Display Results
```

## 📂 Project Structure

```text
dna-sequence-toolkit/
│
├── data/
│   └── example.fasta
│
├── tests/
│   └── test_dna_analyzer.py
│
├── dna_analyzer.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 📥 Example FASTA Input

```text
>example_sequence
ATGCGTACGTAGCTAGCTAG
```

The FASTA header and DNA sequence are extracted automatically by the parser.

## 💻 Usage

### 1. Install the required dependency

```bash
pip install -r requirements.txt
```

### 2. Run the analyzer

From inside the `dna-sequence-toolkit` directory:

```bash
python dna_analyzer.py
```

The program reads the sequence from:

```text
data/example.fasta
```

and performs the analysis.

### 3. Enter a motif

When prompted:

```text
Enter a motif to search for:
```

enter a DNA motif such as:

```text
CGT
```

## 📊 Example Output

```text
FASTA Header: example_sequence
DNA Sequence: ATGCGTACGTAGCTAGCTAG
Sequence Length: 20
A: 4
T: 5
G: 6
C: 5
GC Content: 55.0 %
Enter a motif to search for: CGT
Motif: CGT
Motif Positions: [3, 7]
```

> Motif positions use Python's zero-based indexing.

## 🧪 Automated Testing

The project uses **pytest** to test the core sequence-analysis functions.

The test suite currently covers:

* DNA sequence validation
* Sequence length calculation
* Nucleotide counting
* GC content calculation
* Motif searching
* FASTA parsing

Run the complete test suite with:

```bash
python -m pytest
```

Current test status:

```text
6 passed
```

## 🧠 Python & Bioinformatics Concepts Applied

### Python

* Functions
* Strings and string methods
* Dictionaries
* Sets
* Conditional statements
* Loops
* File handling
* List operations
* Docstrings
* Modular program design

### Bioinformatics

* FASTA sequence representation
* DNA sequence validation
* Nucleotide composition
* GC content
* Sequence motifs
* Biological sequence parsing

## 🚀 Future Improvements

Potential future extensions include:

* [ ] Reverse complement generation
* [ ] DNA → RNA transcription
* [ ] RNA → protein translation
* [ ] Support for multiple FASTA records
* [ ] Command-line arguments
* [ ] Additional biological sequence statistics

These features are intentionally left for future versions while **v1.0 focuses on reliable fundamental DNA sequence analysis**.

## 👨‍💻 Author

**Surya Varaprasad**

Biotechnology Undergraduate | Aspiring Bioinformatician

## 📄 License

This project is part of the `python-bioinformatics` repository, which is distributed under the MIT License.


 