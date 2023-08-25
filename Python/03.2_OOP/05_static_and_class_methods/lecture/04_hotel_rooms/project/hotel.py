from project.room import Room


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

# The class should have 5 more methods:
# • from_stars(stars_count: int) - creates a new instance with name "{stars_count} stars Hotel"
#• add_room(room: Room) - adds the room to the list of rooms
# • take_room(room_number, people) - finds the room with that number and tries to accommodate the guests in the room
# • free_room(room_number) - finds the room with that number and tries to free it
# • status() - returns information about the hotel in the following format:
# "Hotel {name} has {guests} total guests
# Free rooms: {numbers of all free rooms separated by comma and space}
# Taken rooms: {numbers of all taken rooms separated by comma and space}"

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        # II:
        # room = [r for r in self.rooms if r.number == room_number][0]
        # room.take_room(people)
        # self.guests += people
        for room in self.rooms:
            if room.number == room_number:
                self.guests += people
                # room.take_room(people)  # < -- here we need to put return, so the print isn't empty
                return room.take_room(people)

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                # room.free_room()  # < -- here we need to put return, so the print isn't empty
                self.guests -= room.guests
                return room.free_room()

    def status(self):
        result = f"Hotel {self.name} has {self.guests} total guests\n"
        result += f"Free rooms: {', '.join([str(room.number) for room in self.rooms if not room.is_taken])}\n"
        result += f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken])}"
        return result




