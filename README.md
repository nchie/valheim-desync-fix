# Valheim desync fix

Python script to apply patch which fixes the server lag/desyncs. 

This assumes that the server is installed through LGSM, and the script is in the home-folder of the user where `vhserver` is installed. It should be usable for other types of installs, but you'll likely need to change the hardcoded path.

The script will likely stop working if they update the m_dataPerSec variable from 61440.
