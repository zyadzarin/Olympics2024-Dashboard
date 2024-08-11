# The first stage
# Build Vite React static files
FROM node:16-alpine as build

WORKDIR /app/frontend
COPY ./frontend/package.json ./
COPY ./frontend/package-lock.json ./
RUN npm ci
COPY ./frontend/ ./
RUN npm run build

# The second stage
# Copy Vite React static files and start nginx
FROM nginx:stable-alpine

# Install openssl
RUN apk add --no-cache openssl

# Copy the built assets from the build stage
COPY --from=build /app/frontend/dist /usr/share/nginx/html

# Copy nginx configuration (if you have a custom nginx.conf)
# COPY ./nginx.conf /etc/nginx/nginx.conf

# Copy the SSL generation script (commented out for now)
# COPY ./docker/nginx/generate_ssl_certs.sh /usr/local/bin/

# Make the script executable (commented out for now)
# RUN chmod +x /usr/local/bin/generate_ssl_certs.sh

# Run the script to generate SSL certificates (commented out for now)
# RUN /usr/local/bin/generate_ssl_certs.sh

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]