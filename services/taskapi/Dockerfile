# builder stage
FROM python:3.12-slim AS builder

# Optimized: Instantly pull the pre-compiled 'uv' binary directly into your container
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Enable bytecode compilation to make your app start faster
ENV UV_COMPILE_BYTECODE=1

# Force uv to use copies instead of hardlinks inside the container
ENV UV_LINK_MODE=copy

COPY pyproject.toml uv.lock ./

# Cache Optimization: Install dependencies, but skip your actual project source code
# --no-install-project: This flag separates the heavy download phase of your third-party dependencies
# from your local application source code. If you change a line of python code tomorrow,
# Docker reuses this layer instantly rather than downloading your packages again.
RUN uv sync --frozen --no-install-project --no-dev

# runtime stage
FROM python:3.12-slim AS runtime

WORKDIR /app

# Create a non-root user for security best practices
RUN groupadd -g 1001 appgroup && \
    useradd -u 1001 -g appgroup -m -d /app -s /bin/false appuser

# Copy the lightweight virtual environment created by uv in the builder stage
COPY --from=builder /app/.venv /app/.venv

# Copy your actual application source code
COPY app ./app

# Add the virtual environment to the system PATH so you don't need 'uv run'
# Environment PATH Injection: By pushing /app/.venv/bin directly to ENV PATH,
# you drop the requirement to bundle the uv tool inside your final runtime
# container entirely, heavily reducing the image size and shrinking its exploit attack surface.
ENV PATH="/app/.venv/bin:$PATH"

# Set permissions for the non-root user
RUN chown -R appuser:appgroup /app
USER appuser

# Expose your application port (example for web APIs)
EXPOSE 8000

# Execute your app directly from the virtual environment
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
