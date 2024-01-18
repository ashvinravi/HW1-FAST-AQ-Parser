from seqparser import (
        FastaParser,
        FastqParser,
        transcribe,
        reverse_transcribe)

def main():
    """
    The main function
    """
    # Create instance of FastaParser
    # Create instance of FastqParser
    parser_fa = FastaParser("data/test.fa")
    parser_fq = FastqParser("data/test.fq")

    # For each record of FastaParser, Transcribe the sequence
    # and print it to console
    for sequence in parser_fa:
        transcribed_seq = transcribe(sequence[1])
        print(sequence[0], transcribed_seq)

    # For each record of FastqParser, Transcribe the sequence
    # and print it to console
    for sequence in parser_fq:
        transcribed_seq = transcribe(sequence[1])
        print(sequence[0], transcribed_seq)

    # For each record of FastaParser, Reverse Transcribe the sequence
    # and print it to console
    for sequence in parser_fa:
        reverse_transcribed_seq = reverse_transcribe(sequence[1])
        print(sequence[0], reverse_transcribed_seq)
       
    # For each record of FastqParser, Reverse Transcribe the sequence
    # and print it to console
    for sequence in parser_fq:
        reverse_transcribed_seq = reverse_transcribe(sequence[1])
        print(sequence[0], reverse_transcribed_seq)


"""
When executing a python script from the command line there will
always be a hidden variable `__name__` set to the value `__main__`.

Since this is guaranteed you can execute your `main` function with
the following if statement
"""
if __name__ == "__main__":
    main()
