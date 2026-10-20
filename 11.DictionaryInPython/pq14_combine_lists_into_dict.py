"""
Q92. Combine Lists into Dictionary
You have two separate lists: one containing subject names and another containing
corresponding marks. Create a dictionary from these two
lists using dictionary comprehension, mapping each subject to its mark.
"""

subjects = ["english", "hindi", "maths"]
scores = [93, 92, 99]

sub_scores = {s: sc for s, sc in zip(subjects, scores)}
print(sub_scores)
