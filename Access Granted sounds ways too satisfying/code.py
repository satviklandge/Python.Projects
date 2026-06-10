import time
import sys

print("""
╔══════════════════════╗
║  FINGERPRINT SCAN   ║
╚══════════════════════╝
""")

input("Place Finger And Press Enter...")

for i in range(101):
    sys.stdout.write(f"\rScanning: {i}% ")
    sys.stdout.flush()
    time.sleep(0.03)

print("\nFingerprint Detected ✓")
time.sleep(1)

for msg in [
    "Reading Biometric Data...",
    "Matching Records...",
    "Identity Verified..."
]:
    print(msg)
    time.sleep(1.5)

print("\n🔓 ACCESS GRANTED")