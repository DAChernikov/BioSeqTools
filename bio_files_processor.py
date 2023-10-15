def convert_multiline_fasta_to_oneline(input_fasta, output_fasta=None):
    with open(input_fasta, 'r') as input_file:
        fasta_lines = input_file.readlines()

    sequences = {}
    current_id = None

    for line in fasta_lines:
        line = line.strip()

        if line.startswith('>'):
            current_id = line[1:]
            sequences[current_id] = ''
        else:
            if current_id:
                sequences[current_id] += line

    if output_fasta is None:
        output_fasta = input_fasta + ".fasta"

    with open(output_fasta, 'w') as output_file:
        for seq_id, sequence in sequences.items():
            output_file.write(f'>{seq_id}\n{sequence}\n')

    print(f"Converted data saved as {output_fasta}")


def select_genes_from_gbk_to_fasta(input_gbk, genes_of_interest, n_before=1,
                                   n_after=1, output_fasta=None):

    with open(input_gbk, 'r') as gbk_file:
        gbk_data = gbk_file.read()
    gene_data = {}
    gene_records = gbk_data.split('//')

    for record in gene_records:
        if any(gene in record for gene in genes_of_interest):
            for gene in genes_of_interest:
                gene_start = record.find(f'/gene="{gene}"')
                if gene_start != -1:
                    gene_end = record.find('/translation="', gene_start)
                    if gene_end != -1:
                        protein_sequence = record[
                                           gene_end + len('/translation="'):]
                        protein_sequence = protein_sequence[
                                           :protein_sequence.find('"')]

                        gene_data[gene] = protein_sequence

    if output_fasta is None:
        output_fasta = 'HW6_Files/output_selected_genes.fasta'

    with open(output_fasta, 'w') as fasta_file:
        for gene, protein_sequence in gene_data.items():
            fasta_file.write(f'>{gene}\n{protein_sequence}\n')

    print(f"Created FASTA-file: {output_fasta}")


def change_fasta_start_pos(input_fasta, shift, output_fasta):
    with open(input_fasta, 'r') as input_file:
        lines = input_file.readlines()

    if len(lines) != 2 or not lines[0].startswith('>'):
        print("Invalid input FASTA format.")
        return

    header = lines[0]
    sequence = lines[1].strip()

    if shift > 0:
        sequence = sequence[shift:] + sequence[:shift]
    elif shift < 0:
        sequence = sequence[shift:] + sequence[:shift]

    with open(output_fasta, 'w') as output_file:
        output_file.write(header)
        output_file.write(sequence)

    print(f"FASTA with shifted start position saved to {output_fasta}")


def parse_blast_output(input_file, output_file=None):
    with open(input_file, 'r') as f:
        lines = f.read().splitlines()

    query_results = {}
    current_query = None
    for line in lines:
        if line.startswith("Query #"):
            current_query = line.split("Query ID: ")[1].split(" Length:")[0]
            query_results[current_query] = []
        elif line.startswith("Description"):
            description = line.split("Description")[1].strip()
            query_results[current_query].append(description)

    if output_file:
        with open(output_file, 'w') as output:
            for query, descriptions in query_results.items():
                for description in sorted(descriptions):
                    output.write(f"{query}\t{description}\n")

    print("Blast results parsed.")
