## Some Resources and Generators
- Logo Repository: <https://github.com/devicons/devicon/tree/master>
- For tables generation [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) and [Excel to HTML](https://tableconvert.com/excel-to-html)
- ASCII Diagrams Generator: <https://asciiflow.com/#/>
- For PlantUML Diagrams: <https://www.planttext.com/>
- For Mermaid Diagrams: <https://mermaid.live/edit> and Documentation: <https://mermaid.js.org/intro/>
- [Equation to Latex](https://editor.codecogs.com/)
- [Markdown Emojis](https://gist.github.com/rxaviers/7360908)
- [ASCII Text Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) 
    - ANSI Figlet fonts are the best

### Useful Characters/Symbols
- Right arrow →
- Left arrow ←
- Degree Symbol (°)
- Ohms symbol (Ω)

## Insert Images
Just **insert image** like markdown. Unlike markdown, this gives the option to change the sizing of the image.
```html
<br>
<center>

<img src=/path/image.png width=70% height=70%>

</center>
<br>
```


**Insert Images side by side**, but this might not work in all in Markdown reder engines (GitHub)

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/cplusplus/cplusplus-original.svg" width="15%" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/c/c-original.svg" width="15%" />
</p>

And some code
```html
<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/cplusplus/cplusplus-original.svg" width="15%" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/c/c-original.svg" width="15%" />
</p>
```

> image to the side doesn't work on GitHub, and instead, two columns in a table should be used. Example below

<table style="width:100%" border="0">
<tr><td style="width:30%"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/af/Dew_Formed_on_the_Surface_of_Strawberry_Leafs.jpg/1920px-Dew_Formed_on_the_Surface_of_Strawberry_Leafs.jpg" border="1"></td>

<td>
<strong>dew</strong> are the small droplets of water and condensation which appear on the surface of objects. It poses no risk to UAS

However, under freezing temperatures, dew will form <strong>frost</strong> which is a flight safety hazard, it can disrupt the flow of air over the wing and can reduce lift and increase drag. It must be cleaned off the UAS before
</td>

<td style="width:30%"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/D%C3%BClmen%2C_Hausd%C3%BClmen%2C_Distel_--_2021_--_5079.jpg/1920px-D%C3%BClmen%2C_Hausd%C3%BClmen%2C_Distel_--_2021_--_5079.jpg" border="1"></td>
</table>

And the code
```html
<table style="width:100%" border="0">
<tr>

<td style="width:30%"><img src="/assets/machine_learn/underfit.png" border="1"></td>
<td>Words here, image above. Edit 30% field for image sizing</td>

</tr>
</table>
```


More

## Earliest Finds

<table style="width:100%" border="0">
<tr><td style="width:30%"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b3/AMNH_3982_Manospondylus.jpg/330px-AMNH_3982_Manospondylus.jpg" border="1"></td><td>

A tooth from what is now documented as a *Tyrannosaurus rex* was found in July 1874 upon [South Table Mountain (Colorado)](https://en.wikipedia.org/wiki/South_Table_Mountain_(Colorado) "South Table Mountain (Colorado)") by [Jarvis Hall (Colorado)](https://en.wikipedia.org/wiki/Jarvis_Hall_(Colorado) "Jarvis Hall (Colorado)") student Peter T. Dotson under the auspices of Prof. [Arthur Lakes](https://en.wikipedia.org/wiki/Arthur_Lakes "Arthur Lakes") near [Golden, Colorado](https://en.wikipedia.org/wiki/Golden,_Colorado "Golden, Colorado").(https://en.wikipedia.org/wiki/Tyrannosaurus#cite_note-2) In the early 1890s, [John Bell Hatcher](https://en.wikipedia.org/wiki/John_Bell_Hatcher "John Bell Hatcher") collected postcranial elements in eastern [Wyoming](https://en.wikipedia.org/wiki/Wyoming "Wyoming"). The fossils were believed to be from the large species _[Ornithomimus grandis](https://en.wikipedia.org/wiki/Ornithomimus "Ornithomimus")_ (now _[Deinodon](https://en.wikipedia.org/wiki/Deinodon "Deinodon")_) but are now considered _T. rex_ remains.[](https://en.wikipedia.org/wiki/Tyrannosaurus#cite_note-quinlanetal2007-3)

</td></tr></table>


<table style="width:100%" border="0">
<tr>
    <td>
    A tooth from what is now documented as a *Tyrannosaurus rex* was found in July 1874 upon [South Table Mountain (Colorado)](https://en.wikipedia.org/wiki/South_Table_Mountain_(Colorado) "South Table Mountain (Colorado)") by [Jarvis Hall (Colorado)](https://en.wikipedia.org/wiki/Jarvis_Hall_(Colorado) "Jarvis Hall (Colorado)") student Peter T. Dotson under the auspices of Prof. [Arthur Lakes](https://en.wikipedia.org/wiki/Arthur_Lakes "Arthur Lakes") near [Golden, Colorado](https://en.wikipedia.org/wiki/Golden,_Colorado "Golden, Colorado").[[1]](https://en.wikipedia.org/wiki/Tyrannosaurus#cite_note-2) In the early 1890s, [John Bell Hatcher](https://en.wikipedia.org/wiki/John_Bell_Hatcher "John Bell Hatcher") collected postcranial elements in eastern [Wyoming](https://en.wikipedia.org/wiki/Wyoming "Wyoming"). The fossils were believed to be from the large species _[Ornithomimus grandis](https://en.wikipedia.org/wiki/Ornithomimus "Ornithomimus")_ (now _[Deinodon](https://en.wikipedia.org/wiki/Deinodon "Deinodon")_) but are now considered _T. rex_ remains.[](https://en.wikipedia.org/wiki/Tyrannosaurus#cite_note-quinlanetal2007-3)
    </td>
</tr> 

<tr><td style="width:30%"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9f/Tyrannosaurus_skeleton.jpg/330px-Tyrannosaurus_skeleton.jpg" border="1"></td><td>

</td></tr></table>


# Advanced Markdown

## Expandable Content

Use `<details>` and `<summary>` HTML tags to create an expandable drop down. Example below

<details><summary><strong>Toggle me!</strong></summary>Peek a boo!</details>

Works like this.
```html
<details><summary>Toggle me!</summary>Peek a boo!</details>
```

> add `<strong>` and `</strong>` tags to bold the drop down title

## Math with Latex

Use `$` for inline latex and `$$` for a Latex block. This works for **Wiki.js**, **VS Code** (using the Markdown Preview Enhanced Extension), and **GitHub**

$$
J(\vec{w}, b) = -\frac{1}{n}\sum_{i=1}^{n}[y^{(i)}\log(f_w,_b (\vec{x}^{(i)})) + (1 - y^{(i)})\log(1 - f_w,_b (\vec{x}^{(i)}))]
$$


For multi line, use `\begin{aligned}` and `\begin{gathered}`.

`\begin{aligned}`
- Not supported as well by GitHub
- Aligns to the right by default
- Can use `&` to align the lines, for example, `&=` to make sure that all equal sings are aligned

$$
\begin{aligned}
F_g &= G\frac{m_1 \times m_2}{r^2}\\\\

G \text{ (Universal Gravity Constant)} &= 6.674 \times 10^{-11} 
\text{N}\cdot\text{m}^{2}\text{\\kg}^{2}\\\\

\text{Could also be define as } &= 6.674 \times 10^{-11}\text{m}^3\text{kg}^{-1}\text{s}^{-2}
\end{aligned}
$$

`\begin{gathered}` 
- Better supported by GitHub
- Automatically aligns to the center
$$
\begin{gathered}
F_g = G\frac{m_1 \times m_2}{r^2} \\\\
G \text{ (Universal Gravity Constant)} = 6.674 \times 10^{-11} 
\text{N}\cdot\text{m}^{2}\text{\\kg}^{2} \\\\
\text{Could also be defined as } = 6.674 \times 10^{-11}\text{m}^3\text{kg}^{-1}\text{s}^{-2}
\end{gathered}
$$


For **GitHub** especially, latex support seems to be a little sensitive, and to get full support, use `math` highlighting with a qouted code block.

```math
J(\vec{w}, b) = -\frac{1}{n}\sum_{i=1}^{n}[y^{(i)}\log(f_w,_b (\vec{x}^{(i)})) + (1 - y^{(i)})\log(1 - f_w,_b (\vec{x}^{(i)}))]
```

> Note that using `math` highlighting with a quoted code block does not work in **Wiki.js**

General guidelines
- Use a newline between regular text and `$$` block
- With matrices, try to not use too many new lines

## Multiple Columns
- [ ] how to do two columns or more in a note


## Highlighted blocks
See of the block below which allow you to define errors, warnings, info, etc

> [!WARNING]
> warning message
>```shell
>sudo systemctl disable --now docker.service docker.socket
>sudo rm /var/run/docker.sock
>```
> more notes


> [!SUCCESS]
>
> success message

> [!ERROR]
> error message

> [!NOTE]
> standard note

> [!INFO]
> info message



# Diagrams
Use either `plantuml` or `mermaid` diagrams

```mermaid
flowchart LR
    A[Hard edge] -->|Link text| B(Round edge)
    B --> C{Decision}
    C -->|One| D[Result one]
    C -->|Two| E[Result two]
```

## Pie Chart
```mermaid
pie
    title Pie Chart
    "Dogs" : 386
    "Cats" : 85
    "Rats" : 150 
```

## Decision Tree Like
**Diagram with Title**
```mermaid
graph TD;
title[Cat Classifier Decision Tree]
id1(Ear Shape) ---|Pointy| id2(Face Shape);
id1(Ear Shape) ---|Floppy| id3(Whiskers);

id2(Face Shape) ---|Round| id4[Cat];
id2(Face Shape) ---|Not ROUND| id5[Not a Cat];

id3(Whiskers) ---|Present| id7[Cat];
id3(Whiskers) ---|Not Present| id8[Not a cat];
```

**Multiple Diagrams**

```mermaid
graph TD;
subgraph three [Decision Tree 3]
id12(face shape) ---|round| id16[cat];
id12(face shape) ---|not round| id13(whiskers);

id13(whiskers) ---|present| id14[cat];
id13(whiskers) ---|not present| id15[not a cat];
end

subgraph two [Decision Tree 2]
id6(ear shape) ---|pointy| id7(face shape);
id6(ear shape) ---|floppy| id8(whiskers);
id7(ear shape) ---|pointy| id9[cat];
id7(ear shape) ---|floppy| id10[not a cat];
id8(whiskers) ---|present| id11[cat];
id8(whiskers) ---|not present| id117[not a cat];
end

subgraph one [Decision Tree 1];
id1(whiskers) ---|present| id2(ear shape);
id1(whiskers) ---|absent| ids3[not cat];
id2(ear shape) ---|pointy| id4[cat];
id2(ear shape) ---|floppy| id5[not a cat];
end
```



