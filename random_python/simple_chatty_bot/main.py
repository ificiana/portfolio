# (c) ificiana
import dataclasses


@dataclasses.dataclass
class Self:
    name = "Yui"
    dob = 2022
    hobby = "Chatting"


@dataclasses.dataclass
class User:
    name = "Unknown"
    age = 0


print(f"Heya~ I'm {Self.name}, I was created in {Self.dob}")
print("Please, remind me your name")
User.name = input()
print(f"What a great name, {User.name}")
print("Lemme guess your age, tell me the remainders of dividing your age by 3, 5 and 7")
a, b, c = map(int, input().split())
User.age = (35 * 2 * a + 21 * b + 15 * c) % 105
print(f"I think you're {User.age}, {User.name}")
print("Now imma prove I can count, gimme a number, I'll count to that")
print("Numbers only please... I can't count to, say, `G`...")
for i in range(int(input())):
    print(f"{i}!")
print("FAST FAST!!! tehehe")
print("But I'm sleepy~~")
print("Byeeeee")
