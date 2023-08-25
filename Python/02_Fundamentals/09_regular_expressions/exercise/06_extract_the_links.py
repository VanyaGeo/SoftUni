import re

sentence = input()
pattern = r"(www\.[A-Za-z\d]+(\-[A-z\d]+)*(\.[a-z]+)+)"
result = []

while sentence:
    matches = re.findall(pattern, sentence)
    if matches:
        result.append(matches[0])
    sentence = input()

for email in result:
    print(email[0])


# Need information about cheap hotels in London?
# You can check us at www.london-hotels.co.uk !
# We provide the best services in London.
# Here are some reviews in some blogs:
# London Hotels are awesome! - www.indigo.bloggers.com
# I am very satisfied with their services - ww.ivan.bg
# Best Hotel Services! - www.rebel21.sedecrem.moc
# www.weird_site.hit.bg