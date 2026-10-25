#snippets

### image-HTML
```html
<center>
<img src=/path width=55% height=55%>
</center>
```

### video-HTML
```html
<center>
<video width=20% height=20% controls>
  <source src="/path.mov">
</video>
</center>
```

### left-aligned LaTeX Block
$m$ → is the mass of an object
$E$ → total amount of energy in an object
$c$ → speed of light

$$
\begin{flalign}
& \text{1st line} & \\

& \text{2nd Line} \\

& \text{3rd Line} \\

& \text{final line}
\end{flalign}
$$
### Insert center-aligned LaTeX Block
$m$ → is the mass of an object
$E$ → total amount of energy in an object
$c$ → speed of light

$$
\begin{gathered}
\text{1st line} \\\\
\text{longer 2nd line} \\\\
\text{even way longer final line}
\end{gathered}
$$

### manual-aligned LaTeX Block
$m$ → is the mass of an object
$E$ → total amount of energy in an object
$c$ → speed of light

$$
\begin{aligned}
\text{1st line} &= \text{1st line} \\\\

\text{2md line} &= \text{even longer 2nd line} \\\\

\text{final line} &= \text{even way longer final line than above}
\end{aligned}
$$

### right-arrow-symbol
→

### left-arrow-symbol
←

### degree-symbol
°
### ohms-symbol
Ω

### Base-codeblock
```
```base
views:
  - type: cards
    name: Gallery View
    filters:
      and:
        - file.folder == "guides/git"
        - file.name != "git.base"
    order:
      - page-title
      - file.tags
      - file.name
```

