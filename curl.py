from argparse import ArgumentParser
import requests

parser = ArgumentParser()

parser.add_argument('url')
parser.add_argument('-X', dest='method', choices=['GET', 'POST'], default='GET')
parser.add_argument('-H', '--header', nargs='+', action='extend')
# -H "My-Header : aa" -H "My-Header2 : bb" -H "My-Header3 : c" "My-Header4 : d"
parser.add_argument('-d', '--data')
parser.add_argument('-G', action='store_true')
parser.add_argument('-m', '--max-time', type=float, dest='timeout')
parser.add_argument('-o', dest='file_name')

args = parser.parse_args()
# print(args)

headers = {}
if args.header:
    headers = {k.strip():v.strip() for k, v in map(lambda x: x.split(':'), args.header)}

kwargs = {}
if args.data:
    if args.method == 'GET' and args.G:
        kwargs['params'] = args.data
    else:
        kwargs['data'] = args.data

# print(args.method.lower())
resp = requests.request(method=args.method.lower(), 
                        url=args.url, 
                        headers=headers,
                        timeout=args.timeout,
                        **kwargs
                        )

if args.file_name:
    with open(args.file_name, 'wb') as fp:
        fp.write(resp.content)
else:
    print(resp.text)






