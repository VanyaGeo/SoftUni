from math import ceil


class PhotoAlbum:
    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [[] for i in range(self.pages)]
        print(len(self.photos))

    @classmethod
    def from_photos_count(cls, photos_count: int):  # -> дават ни се определен брой снимки, които да разпределим по страници
        pages = ceil(photos_count / 4)  # -> не можем да имаме повече от 4 снимки на страница
        return cls(pages)  # -> връща нужния брой страници за дадените снимки

    def add_photo(self, label: str):
        for r in range(len(self.photos)):  # ->  добавяме снимка, ако страницата е по-малка от 5 позиции
            if len(self.photos[r]) < 4:
                self.photos[r].append(label)

                return f"{label} photo added successfully on page {r + 1}" \
                       f" slot {len(self.photos[r])}"

        return "No more free slots"

    def display(self):
        result = "-----------\n"
        for page in self.photos:
            result += " ".join(["[]" for photo_name in page])
            result += "\n-----------\n"
        return result

# album = PhotoAlbum(2)
# print(album.add_photo("baby"))
# print(album.add_photo("first grade"))
# print(album.add_photo("eight grade"))
# print(album.add_photo("party with friends"))
# print(album.photos)
# print(album.add_photo("prom"))
# print(album.add_photo("wedding"))
# print(album.display())


