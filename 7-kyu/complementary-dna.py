# Given a string containing segments of DNA, return a string of the complementary segments
# 'A' & 'T' complement each other
# 'C' & 'G' complement each other
# e.g "ATTGC" --> "TAACG"
# e.g "GTAT" --> "CATA"

# Declare new_dna string variable to contain new string
# Iterate over each index of dna:
    # If char at current index = A, concat T to new_dna
    # If char at current index = T, concat A to new_dna
    # etc
# Return

def complementary_dna(dna):
    new_dna = ""
    for i in range(0, len(dna)):
        match dna[i]:
            case "A":
                new_dna += "T"
            case "T":
                new_dna += "A"
            case "C":
                new_dna += "G"
            case "G":
                new_dna += "C"
            case _:
                return
    return new_dna