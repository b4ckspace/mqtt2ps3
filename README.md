# mqtt2soundboard

Rewrites mqtt-messages from backspace home-automation to [soundboard](https://github.com/b4ckspace/soundboard)

## Usage
### docker-compose
```yaml
version: '3'

services:
  mqtt2soundboard:
    build: ./
    restart: always
    environment:
      - MQTT_HOST=somehost
      - MQTT_USER=someone
      - MQTT_PASS=changeme
      - MQTT_PORT=1883
```
