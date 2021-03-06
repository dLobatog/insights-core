"""
dirsrv_sysconfig - file ``/etc/sysconfig/dirsrv``
=================================================

This module provides the ``DirsrvSysconfig`` class parser, for reading the
options in the ``/etc/sysconfig/dirsrv`` file.

Sample input::

    # how many seconds to wait for the startpid file to show
    # up before we assume there is a problem and fail to start
    # if using systemd, omit the "; export VARNAME" at the end
    #STARTPID_TIME=10 ; export STARTPID_TIME
    # how many seconds to wait for the pid file to show
    # up before we assume there is a problem and fail to start
    # if using systemd, omit the "; export VARNAME" at the end
    #PID_TIME=600 ; export PID_TIME
    KRB5CCNAME=/tmp/krb5cc_995
    KRB5_KTNAME=/etc/dirsrv/ds.keytab

Examples:

    >>> dirsrv_conf = shared[DirsrvSysconfig]
    >>> dirsrv.KRB5_KTNAME
    '/etc/dirsrv/ds.keytab'
    >>> 'PID_TIME' in dirsrv.data
    False

"""

from .. import parser, SysconfigOptions
from insights.specs import Specs


@parser(Specs.dirsrv)
class DirsrvSysconfig(SysconfigOptions):
    """
    Parse the `dirsrv` service's start-up configuration.
    """
    set_properties = True
