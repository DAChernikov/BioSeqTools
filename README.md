# BioSeqTools

BioSeqTools is a versatile bioinformatics toolkit designed to manipulate and analyze biological sequences, including DNA, RNA, and fastq sequences.

## Overview

BioSeqTools offers a set of powerful utilities to assist with various bioinformatics tasks. It provides functions to filter and analyze sequences based on different criteria, helping researchers and bioinformaticians in their daily work.

## Installation

To install BioSeqTools, you can clone this repository to your local machine:

```bash
git clone https://github.com/yourusername/BioSeqTools.git
```

Then, navigate to the BioSeqTools directory and open BioSeqTools.py:

```bash
cd BioSeqTools
open BioSeqTools.py
```

Or you can just `download BioSeqTools.py file and Modules folder to your .py-project directory`

## Usage
To use BioSeqTools simply import `run_aminoacid_tools` into your `*.py` script as shown below:

```python
from BioSeqTools import run_BioSeqTools
```

Also you need to import additional libraries for correct tool work 

```python
from Modules.filter_fastq import run_filter_fastq
from Modules.dna_rna_tools import run_dna_rna_tools
from Modules.aminoacids_tools import run_aminoacid_tools
from filter_fastq_files import run_filter_fastq
from bio_files_processor import select_genes_from_gbk_to_fasta, \
    change_fasta_start_pos, \
    convert_multiline_fasta_to_oneline, \
    parse_blast_output
```
### Input - BioSeqTools (function do not process files, to work with files - read the 'File processing' below
The program has some required input parameters - `run_BioSeqTools(tool_name, *args)`:
* (`str` type) Name of the instrument to be executed, keyword argument.
* (`str` or `int` type) Arguments for the instrument (number of arguments are different for each type of instrument, check the information below), keyword argument.

You can choose one of three tools you need to execute in `tool_name` argument:
#### 'run_dna_rna_tools'
If you want to execute dna_rna_tools for your sequence, your code must be like:
`run_BioSeqTools('run_dna_rna_tools', *sequencies, operation)`, where:
- `*sequencies` - list (or string, if you got only one sequence) of sequencies
- `operation` - operation, that you want to perform for your sequence (or sequencies)

Operations in `run_dna_rna_tools`:
* `transcribe` - operation, that transcribes the input sequencies of DNA to RNA or RNA to DNA sequencies, like GCGTA -> CGCTU
* `reverse` - operation, that "flip" the sequence, like ACGT -> TGCA
* `complement` - operation, that create the complement sequence from input one, like AUGC -> UACG
* `reverse_complement` - operation that combines `reverse` and `compliment` operations. Example: AUGC -> GCAU

#### 'run_aminoacid_tools'
If you want to execute aminoacid_tools for your sequence, your code must be like:
`run_BioSeqTools('run_aminoacid_tools', *seqs, operation)`, where:
- `*sequencies` - list (or string, if you got only one sequence) of sequencies
- `operation` - operation, that you want to perform for your sequence (or sequencies)

Operations in `run_aminoacid_tools`:
* `calculate_percentage` - operation, that calculates the percentage of amino acids in the entered amino acid sequence
* `calculate_molecular_weight` - operation, that calculates the molecular weight of entered amino acid sequence
* `calculate_hydrophobicity_eisenberg` - operation, that determine hydrophilicity/hydrophobicity of sequence by Eisenberg scale of hydrophilicity/hydrophobicity
* `calculate_pI` - operation that calculates the Isoelectric point for the sequence
* `find_cleavage_sites` - operation that finds cleavage sites for motif-specific proteases

:exclamation: The amino acid sequence must be written in single-letter form and in uppercase.

#### 'run_filter_fastq'
This instrument contains more specific arguments than previous ones.
The filter_fastq instrument is designed to filter and process data in the FASTQ format (in python it`s just a dictionary), which is commonly used in bioinformatics for storing sequence information. The FASTQ format contains information about DNA, RNA, or protein sequences, as well as the quality of each nucleotide or amino acid in the sequence.

Here is the example of the instrument work input:
`run_BioSeqTools('run_filter_fastq', dictionary_of_seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0)` 

or

`run_BioSeqTools('run_filter_fastq', dictionary_of_seqs, (10, 30), (0, 2**32), 0)` # Without names of parameteres

##### Description of how the filter_fastq function works
For correct function work there is need to input the following arguments (in correct way):
- sequencies - a dictionary containing FASTQ sequences. The keys in the dictionary represent sequence names, and the values are tuples containing the sequence and quality.
- gc_bounds - the GC content interval in percentages for filtering. It can be specified as a single number or a tuple representing the lower and upper bounds. Sequences that meet this criterion are retained.
- length_bounds - the length interval for filtering, similar to gc_bounds. It defines the allowable range of sequence lengths.
- quality_threshold - the threshold value for average quality filtering. Reads with an average quality below this threshold are discarded.

The function iterates through all sequences in the seqs dictionary and applies filters based on the specified parameters.
Sequences that pass all the filters (GC content, length, quality) are saved in a new dictionary.
That new dictionary containing only the filtered sequences is returned as the result of the function.

:exclamation: You must use one of predefined tools and their operation names described in the "Input" section .

### Output
A string or dictionary with details of performed operation.


## File processing 

### run_filter_fastq (file processing)
The `run_filter_fastq` function is designed to filter and process data in the FASTQ format, which is commonly used in bioinformatics for storing sequence information. This function accepts several parameters to customize the filtering process and save the filtered data. Here's a breakdown of its functionality:

- **Parameters**:
   - `input_path`: The path to the input FASTQ file to be processed.
   - `gc_bounds`: A tuple specifying the range of GC content in percentages for filtering. Sequences outside this range will be filtered out.
   - `length_bounds`: A tuple specifying the range of sequence lengths for filtering.
   - `quality_threshold`: A threshold value for average quality. Sequences with an average quality below this threshold will be filtered out.
   - `output_filename`: The name of the output FASTQ file where the filtered sequences will be saved. If not provided, a default filename, "filtered_output.fastq," will be used.

- **Functionality**:
   1. The function reads the input FASTQ file specified by `input_path` and parses it, storing the sequences and their associated quality scores in a dictionary.
   2. It then iterates through the sequences, calculating the GC content and average quality for each sequence.
   3. Sequences are filtered based on the following criteria:
      - GC content must fall within the specified `gc_bounds` range.
      - Sequence length must be within the `length_bounds` range.
      - The average quality must be equal to or greater than the `quality_threshold`.
   4. Filtered sequences are stored in a new dictionary called `filtered_seqs`.
   5. The function saves the filtered sequences to an output FASTQ file, using the specified `output_filename` or the default "filtered_output.fastq."

In summary, the `run_filter_fastq` function provides a flexible way to filter FASTQ sequences based on user-defined criteria, making it a valuable tool for bioinformatics data processing.

### convert_multiline_fasta_to_oneline
The `convert_multiline_fasta_to_oneline` function is designed to convert a multiline FASTA file into a one-line FASTA format. Here's a description of its functionality:

Parameters:
* `input_fasta`: The path to the input multiline FASTA file to be processed.
* `output_fasta`: The name of the output one-line FASTA file. If not provided, a default filename, created by adding ".fasta" to the input filename, will be used.
Functionality:
The function reads the input multiline FASTA file specified by input_fasta.
It parses the input file and stores the sequence data in a dictionary, where the keys represent the sequence IDs (from the FASTA headers), and the values store the corresponding sequences as a single line.
The sequences are processed, removing line breaks and creating a single-line sequence.
The function saves the processed sequences into an output one-line FASTA file specified by output_fasta.
* If `output_fasta` is not provided, the function creates a default output filename by adding ".fasta" to the input filename.
A message is printed to confirm that the converted data has been saved as the output file.

### change_fasta_start_pos
The `change_fasta_start_pos` function is designed to modify the start position of a DNA or protein sequence in FASTA format by shifting the sequence. Here's a description of its functionality:

Parameters:
* `input_fasta`: The path to the input FASTA file that contains the sequence you want to modify.
* `shift`: An integer representing the number of positions to shift the sequence. A positive value shifts the sequence to the right (i.e., in the 3' to 5' direction), while a negative value shifts the sequence to the left (i.e., in the 5' to 3' direction).
* `output_fasta`: The name of the output FASTA file where the modified sequence will be saved.
Functionality:
The function reads the content of the input FASTA file specified by input_fasta.
It checks whether the input FASTA file is in a valid format. Specifically, it verifies that the file contains exactly two lines and that the first line starts with a '>' character, indicating a header line.
If the input FASTA format is invalid, the function prints an error message, "Invalid input FASTA format," and returns without making any modifications.

If the input format is valid, the function proceeds to modify the sequence as follows:
- If `shift` is a positive integer, the function shifts the sequence to the right by shift positions. It wraps the shifted portion around to the start of the sequence.
- If `shift` is a negative integer, the function shifts the sequence to the left by the absolute value of shift positions.
The modified sequence is written to the output FASTA file specified by `output_fasta`. The header from the input file is preserved.

A message is printed to confirm that the FASTA file with the shifted start position has been saved to `output_fasta`.

### parse_blast_output
The `parse_blast_output` function is used to parse and process the output from a BLAST (Basic Local Alignment Search Tool) result file. Here's a description of what this code does:

Parameters:
* `input_file`: The path to the input BLAST result file that contains the data you want to parse.
* `output_file`: (Optional) The name of the output file where the parsed data will be saved. If not provided, the function will not create an output file.
Functionality:
The function opens and reads the content of the input BLAST result file specified by input_file.
It initializes an empty dictionary called query_results to store the parsed data. This dictionary will map query IDs to a list of descriptions.
The function iterates through the lines in the input file:
- If a line starts with "Query #", it is considered the start of a new query, and the query ID is extracted. The query ID is obtained by splitting the line on "Query ID:" and taking the part before "Length:". A new list is created in the query_results dictionary to store the descriptions for this query.
- If a line starts with "Description", it is considered a description of the query, and the description is extracted and appended to the list of descriptions for the current query.
- If an `output_file` is provided, the function opens and writes the parsed data to that file. The output file contains lines in the format: "query_id description", where the query IDs are sorted, and multiple descriptions for each query are listed.

The function prints the message "Blast results parsed" to indicate that the parsing is complete.

## Example 

Import the necessary modules:
```python
from BioSeqTools import run_BioSeqTools
from Modules.filter_fastq import run_filter_fastq
from Modules.dna_rna_tools import run_dna_rna_tools
from Modules.aminoacids_tools import run_aminoacid_tools
from filter_fastq_files import run_filter_fastq
from bio_files_processor import select_genes_from_gbk_to_fasta, \
    change_fasta_start_pos, \
    convert_multiline_fasta_to_oneline, \
    parse_blast_output
```

##### Examples of instrument work
- `dna_rna_tools`:
```python
# Input
print(run_BioSeqTools('run_dna_rna_tools', 'AUGC', 'reverse_complement'))
```
```python
# output
GCUT
```

- `aminoacid_tools`
```python
# Input
print(run_BioSeqTools('run_aminoacid_tools', 'ADMGC', 'calculate_pI'))
```
```python
# output
Isoelectric point for the sequence ADMGC: 6.3675
```

- `filter_fastq`
```python
# Input

# 1 - Example_fastq_dictionary
EXAMPLE_FASTQ = {
    # 'name' : ('sequence', 'quality')
    '@SRX079804:1:SRR292678:1:1101:21885:21885': ('ACAGCAACATAAACATGATGGGATGGCGTAAGCCCCCGAGATATCAGTTTACCCAGGATAAGAGATTAAATTATGAGCAACATTATTAA', 'FGGGFGGGFGGGFGDFGCEBB@CCDFDDFFFFBFFGFGEFDFFFF;D@DD>C@DDGGGDFGDGG?GFGFEGFGGEF@FDGGGFGFBGGD'),
    '@SRX079804:1:SRR292678:1:1101:24563:24563': ('ATTAGCGAGGAGGAGTGCTGAGAAGATGTCGCCTACGCCGTTGAAATTCCCTTCAATCAGGGGGTACTGGAGGATACGAGTTTGTGTG', 'BFFFFFFFB@B@A<@D>BDDACDDDEBEDEFFFBFFFEFFDFFF=CC@DDFD8FFFFFFF8/+.2,@7<<:?B/:<><-><@.A*C>D'),
    '@SRX079804:1:SRR292678:1:1101:30161:30161': ('GAACGACAGCAGCTCCTGCATAACCGCGTCCTTCTTCTTTAGCGTTGTGCAAAGCATGTTTTGTATTACGGGCATCTCGAGCGAATC', 'DFFFEGDGGGGFGGEDCCDCEFFFFCCCCCB>CEBFGFBGGG?DE=:6@=>A<A>D?D8DCEE:>EEABE5D@5:DDCA;EEE-DCD'),
    '@SRX079804:1:SRR292678:1:1101:47176:47176': ('TGAAGCGTCGATAGAAGTTAGCAAACCCGCGGAACTTCCGTACATCAGACACATTCCGGGGGGTGGGCCAATCCATGATGCCTTTG', 'FF@FFBEEEEFFEFFD@EDEFFB=DFEEFFFE8FFE8EEDBFDFEEBE+E<C<C@FFFFF;;338<??D:@=DD:8DDDD@EE?EB'),
    '@SRX079804:1:SRR292678:1:1101:149302:149302': ('TAGGGTTGTATTTGCAGATCCATGGCATGCCAAAAAGAACATCGTCCCGTCCAATATCTGCAACATACCAGTTGGTTGGTA', '@;CBA=:@;@DBDCDEEE/EEEEEEF@>FBEEB=EFA>EEBD=DAEEEEB9)99>B99BC)@,@<9CDD=C,5;B::?@;A'),
    '@SRX079804:1:SRR292678:1:1101:170868:170868': ('CTGCCGAGACTGTTCTCAGACATGGAAAGCTCGATTCGCATACACTCGCTGAGTAAGAGAGTCACACCAAATCACAGATT', 'E;FFFEGFGIGGFBG;C6D<@C7CDGFEFGFHDFEHHHBBHHFDFEFBAEEEEDE@A2=DA:??C3<BCA7@DCDEG*EB'),
    '@SRX079804:1:SRR292678:1:1101:171075:171075': ('CATTATAGTAATACGGAAGATGACTTGCTGTTATCATTACAGCTCCATCGCATGAATAATTCTCTAATATAGTTGTCAT', 'HGHHHHGFHHHHFHHEHHHHFGEHFGFGGGHHEEGHHEEHBHHFGDDECEGGGEFGF<FGGIIGEBGDFFFGFFGGFGF'),
    '@SRX079804:1:SRR292678:1:1101:175500:175500': ('GACGCCGTGGCTGCACTATTTGAGGCACCTGTCCTCGAAGGGAAGTTCATCTCGACGCGTGTCACTATGACATGAATG', 'GGGGGFFCFEEEFFDGFBGGGA5DG@5DDCBDDE=GFADDFF5BE49<<<BDD?CE<A<8:59;@C.C9CECBAC=DE'),
    '@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE'),
    '@SRX079804:1:SRR292678:1:1101:190845:190845': ('CCTCAGCGTGGATTGCCGCTCATGCAGGAGCAGATAATCCCTTCGCCATCCCATTAAGCGCCGTTGTCGGTATTCC', 'FF@FFCFEECEBEC@@BBBBDFBBFFDFFEFFEB8FFFFFFFFEFCEB/>BBA@AFFFEEEEECE;ACD@DBBEEE'),
    '@SRX079804:1:SRR292678:1:1101:198993:198993': ('AGTTATTTATGCATCATTCTCATGTATGAGCCAACAAGATAGTACAAGTTTTATTGCTATGAGTTCAGTACAACA', '<<<=;@B??@<>@><48876EADEG6B<A@*;398@.=BB<7:>.BB@.?+98204<:<>@?A=@EFEFFFEEFB'),
    '@SRX079804:1:SRR292678:1:1101:204480:204480': ('AGTGAGACACCCCTGAACATTCCTAGTAAGACATCTTTGAATATTACTAGTTAGCCACACTTTAAAATGACCCG', '<98;<@@@:@CD@BCCDD=DBBCEBBAAA@9???@BCDBCGF=GEGDFGDBEEEEEFFFF=EDEE=DCD@@BBC')
    }

# 2 - tool work
print(run_BioSeqTools('run_filter_fastq', EXAMPLE_FASTQ, (10, 30), (0, 2**32), 0))
```
```python
# output - in this example there must be the return of dictionary with one key and two values
{'@SRX079804:1:SRR292678:1:1101:190136:190136': ('GAACCTTCTTTAATTTATCTAGAGCCCAAATTTTAGTCAATCTATCAACTAAAATACCTACTGCTACTACAAGTATT', 'DACD@BEECEDE.BEDDDDD,>:@>EEBEEHEFEHHFFHH?FGBGFBBD77B;;C?FFFFGGFED.BBABBG@DBBE')}
```

#### Examples of file-processing work

* `run_filter_fastq`

Input:
```python
run_filter_fastq('input.fastq', gc_bounds=(40, 60), quality_threshold=30, output_filename='filtered_output.fastq')
```
Out - creates `filtered_output.fastq` file in working directory (optionable)

* `convert_multiline_fasta_to_oneline`

Input:
```python
input_fasta_file = 'input.fasta'
output_fasta_file = 'output.fasta'
convert_multiline_fasta_to_oneline(input_fasta_file, output_fasta_file)
```
Out - creates `output.fasta` file in working directory (optionable)

* `select_genes_from_gbk_to_fasta`

Input:
```python
input_gbk_file = 'input.gbk'
genes_of_interest = ['gene1', 'gene2']  # chose the interest one's
select_genes_from_gbk_to_fasta(input_gbk_file, genes_of_interest)
```
Out - creates `output.fasta` file in working directory (optionable)

* `change_fasta_start_pos`

Input:
```python
input_fasta_file = 'input.fasta'
shift_amount = 2  # change the preffered shift amount
output_fasta_file = 'output.fasta'
change_fasta_start_pos(input_fasta_file, shift_amount, output_fasta_file)
```
Out - creates `output.fasta` file in working directory (optionable)

* `parse_blast_output`

Input:
```python
blast_input_file = 'blast_results.txt'
output_results_file = 'parsed_blast_results.txt'  # name can be changed
parse_blast_output(blast_input_file, parsed_blast_results.txt)
```
Out - creates `parsed_blast_results.txt` file in working directory (optionable)


## Project Structure
- BioSeqTools.py - The main script containing functions for working with biological sequences.
- BioSeqTools/Modules - A directory containing additional modules and functions for various sequence types.
- filter_fastq_files.py - A module for reading and filtering FASTQ files.
- bio_files_processor.py - A module for processing biological sequence data.

## Author

Author: `Chernikov Danila`, the student of Bioinformatics institute.
Contact: `danila.chernikov.02@bk.ru`, `damareven@gmail.com`
