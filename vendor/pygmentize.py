#!/usr/bin/env python2.6

import sys, pygments.cmdline
try:
    sys.exit(pygments.cmdline.main(sys.argv))
except KeyboardInterrupt:
    sys.exit(1)
