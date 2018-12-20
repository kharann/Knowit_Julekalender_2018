const emoji_input = "😡😚😀😷😨😥😮😀😩😀😤😩😥😌😀😩😀😷😡😮😮😡😀😤😩😥😀😬😩😫😥😀😣😡😥😳😡😲😎😀😱😚😀😨😯😷😀😣😯😭😥😟😀😡😚😀😨😥😀😤😩😥😤😀😡😭😯😮😧😀😨😩😳😀😦😲😩😥😮😤😳😎";
const sortedEmojis= [...new Set(emoji_input)].sort()
const shiftNumb = sortedEmojis[0].codePointAt() - " ".charCodeAt();

let answer = [...emoji_input].map(emoji => String.fromCharCode(emoji.codePointAt() - shiftNumb))
console.log(answer.join(""))