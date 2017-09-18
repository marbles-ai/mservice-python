#!/usr/bin/env python
from __future__ import unicode_literals, print_function
import os
import sys
from optparse import OptionParser


# Modify python path
thisdir = os.path.dirname(os.path.abspath(__file__))
srcdir = os.path.dirname(thisdir)
sys.path.insert(0, srcdir)


from mservice import executor


class MockExecutor(executor.ServiceExecutor):

    def __init__(self, state):
        super(MockExecutor, self).__init__(wakeup=5*60, state_or_logger=state)

    def on_start(self, workdir):
        pass

    def on_term(self, graceful):
        pass


if __name__ == '__main__':
    usage = 'Usage: %prog [options]'
    parser = OptionParser(usage)
    executor.init_parser_options(parser)

    (options, args) = parser.parse_args()

    svc_name = os.path.splitext(os.path.basename(__file__))[0]
    stream_name = 'svc-' + svc_name
    state = executor.process_parser_options(options, svc_name, stream_name)

    svc = MockExecutor(state)
    svc.run(thisdir)
