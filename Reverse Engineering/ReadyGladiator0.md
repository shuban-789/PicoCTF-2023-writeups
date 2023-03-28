# PicoCTF 2023 Reverse Engineering: Ready Gladiator 0 - 100 points

## Background
PicoCTF is an annual cybersecurity competition held by professionals from Carnegie Mellon University which challenges competitors’ problem solving skills with various tasks with the objective to obtain a flag to get points. Each task has a slight description, followed with an instance button or a file. With the goal in mind of getting the flag, the competitor must exploit computer related vulnerabilities to extract the flag even though it may seem impossible at first in some cases.

## Ready Gladiator 0 Intro
Scenario and important info

![scen](https://cdn.discordapp.com/attachments/803021452797411348/1087117731255570645/image.png)

### Takeaways:
* Our opponent is the imp
* We are inputting our corewars warrior (a .red file) to the netcat
* We need to lose all 100 games

### Questions I asked myself:
* What the heck is a corewar
* What the heck is a corewars warrior
* What the heck is an imp

## Phase 1: What the heck do I do?
When in doubt, we use Google.

![google](https://cdn.discordapp.com/attachments/803021452797411348/1087118842913902632/image.png)

### Takeaways:
* Our .red file is basically a list of attributes for our corewars warrior
* This is basically our code battling the imp, which is a type of warrior

## Phase 2: Building our loser
First to understand what our warrior code did, I went to the documentation (https://corewar-docs.readthedocs.io/en/latest/). According to the docs, ";" is a comment, "mov" is move, "end" ends the program. Without even knowing what mov does, what if we made a program that just ended. Ergo, here is our champ:
```
;redcode
;name good sport
;assert 1
end
```

## Phase 3: La Batalla  ⚔️
![battle](https://cdn.discordapp.com/attachments/803021452797411348/1087122187372204052/image.png)

He may have lost all those rounds, but in my eyes, he will always be a champion
