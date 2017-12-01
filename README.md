# watch_dog
Package to detect when your data acquisition is interrupted.

watch_dog is run on local computer, it checks watch_pup's text for interruption signals over ssh.
watch_pup is run on data acquisition computer, it checks that data is being acquired  and updates a text.
watch_dog_reset and watch_pup_reset are used to reset each code when data acquisition starts.
siren.wav is just an arbitrary loud sound to warn you when data is interrupted, replace if you like.

To do this, copy over watch_pup and watch_pup_reset to data acquisition computer.
watch_pup constantly checks to see if data is continually updated once it is run, outputs results in log.
watch_pup_reset deletes old log and starts new log.
watch_dog constantly checks watch_pup's log for updates, and logs its own results, runs siren when interrupt detected.
watch_dog_reset and watch_pup_reset just deletes old log and starts new log.
