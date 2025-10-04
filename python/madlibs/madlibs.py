print(" Welcome to the Epic Mad Libs Adventure! \n")


name = input("Enter a name: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
place = input("Enter a magical place: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
food = input("Enter your favorite food: ")
emotion = input("Enter an emotion: ")
superpower = input("Enter a superpower: ")
magic_object = input("Enter a magical object: ")


story = f"""
Once upon a time, there was a {adjective1} hero named {name}, who lived in the distant land of {place}.
{name} had a loyal pet {animal}, who was small but incredibly {adjective2}.
Together, they would {verb1} across the hills and valleys in search of legendary adventures.

One day, they discovered a glowing {magic_object} hidden deep inside a cave.
As soon as {name} touched it, a beam of light shot into the sky, granting {name} the power of {superpower}!

Filled with excitement and {emotion}, {name} and the {animal} raced back home, only to find that their village
was being attacked by a giant broccoli monster!

With courage in their heart and hunger in their belly, {name} decided to fight using the power of {superpower} and a massive plate of {food}.
After an epic battle full of flips, kicks, and {verb2}-ing, the monster was defeated, and peace was restored.

The villagers cheered, threw a feast, and everyone lived happily ever after.
All thanks to the bravery of {name} and their amazing {animal}!

THE END.
"""


print("\n Your Mad Libs Story ")
print(story)
