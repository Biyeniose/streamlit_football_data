# Streamlit + Supabase

Objective is to create a Streamlit GUI to trigger Web Scraping scripts and save data into a Supabase database.

A virtual environment exists but it is not used in the Docker container

## Development flow

- Make sure you have Docker installed
- Clone or download the project then cd into it: `cd streamlit_football_data`
- Run with Watch Mode enabled: `docker compose up --watch`

- To stop the container, kill the Terminal (`CMD+C`) and run: `docker-compose down`
- Remove all unused images: `docker image prune -a`
- Code changes on your machine should now sync with the code in the container
- Insert all code into the `/src` folder to avoid Docker issues

If you want to install new packages list them in the `requirements.txt` file and try restarting the container if any issues come up

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
