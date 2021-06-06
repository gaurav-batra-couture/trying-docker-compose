# Trying Docker Compose
A Simple Django application using Postgresql.

- Has a very simple functionality of adding and seeing coins.
- Each coin is assosiated by an id, name and price.

To run the application,
```bash
docker-compose build
docker-compose up
```

The application will be available on 0.0.0.0:8000.

- Use /get to get all coins added.
- Use /add to add coins as follows:
```bash
curl -XPOST -H "Content-type: application/json" -d '{"name": "doge", "price": 5500}' 'http://localhost:8000/app/add'
```