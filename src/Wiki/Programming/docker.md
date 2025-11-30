
## BuildKit cache mounts turn npm ci into milliseconds

Enable BuildKit (`DOCKER_BUILDKIT=1`) and add cache mounts so expensive steps reuse artifacts across builds.

```bash
RUN --mount=type=cache,target=/root/.npm \
    npm ci --prefer-offline
```

Treat cache mounts like shared volumes: never bake secrets into them and periodically invalidate them with `--build-arg CACHE_BUST=$(date +%s)` when dependencies change.

## Secrets stay out of layers with `RUN --mount=type=secret`

Stop copying .env files into images. BuildKit can inject secrets at build time that never persist in the final layer.

```bash
docker build \
  --secret id=npmrc,src=$HOME/.npmrc \
  -t web:secure .
```

```bash
RUN --mount=type=secret,id=npmrc target=/root/.npmrc \
    npm publish
```

Now your source image remains clean, satisfying both auditors and future you.

## 4. Compose profiles keep local, staging, and prod in one file

Instead of juggling `docker-compose.dev.yml`, `*-prod.yml`, etc., define profiles and start only what each environment needs.

```yaml
services:
  db:
    image: postgres:16
    profiles: [core]
  mailhog:
    image: mailhog/mailhog
    profiles: [dev]
  worker:
    build: ./worker
    profiles: [core, prod]
```

Run `docker compose --profile core --profile dev up` during development and `--profile core --profile prod up -d` in staging. One file, zero drift.

References:

- [10 Docker Superpowers Developers Forget to Use](https://oneuptime.com/blog/post/2025-11-27-ten-docker-superpowers-youre-probably-not-using/view)