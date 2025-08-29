import random
import time
import logging
from datetime import datetime, timedelta

# =======================================
# Logging Setup (Auditing & Compliance)
# =======================================
logging.basicConfig(
    filename="kms_audit.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# =======================================
# Rabin Cryptosystem (Basic Version)
# =======================================
def is_prime(n, k=5):
    """ Miller-Rabin primality test (simple) """
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    # Fermat test
    for _ in range(k):
        a = random.randrange(2, n - 1)
        if pow(a, n-1, n) != 1:
            return False
    return True

def generate_large_prime(bits=128):
    while True:
        num = random.getrandbits(bits)
        if num % 4 == 3 and is_prime(num):
            return num

def generate_rabin_keys(bits=128):
    p = generate_large_prime(bits)
    q = generate_large_prime(bits)
    n = p * q
    return (n,), (p, q)   # Public, Private


# =======================================
# Key Management Service
# =======================================
class KeyManagementService:
    def __init__(self, key_size=128):
        self.key_size = key_size
        self.keys = {}  # { hospital_name : {public, private, expiry} }
    
    def register_hospital(self, name):
        pub, priv = generate_rabin_keys(self.key_size)
        expiry = datetime.now() + timedelta(days=365)  # 12 months
        self.keys[name] = {"public": pub, "private": priv, "expiry": expiry}
        logging.info(f"Key generated for {name}. Expiry: {expiry}")
        print(f"[KMS] Registered {name} with new Rabin keys.")
    
    def get_keys(self, name):
        if name in self.keys:
            logging.info(f"Keys distributed to {name}.")
            return self.keys[name]
        else:
            print("[KMS] Hospital not found.")
            return None
    
    def revoke_keys(self, name):
        if name in self.keys:
            del self.keys[name]
            logging.info(f"Keys revoked for {name}.")
            print(f"[KMS] Revoked keys for {name}.")
    
    def renew_keys(self, name):
        if name in self.keys:
            pub, priv = generate_rabin_keys(self.key_size)
            expiry = datetime.now() + timedelta(days=365)
            self.keys[name] = {"public": pub, "private": priv, "expiry": expiry}
            logging.info(f"Keys renewed for {name}. Expiry: {expiry}")
            print(f"[KMS] Renewed keys for {name}.")
    
    def auto_renew_all(self):
        for name in self.keys:
            if self.keys[name]["expiry"] <= datetime.now():
                self.renew_keys(name)
        logging.info("Automatic renewal process completed.")


# =======================================
# Demo Simulation
# =======================================
if __name__ == "__main__":
    kms = KeyManagementService(key_size=64)  # Small for demo
    
    # Register hospitals
    kms.register_hospital("Hospital_A")
    kms.register_hospital("Clinic_B")
    
    # Key Distribution
    keys_A = kms.get_keys("Hospital_A")
    print("Hospital A Public Key:", keys_A["public"])
    
    # Revocation
    kms.revoke_keys("Clinic_B")
    
    # Renewal
    kms.renew_keys("Hospital_A")
    
    # Auto Renewal (simulated)
    kms.auto_renew_all()
    
    print("\nAudit log written to kms_audit.log")
 