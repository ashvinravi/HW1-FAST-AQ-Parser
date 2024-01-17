# DNA -> RNA Transcription
from typing import Union

TRANSCRIPTION_MAPPING = {"A": "U", "C": "G", "T": "A", "G": "C"}
ALLOWED_NUC = TRANSCRIPTION_MAPPING.keys()

def transcribe(seq: str, reverse: bool = False) -> str:
    """
    Write a function that will transcribe (replace DNA sequence to RNA
    by replacing all 'T' to 'U') in an input sequence
    """

    assert (len(seq) > 0), "Sequence length must be greater than 0."

    transcribed_seq = ""

    for nucleotide in seq:
        transcribed_nuc = ""
        for k,v in TRANSCRIPTION_MAPPING.items():
            # transcribe DNA to RNA nucleotide by nucleotide
            if nucleotide == k:
                transcribed_nuc = v
            # if nucleotide does not match any of the allowed nucleotides throw error
        if transcribed_nuc == "":
            raise ValueError("Sequence contains non-DNA nucleotides and cannot be transcribed.")
        # Append transcribed nucleotide to new sequence
        transcribed_seq += transcribed_nuc
    return transcribed_seq
    

def reverse_transcribe(seq: str) -> str:
    """
    Write a function that will transcribe an input sequence and reverse
    the sequence
    """
    assert (len(seq) > 0), "Sequence length must be greater than 0."

    transcribed_seq = ""
    for nucleotide in seq:
        transcribed_nuc = ""
        for k,v in TRANSCRIPTION_MAPPING.items():
            # transcribe DNA to RNA nucleotide by nucleotide
            if nucleotide == k:
                transcribed_nuc = v
            # if nucleotide does not match any of the allowed nucleotides throw error
        if transcribed_nuc == "":
            raise ValueError("Sequence contains non-DNA nucleotides and cannot be transcribed.")
        # Append transcribed nucleotide to new sequence
        transcribed_seq = transcribed_nuc + transcribed_seq
    return transcribed_seq
    

