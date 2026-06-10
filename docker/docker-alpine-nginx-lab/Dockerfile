# Use Alpine Linux as base image
FROM alpine:latest
# Update package repository and install nginx
RUN apk update && \
    apk add --no-cache nginx
# Copy custom nginx configuration (we'll create this next)
COPY nginx.conf /etc/nginx/nginx.conf
# Create a simple index.html file
RUN echo '<h1>Hello from Alpine + Nginx!</h1>' > /var/lib/nginx/html/index.html
# Expose port 80
EXPOSE 80
# Start nginx in foreground
CMD ["nginx", "-g", "daemon off;"]