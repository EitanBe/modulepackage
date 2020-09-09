# bar.py

from . import foo

__all__ = ['Bar']

class Basr(object):
  pass
print ('bar imported')

# bash $ python3 -m spam.bar
# vs
# bash $ python3 spam/bar.py
