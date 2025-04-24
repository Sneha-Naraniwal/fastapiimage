# 🚀 GitHub Actions: Docker Image Build and Push

This repository uses **GitHub Actions** to automate the process of building a Docker image and pushing it to **Docker Hub** whenever changes are pushed to the `main` branch.

## ⚙️ Workflow Overview

The GitHub Actions workflow (`.github/workflows/DockerBuild.yml`) consists of the following steps:

1. ✅ **Checkout the repository**
2. 🔑 **Authenticate with Docker Hub** using secrets
3. 📦 **Build the Docker image**
4. 🚀 **Push the image to Docker Hub**
5. 🔒 **Logout from Docker Hub**

### 📜 Workflow Configuration

```yaml
name: Docker Image Build and Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout Repository
        uses: actions/checkout@v3
      
      - name: Log in to Docker Hub
        run: |
          echo "${{ secrets.DOCKERTOKEN }}" | docker login -u "${{ secrets.DOCKER_USERNAME }}" --password-stdin
      
      - name: Build Docker Image
        run: |
          docker build -t ${{ secrets.DOCKER_USERNAME }}/fastapi-app:latest .
      
      - name: Push Docker Image to Docker Hub
        run: |
          docker push ${{ secrets.DOCKER_USERNAME }}/fastapi-app:latest
      
      - name: Logout from Docker Hub
        run: docker logout
