# Twitter Avatar

A simple python script to retrieve someone avatar's url from their twitter name.

## Use case

- If you want to create fake twitter embed for discord (using the parameter `discord=1`)
- If you want to download someone's image rapidly

## How to use

You just need to create a json file named `profile` and paste the value you get from your application. Get your twitter [Bearer Token](https://developer.twitter.com/en/portal/dashboard)

A default `profile` would be:

```json
{
  "api_key": "XXXXXXXXXXXXXXXXXXXXXXXXX",
  "api_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "token_key": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "token_secret": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  "bearer_token": "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
}
```

but you only need the field `bearer_token`

# Examples
```bash
python main.py elonmusk # Will display the URL for elon musk's profile image
python main.py VivienErwan discord=1 # Will print a _ready-to-use_ discord embed using the twitter embed setup
```
Output1:
```
elonmusk:
https://pbs.twimg.com/profile_images/1364491704817098753/V22-Luf7.jpg
```
Output2
```
VivienErwan:
{
  "embed": {
    "description": "CHANGE THIS MESSAGE",
    "image": {
      "url": "CHANGE THIS URL IF YOU WANT TO HAVE AN EMBED IMAGE, OTHERWISE, REMOVE THE IMAGE FIELD"
    },
    "color": 1942002,
    "footer": {
      "icon_url": "https://abs.twimg.com/icons/apple-touch-icon-192x192.png",
      "text": "Twitter"
    },
    "author": {
      "name": "Erwan VIVIEN (@VivienErwan)",
      "icon_url": "https://pbs.twimg.com/profile_images/1358770497882886146/d8NVlGIE.png",
      "url": "https://twitter.com/VivienErwan"
    },
    "fields": [
      {
          "name": "Retweets",
          "value": "500",
          "inline": true
      },
      {
          "name": "Likes",
          "value": "500",
          "inline": true
      }
    ]
  }
}
```

Using an [Embed Visualizer](https://leovoel.github.io/embed-visualizer/) we can get this output: 

![image](https://user-images.githubusercontent.com/44021072/109476164-def10880-7a76-11eb-8279-478d698307f1.png)

_as you can see_ you need need to update the url or remove the `"image"` field in the embed to have something viable
