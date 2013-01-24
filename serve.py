from SimpleHTTPServer import SimpleHTTPRequestHandler
import SocketServer
import argparse


def serve(hostname, port):
    SimpleHTTPRequestHandler.extensions_map.update({
        '.appcache': 'text/cache-manifest',
        '.webapp': 'application/x-web-app-manifest+json',
    })

    httpd = SocketServer.TCPServer((hostname, port), SimpleHTTPRequestHandler)
    print "serving on http://%s:%s" % (hostname, port)
    httpd.serve_forever()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Serve your webapp files with the right Content-Type""",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--port', dest='port', type=int,
                        help='The port to serve to', default=8000)

    parser.add_argument('--hostname', dest='hostname',
                        help='The hostname', default='0.0.0.0')

    args = parser.parse_args()
    serve(args.hostname, args.port)
