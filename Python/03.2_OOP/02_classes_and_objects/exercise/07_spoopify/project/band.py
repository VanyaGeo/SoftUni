from project.album import Album
from project.song import Song


class Band:
    def __init__(self, name: str):
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        # if album.name in self.albums:
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."

        self.albums.append(album)
        # self.albums.append(album.name)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        for current_album in self.albums:
            print(current_album)
            print(current_album.name)
            if current_album.name == album_name:

                if not current_album.published:
                    self.albums.remove(current_album)
                    return f"Album {current_album.name} has been removed."

                return f"Album has been published. It cannot be removed."

        return f"Album {album_name} is not found."

    def details(self):
        result = [f"Band {self.name}"]
        for album in self.albums:
            result.append(f"{album.details()}")

        return "\n".join(result)


