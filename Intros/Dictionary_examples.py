d = {} # empty dictionary
eng_to_spa = {"one":"uno", "two":"dos", "three":"tres"}
print(eng_to_spa)
eng_to_spa["i"] = "yo"
eng_to_spa["am"] = "soy"
eng_to_spa["spanish"] = "espanol"
print(eng_to_spa)
sentence = "i am spanish"
words = sentence.split()
for word in words:
    print(eng_to_spa[word])
eng_to_spa.update({"yes":"si", "no":"no"})
print(eng_to_spa)
del eng_to_spa["no"] # to take things out the dictionary
print(eng_to_spa)

# print(eng_to_spa.popitem()) # not that useful as its hard to know in which position each item is in
print(eng_to_spa.pop("two")) # much better to pop the value out using its key rather than position

if "tree" in eng_to_spa:
    print(eng_to_spa["tree"])
else:
    print("i dont know that word")

print(eng_to_spa.get("tree", "unknown word"))

for key in eng_to_spa:
    print(f"{eng_to_spa[key]} means {key}")

for key, value in eng_to_spa.items():