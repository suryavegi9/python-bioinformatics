# 🧬 DNA Sequence Toolkit

A Python-based toolkit for performing fundamental DNA sequence analysis.

## 📌 Project Status

🚧 **In Development**

This project is being developed incrementally while learning Python and applying programming concepts to bioinformatics.

## 🎯 Objectives

The toolkit aims to provide basic functionality for:

- DNA sequence validation
- Sequence length calculation
- Nucleotide composition analysis
- GC content calculation
- Motif searching
- Reverse complement generation
- DNA → RNA transcription
- RNA → protein translation

## 🛠️ Current Features

The current version supports:

- ✅ DNA sequence validation
- ✅ Uppercase and lowercase DNA input
- ✅ Sequence length calculation
- ✅ A/T/G/C nucleotide counting
- ✅ GC content calculation
- ✅ Empty-sequence handling

## 💻 Usage

Run the analyzer from the repository root:

```bash
python projects/dna-sequence-toolkit/dna_analyzer.py
```

### Example Input

```text
ATGCGTACGTAGCTAGCTAG
```

### Example Output

```text
Sequence is valid DNA.
DNA Sequence: ATGCGTACGTAGCTAGCTAG
Sequence Length: 20
A: 5
T: 5
G: 5
C: 5
GC Content: 50.0 %
```

## 🧪 Validation

The analyzer checks whether a sequence contains only valid DNA bases:

```text
A — Adenine
T — Thymine
G — Guanine
C — Cytosine
```

Invalid sequences are rejected rather than analyzed.

The program also handles edge cases such as:

- Empty sequences
- Lowercase input
- Invalid nucleotide characters

## 📂 Project Structure

```text
dna-sequence-toolkit/
│
├── README.md
└── dna_analyzer.py
```

## 🧠 Concepts Practiced

This project currently applies:

- Python strings
- String methods
- `len()`
- Dictionaries
- Sets
- Conditional statements
- Functions
- Return values
- Docstrings
- Basic error and edge-case handling

## 🚀 Planned Improvements

Future versions will introduce:

- [ ] Motif searching
- [ ] Reverse complement
- [ ] DNA → RNA transcription
- [ ] RNA → protein translation
- [ ] FASTA file input
- [ ] Command-line arguments
- [ ] Automated tests
- [ ] Improved error handling
- [ ] Biological datasets for testing

## 📈 Development Philosophy

The toolkit is being developed incrementally:

```text
Learn Python
     ↓
Apply the concept
     ↓
Test the implementation
     ↓
Identify edge cases
     ↓
Improve the code
     ↓
Document the change
```

## 👨‍💻 Author

**Surya Varaprasad**

Biotechnology Undergraduate | Aspiring Bioinformatician

## 📄 License

This project is licensed under the MIT License.