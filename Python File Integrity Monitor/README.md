# Python File Integrity Monitor

I created a simple File Integrity Monitor that detects unauthorized changes to a file we are monitoring. It calculates the file’s hash and checks if it changes over time (every 5 seconds). If a change is detected, the event is logged, and it will tell you that there has been a change to the file.

This Python script:
- Watches a file called watched_file.txt
- Calculates its SHA-256 hash every 5 seconds
- Logs a warning if the file is modified
- Saves all changes in `logs/file_changes.log`

To run, simply run the file in your terminal!
