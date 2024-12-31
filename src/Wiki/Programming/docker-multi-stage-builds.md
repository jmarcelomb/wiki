# How to have image with multiple builds:
    
## Python example:

Use commands:

```bash
docker build --target development # build an image with both production and development dependencies while
docker build --target production # build an image with only the production dependencies.
```

Dockerfile:

```docker
# Stage 1: Build
FROM python:3.10 AS build

# Install 
RUN apt update && \
    apt install -y sudo 

# Add non-root user
ARG USERNAME=nonroot
RUN groupadd --gid 1000 $USERNAME && \
    useradd --uid 1000 --gid 1000 -m $USERNAME
## Make sure to reflect new user in PATH
ENV PATH="/home/${USERNAME}/.local/bin:${PATH}"
USER $USERNAME

## Pip dependencies
# Upgrade pip
RUN pip install --upgrade pip
# Install production dependencies
COPY --chown=nonroot:1000 requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt && \
    rm /tmp/requirements.txt

# Stage 2: Development
FROM build AS development
# Install development dependencies
COPY --chown=nonroot:1000 requirements-dev.txt /tmp/requirements-dev.txt
RUN pip install -r /tmp/requirements-dev.txt && \
    rm /tmp/requirements-dev.txt

# Stage 3: Production
FROM build AS production
# No additional steps are needed, as the production dependencies are already installed
```

# Example 2:

devcontainer.json snippet:

```json
{
    "build": {
        "dockerfile": "Dockerfile",
        "target": "development"
    }
}
```

Dockerfile:

```docker
FROM mcr.microsoft.com/vscode/devcontainers/typescript-node:12 AS development

# Build steps go here
FROM development as builder
WORKDIR /app
COPY src/ *.json ./
RUN yarn install \
    && yarn compile \
    #  Just install prod dependencies
    && yarn install --prod

# Actual production environment setup goes here
FROM node:12-slim AS production
WORKDIR /app
COPY --from=builder /app/out/ ./out/
COPY --from=builder /app/node_modules/ ./node_modules/
COPY --from=builder /app/package.json .
EXPOSE 3000
ENTRYPOINT [ "/bin/bash", "-c" ]
CMD [ "npm start" ]
```
    
