# Part A — Identification

**Snippet 1: Encapsulation (OOP)**
This snippet demonstrates encapsulation by using the `@property` decorator to create a getter. It hides the internal state (`self._title`) from direct external modification, allowing for controlled access and potential future validation without changing the external interface.

**Snippet 2: Composition / Aggregation (OOP)**
This demonstrates composition (specifically aggregation), representing a "has-a" relationship. The `Library` class maintains a collection of `Playlist` objects within its own internal dictionary, managing them as parts of a larger whole.

**Snippet 3: Strategy (Pattern)**
This is the Strategy pattern. Instead of hardcoding the sorting logic directly inside the method, the class delegates the algorithm to an injected strategy object (`self._sort`), allowing the sorting behavior to be swapped at runtime.

**Snippet 4: Observer (Pattern)**
This is the Observer pattern (specifically a Publish-Subscribe mechanism). The `publish` method iterates through a list of subscribed callback functions (observers) mapped to an `event_name` and notifies them by passing the `payload` when the event occurs.
