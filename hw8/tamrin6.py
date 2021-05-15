import sys
import argparse
import translators
import socket




def translator(to_lang='fa', from_lang='auto', provider='google', save_path=None, file_name=None):
    translator_func = getattr(translators, provider)
    if file_name:
        with open(file_name, 'r') as f1:
            text = f1.read()
    res = translator_func(text, from_language=from_lang, to_language=to_lang)
    if save_path:
        with open(save_path, 'w') as f:
            f.write(res)
            return print(save_path)
    else:
        return print(res)


# print(translator('hi world'))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Translator Program')

    parser.add_argument('-t', '--to_lang', metavar='TO_LANG', action='store', default='fa', required=True,
                        help='specify language to translat')
    parser.add_argument('-f', '--from_lang', metavar='FROM_LANG', action='store', default='auto',
                        help='specify language translat from')
    parser.add_argument('-d', '--provider', metavar='PROVIDER', action='store', default='google',
                        help='specify provider for translat')
    parser.add_argument('-s', '--save_path', metavar='SAVE_PATH', action='store', nargs='?',
                        help='specify path for save')
    parser.add_argument('file_name', metavar='FILE_NAME', action='store', help='specify a file for translate')

    args = parser.parse_args()
    translator(to_lang=args.to_lang, from_lang=args.from_lang, provider=args.provider, save_path=args.save_path,
               file_name=args.file_name)

# server
s = socket.socket()
port = 8000
ip = '192.168.1.51'
s.bind((ip, port))
s.listen()
c, addr = s.accept()
print('Connected')
while True:
    message = input('Your Message : ')
    c.send(message.encode())
    print(c.recv(1024).decode())

# client

s = socket.socket()
port = 8000
ip = '192.168.1.51'
s.connect((ip, port))
print('Connected')
while True:
    print(s.recv(1024).decode())

    s.send(translators.encode())
