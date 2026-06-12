from abc import ABC, abstractmethod

MEDIA_DATA = [
    {"type": "song", "title": "Bohemian Rhapsody", "creator": "Queen", "duration": 354, "genre": "Rock"},
    {"type": "song", "title": "Blinding Lights", "creator": "The Weeknd", "duration": 200, "genre": "Pop"},
    {"type": "podcast", "title": "Lex Fridman #400", "creator": "Lex Fridman", "duration": 7200, "episode_number": 400},
    {"type": "audiobook", "title": "Clean Code", "creator": "Robert Martin", "duration": 25200, "chapters": 17},
]


# ==========================================
# B1 — OOP Hierarchy
# ==========================================
class MediaItem(ABC):
    def __init__(self, title, creator, duration):
        if not title or not creator:
            raise ValueError("Title and creator cannot be empty.")
        if duration <= 0:
            raise ValueError("Duration must be greater than 0.")

        self.title = title
        self.creator = creator
        self.duration = duration

    @abstractmethod
    def describe(self):
        pass


class Song(MediaItem):
    def __init__(self, title, creator, duration, genre):
        super().__init__(title, creator, duration)
        self.genre = genre

    def describe(self):
        return f"Song: {self.title} by {self.creator} [{self.genre}] ({self.duration}s)"


class Podcast(MediaItem):
    def __init__(self, title, creator, duration, episode_number):
        super().__init__(title, creator, duration)
        self.episode_number = episode_number

    def describe(self):
        return f"Podcast: {self.title} by {self.creator} [Episode {self.episode_number}] ({self.duration}s)"


class Audiobook(MediaItem):
    def __init__(self, title, creator, duration, chapters):
        super().__init__(title, creator, duration)
        self.chapters = chapters

    def describe(self):
        return f"Audiobook: {self.title} by {self.creator} [{self.chapters} chapters] ({self.duration}s)"


# ==========================================
# B4 — Observer Pattern
# ==========================================
class EventBus:
    def __init__(self):
        self._subscribers = {}

    def subscribe(self, event, callback):
        if event not in self._subscribers:
            self._subscribers[event] = []
        self._subscribers[event].append(callback)

    def publish(self, event, payload):
        for callback in self._subscribers.get(event, []):
            callback(payload)


# ==========================================
# B5 — Strategy Pattern
# ==========================================
class SortByTitle:
    def sort(self, items):
        return sorted(items, key=lambda x: x.title.lower())


class SortByDuration:
    def sort(self, items):
        return sorted(items, key=lambda x: x.duration)


# ==========================================
# B2 — Composition
# ==========================================
class Playlist:
    def __init__(self, name, event_bus=None):
        self.name = name
        self._items = []
        self._event_bus = event_bus
        self._sort_strategy = None

    def add_item(self, item):
        if not isinstance(item, MediaItem):
            raise TypeError("Only MediaItem instances can be added.")
        self._items.append(item)
        if self._event_bus:
            self._event_bus.publish("item_added", {"title": item.title})

    def total_duration(self):
        return sum(item.duration for item in self._items)

    def __len__(self):
        return len(self._items)

    def set_sort_strategy(self, strategy):
        self._sort_strategy = strategy

    def items_sorted(self):
        if not self._sort_strategy:
            return self._items
        return self._sort_strategy.sort(self._items)


class Library:
    def __init__(self, name):
        self.name = name
        self._playlists = []

    def add_playlist(self, playlist):
        self._playlists.append(playlist)

    def statistics(self):
        total_items = sum(len(p) for p in self._playlists)
        total_duration = sum(p.total_duration() for p in self._playlists)
        return {"total_items": total_items, "total_duration": total_duration}


# ==========================================
# B3 — Factory Method
# ==========================================
def load_items(data):
    items = []
    for record in data:
        t = record.get("type")
        if t == "song":
            items.append(Song(record["title"], record["creator"], record["duration"], record["genre"]))
        elif t == "podcast":
            items.append(Podcast(record["title"], record["creator"], record["duration"], record["episode_number"]))
        elif t == "audiobook":
            items.append(Audiobook(record["title"], record["creator"], record["duration"], record["chapters"]))
        else:
            raise ValueError(f"Unknown media type: {t}")
    return items


# ==========================================
# B6 — Template Method
# ==========================================
class CatalogExporter(ABC):
    def export(self, rows):
        header = self.format_header()
        body = self.format_rows(rows)
        return header + body

    @abstractmethod
    def format_header(self):
        pass

    @abstractmethod
    def format_rows(self, rows):
        pass


class CsvCatalogExporter(CatalogExporter):
    def format_header(self):
        return "type,title,duration\n"

    def format_rows(self, rows):
        lines = []
        for row in rows:
            lines.append(f"{row['type']},{row['title']},{row['duration']}")
        return "\n".join(lines)


# ==========================================
# B6 — Facade
# ==========================================
def run_media_hub():
    # 1. Load items using Factory
    items = load_items(MEDIA_DATA)

    # Polymorphism demo
    for item in items:
        print(item.describe())

    # 2. Composition Setup & 3. Observer Setup
    event_bus = EventBus()
    action_log = []

    # Subscribe to event bus
    event_bus.subscribe("item_added", lambda p: action_log.append(f"added:{p['title']}"))

    my_playlist = Playlist("My Favorites", event_bus)
    for item in items:
        my_playlist.add_item(item)

    my_library = Library("Main Library")
    my_library.add_playlist(my_playlist)

    # 4. Print Outputs
    print("\n--- Statistics ---")
    print(my_library.statistics())

    print("\n--- Action Log ---")
    print(action_log)

    print("\n--- Sorted by Title (Strategy) ---")
    my_playlist.set_sort_strategy(SortByTitle())
    sorted_titles = [item.title for item in my_playlist.items_sorted()]
    print("Sorted: " + " | ".join(sorted_titles))

    print("\n--- CSV Export (Template Method) ---")
    exporter = CsvCatalogExporter()
    rows = [{"type": type(item).__name__, "title": item.title, "duration": item.duration} for item in items]
    print(exporter.export(rows))


if __name__ == "__main__":
    run_media_hub()
