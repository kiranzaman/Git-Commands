from typing import Final
import io
import unittest
from contextlib import redirect_stdout
import sys

"""
hello_world.py

Some change in file

Simple, testable "Hello, World!" example following best practices:
- Pure function that returns a string
- Small CLI entrypoint that prints
- Built-in unit tests using unittest (run with: python hello_world.py test)
"""


MESSAGE: Final[str] = "Hello, World!"


def get_hello_world() -> str:
    """Return the canonical hello world message."""
    return MESSAGE


def main() -> None:
    """Print the hello world message to stdout."""
    print(get_hello_world())


class HelloWorldTests(unittest.TestCase):
    def test_get_hello_world_returns_expected_string(self) -> None:
        self.assertEqual(get_hello_world(), MESSAGE)

    def test_main_prints_message(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            main()
        # strip to avoid failing on trailing newline differences
        self.assertEqual(buffer.getvalue().strip(), MESSAGE)


if __name__ == "__main__":

    # Run tests if invoked with "test" argument, otherwise run the CLI.
    if "test" in sys.argv:
        unittest.main(argv=[sys.argv[0]])
    else:
        main()