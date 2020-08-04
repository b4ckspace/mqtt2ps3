# mqtt2ps3

Rewrites mqtt-messages from backspace home-automation to ps3 with WebMAN

## Usage
### docker-compose
```yaml
version: '3'

services:
  mqtt2ps3:
    build: ./
    restart: always
    environment:
      - MQTT_HOST=somehost
      - MQTT_USER=someone
      - MQTT_PASS=changeme
      - MQTT_PORT=1883
      - PS3_HOST=ps3ip
```
