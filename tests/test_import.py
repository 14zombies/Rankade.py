import importlib
import sys
import unittest
from types import ModuleType


class TestImport(unittest.TestCase):
    def _import(self, name: str) -> ModuleType:
        module = importlib.import_module(name)

        try:
            sys.modules.pop(name)
        finally:
            del module

    def test_import(self):
        self._import("rankade")


if __name__ == "__main__":
    unittest.main()
