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
```
### Input
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

## Example 

Import the necessary modules:
```python
from BioSeqTools import run_BioSeqTools
from Modules.filter_fastq import run_filter_fastq
from Modules.dna_rna_tools import run_dna_rna_tools
from Modules.aminoacids_tools import run_aminoacid_tools
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

## Project Structure
- BioSeqTools.py - The main script containing functions for working with biological sequences.
- BioSeqTools/Modules - A directory containing additional modules and functions for various sequence types.

## Author

Author: `Chernikov Danila`, the student of Bioinformatics institute.
Contact: `danila.chernikov.02@bk.ru`, `damareven@gmail.com`
