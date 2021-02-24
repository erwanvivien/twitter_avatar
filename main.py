import requests


def get_content(file):
    # Read file content
    try:
        file = open(file, "r")
        s = file.read()
        file.close()
    except Exception:
        return ""
    return s


api_key = get_content("api_key")
api_secret = get_content("api_secret")

bearer_token = get_content("bearer_token")

token_key = get_content("token_key")
token_secret = get_content("token_secret")


screen_name = "elonmusk"
header = {"Authorization": f"Bearer {bearer_token}"}
r = requests.get(
    f"https://api.twitter.com/1.1/users/show.json?screen_name={screen_name}", headers=header)

# print(r)
# print(r.json())
js = r.json()

screen_name = js["name"]
id_name = js["screen_name"]
icon_url = js["profile_image_url_https"]
message = "BRUUUUH"


random1 = 500
random2 = 500

embed_string = '''
{
  "embed": {
    "description": "''' + message + '''",
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
}
'''

# embed_string = embed_string.format(
#     screen_name, id_name, icon_url, 500, 580, "bruuuh")

print(embed_string)
