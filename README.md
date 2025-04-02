# Load Balanced URL Shortener

This project is a simple **URL shortener** built using Flask and Redis. It allows users to shorten long URLs and retrieve them later using a unique short code. The system is containerized using Docker and managed with Docker Compose for easy deployment.

## Features
- Shortens long URLs using a **hash-based approach**.
- Stores and retrieves URLs efficiently using **Redis**.
- Implements a **Flask API** for URL shortening and redirection.
- Designed to be **scalable** with load balancing (to be added in future updates).

## Tech Stack
- **Flask** for the web application.
- **Redis** as the in-memory key-value store.
- **Docker & Docker Compose** for containerized deployment.

## How It Works
1. The user submits a long URL.
2. A short code is generated using a hashing algorithm.
3. The short code and long URL are stored in Redis.
4. When a user accesses the short URL, they are redirected to the original URL.

## Future Enhancements
- Implementing a **load balancer** for better scalability.
- Adding **database persistence** for long-term URL storage.
- User authentication for managing shortened URLs.

## License
This project is licensed under the **MIT License**.

