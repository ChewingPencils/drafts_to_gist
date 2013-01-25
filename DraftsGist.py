# drafts_to_gist.py
# Sean Korzdorfer
# 2013-01-25
# Verson 1

import requests
import sys
import json
import pprint
import webbrowser
pp = pprint.PrettyPrinter(indent=4)

# Setting for Github Token
gistToken = ''

# Setting for creating private or public gists. Must be bool. True is public.
gistView = False
    
# GetHub URL
apiURL = 'https://api.github.com/gists?access_token=' + gistToken


def formatData(gistTitle, gistBody):
    """ Creates dictionary structure for gist api request
        Returns encoded JSON
    """
    payload = {
        'public' : gistView,
        'files': {
            gistTitle : {
                'content' : gistBody
            }
        }
    }
    # JSON encoding data 
    payload = json.dumps(payload)
    return payload

def makeGist (apiURL, payload):
    """ Makes HTTP request to GitHub API
    Checks for a status code of 201
    If gist was created, returns JSON encoded response
    """
    # Making POST request to GitHub
    r = requests.post(apiURL, data=payload)
    # Verifying Response
    if r.status_code != 201:
        print '\n\nERROR: Gist NOT CREATED. ERROR CODE: ' + str(r.status_code)
    return json.loads(r.content)

def main():
    # Get data passed by Drafts
    gistTitle = sys.argv[1]
    gistBody = sys.argv[2]
    
    payload = formatData(gistTitle, gistBody)
    gistResponse = makeGist(apiURL, payload)

    # In case anyone wants to see the data returned
    #pp.pprint(parsed_json)
    webbrowser.open(gistResponse["files"][gistTitle]["raw_url"])

if __name__ == '__main__':
    main()