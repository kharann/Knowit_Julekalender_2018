EmojiInput = "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎"

def findShiftNumb():
    emojiCounter = {}
    for emoji in EmojiInput:
        emojiCounter[emoji] = emojiCounter.get(emoji,0) + 1
    mostFrequent_emoji = max(emojiCounter, key = emojiCounter.get)
    shiftNumb = ord(mostFrequent_emoji) - ord(" ")
    return shiftNumb



def decodeEmojis():
    Emojis = sorted(list(set(EmojiInput)))
    EmojiCode = [ord(emoji) for emoji in Emojis]
    Emoji_dict = dict([(chr(i),chr(i - findShiftNumb())) for i in EmojiCode])
    return Emoji_dict
Emoji_dict = decodeEmojis()

answer = ""
for emoji in EmojiInput:
    answer += Emoji_dict[emoji]
print(answer)

print(ord("A"))