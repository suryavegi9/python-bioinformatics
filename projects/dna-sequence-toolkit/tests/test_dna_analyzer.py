from dna_analyzer import (
    validate_sequence,
    calculate_length,
    count_nucleotides,
    calculate_gc_content
)


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