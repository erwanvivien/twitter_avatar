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
