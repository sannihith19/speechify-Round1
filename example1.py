import re
from collections import Counter
# === Speechify Mock Test: SSML Parsing ===

ssml = """
<speak>
  <prosody rate="fast">This is a <emphasis>sample</emphasis> test to check <emphasis level='strong'>attention</emphasis>.</prosody>
  <prosody pitch="-5%">Make sure you remove all <emphasis>tags</emphasis> but not their text.</prosody>
  <prosody volume="loud">Consistency is the <emphasis>key</emphasis> to success.</prosody>
  <p>This should <emphasis>not</emphasis> be counted.</p>
</speak>
"""

# === Your Tasks ===
# Task 1: Extract only <prosody> tag content (ignore other tags like <p>)
# Task 2: Remove nested tags but keep their text
# Task 3: Print:
#   - Total number of words
#   - Number of unique words
#   - All words with highest frequency

# Write your solution below:

task1 = re.findall(r"<prosody[^>]*>(.*?)</prosody>", ssml)
print("Task 1: ", task1)

task2 = [re.sub(r"<[^>]*>", "", t) for t in task1] 
print("Task 2: ", task2)

words = " ".join(task2).split()
max_freq = max(Counter(words).values())

print("Task 3:")
print("Total number of words: ", len(words))
print("Number of unique words: ", len(set(words)))
print("All words with highest frequency: ", [val for val, freq in Counter(words).items() if freq == max_freq])
