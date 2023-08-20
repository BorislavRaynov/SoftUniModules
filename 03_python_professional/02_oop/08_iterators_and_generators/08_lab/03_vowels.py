class vowels:

    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']

    def __init__(self, text: str):
        self.text = text
        self.vowels_in_text = [v for v in self.text if v.lower() in vowels.VOWELS]

    def __iter__(self):
        return self

    def __next__(self):
        if not self.vowels_in_text:
            raise StopIteration

        return self.vowels_in_text.pop(0)


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
