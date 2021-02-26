#!/bin/python3

import os

file_path = "./serverfiles/valheim_server_Data/Managed/assembly_valheim.dll"

input_file = open(file_path,"rb")
input_data = input_file.read()
input_file.close()

original_signature = b'\x20\x00\xF0\x00\x00'
patch_signature = b'\x20\x00\x00\x04\x00'

signature_count = input_data.count(original_signature)

if signature_count < 1:
    print("Aborting, signature not found!")
elif signature_count > 1:
    print("Aborting, signature found more than once")
elif signature_count == 1:
    output_data = input_data.replace(original_signature, patch_signature)

    backup_file_path = "%s.original" % file_path
    print("Renaming %s to %s" % (file_path, backup_file_path))
    os.rename(file_path, backup_file_path)

    print("Creating new patched file %s" % file_path)
    f_new = open(file_path, "wb")
    f_new.write(output_data)
    f_new.close()

    print("Updating permissions on %s" % file_path)
    os.chmod(file_path, 0o775)

