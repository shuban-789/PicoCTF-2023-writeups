# PicoCTF 2023 Reverse Engineering: Ready Gladiator 1 - 200 points

## Background
PicoCTF is an annual cybersecurity competition held by professionals from Carnegie Mellon University which challenges competitors’ problem solving skills with various tasks with the objective to obtain a flag to get points. Each task has a slight description, followed with an instance button or a file. With the goal in mind of getting the flag, the competitor must exploit computer related vulnerabilities to extract the flag even though it may seem impossible at first in some cases.

## Ready Gladiator 2 Intro (WARNING: This builds off of Ready Gladiator 0, so if you have not read that writeup, check it out)
Scenario and important info
![glad2](https://cdn.discordapp.com/attachments/803021452797411348/1087124683201204264/image.png)

Free hint!

![hint](https://cdn.discordapp.com/attachments/803021452797411348/1087125696901558352/image.png)

Same thing as Ready Gladiator 0 but now we want to beat the pulp out of our opponent

## Phase 1: Finding a worthy warrior
For Ready Gladiator 0, reading the docs was somewhat crucial to get an idea of how a CoreWars warrior is coded. But if you went in depth, you would see different strategies (some main ones I found being Rock, Paper, and Scissors). The hint says that there might be a worthy CoreWars warrior in the docs. Now trust me, I am no script kiddie, but if the hint itself says the warrior we are looking for is in the docs, you bet im searching for that warrior. After what felt like days, I finally found the chosen warrior. Behold, the knight of shadow clones, a certified Paper strategy (meaning it clones itself in the core and has a process for every clone using `spl`), silk.
```
;name silk
      spl     1
      mov     -1,       0
      spl     1

paper spl     @paper,   2364
      mov.i   }paper,   >paper
      mov.i   bmb,      >paper
      mov.i   bmb,      {-61
      mov.i   bmb,      {4000
silk  jmp     @0,       {paper
bmb   dat.f   <2667,    <2*2667
```

## Phase 2: Ez dubs
![dub](https://cdn.discordapp.com/attachments/803021452797411348/1087127755721822310/image.png)
