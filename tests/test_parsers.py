# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2


def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    parser_ex = FastaParser(filename="data/test.fa")
    fasta_sequences = []
    i = 0
    for sequence in parser_ex:
        # not only checks for bad.fa, but also checks for any .fa file that has missing lines/doesn't have sequences.
        assert (sequence[0] != ValueError), f"Line '{i}' had 0 lines."
        assert len(sequence) == 2, f"Line '{i}' is missing sequence name/sequencing"
        fasta_sequences.append(sequence)
        i += 1

    # check that length of fasta_sequences is exactly half the length of original file
    # original file - 2 lines for each sequence (line1: seq0, line2: sequence)
    with open("data/test.fa", "r") as f:
        file_length = len(f.readlines())
    assert len(fasta_sequences) == file_length / 2, "FASTA file is not being read in correctly: differing lengths." 

    seq0 = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    # check that first sequence is read in correctly
    assert fasta_sequences[0][1] == "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA", "Incorrect first sequence read in."

    # check that random sequence in the middle is read correctly
    assert fasta_sequences[55][1] == "TTGTTAATGCGCGATTACCCACAGGATGCACCTCTGACACACCCCCCCCCATCTCCAGGATGAAGTACTTGGCAGGTGGGGTCCAGTAACTTTCCCCCGG", "Incorrect 55th sequence read in."

def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in. If a fastq file is
    read, the first item is None
    """
    parser_ex = FastaParser(filename="data/test.fa")
    fasta_sequences = []
    for sequence in parser_ex:
        fasta_sequences.append(sequence)
        # check that first item read in is None. 
        assert sequence[0] != None, "File read in must be in FASTA format."
        break
    # assert fasta_sequences[0][0] == None

def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    parser_ex = FastqParser(filename="data/test.fq")
    fastq_sequences = []
    i = 0
    for sequence in parser_ex:
        # not only checks for bad.fa, but also checks for any .fq file that has missing lines/doesn't have sequences.
        assert (sequence[0] != ValueError), f"Line '{i}' had 0 lines."
        fastq_sequences.append(sequence)
        i += 1

    # check that length of fastq_sequences is exactly a quarter the length of original file
    # original file - 2 lines for each sequence (line1: seq0, line2: sequence, line3: sequence identifier, line4: quality values for sequence)
    with open("data/test.fq", "r") as f:
        file_length = len(f.readlines())
    assert len(fastq_sequences) == file_length / 4, "FASTQ file is not being read in correctly: differing lengths." 

    seq0 = "TGATTGAATCTTTTGAGGGTCACGGCCCGGAAGCCAGAATTTCGGGGTCCTCTGTGGATATTAATCGAGCCCACACGGTGTGAGTTCAGCGGCCCCCGCA"
    # check that first sequence is read in correctly
    assert fastq_sequences[0][1] == "TGTGGTCGTATAGTTATTGTCATAAATTACACAGAATCGCGATTCTCCGCGTCCACCAATCTTAGTGCACCACAGCATCGACCCGATTTATGACGCTGAG", "Incorrect first sequence read in."

    # check that random sequence in the middle is read correctly
    assert fastq_sequences[55][1] == "AATATGCAAGCCCGAACGGGCGCCCTCGTAAGGGGTGCAGCGCTAATCGCATTCCTAGGCTTTACCCACGCCCAGGTTGCCCACAGCCTGCAGTGATAGT", "Incorrect 55th sequence read in."

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    parser_ex = FastqParser(filename="data/test.fq")
    fastq_sequences = []
    j = 0
    for sequence in parser_ex:
        fastq_sequences.append(sequence)
        # check that first item read in is None. 
        assert sequence[0] != None, "File read in must be in FASTQ format."
        j += 1
    


