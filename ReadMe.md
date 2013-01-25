# Drafts App Action: Create Gist

A [Drafts App][1] URL action combined with a python script for creating quick gists on iOS. 

## Requirements

- [Drafts App][1]
- [Pythonista App][2]
- Git Hub OAuth token

## Installation

### Step 1: Create GitHub OAuth token
    
Since this script runs on an iOS app, a GitHub OAuth token must be created prior to use. It's easy to create a token using curl from the terminal. Make sure to **add your GitHub username** to the following command:

    curl https://api.github.com/authorizations \
    --user "YOUR_GITHUB_USERNAME" \
    --data '{"scopes":["gist"],"note":"Drafts"}'

### Edit DraftsGist.py
The response will contain a line: `"token" : foo` where foo is the token string.
Add the token to line 14.

There is also an option for creating public or private gists on line 17.

You can verify the token is enabled at: <https://github.com/settings/applications>


##Step 2: Create a Drafts URL Action

The following URL will create an URL action in Drafts:

<drafts://x-callback-url/import_action?type=URL&name=Gist&url=pythonista%3A%2F%2FDraftsGist%3Faction%3Drun%26args%3D%2522%5B%5Btitle%5D%5D%2522%2520%2522%5B%5Bbody%5D%5D%2522>

Source:

	drafts://x-callback-url/import_action?type=URL&name=Gist&url=pythonista%3A%2F%2FDraftsGist%3Faction%3Drun%26args%3D%2522%5B%5Btitle%5D%5D%2522%2520%2522%5B%5Bbody%5D%5D%2522

## Step 3: Create Pythonista Script

Paste the contents of Drafts.py into a new Pythonista file. It **must have the title: DraftsGist**.

## Using The Drafts Action.

Easy peasy. Format your note as such:

	This is the first line of the note and the gist's title
	Everything else is the content of the note. This is the 1st paragraph.
	
	Line breaks are preserved.
	
	This will be the third paragraph of the note.
	
Use the Gist action to send the note to  Pythonista. Once gist is created, a web browser will open to show the raw contents of the gist.


[1]: http://agiletortoise.com/drafts
[2]: http://omz-software.com/pythonista/
