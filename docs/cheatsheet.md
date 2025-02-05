---
title: Editor Cheatsheet
description: 
published: true
date: 2023-12-13T06:30:25.082Z
tags: 
editor: markdown
dateCreated: 2023-10-17T06:18:27.397Z
---

## Some Resources and Generators.

- **Logo Repository: <https://github.com/devicons/devicon/tree/master>**
- **For tables generation [Markdown Tables Generator](https://www.tablesgenerator.com/markdown_tables) and [Excel to HTML](https://tableconvert.com/excel-to-html)**
- **ASCII Diagrams Generator: <https://asciiflow.com/#/>**
- For PlantUML Diagrams: <https://www.planttext.com/>
- For Mermaid Diagrams: <https://mermaid.live/edit> and Documentation: <https://mermaid.js.org/intro/>
- **[Equation to Latex](https://editor.codecogs.com/)**
- **[Markdown Emojis](https://gist.github.com/rxaviers/7360908)**
- **[ASCII Text Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)** 
ANSI Figlet fonts are the best

```bash
# ANSI Shadow

██╗  ██╗███████╗██╗     ██╗      ██████╗     ███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗     
██║  ██║██╔════╝██║     ██║     ██╔═══██╗    ████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗    
███████║█████╗  ██║     ██║     ██║   ██║    ██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝    
██╔══██║██╔══╝  ██║     ██║     ██║   ██║    ██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗    
██║  ██║███████╗███████╗███████╗╚██████╔╝    ██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║    
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝ ╚═════╝     ╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝    
                                                                                                     
 ██████╗███████╗███████╗ █████╗ ██████╗                                                              
██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗                                                             
██║     █████╗  ███████╗███████║██████╔╝                                                             
██║     ██╔══╝  ╚════██║██╔══██║██╔══██╗                                                             
╚██████╗███████╗███████║██║  ██║██║  ██║                                                             
 ╚═════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝                                                  

```

## Insert Images

- **Insert Image**
```html
<br>
<center>

<img src=/path/image.png width=70% height=70%>

</center>
<br>
```

<details>
<summary><strong>Insert Images side by side</strong></summary>

```html
<center>

<p align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/cplusplus/cplusplus-original.svg" width="15%" />
  <img src="https://raw.githubusercontent.com/devicons/devicon/55609aa5bd817ff167afce0d965585c92040787a/icons/c/c-original.svg" width="15%" /> 
  <h1>C and C++ Language Notes</h1>
</p>

</center>

```

</details>


<details>
<summary><strong>Insert Images to the side</strong></summary>

```html
<div>
    <p style="float: left;"><img src="/assets/machine_learn/overfitting.png" width="75%x" border="1"></p>
    <p></p>
</div>
```

> image to the side doesn't work on GitHub, and instead, two columns in a table should be used. Example below

```html
<table style="width:100%" border="0">
<tr><td style="width:30%"><img src="/assets/machine_learn/underfit.png" border="1"></td><td>

Words here, image above. Edit 30% field for image sizing

</td></tr></table>
```

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

<br>

For **GitHub** especially, latex support seems to be a little sensitive, and to get full support, use `math` highlighting with a qouted code block.

```math
J(\vec{w}, b) = -\frac{1}{n}\sum_{i=1}^{n}[y^{(i)}\log(f_w,_b (\vec{x}^{(i)})) + (1 - y^{(i)})\log(1 - f_w,_b (\vec{x}^{(i)}))]
```

> Note that using `math` highlighting with a quoted code block does not work in **Wiki.js**

General guidelines
- Use a newline between regular text and `$$` block
- With matrices, try to not use too many new lines

<br>
<br>

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



## Obsidian Specific
### Canvas
Main page: <https://obsidian.md/canvas>

