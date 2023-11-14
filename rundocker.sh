docker build -f "Dockerfile" -t kanakresume:latest "."
docker stop kanakresume
docker run --rm -d -p 8502:8502/tcp --name kanakresume kanakresume