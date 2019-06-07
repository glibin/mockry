# flake8: noqa
import subprocess
import sys
import unittest

_import_everything = b"""
# The event loop is not fork-safe, and it's easy to initialize an asyncio.Future
# at startup, which in turn creates the default event loop and prevents forking.
# Explicitly disallow the default event loop so that an error will be raised
# if something tries to touch it.
import asyncio
asyncio.set_event_loop(None)

import mockry.version
import mockry.app
import mockry.handler
import mockry.processor
import mockry.processor.csv_processor
"""


class ImportTest(unittest.TestCase):
    def test_import_everything(self):
        # Test that all Mockry modules can be imported without side effects,
        # specifically without initializing the default asyncio event loop.
        # Since we can't tell which modules may have already beein imported
        # in our process, do it in a subprocess for a clean slate.
        proc = subprocess.Popen([sys.executable], stdin=subprocess.PIPE)
        proc.communicate(_import_everything)
        self.assertEqual(proc.returncode, 0)
