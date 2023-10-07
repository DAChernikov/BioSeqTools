from typing import Dict


def calculate_percentage(seq: str) -> str:
    """
    Calculates the percentage of amino acids in the entered amino acid 
sequence
    Arguments:
        - seq (str): amino acid sequences to be analyzed
    Return:
        - str: a string with the percentage of each amino acid
    """
    amino_acid_counts: Dict[str, int] = {}  # dict to store count of each amino acid
    for amino_acid in seq:
        if amino_acid in amino_acid_counts:
            amino_acid_counts[amino_acid] += 1
        else:
            amino_acid_counts[amino_acid] = 1
    total_amino_acids = len(seq)
    amino_acid_percentages = {}  # dict to store each amino acid and its %
    for amino_acid, count in amino_acid_counts.items():
        percentage = round(((count / total_amino_acids) * 100), 2)
        amino_acid_percentages[amino_acid] = percentage
    return f'Amino acids percentage of the sequence {seq}: {amino_acid_percentages}'


def calculate_molecular_weight(seq: str) -> str:
    """
    Calculates the molecular weight of entered amino acid sequence
    Arguments:
        - seq (str): amino acid sequences to be analyzed
    Return:
        - str: a string with the molecular weight value for amino acid 
sequence
    """
    amino_acid_weights = {
        'G': 57.051, 'A': 71.078, 'S': 87.077, 'P': 97.115, 'V': 99.131,
        'T': 101.104, 'C': 103.143, 'I': 113.158, 'L': 113.158, 'N': 
114.103,
        'D': 115.087, 'Q': 128.129, 'K': 128.172, 'E': 129.114, 'M': 
131.196,
        'H': 137.139, 'F': 147.174, 'R': 156.186, 'Y': 163.173, 'W': 
186.210
    }
    weight = 18.02  # for the H and OH at the termini
    for amino_acid in seq:
        weight += amino_acid_weights[amino_acid]
    return f'Molecular weight of the sequence {seq}: {round(weight, 2)} Da'


def calculate_hydrophobicity_eisenberg(sequence):

    # Amino acid hydrophilicity/hydrophobicity scale by Eisengerg
    hydrophobicity_values = {
        'A': 0.5, 'R': 0.65, 'N': 1.0, 'D': 1.3, 'C': -0.15,
        'Q': 1.0, 'E': 1.5, 'G': 0.75, 'H': 0.7, 'I': -1.3,
        'L': -1.3, 'K': 0.75, 'M': -1.1, 'F': -1.9, 'P': 0.55,
        'S': 0.6, 'T': 0.3, 'W': -0.5, 'Y': -1.65, 'V': -0.9
    }

    # Calculate sum of hydrophilicities for all amino acids in the sequence
    hydrophobicity_sum = sum(hydrophobicity_values.get(aa, 0) for aa in sequence)

    # Determine hydrophilicity/hydrophobicity of sequence
    if hydrophobicity_sum > 0:
        return f"Sequence {sequence}: Hydrophilic"
    elif hydrophobicity_sum < 0:
        return f"Sequence {sequence}: Hydrophobic"
    else:
        return f"Sequence {sequence}: Neutral"


def calculate_pI(sequence):
    """Create a dictionary of pK values (COO-, NH3+, R) information taken
    from source 
http://www.sev-chem.narod.ru/spravochnik/piaminoacid.htm"""
    pK_values = {
        'A': (2.34, 9.60),
        'R': (2.17, 9.04, 12.48),
        'N': (2.02, 8.80),
        'D': (2.09, 9.82, 3.86),
        'C': (1.71, 8.33, 10.30),
        'Q': (2.17, 9.13),
        'E': (2.19, 9.76, 4.25),
        'G': (2.34, 9.60),
        'H': (1.82, 9.17, 6.00),
        'I': (2.32, 9.76),
        'L': (2.36, 9.60),
        'K': (2.18, 8.95, 10.5),
        'M': (2.28, 9.21),
        'F': (2.58, 9.24),
        'P': (2.00, 10.60),
        'S': (2.21, 9.15),
        'T': (2.63, 10.43),
        'W': (1.22, 9.39),
        'Y': (2.20, 9.11, 10.10),
        'V': (2.29, 9.72)
    }

    # Initialization of variables for leftmost and rightmost elements
    N_end_pK = None
    C_end_pK = None

    # Find the marginal elements and their corresponding pKs
    for amino_acid in sequence:
        if amino_acid in pK_values:
            pK_list = pK_values[amino_acid]
            if len(pK_list) >= 2:
                if N_end_pK is None:
                    N_end_pK = pK_list[1]  # Второй pK
                C_end_pK = pK_list[0]  # Первый pK

    # If no amino acid sequence is specified - return None
    if N_end_pK is None or C_end_pK is None:
        return None

    # Calculate pI
    total_pK = N_end_pK + C_end_pK
    count = 2  # We take into account the found pKs - there are at least 2

    # Also add pK of AA radicals - the dictionary contains 3 pK values
    for amino_acid in sequence:
        if amino_acid in pK_values:
            pK_list = pK_values[amino_acid]
            if len(pK_list) >= 3:
                total_pK += pK_list[2]  # Третий pK
                count += 1

    # Substitute all found values into the formula and calculate pI
    pI = total_pK / count
    return f"Isoelectric point for the sequence {sequence}: {pI}"


def find_cleavage_sites(seq: str, motif: list) -> list:
    """Find cleavage sites for motif-specific proteases.
    Arguments:
    - seq - string sequence to be analyzed
    - motif - subsequence to be found in a sequence. Subsequence is 
specified as list of lists.
    Each nested list means more than one possible aminoacid at a single 
position (checked by OR condition).
    Return:
    - list of cleavage sites coordinates (C-end aminoacid of *potentially* 
cleaved sequence)
    """
    cleavage_sites = []
    seq_idx = 0
    while seq_idx < len(seq):
        motif_idx = 0
        chars_at_motif_idx = motif[motif_idx]
        seq_char = seq[seq_idx]
        if seq_char in chars_at_motif_idx:
            motif_idx += 1
            while motif_idx < len(motif):
                chars_at_motif_idx = motif[motif_idx]
                seq_char = seq[seq_idx+motif_idx]
                if seq_char in chars_at_motif_idx:
                    motif_idx += 1
                else:
                    break
            if motif_idx == len(motif):
                cleavage_sites.append(seq_idx + motif_idx)
        seq_idx += 1
    return cleavage_sites


motif_dict = {
    'Caspase 3': [['D'], ['M'], ['Q'], ['D']],
    'Caspase 6': [['V'], ['E'], ['H', 'I'], ['D']],
    'Caspase 7': [['D'], ['E'], ['V'], ['D']],
    'Enterokinase': [['D', 'E'], ['D', 'E'], ['D', 'E'], ['K']]
}


def get_cleavage_sites(seq: str) -> str:
    "Return amount and coordinates of cleavage sites for proteases, specified in motif_dict"
    output = f'{seq}\n'
    for motif_name, motif_value in motif_dict.items():
        sites = find_cleavage_sites(seq, motif_value)
        output += f'{len(sites)} protease cleavage site(s) for {motif_name}: {sites}\n'
    return output


all_aminoacids = {
    'A', 'R', 'N', 'D', 'C', 'H', 'G', 'Q', 'E', 'I',
    'L', 'K', 'M', 'P', 'S', 'Y', 'T', 'W', 'F', 'V'
}


def is_peptide(seq: str) -> bool:
    "Check whether the incoming sequence is an aminoacid"
    if set(seq).issubset(all_aminoacids):  # if set(seq) <= all_aminoacids
        return True
    raise ValueError(f'Incoming sequence {seq} is not a peptide')


operation_dict = {
    'get_cleavage_sites': get_cleavage_sites,
    'calculate_molecular_weight': calculate_molecular_weight,
    'calculate_percentage': calculate_percentage,
    'calculate_pI': calculate_pI,
    'calculate_hydrophobicity_eisenberg': 
calculate_hydrophobicity_eisenberg
}


def run_aminoacid_tools(*seqs: str, operation: str) -> str:
    """Run AminoAcid Tools
    Arguments:
    - *seqs - one or more string sequences to be analyzed
    - operation - action to be done with sequence(s)
    Return:
    - string that contains incoming sequence and result of operation"""
    if operation == '':
        raise ValueError('Operation value is not specified')
    if operation not in operation_dict:
        raise ValueError(f'Incorrect operation value\nSupported operations: {list(operation_dict.keys())}')
    for seq in seqs:
        is_peptide(seq)
    output = ''
    for seq in seqs:
        output += operation_dict[operation](seq)
        output += '\n\n'
    return output
