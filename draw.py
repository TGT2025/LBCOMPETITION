import hashlib
import random

# === CONFIG ===
entries_file = r"C:\\Users\\TGT\\Desktop\\COMP\\entries.txt"  # Change path if needed
num_winners = 5

# === GET USER INPUT ===
timestamp_input = input("Enter a timestamp string (e.g. 2025-06-01 23:59:59 UTC): ").strip()
if not timestamp_input:
    print("❌ No input received. Aborting.")
    exit()

# === HASH INPUT TO SEED RNG ===
hash_digest = hashlib.sha256(timestamp_input.encode()).hexdigest()
print(f"\n🔐 SHA256 of timestamp: {hash_digest}")

seed_int = int(hash_digest, 16)
random.seed(seed_int)

# === LOAD ENTRIES ===
try:
    with open(entries_file, "r", encoding="utf-8") as f:
        entries = [line.strip() for line in f if line.strip() and len(line.strip()) == 24]
except FileNotFoundError:
    print(f"❌ Could not find file: {entries_file}")
    exit()

if len(entries) < num_winners:
    print("❌ Not enough entries to draw winners.")
    exit()

# === DRAW ===
winners = random.sample(entries, num_winners)

print("\n🎉 WINNERS:")
for idx, winner in enumerate(winners, 1):
    print(f"{idx}. {winner}")

print("\n✅ Draw complete. Anyone can verify this by using the same timestamp + entries.txt")