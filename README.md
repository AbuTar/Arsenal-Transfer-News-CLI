# Arsenal-Transfer-News-CLI
A command-line Python app that fetches the latest Arsenal transfer news from trusted football journalists using the Twitter API.

(CHAT GPT was used to help me generate the README file)

What does it do?
- Connects to twitter via the API
- Pulls tweets from reputable sources (e.g. Fabrizio Romano, David Ornstein etc....)
- Filters for Arsenal-related content (e.g., "arsenal", "afc", "gunners")
- Displays only the most revent relevant tweet per journalists
- Saves results in a local .txt file to help keep a history log

Set Up Instructions:
- Sign up for a twitter Developer Account at developer.twitter.com
- Create a project and copy your bearer token
- Open fetcher.py and replace the BEARER_TOKen with your own token
- e.g. BEARER_TOKEN = "YOUR_TWITTER_API_BEARER_TOKEN"

Customisation:
You can track any team, club, or topic by modifying two parts of the code:
In client.py:
- Update the accounts dictionary to include Twitter usernames of relevant sources:
  accounts ={
      "Your Source Name": "TwitterHandle",
      ....
  }
