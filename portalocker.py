import os
import fcntl
from fcntl import LOCK_EX, LOCK_SH, LOCK_NB

if os.name == 'posix':
    def lock(file, flags):
        fcntl.flock(file.fileno(  ), flags)

    def unlock(file):
        fcntl.flock(file.fileno(  ), fcntl.LOCK_UN)
else:
    raise RuntimeError("PortaLocker only defined for nt and posix platforms")
