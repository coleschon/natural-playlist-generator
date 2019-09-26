from paramiko import SSHClient, AutoAddPolicy, RSAKey
from scp import SCPClient
import keyring
from numpy.core._internal import recursive
from data_reader import DataReader


def create_library():
    pkey_filename = '/Users/cole/.ssh/million-song-dataset.pem'
    pkey_password = keyring.get_password('SSH', pkey_filename)
    pkey = RSAKey.from_private_key_file(pkey_filename, password=pkey_password)
    ssh = SSHClient()
    ssh.set_missing_host_key_policy(AutoAddPolicy())
    ssh.connect('52.91.85.148', username='ubuntu', pkey=pkey)

    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
               'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters3 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    dr = DataReader()
    dr.reset_lib()
    import shutil
    for letter in letters:
        for letter2 in letters2:
            for letter3 in letters3:
                with SCPClient(ssh.get_transport()) as scp:
                    print letter + letter2 + letter3
                    scp.get('/mnt/snap/data/' + letter + '/' + letter2 + '/' + letter3,
                            '/Users/cole/eclipse-workspace/EC2 File Transfer/Data/', 1)
                    dr.append_files(letter3);
                    shutil.rmtree('/Users/cole/eclipse-workspace/EC2 File Transfer/Data/' + letter3);
                    scp.close()
    ssh.close()