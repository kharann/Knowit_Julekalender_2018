EmojiInput = "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎"

def findShiftNumb():
    emojiCounter = {}
    for emoji in EmojiInput:
        emojiCounter[emoji] = emojiCounter.get(emoji,0) + 1

    mostFrequent_emoji = max(emojiCounter, key = emojiCounter.get)
    shiftNumb = ord(mostFrequent_emoji) - ord(" ")

    return shiftNumb
shiftNumb = findShiftNumb()

Emojis = sorted(list(set(EmojiInput)))
EmojiCode = [ord(emoji) for emoji in Emojis]
Emoji_to_letter = dict([(chr(i),chr(i -shiftNumb)) for i in EmojiCode])

print(Emoji_to_letter)

answer = ""
for emoji in EmojiInput:
    answer += Emoji_to_letter[emoji]
print(answer)
