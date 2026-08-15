from dna_analyzer import (
    validate_sequence,
    calculate_length,
    count_nucleotides,
    calculate_gc_content,
    find_motif,
    read_fasta,)




def test_validate_sequence():
    assert validate_sequence("ATGC") is True
    assert validate_sequence("ATGCXYZ") is False
    assert validate_sequence("") is False


def test_calculate_length():
    assert calculate_length("ATGC") == 4
    assert calculate_length("") == 0


def test_count_nucleotides():
    result = count_nucleotides("ATGCATGC")

    assert result["A"] == 2
    assert result["T"] == 2
    assert result["G"] == 2
    assert result["C"] == 2


def test_calculate_gc_content():
    assert calculate_gc_content("ATGC") == 50.0
    assert calculate_gc_content("GGGGCCCC") == 100.0
    assert calculate_gc_content("AAAAATTTTT") == 0.0
    assert calculate_gc_content("") == 0.0

def test_find_motif():
    assert find_motif("ATGCATGC", "ATG") == [0, 4]
    assert find_motif("ATGCATGC", "TGC") == [1, 5]
    assert find_motif("ATGCATGC", "XYZ") == []

def test_read_fasta():
    header, sequence = read_fasta("data/example.fasta")
    assert header == "example_sequence"
    assert sequence ==  "ATGCGCTAGCTGACTGACTAGCTAGCGTACGTACGTAACGTGAC"
