# write tests for transcribe functions
import pytest
from seqparser import (
        transcribe,
        reverse_transcribe)


def test_freebie_transcribe_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True


def test_freebie_transcribe_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

def test_transcribe_len_formatting():
    # ensure that transcribe can only take in sequences with length non-zero. 
    with pytest.raises(AssertionError):
        transcribe("")
    
    # transcribe() returns Value Error with FASTA sequence that has spaces in it
    with pytest.raises(ValueError):
        transcribe("AGTCGGA ")

def test_transcribe():
    """
    Write your unit test for the transcribe function here.
    """
    # transcribe() works with sequences of length 1. 
    assert (transcribe("A") == "U") 

    # transcribe() returns Value Error with non-DNA nucleotides. 
    with pytest.raises(ValueError):
        transcribe("AGUGCGU")

    # example test case
    test_sequence = "ACTGAACCC"
    assert (transcribe(test_sequence) == "UGACUUGGG")

def test_reverse_transcribe():
    """
    Write your unit test for the reverse transcribe function here.
    """
    assert (reverse_transcribe("A") == "U") 

    with pytest.raises(ValueError):
        reverse_transcribe("AGUGCGU")
    
    assert (reverse_transcribe("ACTGAACCC") == "GGGUUCAGU")
    print("All test cases passed!") 
    
