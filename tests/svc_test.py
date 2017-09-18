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
        daemon.send_signal(signal.SIGINT)
        daemon.wait()
        self.assertTrue(daemon.returncode == 0)

if __name__ == '__main__':
    unittest.main()

