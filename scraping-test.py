import requests
from http.server import HTTPServer, BaseHTTPRequestHandler


def main():
    try:
        response = requests.get(
            headers={
                'User-Agent': 'AdsBot-Google (+http://www.google.com/adsbot.html)'
            },
            url='https://www.google.com/robots.txt'
        )
        print(response.status_code)

    except Exception as e:
        print("opps: ", e)
        return

    try:
        text = response.text.split(
            '# AdsBot\nUser-agent:')[1].split('Disallow:')[0]
    except Exception as e:
        print("Text match error: ", e)
        return

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(text.encode('utf-8'))

    print("Server listening on http://localhost:8000")

    HTTPServer(('localhost', 8000), Handler).serve_forever()


main()
