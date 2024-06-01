import random

text = f"""
<table><tr><td>
Розв'яжіть рівняння:<br>
<ol>
"""
answers = []

for i in range(20):
    x1 = random.randint(-10, 5)
    x2 = x1 + random.randint(1, 5)
    a = random.randint(1, 5) * random.choice([-1, 1])
    b = -a * (x1 + x2)
    c = a * x1 * x2

    if a == 1:
        a = 'x<sup>2</sup>'
    elif a == -1:
        a = '-x<sup>2</sup>'
    else:
        a = f"{a}x<sup>2</sup>"

    if b == 1:
        b = '+x'
    elif b == -1:
        b = '-x'
    elif b == 0:
        b = ''
    elif b > 0:
        b = f"+{b}x"
    else:
        b = f"{b}x"

    if c == 0:
        c = ''
    elif c > 0:
        c = f"+{c}x"
    else:
        c = f"{c}x"

    text += f"<li>{a}{b}{c}=0</li>"

    answers.append((x1, x2))

text += f"""
</ol></td><td>
Розв'язки:<br>
<ol>
"""

for i in range(20):
    text += f"<li>x<sub>1</sub>={answers[i][0]}; x<sub>2</sub>={answers[i][1]}</li>"

text += f"""
</ol></td></tr></table>
"""

with open('html.html', 'w') as f:
    f.write(text)
