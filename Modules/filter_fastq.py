def run_filter_fastq(seqs, gc_bounds=(0, 100), length_bounds=(0, 2**32), quality_threshold=0):
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

    return filtered_seqs

