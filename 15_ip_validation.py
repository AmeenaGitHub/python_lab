# 15 Input validation
import re

# Regular expression patterns
email_pattern = r"^[\w.+-]+@[\w-]+(\.[\w-]+)*\.[a-zA-Z]{2,}$"
phone_pattern = r"^(\+91[- ]?)?[6-9]\d{9}$"   # Indian mobile number
txn_pattern = r"TXN\d{6,10}"                  # e.g. TXN458921

# 1. Email validation
emails = ["amit@gmail.com", "riya.s@mail.co.in", "john@mail", "sara@@gmail.com", "bad email@x.com"]
print("--- Email Validation ---")
for e in emails:
    print(f"{e:<20}", "Valid" if re.match(email_pattern, e) else "Invalid")

# 2. Phone number validation
phones = ["9876543210", "+91 9123456780", "1234567890", "98765", "+91-98765ABCDE"]
print("\n--- Phone Validation ---")
for p in phones:
    print(f"{p:<20}", "Valid" if re.match(phone_pattern, p) else "Invalid")

# 3. Extract transaction IDs from logs
log = """
2026-10-26 10:15:02 INFO  Payment success TXN458921 user=amit
2026-10-26 10:16:45 ERROR Payment failed  TXN458922 user=riya
2026-10-26 10:18:10 INFO  Refund processed TXN90817345 user=john
2026-10-26 10:20:31 INFO  Login success user=sara
"""
print("\n--- Transaction IDs Found ---")
ids = re.findall(txn_pattern, log)
print(ids)
print("Total:", len(ids))