# PicoCTF 2023 Reverse Engineering: Ready Gladiator 2 - 400 points

## Background 
PicoCTF is an annual cybersecurity competition held by professionals from Carnegie Mellon University which challenges competitors’ problem solving skills with various tasks with the objective to obtain a flag to get points. Each task has a slight description, followed with an instance button or a file. With the goal in mind of getting the flag, the competitor must exploit computer related vulnerabilities to extract the flag even though it may seem impossible at first in some cases.

## Ready Gladiator 2 intro (WARNING: I highly reccomend you ready the writeups for Ready Gladiator problems 0 and 1):
![scenario](https://cdn.discordapp.com/attachments/803021452797411348/1087130159909441586/image.png)

So we are back at it again, except we need to win 100 times

## Phase 1: Previous warrior
Let's see if the warrior we used in Ready Gladiator 1 will work.

![test](https://cdn.discordapp.com/attachments/803021452797411348/1087131030542094407/image.png)

Close, but not close enough

## Phase 2: Warrior searching (again)
After this point, I was clueless on what code could beat the imp. I basically searched far and wide for any code which could beat it all 100 times. Until I came by a diamond in the rough. Behold, D-Clear with JMP/ADD Launch. The perfect warrior to beat up an imp. A mix of imp spiral and core-clear. Said to do well against imps.

![champ](https://cdn.discordapp.com/attachments/803021452797411348/1087132490088599713/image.png)

Lets test it out

![96](https://cdn.discordapp.com/attachments/803021452797411348/1087133360192770088/image.png)

Now that's close. The hint stated that if our warrior does not get 100 wins AND is very close, we must try to execute it again. 

![hint](https://cdn.discordapp.com/attachments/803021452797411348/1087133869632925797/image.png)

However, after executing it 10 times manually, I struck 99, but still no luck. That lead me to use my incredible BASH skills to the test

## Phase 3: Endgame 
![bash](https://cdn.discordapp.com/attachments/803021452797411348/1087134418730225745/image.png)
```
while :
do
	nc saturn.picoctf.net 63348 < imp.red
done
```

Now, we must let it run, and direct it to a file. In the mean time we can intensify the atmosphere with a bit of music.

![script](https://cdn.discordapp.com/attachments/803021452797411348/1087135513661673472/image.png)

https://www.youtube.com/watch?v=btPJPFnesV4

A few minutes have passed. It is time for the moment of truth.

![flag](https://cdn.discordapp.com/attachments/803021452797411348/1087136034611007619/image.png)

GG 🎮
