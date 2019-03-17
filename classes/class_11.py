"""
Create follolwing pattern

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

  c
 bcb
cbabc


"""

number = 6
rows = list()
for i in range(1, number+1):
    sequence = list()
    space = list()
    for s in range(0, (number-i)*2):
        space.append("")
    chars = list()
    for j in range(0, i):
        chars.append(chr(96+number-j))
    sequence = space + chars + chars[::-1][1:] + space
    rows.append(sequence)
    print("-".join(sequence), end="")
    print("")

for i in rows[::-1][1:]:
    print("-".join(i))
