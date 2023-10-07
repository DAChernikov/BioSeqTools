def transcribe(dna_sequence):
    rna_sequence = ''
    for base in dna_sequence:
        if base == 'T':
            rna_sequence += 'U'
        elif base == 't':
            rna_sequence += 'u'
        elif base == 'U':
            rna_sequence += 'T'
        elif base == 'u':
            rna_sequence += 't'
        else:
            rna_sequence += base
    return rna_sequence

def reverse(sequence):
    return sequence[::-1]

def complement(sequence):
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't',
                       't': 'a', 'c': 'g', 'g': 'c'}
    complement_sequence = ''.join(complement_dict.get(base, base)
                                  for base in sequence)
    return complement_sequence

def reverse_complement(dna_sequence):
    # можно также "complement_sequence = complement(dna_sequence)"
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C', 'a': 't',
                       't': 'a', 'c': 'g', 'g': 'c'}
    complement_sequence = ''.join(complement_dict.get(base, base)
                                  for base in dna_sequence)
    return complement_sequence[::-1]

def run_dna_rna_tools(*args):
    if not args:
        return "There are no function arguments"
    action = args[-1].lower()
    sequences = args[:-1]
    results = []
    for sequence in sequences:
        if not all(base in 'ACGTU' for base in sequence.upper()):
            results.append(f"Invalid sequence: {sequence}")
        elif action == 'transcribe':
            results.append(transcribe(sequence))
        elif action == 'reverse':
            results.append(reverse(sequence))
        elif action == 'complement':
            results.append(complement(sequence))
        elif action == 'reverse_complement':
            results.append(reverse_complement(sequence))
        else:
            results.append(f"Invalid action: {action}")
    return results[0] if len(results) == 1 else results
