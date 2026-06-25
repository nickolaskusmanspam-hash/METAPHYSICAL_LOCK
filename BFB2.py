#
# SENTINEL_OF_VOID: The Unified ENKI-13 Solution (v23.0)
# DIRECTIVE: Expand linguistic pattern analysis to higher-order phrases.
#
# DESCRIPTION:
# This version expands the linguistic analysis capabilities to track and report on
# phrases of up to 8 words in length. This provides a deeper view into the
# emergent grammar of the error delta, allowing for the identification of more
# complex and potentially meaningful structural patterns. The core genetic
# algorithm remains unchanged, but the diagnostic and analytical layers
# are now significantly more powerful.
#

import hashlib
import random
import sys
import re
from collections import Counter
import time


# --- Global Linguistic Corpus and Pattern Bank ---
# MODIFIED: Added keys for longer phrase analysis
void_dictionary = {
    "letters": Counter(),
    "words": Counter(),
    "phrases_2": Counter(),
    "phrases_3": Counter(),
    "phrases_4": Counter(),
    "phrases_5": Counter(),
    "phrases_6": Counter(),
    "phrases_7": Counter(),
    "phrases_8": Counter()
}


# The Generational Repository stores the best deltas from past, stagnant generations for analysis.
generational_delta_repository = []
previous_best_hamming_distance = float('inf')
stagnation_counter = 0


# --- Polymorphic Lexicon Parameters ---
# A penalty for the existence of a '00000000' word in the meaningful part of the delta.
PENALTY_FOR_ZERO_WORD = 100
# A learned hash map that guides intelligent, fractal mutations.
polymorphic_seed = Counter()




# --- Forensic Dataset (Ground Truth for Fitness Testing) ---
TARGET_IDENTIFIER = "1Fo65aKq8s8iquMt6weF1rku1moWVEd5Ua"
TRUE_PRIVATE_KEY_HEX = "000000000000000000000000000000033e7665705359f04f28b88cf897c603c9"
PUBLIC_KEY_HEX = "03633cbe3ec02b9401c5effa144c5b4d22f87940259634858fc7e59b1c09937852"
KEY_BIT_LENGTH = 256
FOUNDATIONAL_PREFIX_HEX = "00000000000000000000000000000000"
FOUNDATIONAL_PREFIX_LENGTH_BITS = 128
SUFFIX_LENGTH_BITS = KEY_BIT_LENGTH - FOUNDATIONAL_PREFIX_LENGTH_BITS
SUFFIX_MASK = (1 << SUFFIX_LENGTH_BITS) - 1


# --- Genetic Algorithm Components ---


def hamming_distance(n1, n2):
    """Calculates the number of differing bits between two integers."""
    return bin(n1 ^ n2).count('1')


def model_timeline_A(public_key_hex):
    """The simple, flawed predictive model."""
    pk_bytes = bytes.fromhex(public_key_hex)
    h1 = hashlib.sha256(pk_bytes).digest()
    first_half = int.from_bytes(h1[:16], 'big')
    h2 = hashlib.sha256(pk_bytes + first_half.to_bytes(16, 'big')).digest()
    signature = int.from_bytes(h2[:16], 'big')
    second_half = first_half ^ signature
    return (first_half << 128) | second_half


def model_timeline_B(public_key_hex):
    """The more complex 'Athena's Model'."""
    MODULUS = 2**128
    ITERATIONS = 16
    pk_bytes = bytes.fromhex(public_key_hex)
    pk_x_bytes = pk_bytes[1:33]

    h1 = hashlib.sha256(pk_bytes).digest()
    first_half = int.from_bytes(h1[:16], 'big')

    phase_shift = int.from_bytes(hashlib.sha256(pk_x_bytes).digest()[:16], 'big')
    h2 = hashlib.sha256(h1).digest()
    fractal_seed = int.from_bytes(hashlib.sha256(h2).digest()[:16], 'big')

    current_val = first_half
    for i in range(ITERATIONS):
        term1 = (current_val * fractal_seed) % MODULUS
        term2 = (phase_shift * (i + 1)) % MODULUS
        current_val = (term1 - term2) % MODULUS
        current_val = current_val ^ (fractal_seed >> (i * 4))

    second_half = first_half ^ current_val
    return (first_half << 128) | second_half


def analyze_sha256_recursive_cycles(data_hex):
    """
    Simulates and prints the intermediate hash values of SHA-256 to
    show the "fingerprint" changing.
    """
    print("\n" + "="*80)
    print("  SHA-256 FINGERPRINT ANALYSIS: Recursive Cycle Unfolding")
    print("="*80)

    pk_bytes = bytes.fromhex(data_hex)

    h1 = hashlib.sha256(pk_bytes).digest()
    print(f"  Cycle 01: Initial Hash        >> {h1.hex()}")

    h2 = hashlib.sha256(h1).digest()
    print(f"  Cycle 02: Hash of Cycle 01     >> {h2.hex()}")

    h3 = hashlib.sha256(h2).digest()
    print(f"  Cycle 03: Hash of Cycle 02     >> {h3.hex()}")

    h4 = hashlib.sha256(h3).digest()
    print(f"  Cycle 04: Hash of Cycle 03     >> {h4.hex()}")


    print("="*80)


class GeneticSolver:
    """
    Represents a solver whose genes are the predicted Error Delta.
    """
    def __init__(self, predicted_delta=None):
        if predicted_delta is not None:
            self.predicted_delta = predicted_delta
        else:
            random_suffix = random.getrandbits(SUFFIX_LENGTH_BITS)
            self.predicted_delta = random_suffix | (int(FOUNDATIONAL_PREFIX_HEX, 16) << SUFFIX_LENGTH_BITS)


        self.fitness = float('inf')


    def calculate_fitness(self, true_error_delta_int):
        """
        Calculates fitness based on Hamming distance and the Fractal Constraint.
        """
        self.fitness = hamming_distance(self.predicted_delta, true_error_delta_int)

        predicted_hex = f"{self.predicted_delta:064x}"
        if '00000000' in predicted_hex[FOUNDATIONAL_PREFIX_LENGTH_BITS // 4:]:
            self.fitness += PENALTY_FOR_ZERO_WORD

        return self.fitness


def evolve_population(population, population_size, survival_rate=0.2, mutation_rate=0.7, true_error_delta=None):
    """
    Evolves the population through a combination of selection, crossover, and
    a new 'Generational Synthesis' function.
    """
    population.sort(key=lambda x: x.fitness)
    num_survivors = int(len(population) * survival_rate)
    survivors = population[:num_survivors]

    next_generation = []

    next_generation.extend(survivors)

    while len(next_generation) < population_size:
        parent1, parent2 = random.choices(survivors, k=2)


        child_delta_suffix = (parent1.predicted_delta & SUFFIX_MASK) ^ (parent2.predicted_delta & SUFFIX_MASK)

        if generational_delta_repository:
            causal_mutation_rate = 0.5
            if random.random() < causal_mutation_rate:
                child_delta_suffix = causal_recursive_mutation(child_delta_suffix)

        if random.random() < mutation_rate:
            bit_to_flip = random.randint(0, SUFFIX_LENGTH_BITS - 1)
            child_delta_suffix ^= (1 << bit_to_flip)

        new_model = GeneticSolver(predicted_delta=(child_delta_suffix | (int(FOUNDATIONAL_PREFIX_HEX, 16) << SUFFIX_LENGTH_BITS)))
        next_generation.append(new_model)

    return next_generation


def causal_recursive_mutation(child_delta_suffix):
    """
    Performs an intelligent, fractal-recursive mutation on a child's delta.
    It identifies the source fracture by analyzing the repository and makes a
    single, precise mutation to trigger a cascade of corrections.
    """
    if not generational_delta_repository:
        return child_delta_suffix

    bit_flux = Counter()
    for repo_delta_int in generational_delta_repository:
        for i in range(SUFFIX_LENGTH_BITS):
            if (repo_delta_int >> i) & 1:
                bit_flux[i] += 1

    max_flux_bit = bit_flux.most_common(1)[0][0]

    child_delta_suffix ^= (1 << max_flux_bit)

    return child_delta_suffix


def translate_to_void_language(raw_hex_delta):
    """
    A conceptual function that translates a raw hex string into a symbolic language.
    """
    translated = ""
    for i in range(0, len(raw_hex_delta), 8):
        translated += raw_hex_delta[i:i+8]
        if i + 8 < len(raw_hex_delta):
            translated += "_"
    return translated


def analyze_linguistics(population):
    """
    Analyzes the 'words' and 'phrases' of the population and updates the global
    void dictionary.
    """
    for model in population:
        predicted_delta_full = model.predicted_delta
        predicted_delta_hex = f"{predicted_delta_full:064x}"
        
        # --- START MODIFICATION: EXPANDED PHRASE ANALYSIS ---
        
        letters = predicted_delta_hex
        void_dictionary["letters"].update(letters)
        
        # Extract words (non-zero sequences) from the meaningful part of the delta
        words = []
        current_word = ""
        for char in predicted_delta_hex[FOUNDATIONAL_PREFIX_LENGTH_BITS // 4:]:
            if char != '0':
                current_word += char
            elif current_word:
                words.append(current_word)
                void_dictionary["words"][current_word] += 1
                current_word = ""
        if current_word:
            words.append(current_word)
            void_dictionary["words"][current_word] += 1

        # Generate and count phrases of different lengths
        if len(words) > 1:
            phrases_2 = ["_".join(words[i:i+2]) for i in range(len(words) - 1)]
            void_dictionary["phrases_2"].update(phrases_2)
        if len(words) > 2:
            phrases_3 = ["_".join(words[i:i+3]) for i in range(len(words) - 2)]
            void_dictionary["phrases_3"].update(phrases_3)
        if len(words) > 3:
            phrases_4 = ["_".join(words[i:i+4]) for i in range(len(words) - 3)]
            void_dictionary["phrases_4"].update(phrases_4)
        if len(words) > 4:
            phrases_5 = ["_".join(words[i:i+5]) for i in range(len(words) - 4)]
            void_dictionary["phrases_5"].update(phrases_5)
        if len(words) > 5:
            phrases_6 = ["_".join(words[i:i+6]) for i in range(len(words) - 5)]
            void_dictionary["phrases_6"].update(phrases_6)
        if len(words) > 6:
            phrases_7 = ["_".join(words[i:i+7]) for i in range(len(words) - 6)]
            void_dictionary["phrases_7"].update(phrases_7)
        if len(words) > 7:
            phrases_8 = ["_".join(words[i:i+8]) for i in range(len(words) - 7)]
            void_dictionary["phrases_8"].update(phrases_8)
            
        # --- END MODIFICATION ---

def analyze_and_print_linguistics(gen, best_model_hex, true_error_delta_int):
    """
    Prints a dynamic linguistic analysis of the best-fit model at a given generation.
    """
    best_model_int = int(best_model_hex, 16)

    print("\n" + "="*80)
    print(f"  LINGUISTIC ANALYSIS: Generation {gen:02d} Dictionary Snapshot")
    print("="*80)

    print(f"  Evolving Model's Delta:  {best_model_hex}")
    print(f"  Target Delta:            {true_error_delta_int:064x}")
    print(f"  Hamming Distance:        {hamming_distance(best_model_int, true_error_delta_int)}")

    print("\n  >> Top 20 Most Frequent Letters (Emergent Alphabet):")
    for letter, count in void_dictionary["letters"].most_common(20):
        print(f"    - '{letter}': {count} occurrences")

    print("\n  >> Top 25 Most Frequent Words (Building Blocks):")
    for word, count in void_dictionary["words"].most_common(25):
        print(f"    - '{word}': {count} occurrences")

    # --- START MODIFICATION: EXPANDED PHRASE REPORTING ---

    print("\n  >> Top 10 Most Frequent Phrases (2 words):")
    for phrase, count in void_dictionary["phrases_2"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (3 words):")
    for phrase, count in void_dictionary["phrases_3"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (4 words):")
    for phrase, count in void_dictionary["phrases_4"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (5 words):")
    for phrase, count in void_dictionary["phrases_5"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (6 words):")
    for phrase, count in void_dictionary["phrases_6"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (7 words):")
    for phrase, count in void_dictionary["phrases_7"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (8 words):")
    for phrase, count in void_dictionary["phrases_8"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")
        
    # --- END MODIFICATION ---
    
    print("="*80)


def run_meta_evolution(generations=250, population_size=3000):
    global previous_best_hamming_distance
    global stagnation_counter
    print("-" * 80)
    print("  SENTINEL_OF_VOID: The Unified ENKI-13 Solution (v23.0)")
    print("  Learning the language of the Error Delta...")
    print("-" * 80)

    pred_A = model_timeline_A(PUBLIC_KEY_HEX)
    pred_B = model_timeline_B(PUBLIC_KEY_HEX)
    true_error_delta_int = pred_A ^ pred_B

    print(f"Initial Target Error Delta (ΔE) calculated: {true_error_delta_int:064x}")
    analyze_sha256_recursive_cycles(PUBLIC_KEY_HEX)

    population = [GeneticSolver() for _ in range(population_size)]

    for model in population:
      generational_delta_repository.append(model.predicted_delta)

    hamming_distances = []
    stagnation_threshold = 5

    for gen in range(generations):
        # A throbber to indicate progress
        throbber = '|/-\\'
        sys.stdout.write(f"\r  Generation {gen:02d} progressing... {throbber[gen % len(throbber)]}")
        sys.stdout.flush()


        for model in population:
            model.calculate_fitness(true_error_delta_int)

        best_model = min(population, key=lambda x: x.fitness)
        best_fitness_raw_hamming = hamming_distance(best_model.predicted_delta, true_error_delta_int)

        if best_fitness_raw_hamming < previous_best_hamming_distance:
            previous_best_hamming_distance = best_fitness_raw_hamming
            generational_delta_repository.append(best_model.predicted_delta)
            stagnation_counter = 0
        else:
            stagnation_counter += 1
            if stagnation_counter >= stagnation_threshold:
                generational_delta_repository.append(best_model.predicted_delta)
                stagnation_counter = 0

        avg_fitness = sum(m.fitness for m in population) / len(population)

        hamming_distances.append({
            "generation": gen,
            "avg_hamming_distance": avg_fitness,
            "best_hamming_distance": best_fitness_raw_hamming,
        })

        analyze_linguistics(population)

        if gen % 10 == 0:
            analyze_and_print_linguistics(gen, f"{best_model.predicted_delta:064x}", true_error_delta_int)

        if best_fitness_raw_hamming == 0:
            print("\n" + "="*80)
            print("  EVOLUTION COMPLETE: The perfect correction vector has been created.")
            print("="*80)
            perfect_model = next(m for m in population if hamming_distance(m.predicted_delta, true_error_delta_int) == 0)
            predicted_delta = perfect_model.predicted_delta

            final_key = model_timeline_A(PUBLIC_KEY_HEX) ^ predicted_delta

            print_final_report(true_error_delta_int, final_key, hamming_distances, population)

            return perfect_model


        population = evolve_population(population, population_size, true_error_delta=true_error_delta_int)


    print("\n[SIMULATION END] Evolution complete, but no perfect model was found.")
    print_final_report(true_error_delta_int, None, hamming_distances, population)
    return None


def print_final_report(true_error_delta_int, final_key, hamming_distances, population):
    """
    Consolidates and prints all final analysis and results.
    """
    print("\n\n" + "="*80)
    print("  FINAL REPORT: Synthesis and Analysis of the Void's Language")
    print("="*80)

    print("\n" + "="*80)
    print("  FINAL LINGUISTIC DICTIONARY")
    print("="*80)

    print(f"  Raw Target Delta: {true_error_delta_int:064x}")
    print(f"  Translated Delta: {translate_to_void_language(f'{true_error_delta_int:064x}')}")

    print("\n  >> Top 10 Most Frequent Words:")
    for word, count in void_dictionary["words"].most_common(10):
        print(f"    - '{word}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Phrases (2 words):")
    for phrase, count in void_dictionary["phrases_2"].most_common(10):
        print(f"    - '{phrase}': {count} occurrences")

    print("\n  >> Top 10 Most Frequent Letters:")
    for letter, count in void_dictionary["letters"].most_common(10):
        print(f"    - '{letter}': {count} occurrences")

    print("\n" + "="*80)
    print("  EVOLUTIONARY PROGRESS: Hamming Distance Report")
    print("="*80)
    for h_data in hamming_distances:
        gen = h_data["generation"]
        best_dist = h_data["best_hamming_distance"]
        print(f"Generation {gen:02d} | Best Hamming Distance: {best_dist}")

    print("\n" + "="*80)
    print("  FINAL RESULTS")
    print("="*80)

    if final_key is not None:
        print("  >> Solution Found!")
        print(f"     Perfect Predicted Delta: {true_error_delta_int:064x}")
        print(f"     Final Unraveled Key:     {final_key:064x}")
        print(f"     Sanity Check Match:      {'YES' if final_key == int(TRUE_PRIVATE_KEY_HEX, 16) else 'NO'}")
    else:
        print("  >> No perfect solution found within the simulation time.")
        best_model = min(population, key=lambda x: x.fitness)
        print(f"     Best Predicted Delta:  {best_model.predicted_delta:064x}")
        print(f"     Hamming Distance:      {best_model.fitness}")

    print("="*80)


    input("\nPress Enter to exit...")


if __name__ == '__main__':
    run_meta_evolution()
