import random
import math
import time

# ========================
# RSA IMPLEMENTATION
# ========================
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d
    return None

def generate_rsa_keys():
    # Small primes for demo (use large in real-world)
    p, q = 61, 53
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 17  # Public exponent
    d = mod_inverse(e, phi)
    return (e, n), (d, n)

def rsa_encrypt(message, public_key):
    e, n = public_key
    return pow(message, e, n)

def rsa_decrypt(cipher, private_key):
    d, n = private_key
    return pow(cipher, d, n)


# ========================
# DIFFIE-HELLMAN IMPLEMENTATION
# ========================
def generate_private_key(P):
    return random.randint(2, P-2)

def generate_public_key(private, G, P):
    return pow(G, private, P)

def compute_shared_secret(peer_pub, private, P):
    return pow(peer_pub, private, P)


# ========================
# KEY MANAGEMENT
# ========================
class KeyManager:
    def __init__(self):
        self.keys = {}   # store subsystem RSA keys
    
    def register_system(self, name):
        pub, priv = generate_rsa_keys()
        self.keys[name] = {"public": pub, "private": priv}
        print(f"[KeyManager] Registered {name} with RSA keys.")
    
    def revoke_system(self, name):
        if name in self.keys:
            del self.keys[name]
            print(f"[KeyManager] Revoked keys for {name}.")
    
    def get_public_key(self, name):
        return self.keys[name]["public"] if name in self.keys else None
    
    def get_private_key(self, name):
        return self.keys[name]["private"] if name in self.keys else None


# ========================
# SIMULATION
# ========================
if __name__ == "__main__":
    # Initialize systems
    systems = ["Finance", "HR", "SupplyChain"]
    manager = KeyManager()
    
    # Register subsystems
    for s in systems:
        manager.register_system(s)
    
    # Parameters for Diffie-Hellman (small for demo)
    P, G = 23, 5
    
    print("\n--- Secure Communication Example (Finance <-> HR) ---")
    
    # Finance and HR generate private/public DH keys
    start = time.time()
    finance_priv = generate_private_key(P)
    hr_priv = generate_private_key(P)
    
    finance_pub = generate_public_key(finance_priv, G, P)
    hr_pub = generate_public_key(hr_priv, G, P)
    keygen_time = time.time() - start
    
    # Exchange and compute shared secret
    start = time.time()
    finance_secret = compute_shared_secret(hr_pub, finance_priv, P)
    hr_secret = compute_shared_secret(finance_pub, hr_priv, P)
    exchange_time = time.time() - start
    
    print("Finance DH Secret:", finance_secret)
    print("HR DH Secret     :", hr_secret)
    
    # Now Finance wants to send a "document" (message) securely
    message = 123  # Demo: numeric doc
    print("\nOriginal Message:", message)
    
    # Encrypt with HR's RSA public key
    hr_pubkey = manager.get_public_key("HR")
    cipher = rsa_encrypt(message, hr_pubkey)
    print("Encrypted with RSA:", cipher)
    
    # Decrypt with HR's private key
    hr_privkey = manager.get_private_key("HR")
    decrypted = rsa_decrypt(cipher, hr_privkey)
    print("Decrypted at HR:", decrypted)
    
    print("\nPerformance:")
    print("Key Generation Time: {:.6f}s".format(keygen_time))
    print("Key Exchange Time  : {:.6f}s".format(exchange_time))
    
    # Demonstrating scalability
    print("\n--- Adding New Subsystem: Analytics ---")
    manager.register_system("Analytics")
    
    # Demonstrating revocation
    print("\n--- Revoking HR system keys ---")
    manager.revoke_system("HR")
