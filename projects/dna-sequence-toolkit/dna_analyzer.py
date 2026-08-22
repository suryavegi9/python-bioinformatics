 # DNA Sequence Analyzer
# Version 5: reusable functions for DNA sequence analysis


def validate_sequence(sequence):
    """Check whether a sequence contains only valid DNA bases."""
    valid_bases = set("ATGC")
    return len(sequence) > 0 and set(sequence.upper()).issubset(valid_bases)


def calculate_length(sequence):
    """Return the length of a DNA sequence."""
    return len(sequence)


def count_nucleotides(sequence):
    """Return the count of each DNA nucleotide."""
    sequence = sequence.upper()

    return {
        "A": sequence.count("A"),
        "T": sequence.count("T"),
        "G": sequence.count("G"),
        "C": sequence.count("C")
    }


def calculate_gc_content(sequence):
    """Calculate the GC content of a DNA sequence."""
    sequence = sequence.upper()
    if len(sequence) == 0:
        return 0.0

    gc_count = sequence.count("G") + sequence.count("C")

    return (gc_count / len(sequence)) * 100

def find_motif(sequence, motif):
    """Find all occurrences of a motif in a DNA sequence."""
    sequence = sequence.upper()
    motif = motif.upper()
    positions = []
    for i in range(len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)] == motif:
            positions.append(i )

    return positions
def read_fasta(file_path):
    """Read a FASTA file and return its sequence and header."""
    header = ""
    sequence_parts = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                header = line[1:]  # Remove the '>' character
            elif line:
                sequence_parts.append(line)

    sequence = "".join(sequence_parts)
    return header, sequence


# Example DNA sequence
def main():
    fasta_file =  "data/example.fasta"
    header, sequence = read_fasta(fasta_file)
    if validate_sequence(sequence):
        print("FASTA Header:", header)
        print("FASTA Sequence:", sequence)

        print("Sequence is valid DNA.")

        print("DNA Sequence:", sequence)
        print("Sequence Length:", calculate_length(sequence))

        nucleotide_counts = count_nucleotides(sequence)

        print("A:", nucleotide_counts["A"])
        print("T:", nucleotide_counts["T"])
        print("G:", nucleotide_counts["G"])
        print("C:", nucleotide_counts["C"])

        print("GC Content:", calculate_gc_content(sequence), "%")
        motif = input("Enter a motif to search for: ")
        positions = find_motif(sequence, motif)
        print("motif:", motif)
        print("Motif positions:", positions)

    else:
        print("Invalid DNA sequence. Please ensure it contains only A, T, G, and C.")
if __name__ == "__main__":
    main()
