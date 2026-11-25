import os

MAX_CHARS = 200

PART1 = "In the event of a service outage lasting "
PART2 = "more than seventy-two (72) hours, the user "
PART3 = "is entitled to one (1) apology goat, "
PART4 = "redeemable in person, while stocks last."
LINE = PART1 + PART2 + PART3 + PART4

assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be exactly one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
