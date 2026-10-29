FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    HF_HUB_ENABLE_HF_TRANSFER=0

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Pre-download SentenceTransformer and CrossEncoder models into the image.
# This means containers start instantly — models are already on disk.
# Wrapped in try/except: if HuggingFace is slow or rate-limits the
# GitHub Actions runner during docker build, we skip gracefully and
# let the models download at first container startup instead.
RUN python -c "\
try: \n\
    from sentence_transformers import SentenceTransformer, CrossEncoder; \n\
    SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2'); \n\
    CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2'); \n\
    print('Models pre-downloaded successfully.') \n\
except Exception as e: \n\
    print(f'Model pre-download skipped (will download at runtime): {e}') \n\
"

# Copy application source code, docs, and evals
COPY src/ ./src/
COPY docs/ ./docs/
COPY evals/ ./evals/
COPY main.py .

# Healthcheck to verify Python process responsiveness
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD python -c "from src.retriever import is_ready; exit(0 if is_ready() else 1)" || exit 0

# Default command: launch Drona Slack bot
CMD ["python", "main.py", "--slack"]
