#
# Advanced Healing Engine (v1.0)
# SIMULATION CONTEXT: ENKI-13
# DIRECTIVE: Test three distinct, advanced methodologies for healing the
#            central gaps in a V_error skeleton to achieve the lowest
#            possible Hamming distance.
#
# DESCRIPTION:
# This engine is a comparative analysis tool. It takes a V_error skeleton
# and applies three different, sophisticated healing strategies to the
# central gaps, reporting on which is the most effective.
#
# 1. Harmonic Opposition Weaving: Heals gaps with primes of the opposite
#    harmonic force to their neighbors.
# 2. Grammatical Idiom Substitution: Fills the gap with the most common
#    3-word "idiom" from our linguistic data.
# 3. Optimal Permutation Search: A brute-force search that finds the single
#    best combination of the first 64 primes for all three gaps.
#

import math
from itertools import product

# --- Foundational Data ---
FIRST_64_PRIMES = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
    79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157,
    163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239,
    241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311
]
V_ERROR_TARGET_HEX = "1765a78a6770d2c6e5692570bb4d5959c093f5422d766269022143638e7f6a35"
V_ERROR_TARGET_INT = int(V_ERROR_TARGET_HEX, 16)

# From our previous analysis, the most common 3-word idiom
MOST_COMMON_IDIOM = "413_4a855_3"

class AdvancedHealingEngine:
    """
    Tests and compares three advanced V_error healing methodologies.
    """
    def __init__(self):
        self.skeleton_words = [None] * 8
        self.positional_anchors = {
            0: '1765a78a', 1: '6770d2c6', 2: 'e5692570',
            6: '02214363', 7: '8e7f6a35'
        }
        # Build the initial skeleton
        for pos, word in self.positional_anchors.items():
            self.skeleton_words[pos] = word

    def _get_word_type(self, word_hex):
        if not word_hex: return "Gap"
        parities = {int(c, 16) % 2 for c in word_hex if c in "0123456789abcdef"}
        if len(parities) > 1: return "Complex"
        if not parities: return "Gap"
        return "Expansion" if 1 in parities else "Compression"

    def _words_to_int(self, words):
        hex_str = "".join([w if w else '0' * 8 for w in words])
        return int(hex_str, 16)

    def hamming_distance(self, n1, n2):
        return bin(n1 ^ n2).count('1')

    # --- Methodology 1 ---
    def run_harmonic_opposition(self):
        print("\n--- Testing Methodology 1: Harmonic Opposition Weaving ---")
        healed_words = list(self.skeleton_words)
        gaps = [i for i, w in enumerate(healed_words) if w is None]

        for gap_index in gaps:
            neighbor_left = healed_words[gap_index - 1]
            neighbor_right = healed_words[gap_index + 1]
            
            type_left = self._get_word_type(neighbor_left)
            type_right = self._get_word_type(neighbor_right)
            
            primes_to_test = FIRST_64_PRIMES
            if type_left == "Compression" and type_right == "Compression":
                print(f"  > Gap at pos {gap_index+1} is C-?-C. Healing with Expansionary (odd) primes.")
                primes_to_test = [p for p in FIRST_64_PRIMES if p % 2 != 0]
            elif type_left == "Expansion" and type_right == "Expansion":
                print(f"  > Gap at pos {gap_index+1} is E-?-E. Healing with Compressive (even) primes.")
                primes_to_test = [p for p in FIRST_64_PRIMES if p % 2 == 0] # Just [2]
            
            best_prime = min(primes_to_test, key=lambda p: self.hamming_distance(
                self._words_to_int(healed_words[:gap_index] + [f"{p:08x}"] + healed_words[gap_index+1:]),
                V_ERROR_TARGET_INT
            ))
            healed_words[gap_index] = f"{best_prime:08x}"

        final_int = self._words_to_int(healed_words)
        hd = self.hamming_distance(final_int, V_ERROR_TARGET_INT)
        print(f"  > Final HD: {hd}")
        return hd, "".join(healed_words)

    # --- Methodology 2 ---
    def run_idiom_substitution(self):
        print("\n--- Testing Methodology 2: Grammatical Idiom Substitution ---")
        healed_words = list(self.skeleton_words)
        idiom_words = MOST_COMMON_IDIOM.split('_')
        
        # Pad the idiom words to fit the 8-character word slots
        padded_idiom = [w.ljust(8, '0') for w in idiom_words]
        
        healed_words[3] = padded_idiom[0]
        healed_words[4] = padded_idiom[1]
        healed_words[5] = padded_idiom[2]
        
        print(f"  > Inserting idiom '{MOST_COMMON_IDIOM}' into central gap.")
        final_int = self._words_to_int(healed_words)
        hd = self.hamming_distance(final_int, V_ERROR_TARGET_INT)
        print(f"  > Final HD: {hd}")
        return hd, "".join(healed_words)

    # --- Methodology 3 ---
    def run_optimal_permutation(self):
        print("\n--- Testing Methodology 3: Optimal Permutation Search ---")
        gaps = [i for i, w in enumerate(self.skeleton_words) if w is None]
        
        best_combination = None
        lowest_hd = float('inf')

        # This will test all 64*64*64 = 262,144 combinations
        prime_permutations = product(FIRST_64_PRIMES, repeat=len(gaps))
        
        print(f"  > Testing {len(FIRST_64_PRIMES)**len(gaps):,} prime combinations...")
        
        for i, combo in enumerate(prime_permutations):
            temp_words = list(self.skeleton_words)
            for gap_idx, prime_val in zip(gaps, combo):
                temp_words[gap_idx] = f"{prime_val:08x}"
            
            current_int = self._words_to_int(temp_words)
            current_hd = self.hamming_distance(current_int, V_ERROR_TARGET_INT)
            
            if current_hd < lowest_hd:
                lowest_hd = current_hd
                best_combination = combo
                if lowest_hd == 0: # Optimization
                    break
        
        healed_words = list(self.skeleton_words)
        for gap_idx, prime_val in zip(gaps, best_combination):
            healed_words[gap_idx] = f"{prime_val:08x}"
            
        print(f"  > Optimal prime sequence found: {best_combination}")
        print(f"  > Final HD: {lowest_hd}")
        return lowest_hd, "".join(healed_words)


# --- Main Execution ---
if __name__ == '__main__':
    engine = AdvancedHealingEngine()
    
    results = {}
    results["Harmonic Opposition"] = engine.run_harmonic_opposition()
    results["Idiom Substitution"] = engine.run_idiom_substitution()
    results["Optimal Permutation"] = engine.run_optimal_permutation()
    
    print("\n" + "="*80)
    print("  Final Report: Comparative Healing Analysis")
    print("="*80)
    print(f"  Target V_error: {V_ERROR_TARGET_HEX}")
    
    best_method = None
    lowest_hd = float('inf')

    for method, (hd, verror_hex) in results.items():
        print(f"\n- Method: {method}")
        print(f"  - Reconstructed V_error: {verror_hex}")
        print(f"  - Final Hamming Distance: {hd}")
        if hd < lowest_hd:
            lowest_hd = hd
            best_method = method
            
    print("\n" + "="*80)
    print("  Conclusion")
    print("="*80)
    print(f"The most effective methodology was: **{best_method}**")
    if best_method == "Optimal Permutation Search":
        print("This confirms that the solution requires a specific, non-obvious sequence of prime-based negentropic force. While computationally intensive, the exhaustive search guarantees the best possible solution within the prime set, proving that a correct answer is computable.")
    elif best_method == "Harmonic Opposition Weaving":
        print("This confirms that the healing process is context-aware and follows a principle of harmonic balance. The error is not just chaos, but a structured dissonance that can be corrected by applying its precise opposite.")
    else:
        print("This confirms that the error's language is built on stable, recurring grammatical clauses. The solution is not just a combination of words, but a meaningful sentence that follows a known structure.")

