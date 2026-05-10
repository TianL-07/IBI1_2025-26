def protein_mass(sequence):
    # Mass table for standard amino acids (monoisotopic masses in Da)
    mass_table = {
        'G': 57.02, 'A': 71.04, 'S': 87.03, 'P': 97.05,
        'V': 99.07, 'T': 101.05, 'C': 103.01, 'I': 113.08,
        'L': 113.08, 'N': 114.04, 'D': 115.03, 'Q': 128.06,
        'K': 128.09, 'E': 129.04, 'M': 131.04, 'H': 137.06,
        'F': 147.07, 'R': 156.10, 'Y': 163.06, 'W': 186.08
    }

    # Initialize total mass to zero
    total_mass = 0
    # Iterate over each amino acid character in the input sequence
    for amino_acid in sequence:
        # If the character is not a valid key in mass_table, raise an error
        if amino_acid not in mass_table:
            raise ValueError(f"Unknown amino acid: {amino_acid}")
        total_mass += mass_table[amino_acid]
    # Add the mass of the current amino acid to the running total
    return total_mass

# Example usage:
if __name__ == "__main__":
    x='VLTC'
    y=protein_mass(x)
    print(y)