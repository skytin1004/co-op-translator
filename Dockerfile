# Multi-stage build for Co‑op Translator
# Builder stage: build wheel using Poetry
FROM python:3.12-slim AS builder
ARG POETRY_EXTRAS=""

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps required for build steps
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    curl \
    git \
 && rm -rf /var/lib/apt/lists/*

# Install Poetry and the export plugin used to build the wheelhouse.
RUN pip install --no-cache-dir poetry==2.1.4 poetry-plugin-export==1.10.0

# Copy only dependency files first for better caching
COPY pyproject.toml poetry.lock* ./

# Export env to ensure Poetry installs with the same Python
ENV POETRY_VIRTUALENVS_CREATE=false

# Export main dependencies and build a local wheelhouse for all deps.
# Pass --build-arg POETRY_EXTRAS=image to include image translation packages.
RUN if [ -n "$POETRY_EXTRAS" ]; then \
      poetry export --without-hashes --only main --extras "$POETRY_EXTRAS" -f requirements.txt -o requirements.txt; \
    else \
      poetry export --without-hashes --only main -f requirements.txt -o requirements.txt; \
    fi
RUN pip wheel -r requirements.txt -w /wheels

# Now copy the application source
COPY src ./src
COPY README.md ./

# Build a wheel from the current source
RUN poetry build --no-interaction --format wheel


# Runtime stage: minimal image with just runtime libs and the package wheel
FROM python:3.12-slim AS runtime
ARG POETRY_EXTRAS=""

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:${PATH}"

# Install runtime system libraries only when image translation dependencies are included.
RUN if [ -n "$POETRY_EXTRAS" ]; then \
      apt-get update \
      && apt-get install -y --no-install-recommends \
        libgl1 \
        libglib2.0-0 \
      && rm -rf /var/lib/apt/lists/*; \
    fi

WORKDIR /work
VOLUME ["/work"]

# Copy the built wheel and dependency wheelhouse from the builder and install them
COPY --from=builder /app/dist/*.whl /tmp/
COPY --from=builder /wheels /wheels
RUN if [ -n "$POETRY_EXTRAS" ]; then \
      WHEEL="$(ls /tmp/*.whl)" \
      && pip install --no-index --find-links=/wheels "${WHEEL}[${POETRY_EXTRAS}]"; \
    else \
      pip install --no-index --find-links=/wheels /tmp/*.whl; \
    fi \
 && rm -f /tmp/*.whl

# Default entrypoint to the primary CLI; override with --entrypoint for other commands
ENTRYPOINT ["translate"]
CMD ["--help"]

# Example runs (documentation only):
# docker run --rm -it --env-file .env -v ${PWD}:/work IMAGE_TAG translate -l "fr es" -md
# docker run --rm -it --env-file .env -v ${PWD}:/work --entrypoint migrate-links IMAGE_TAG -l "all" -y
# docker build --build-arg POETRY_EXTRAS=image -t co-op-translator:image .
