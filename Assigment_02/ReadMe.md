# Media Library Hub

## Overview
The Media Library Hub is a Python application designed to manage and organize various forms of digital media, such as songs, podcasts, and audiobooks. It reads data dictionaries, validates the input, and instantiates the correct media objects. The application allows users to add these items to playlists and subsequently manage those playlists within a centralized library. It uses a robust architecture to calculate overall statistics, publish events upon modifying playlists, sort items flexibly by title or duration, and export catalog data into a structured CSV format.

## How to Run
To run the project locally, ensure you have Python installed, navigate to the directory containing the file, and run:
`python media_library.py`

## Object-Oriented Programming Example
The application strongly leverages **Composition**. A prime example is the relationship between the `Library` and `Playlist` classes, as well as `Playlist` and `MediaItem`. A `Playlist` "has" multiple `MediaItem` objects stored in a list, and the `Library` "has" multiple `Playlist` objects. The library calculates its total duration dynamically by delegating the calculation down to the items contained inside its playlists.

## Design Pattern Example
The **Strategy Pattern** is utilized to handle the sorting of items inside a playlist. Instead of hardcoding sorting algorithms into the `Playlist` class, we implemented separate strategy classes (`SortByTitle` and `SortByDuration`). The playlist holds a reference to a strategy interface, allowing the sorting behavior to be injected and changed dynamically at runtime without altering the playlist's core code.

## Sample Output
```text
Song: Bohemian Rhapsody by Queen [Rock] (354s)
Song: Blinding Lights by The Weeknd [Pop] (200s)
Podcast: Lex Fridman #400 by Lex Fridman [Episode 400] (7200s)
Audiobook: Clean Code by Robert Martin [17 chapters] (25200s)

--- Statistics ---
{'total_items': 4, 'total_duration': 33054}

--- Action Log ---
['added:Bohemian Rhapsody', 'added:Blinding Lights', 'added:Lex Fridman #400', 'added:Clean Code']
