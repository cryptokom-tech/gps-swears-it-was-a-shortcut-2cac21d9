"""The GPS Swears It Was a Shortcut — entry program.

The GPS, caught red-handed after sending the driver down the wrong
road, defends itself in its own voice: it did not take a wrong turn,
it took a shortcut the road has not finished yet. The map drew the
bridge; the river just drew the lake first. The blame lands on the
map, the lake gets the last word, and the GPS stays smug throughout.
"""

import os

# The excuse, in pieces so the setup and the punchline stay readable.
# The first beat reframes the wrong turn as an unfinished shortcut;
# the second beat is the turn the reader does not see coming: the
# river drew the lake first, so the map is innocent and so is the GPS.
SETUP = "I didn't take a wrong turn, I took a shortcut the road hasn't finished yet."
PUNCHLINE = "The map drew the bridge; the river just drew the lake first."

EXCUSE = " ".join([SETUP, PUNCHLINE])


def check(excuse: str) -> str:
    """The gate wants 1 to 200 characters of real text, no more."""
    text = excuse.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError("excuse must be 1 to 200 characters, got %d" % len(text))
    if text != text.split("\n")[0]:
        raise ValueError("excuse must stay one line")
    return text


def main() -> None:
    text = check(EXCUSE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote %d characters to /output/entry.txt" % len(text))


if __name__ == "__main__":
    main()
