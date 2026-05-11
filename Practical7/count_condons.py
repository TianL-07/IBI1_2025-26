import sys
import os
from collections import Counter
import matplotlib.pyplot as plt

def parse_fasta(filename):
    """
    Read a FASTA file and return a list of (header, sequence) tuples.
    The sequence is merged into a single uppercase string.
    """
    records = []
    with open(filename, 'r') as f:
        current_header = None
        current_seq = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                if current_header is not None:
                    records.append((current_header, ''.join(current_seq)))
                current_header = line[1:]   # Remove '>'
                current_seq = []
            else:
                current_seq.append(line.upper())
        if current_header is not None:
            records.append((current_header, ''.join(current_seq)))
    return records

def get_longest_orf_codons(seq, target_stop):
    """
    For a given DNA/RNA sequence, find the longest ORF that:
      - starts with ATG
      - ends with the target_stop (TAA, TAG, or TGA)
      - reads in triplets from the start (no frameshifts)
    Returns a list of codons (including the start ATG, excluding the stop)
    for that longest ORF, or None if no such ORF exists.
    """
    n = len(seq)
    best_length = -1
    best_codons = None

    # Scan every possible start codon position
    for i in range(n - 2):
        if seq[i:i+3] != 'ATG':
            continue
        # Walk forward in steps of 3 from i+3
        j = i + 3
        orf_codons = [seq[i:i+3]]   # Include the start codon
        while j <= n - 3:
            codon = seq[j:j+3]
            if codon in ('TAA', 'TAG', 'TGA'):
                # Stop codon found
                if codon == target_stop:
                    # Valid ORF ending with the target stop
                    length = (j + 3) - i   # total nucleotides from start to stop (including stop)
                    # We only store codons *before* the stop
                    if length > best_length:
                        best_length = length
                        best_codons = orf_codons  # stop not included
                # Regardless of match, stop scanning this start (ORF ends here)
                break
            else:
                orf_codons.append(codon)
                j += 3
        # If loop finishes without break, no stop codon -> ignore

    return best_codons

def main():
    # Input file name 
    input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found.")
        print("Please ensure the file is in the current directory or provide the correct path.")
        sys.exit(1)

    # Ask user for stop codon
    valid_stops = {'TAA', 'TAG', 'TGA'}
    while True:
        stop = input("Enter a stop codon (TAA, TAG, TGA): ").strip().upper()
        if stop in valid_stops:
            break
        print("Invalid input. Please enter one of: TAA, TAG, TGA")

    # Parse FASTA file
    print("Reading FASTA file...")
    records = parse_fasta(input_file)
    print(f"Found {len(records)} gene sequences.")

    # Global codon counter
    codon_counter = Counter()
    genes_with_orf = 0

    # Process each gene
    for header, seq in records:
        codons = get_longest_orf_codons(seq, stop)
        if codons:
            codon_counter.update(codons)
            genes_with_orf += 1

    print(f"Genes containing at least one ORF ending with {stop}: {genes_with_orf}")
    if not codon_counter:
        print("No ORFs found. Cannot generate pie chart.")
        return

    # Prepare data for pie chart
    total_codons = sum(codon_counter.values())
    print(f"Total in-frame codons counted: {total_codons}")
    print(f"Unique codon types: {len(codon_counter)}")

    # Merge low-frequency codons (less than 1% of total) into "Other"
    threshold = 0.01  # 1%
    other_count = 0
    data = {}
    for codon, count in codon_counter.items():
        if count / total_codons >= threshold:
            data[codon] = count
        else:
            other_count += count
    if other_count > 0:
        data['Other'] = other_count

    # Sort data for consistent pie order 
    sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
    labels = [item[0] for item in sorted_items]
    sizes = [item[1] for item in sorted_items]

    # Create pie chart
    plt.figure(figsize=(12, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90,
            labeldistance=1.05, pctdistance=0.85)
    plt.title(f'In‑frame Codon Distribution Upstream of {stop} (longest ORF per gene)')
    plt.axis('equal')  # Equal aspect ratio ensures the pie is circular.

    # Save to file
    output_plot = 'codon_distribution.png'
    plt.savefig(output_plot, dpi=300, bbox_inches='tight')


if __name__ == '__main__':
    main()