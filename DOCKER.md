# 🐳 Docker Guide for CI/CD Demo

Complete guide to running this project with Docker Desktop.

## 📋 Prerequisites

1. **Install Docker Desktop**:
   - Download from: https://www.docker.com/products/docker-desktop
   - Install and start Docker Desktop
   - Verify installation: `docker --version`

## 🚀 Quick Start

### Option 1: Using Docker Commands

#### Build the Docker Image
```bash
docker build -t ci-cd-demo:latest .
```

#### Run the Application
```bash
docker run --rm ci-cd-demo:latest
```

#### Run Tests in Docker
```bash
docker run --rm ci-cd-demo:latest pytest tests/ -v --cov=. --cov-report=term-missing
```

#### Run Interactive Shell
```bash
docker run --rm -it ci-cd-demo:latest /bin/bash
```

### Option 2: Using Docker Compose (Recommended)

#### Run the Application
```bash
docker-compose up app
```

#### Run Tests
```bash
docker-compose up test
```

#### Build and Run
```bash
docker-compose up --build app
```

#### Run in Background
```bash
docker-compose up -d app
```

#### Stop All Services
```bash
docker-compose down
```

## 📦 Docker Image Details

- **Base Image**: `python:3.10-slim`
- **Working Directory**: `/app`
- **Exposed Ports**: None (console application)
- **Default Command**: `python main.py`

## 🔧 Advanced Usage

### Build with Custom Tag
```bash
docker build -t myusername/ci-cd-demo:v1.0 .
```

### Run with Volume Mount (for development)
```bash
docker run --rm -v ${PWD}:/app ci-cd-demo:latest pytest tests/ -v
```

### View Running Containers
```bash
docker ps
```

### View All Containers
```bash
docker ps -a
```

### View Docker Images
```bash
docker images
```

### Remove Image
```bash
docker rmi ci-cd-demo:latest
```

### Clean Up Everything
```bash
docker system prune -a
```

## 🐳 Docker Desktop Usage

### Using Docker Desktop GUI:

1. **Open Docker Desktop**

2. **Build Image**:
   - Open terminal in project directory
   - Run: `docker build -t ci-cd-demo:latest .`
   - Image will appear in Docker Desktop → Images

3. **Run Container**:
   - Go to Images tab
   - Click on `ci-cd-demo:latest`
   - Click "Run" button
   - Configure optional settings
   - Click "Run"

4. **View Logs**:
   - Go to Containers tab
   - Click on running container
   - View logs in real-time

5. **Stop Container**:
   - Go to Containers tab
   - Click stop button on container

## 📊 Docker Compose Services

### `app` Service
- **Purpose**: Run the main application
- **Command**: `python main.py`
- **Usage**: `docker-compose up app`

### `test` Service
- **Purpose**: Run all tests with coverage
- **Command**: `pytest tests/ -v --cov=. --cov-report=term-missing`
- **Usage**: `docker-compose up test`

## 🔍 Troubleshooting

### Docker Desktop Not Running
```bash
# Error: Cannot connect to Docker daemon
# Solution: Start Docker Desktop application
```

### Port Already in Use
```bash
# If you add a web server later and port is busy
docker-compose down
# Or change port in docker-compose.yml
```

### Image Build Fails
```bash
# Clear Docker cache and rebuild
docker-compose build --no-cache
```

### Container Exits Immediately
```bash
# View logs to see what happened
docker logs <container-id>
```

## 🎯 Best Practices

1. **Always use .dockerignore** to exclude unnecessary files
2. **Use specific Python version** (3.10-slim) for consistency
3. **Don't run as root** in production (add USER directive)
4. **Use multi-stage builds** for smaller images (if needed)
5. **Tag images properly** for version control

## 📈 Next Steps

### Add to CI/CD Pipeline
Update `.github/workflows/ci.yml` to build and test Docker images:

```yaml
- name: Build Docker image
  run: docker build -t ci-cd-demo:latest .

- name: Run tests in Docker
  run: docker run --rm ci-cd-demo:latest pytest tests/ -v
```

### Push to Docker Hub
```bash
# Login to Docker Hub
docker login

# Tag image
docker tag ci-cd-demo:latest yourusername/ci-cd-demo:latest

# Push to Docker Hub
docker push yourusername/ci-cd-demo:latest
```

### Deploy to Cloud
- **AWS ECS**: Elastic Container Service
- **Azure Container Instances**: ACI
- **Google Cloud Run**: Serverless containers
- **Kubernetes**: For orchestration

## 📝 Summary

You now have a fully Dockerized Python CI/CD demo! 🎉

**Quick Commands**:
```bash
# Build
docker build -t ci-cd-demo:latest .

# Run app
docker-compose up app

# Run tests
docker-compose up test

# Clean up
docker-compose down
```

---

**Happy Dockerizing! 🐳**
