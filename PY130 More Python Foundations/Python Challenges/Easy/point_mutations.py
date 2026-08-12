class DNA:
    def __init__(self, strand):
        self._strand = strand

    # def hamming_distance(self, other_strand):
        # shortest_strand, longest_strand = self._strand, other_strand

        # if len(self._strand) > len(other_strand):
            # longest_strand, shortest_strand = self._strand, other_strand

        # hamming_distance = 0
        # for idx, char_in_shortest_strand in enumerate(shortest_strand):
            # char_in_longest_strand = longest_strand[idx]
            # if char_in_shortest_strand != char_in_longest_strand:
                # hamming_distance += 1

        # return hamming_distance

    def hamming_distance(self, other_strand):
        differences = 0

        for char1, char2 in zip(self._strand, other_strand):
            if char1 != char2:
                differences += 1

        return differences