class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]
        self.max_photos = pages * 4

    @classmethod
    def from_photos_count(cls, photos_count: int):
        return cls((photos_count // 4) + (photos_count % 4))

    def add_photo(self, label):
        current_photos = sum(len(page) for page in self.photos)
        if current_photos < self.max_photos:
            for x in self.photos:
                if len(x) > 3:
                    continue
                else:
                    x.append(label)
                    page = 0
                    slot = 0
                    for p in range(len(self.photos)):
                        for c in range(len(self.photos[p])):
                            if self.photos[p][c] == label:
                                page = p + 1
                                slot = c + 1
                    return f"{label} photo added successfully on page {page} slot {slot}"
        return "No more free slots"

    def display(self):
        result = ""

        for page in self.photos:
            page_as_string = len(page) * "[] "
            result += f"{'-' * 11}\n" + page_as_string.rstrip() + '\n'

        result += f"{'-' * 11}"
        return result


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
