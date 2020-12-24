import json
import tempfile
import os
import argparse


parser = argparse.ArgumentParser(description='My key-value storage')
parser.add_argument('--key', type=str, help='Key')
parser.add_argument('--val', type=str, default=None, help='Value (default: None)')
my_args = parser.parse_args()


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if os.path.exists(storage_path):
    with open(storage_path, 'r') as f:
        storage_dict = json.loads(f.read())
else:
    storage_dict = dict()
if my_args.val:
    if my_args.key in storage_dict:
        storage_dict[my_args.key] += (', ' + my_args.val)
    else:
        storage_dict[my_args.key] = my_args.val
    with open(storage_path, 'w') as f:
        f.write(json.dumps(storage_dict))
else:
    print(storage_dict.get(my_args.key, None))
