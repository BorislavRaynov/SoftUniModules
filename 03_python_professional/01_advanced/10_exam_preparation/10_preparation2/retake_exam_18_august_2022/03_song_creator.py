def add_songs(*args):
    result = ''
    my_songs = {}

    for el in args:
        title = el[0]
        lyrics = el[1]
        if title not in my_songs:
            my_songs[title] = []
        my_songs[title].extend(lyrics)

    for name, lines in my_songs.items():
        if lines:
            result += f"- {name}\n"
            result += '\n'.join(lines)
            result += '\n'
        else:
            result += f"- {name}\n"

    return result


print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
