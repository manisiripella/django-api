# 🖧 Network Health Check API

This project is a simple FastAPI application that provides basic HTTP endpoints and a `/network-health` route to check internal network connectivity using socket programming. It is Dockerized and includes a CI pipeline using GitHub Actions.

---

## 🚀 Features

- `GET /` - Basic health check
- `GET /network-health` - Checks connectivity to a specified internal IP and port
- Dockerized for easy deployment
- CI/CD with GitHub Actions

---

## 📁 Project Structure

```
.
├── app/                      # FastAPI application code
│   └── main.py               # Main application with endpoints
├── Dockerfile                # Docker build file
├── Tests/
|   └── test_main.py 
├── .github/
│   └── workflows/
│       └── ci.yml            # GitHub Actions CI pipeline
├── requirements.txt          # Python dependencies
└── README.md
```

---

## 🐳 Docker Setup

### Build the Docker image

```bash
docker build -t network-health-api .
```

### Run the container

```bash
docker run -d -p 8000:8000 network-health-api
```

Visit [http://localhost:8000](http://localhost:8000) to check the app.

---

## 🧪 API Endpoints

### `GET /`

Returns a simple greeting:

```json
{
  "Hello": "World"
}
```

### `GET /network-health`

Checks if the app can establish a socket connection to its own IP on port `8000`.

- ✅ Returns:
```json
{
  "status": "ok"
}
```

- ❌ If network issue:
```json
{
  "detail": "Network connection error"
}
```

---

## ⚙️ GitHub Actions CI

Located at `.github/workflows/python-app.yml`, the pipeline typically:

- Installs dependencies
- Lints code
- Runs test suite (if added)

### Example Workflow Snippet

```yaml
name: CI

on: [push, pull_request]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: "3.10"
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      - name: Lint
        run: |
          flake8 app/
```

> ✅ Modify as needed to include tests, formatting, or Docker build checks.

---

## 📦 Requirements

```
fastapi
uvicorn
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 📬 License

MIT License. See `LICENSE` for more info.

---

## 🛠 Author

Made with ❤️ using FastAPI and Docker.
