# bash$ python3 -m http.server

spam/
  __init__.py.  ------> import spam.core
  foo.py.       
  bar.py

test/
  __init__.py
  __main__.py  --------> python3 -m spam.test
  foo.py
  bar.py
 
 
 server/
  __init__.py
  __main__.py  --------> python3 -m spam.server
  
  
  
 ========================================================================
 
 spam/
  foo.py
  bar.py
  __main__.py
  
bash $ python3 spam --> will run the __main__.py
bash $ python3 -m zipfile -c spam.zip spam/*
