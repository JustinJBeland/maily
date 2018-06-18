# General overview
This repository contains a Python routine that allows a user to automatically send an e-mail to a specified account (ususally when a code is complete). 

This code works for a given gmail account. You may need to provide privileges that will compromise the security of your e-mail account.

Credit goes to:
http://naelshiab.com/tutorial-send-email-python/

## Dependencies
	1. smtplib -- put version here 
	2. email -- put version here

## Installation
You can add maily.py to your path by entering the following command

```
>>> python setup.py develop
```

If the setup is successful the you can try to import bo bo from another directory using the following command

```python
>>> from maily import *
```

## ToDo
	1. Send attachments (i.e. figures generated)
	2. Send flag messages
	3. Somehow send an email even if the code crashes indicating the crash and error message
	4. fix python setup.py install (python setup.py develop works)
