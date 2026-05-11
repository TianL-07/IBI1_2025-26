import sys

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

def get_gene_name(header):
    """
    Extract the gene name from the FASTA header line.
    Usually the first word before any space is the gene name (e.g., "YAL001C").
    """
    parts = header.split()
    return parts[0] if parts else header

def find_first_stop_from_atg(seq):
    """
    Find the first start codon (ATG) in the sequence.
    From that ATG, walk forward in steps of 3 codons.
    Return the first stop codon (TAA, TAG, or TGA) encountered.
    If no ATG is found or no stop codon is found after an ATG, return an empty string.
    """
    n = len(seq)
    # Locate the first occurrence of ATG
    for i in range(n - 2):
        if seq[i:i+3] == 'ATG':
            # Walk in triplets after the start codon
            for j in range(i + 3, n - 2, 3):
                codon = seq[j:j+3]
                if codon in ('TAA', 'TAG', 'TGA'):
                    return codon
            # No stop codon found for this ATG
            return ''
    return ''

def main():
    input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
    output_file = 'stop_genes.fa'

    try:
        records = parse_fasta(input_file)
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    out_lines = []
    for header, seq in records:
        gene_name = get_gene_name(header)
        stop = find_first_stop_from_atg(seq)
        if stop:   # Only write genes that have an in-frame stop codon after an ATG
            new_header = f">{gene_name} {stop}"
            out_lines.append(new_header)
            out_lines.append(seq)

    # Write output in FASTA format (header line, then sequence line)
    with open(output_file, 'w') as f:
        for i in range(0, len(out_lines), 2):
            f.write(out_lines[i] + '\n')
            f.write(out_lines[i+1] + '\n')

    print(f"Processed {len(records)} genes, found {len(out_lines)//2} with an in-frame stop codon from first ATG.")
    print(f"Results saved to {output_file}")

if __name__ == '__main__':
    main()