import random
import time

# Diffie-Hellman parameters (small primes for demo, not secure for real use)
P = 23   # Prime number
G = 5    # Primitive root modulo P

def generate_private_key(P):
    """Generate a private key (random number < P)."""
    return random.randint(2, P-2)

def generate_public_key(private_key, G, P):
    """Compute public key = G^private_key mod P."""
    return pow(G, private_key, P)

def compute_shared_secret(public_key, private_key, P):
    """Compute shared secret = public_key^private_key mod P."""
    return pow(public_key, private_key, P)

# --- Simulation of two peers (Alice and Bob) ---

start_time = time.time()

# Key generation
alice_private = generate_private_key(P)
bob_private = generate_private_key(P)

alice_public = generate_public_key(alice_private, G, P)
bob_public = generate_public_key(bob_private, G, P)

keygen_time = time.time() - start_time

# Key exchange (computing shared secret)
start_exchange = time.time()

alice_secret = compute_shared_secret(bob_public, alice_private, P)
bob_secret = compute_shared_secret(alice_public, bob_private, P)

exchange_time = time.time() - start_exchange

# Results
print("Public Parameters: P =", P, ", G =", G)
print("Alice's Private Key:", alice_private)
print("Bob's Private Key:", bob_private)
print("Alice's Public Key:", alice_public)
print("Bob's Public Key:", bob_public)

print("\nShared Secret computed by Alice:", alice_secret)
print("Shared Secret computed by Bob  :", bob_secret)

print("\nTime taken for Key Generation: {:.6f} seconds".format(keygen_time))
print("Time taken for Key Exchange   : {:.6f} seconds".format(exchange_time))
