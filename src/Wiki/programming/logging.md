# Logging tips

[Inspiration](https://tuhrig.de/my-logging-best-practices)

## Log after (and maybe before)

```js
// don't do that
log.info("Making request to REST API")
restClient.makeRequest()
 
// do that
// log.info("Making request to REST API")  // can include this
restClient.makeRequest()
log.info("Made request to REST API -> OK")
```

## Separate parameters and messages

```js
// don't do that
restClient.makeRequest()
log.info("Made request to {} on REST API.", url)
 
// do that
restClient.makeRequest()
log.info("Made request to REST API. [url={}]", url)
```

## Distinguish between WARNING and ERROR

```js
try {
    restClient.makeRequest()
    log.info("Made request to REST API. [url={}]", url)
} catch(e: UnauthorizedException) {
    log.warn("Request to REST API was rejected because user is unauthorized. [url={}, result={}]", url, result)
} catch(e: Exception) {
    log.error("Request to REST API failed. [url={}, exception={}]", url, exception)
}
```

## Don't keep unneeded private user info in logs

Don't need the names/emails in the logs.

```
DEBUG | Saved user to newsletter list. [user="Thomas", email="thomas@tuhrig.de"]
DEBUG | Send welcome mail. [user="Thomas", email="thomas@tuhrig.de"]
INFO  | User registered for newsletter. [user="Thomas", email="thomas@tuhrig.de"]
DEBUG | Started cron job to send newsletter of the day. [subscribers=24332]
INFO  | Newsletter send to user. [user="Thomas"]
INFO  | User unsubscribed from newsletter. [user="Thomas", email="thomas@tuhrig.de"]
```
