FROM node:latest
LABEL description="A Dockerfile for docs"
WORKDIR /app
COPY . .
RUN npm install -g docsify-cli@latest
EXPOSE 3000/tcp
ENTRYPOINT docsify serve .
