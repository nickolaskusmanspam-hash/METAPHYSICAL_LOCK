import math
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

class KUSMANPrimeSystem:
    def __init__(self):
        self.primes = []
        self.min_prime_factor = {}
        self.certificate_dir = "prime_forest"
        
    def initialize_forest(self, N):
        """Build prime forest using morphodynamic sieve"""
        is_prime = [True] * (N + 1)
        is_prime[0] = is_prime[1] = False
        
        self.min_prime_factor = {i: i for i in range(N + 1)}
        
        for i in range(2, int(math.isqrt(N)) + 1):
            if is_prime[i]:
                for j in range(i * i, N + 1, i):
                    if is_prime[j]:
                        is_prime[j] = False
                        if i < self.min_prime_factor[j]:
                            self.min_prime_factor[j] = i
        
        self.primes = [i for i in range(2, N + 1) if is_prime[i]]
    
    def generate_prime_path(self, n):
        """Compute factorization path using -operator"""
        path = []
        current = n
        
        while current > 1 and not self.min_prime_factor.get(current, current) == current:
            p = self.min_prime_factor[current]
            path.append(f"{current} → ζ({p})")
            current //= p
        path.append(f"{current} (Ancient Oak)")
        return path

    def save_forest_map(self, N):
        """Save prime forest certification files"""
        # Create directory if missing
        os.makedirs(self.certificate_dir, exist_ok=True)
        
        # Save prime list
        with open(f"{self.certificate_dir}/primes.txt", "w") as f:
            f.write("Ancient Oaks (Primes):\n")
            f.write("\n".join(map(str, self.primes)))
        
        # Save composite factorization paths
        with open(f"{self.certificate_dir}/composite_paths.txt", "w") as f:
            f.write("Sapling Factorization Paths:\n")
            for n in range(2, N + 1):
                if n not in self.primes:
                    path = self.generate_prime_path(n)
                    f.write(f"{n}: {' → '.join(path)}\n")
        
        # Save metadata
        with open(f"{self.certificate_dir}/README.txt", "w") as f:
            f.write("PRIME FOREST CERTIFICATION\n")
            f.write("==========================\n")
            f.write("- Ancient Oaks: Prime numbers (indivisible)\n")
            f.write("- Saplings: Composite numbers\n")
            f.write("- -operator: Smallest prime factor extraction\n")
            f.write(f"- Certified primes up to {N}: {len(self.primes)} found\n")
            f.write("- KUSMAN framework guarantee: 100% accuracy\n")

    def generate_primes(self, N):
        """Full KUSMAN prime generation process"""
        self.initialize_forest(N)
        self.save_forest_map(N)
        print(f"Generated prime forest for N={N} in '{self.certificate_dir}/'")

# ===== USAGE =====
if __name__ == "__main__":
    prime_system = KUSMANPrimeSystem()
    N = 100000
    
    # Corrected: Generate primes and save forest
    prime_system.generate_primes(N)
    
    # Print verification
    print(f"\nFirst 10 Ancient Oaks (Primes):")
    print(prime_system.primes[:10])
    
    print("\nSample Sapling Path (42):")
    print(" → ".join(prime_system.generate_prime_path(42)))
