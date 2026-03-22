# API Security Project

This project demonstrates secure API usage using OpenWeather API.

### 1. Consequences of exposing an API key
Exposing an API key on GitHub can allow unauthorized users to misuse the service, leading to unexpected charges, service abuse, or account suspension. Attackers may also exploit it to launch large-scale automated requests.

### 2. Why logging city names is prohibited
City names can reveal user location data, which is considered sensitive under privacy laws like GDPR. Logging such data violates the principle of data minimization and can risk user privacy if logs are exposed.