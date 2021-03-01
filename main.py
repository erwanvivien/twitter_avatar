import requests
import json
import sys


def get_content(file):
    # Read file content
    try:
        file = open(file, "r")
        s = file.read()
        file.close()
    except Exception:
        return ""
    return s


if len(sys.argv) <= 1:
    print("You might need to provide some twitter usernames !")
    exit(1)

discord = False
if "discord=1" in [e.lower() for e in sys.argv]:
    discord = True
    sys.argv = [e for e in sys.argv if e.lower() != "discord=1"]

profile = json.loads(get_content("profile"))

bearer_token = profile["bearer_token"]
# api_key = profile["api_key"]
# api_secret = profile["api_secret"]
# token_key = profile["token_key"]
# token_secret = profile["token_secret"]

screen_name = sys.argv[1]
header = {"Authorization": f"Bearer {bearer_token}"}

message = "CHANGE THIS MESSAGE"

for screen_name in sys.argv[1:]:
    print(f"{screen_name}:")
    r = requests.get(
        f"https://api.twitter.com/1.1/users/show.json?screen_name={screen_name}", headers=header)

    js = r.json()

    screen_name = js["name"]
    id_name = js["screen_name"]
    icon_url = js["profile_image_url_https"].replace("_normal.", ".")

    random1 = 500
    random2 = 500

    embed_string = '''{
  "embed": {
    "description": "''' + message + '''",
    "image": {
      "url": "CHANGE THIS URL IF YOU WANT TO HAVE AN EMBED IMAGE, OTHERWISE, REMOVE THE IMAGE FIELD"
    },
    "color": 1942002,
    "footer": {
      "icon_url": "https://abs.twimg.com/icons/apple-touch-icon-192x192.png",
      "text": "Twitter"
    },
    "author": {
      "name": "''' + screen_name + ''' (@''' + id_name + ''')",
      "icon_url": "''' + icon_url + '''",
      "url": "https://twitter.com/''' + id_name + '''"
    },
    "fields": [
      {
          "name": "Retweets",
          "value": "''' + str(random1) + '''",
          "inline": true
      },
      {
          "name": "Likes",
          "value": "''' + str(random2) + '''",
          "inline": true
      }
    ]
  }
}'''

    if discord:
        print(embed_string)
    else:
        print(icon_url)
