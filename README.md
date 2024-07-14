# Streamlit + Supabase

Objective is to create a Streamlit GUI to trigger Web Scraping scripts and save data into a Supabase database.

## Development flow

- Make sure you have Docker installed
- Clone or download the project then cd into it: `cd streamlit_football_data`
- Run with Watch Mode enabled: `docker compose up --watch`
- To stop the container, kill the Terminal (`CMD+C`) and run: `docker-compose down`
- Code changes on your machine should now sync with the code in the container

- Insert all code into the `/code` folder to avoid Docker issues

## Useful Docker commandss

| Command                              | Use                         |
| ------------------------------------ | --------------------------- |
| `docker build -t python-app .`       | build the Dockerfile        |
| `docker run -p 8501:8501 python-app` | run the app after build     |
| `docker ps`                          | list the running containers |
| `docker stop <CONTAINER_ID>`         | stop the container          |
| `docker rm <CONTAINER_ID>`           | remove the container        |
| `docker images`                      | list Docker Images          |
| `docker rmi <IMAGE_ID>`              | remove the Docker Image     |
| `docker image prune -a`              | remove all unused images    |
