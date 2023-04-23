# [poc] chat-gpt app
The objective is to understand how to use chat-gpt api and device a better architecture.

## Architecture
The image is compositions of our chat-gpt app.

![](./document/architecture.svg)

## [WIP]Development guide
1. Building containers
```
docker-compose build --no-cache
```
2. Start containers
```
docker-compose up -d
```
3. Throw request
```
curl -d '{}' http://localhost:9000/2015-03-31/functions/function/invocations
```

## Reference
- sample