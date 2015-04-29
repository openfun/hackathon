#!/usr/bin/env python
import argparse
import urllib2

def main():
    parser = argparse.ArgumentParser(description="Send queries to an ElasticSearch server")
    parser.add_argument('--host', default="http://localhost",
                        help="Adress of the ElasticSearch server")
    parser.add_argument("--no-pretty", action="store_true",
                        help="Disable response formatting")
    parser.add_argument('-p', '--port', type=int, default=9200,
                        help="Port on which the ElasticSearch server is running")
    parser.add_argument("query_path", help="Path to json-formatted query file")
    args = parser.parse_args()

    with open(args.query_path) as json_file:
        json_data = json_file.read()

    url = search_url(args.host, args.port, not args.no_pretty)
    request = urllib2.Request(url, json_data)
    result = urllib2.urlopen(request)
    print result.read()

def search_url(host, port, pretty=True):
    return "{}:{}/_search?pretty={}".format(host, port, "true" if pretty else "false")

if __name__ == "__main__":
    main()
