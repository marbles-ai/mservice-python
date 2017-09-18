from __future__ import unicode_literals, print_function
import unittest
import subprocess
import os
import signal
import time
import psutil


THISDIR = os.path.dirname(os.path.abspath(__file__))


class SvcTest(unittest.TestCase):

    def test_Run(self):
        daemon = subprocess.Popen(['python', os.path.join(THISDIR, 'mock_service.py'),
                                        '--log-level', 'debug'])
        # Wait for a bit
        time.sleep(10)
        # Check if success
        ps = psutil.Process(daemon.pid)
        os.kill(daemon.pid, signal.SIGINT)
        time.sleep(5)
        killed = False
        try:
            ps = psutil.Process(daemon.pid)
        except psutil.NoSuchProcess:
            killed = True
        self.assertTrue(killed)


if __name__ == '__main__':
    unittest.main()

