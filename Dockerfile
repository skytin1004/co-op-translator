# Multi-stage build for Co‑op Translator
# Builder stage: build wheel using Poetry
FROM python:3.13-slim AS builder

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps required for build steps
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    python3-dev \
    curl \
    git \
 && rm -rf /var/lib/apt/lists/*

# Bootstrap the patched pip with the hash-verified wheel recommended by Python's
# eMudhra incident guidance, then install Poetry with the repaired trust bundle.
RUN python -m pip install --no-cache-dir \
    "pip @ https://files.pythonhosted.org/packages/3f/06/3e4420302363fbb71be3c7f35ce042f54bfca330e3e66b3a2e3c4cca579f/pip-26.2.2-py3-none-any.whl#sha256=fd7f4dfa8190e014013b9f08f3e973f4e4c26ffd179a204895533a7254813a70" \
 && python -m pip install --no-cache-dir poetry==2.4.2 poetry-plugin-export==1.10.0

# Copy only dependency files first for better caching
COPY pyproject.toml poetry.lock* ./

# Export env to ensure Poetry installs with the same Python
ENV POETRY_VIRTUALENVS_CREATE=false

# Export main dependencies and build a local wheelhouse for all deps
RUN poetry export --without-hashes --only main -f requirements.txt -o requirements.txt
RUN python -m pip download --no-deps --dest /wheels pip==26.2.2 \
 && python -m pip wheel -r requirements.txt -w /wheels

# Now copy the application source
COPY src ./src
COPY README.md ./

# Build a wheel from the current source
RUN poetry build --no-interaction --format wheel


# Runtime stage: minimal image with just runtime libs and the package wheel
FROM python:3.13-slim AS runtime

ENV PIP_NO_CACHE_DIR=1 \
    PYTHONUNBUFFERED=1 \
    PATH="/usr/local/bin:${PATH}"

# Install minimal runtime system libraries required by some imaging libs (opencv, pillow)
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
    ca-certificates \
    libgl1 \
    libglib2.0-0 \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /work
VOLUME ["/work"]

# Copy the built wheel and dependency wheelhouse from the builder and install them
COPY --from=builder /app/dist/*.whl /tmp/
COPY --from=builder /wheels /wheels
RUN python -m pip install --no-index --find-links=/wheels pip==26.2.2 /tmp/*.whl \
 && rm -f /tmp/*.whl

# Default entrypoint to the primary CLI; override with --entrypoint for other commands
ENTRYPOINT ["translate"]
CMD ["--help"]

# Example runs (documentation only):
# docker run --rm -it --env-file .env -v ${PWD}:/work IMAGE_TAG translate -l "fr es" -md
# docker run --rm -it --env-file .env -v ${PWD}:/work --entrypoint migrate-links IMAGE_TAG -l "all" -y

