def read_fastq_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    fastq_data = {}
    i = 0
    while i < len(lines):
        header = lines[i].strip().lstrip('@')
        sequence = lines[i + 1].strip()
        plus = lines[i + 2].strip()
        quality = lines[i + 3].strip()
        entry = (sequence, quality)
        fastq_data[header] = entry
        i += 4
    return fastq_data

def save_fastq_file(filtered_seqs, output_filename=None):
    output_filename = output_filename if output_filename else 'filtered_output.fastq'
    with open(output_filename, 'w') as file:
        for name, (sequence, quality) in filtered_seqs.items():
            file.write(f'{name}\n{sequence}\n+\n{quality}\n')

def run_filter_fastq(input_path, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0, output_filename=None):
    seqs = read_fastq_file(input_path)
    filtered_seqs = {}

    for name, (sequence, quality) in seqs.items():
        # Estimate GC-content
        gc_content = (sequence.count('G') + sequence.count('C')) / len(sequence) * 100

        # Estimate average quality
        avg_quality = sum(ord(q) - 33 for q in quality) / len(quality)

        # Filtering by user`s conditions
        if (
            gc_bounds[0] <= gc_content <= gc_bounds[1] and
            length_bounds[0] <= len(sequence) <= length_bounds[1] and
            avg_quality >= quality_threshold
        ):
            filtered_seqs[name] = (sequence, quality)

    save_fastq_file(filtered_seqs, output_filename)

# Usage example
run_filter_fastq('./HW6_Files/example_fastq.fastq', gc_bounds=(10, 30), quality_threshold=30, output_filename='filtered_output.fastq')
