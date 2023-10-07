from Modules.filter_fastq import run_filter_fastq
from Modules.dna_rna_tools import run_dna_rna_tools
from Modules.aminoacids_tools import run_aminoacid_tools

def run_BioSeqTools(tool_name, *args):
    if tool_name == "run_aminoacid_tools":
        if len(args) < 2:
            raise ValueError("Not enough arguments for run_aminoacid_tools")
        return run_aminoacid_tools(*args[:-1], operation=args[-1])
    elif tool_name == "run_dna_rna_tools":
        return run_dna_rna_tools(*args)
    elif tool_name == "run_filter_fastq":
        return run_filter_fastq(*args)
    else:
        raise ValueError("Invalid tool_name")
