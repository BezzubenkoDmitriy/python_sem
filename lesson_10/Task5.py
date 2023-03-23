import subprocess
import chardet


def ping_results(web_resource):
    args = ['ping', web_resource]

    ping_results = subprocess.Popen(args, stdout=subprocess.PIPE)

    for line in ping_results.stdout:
        char_detect = chardet.detect(line)
        encoded_line = line.decode(char_detect['encoding']).encode('utf-8')
        print(encoded_line.decode('utf-8'))


ping_results('web_resource')
