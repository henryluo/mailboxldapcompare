# IMAP Mailbox and OpenLDAP comparison

A couple python scripts I've written to compare IMAP Mailbox names and OpenLDAP usernames to determine which Mailboxes are allowed to be deleted. 

## Preliminary Notes

Some scripts do multiple tasks, the most important one is testldapcompare.py, that's where most of the python LDAP integration exists.

The query to LDAP is pretty straight forward after installing the python-ldap module. Make sure you have the correct LDAP base DN and query, as to run scripts on the correct filter.

## Running the scripts

Must have a file named 
Scripts will probably be consolidated at some point, but for now, scripts should be run in this order:
```
1. testeverymailboxsize.py
2. testactivetomailbox.py
3. testldapcompare.py
```

## Built With

* Python 2.7
* python-ldap module 
* OpenLDAP 2.4 (Version shouldn't matter, only concerned with LDAP schema)

## Authors

* **Henry Luo** 
