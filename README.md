# nabla-site-python

Sample FastAPI Hello World project deployable to Vercel and Cloudflare Wrangler.

## Overview

This is a minimal FastAPI application with three endpoints:

- `/` - Returns a hello world message
- `/health` - Health check endpoint
- `/api/info` - API information endpoint

## Local Development

### Prerequisites

- Python 3.12 or higher
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

1. Install uv (if not already installed):

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. Init sample:

[fastapi-sample](https://github.com/vercel/vercel/blob/main/examples/fastapi/pyproject.toml)

[backend-fastapi](https://vercel.com/docs/frameworks/backend/fastapi)
[nextjs-fastapi-starter](https://vercel.com/templates/next.js/nextjs-fastapi-starter)
[medium-fastapi-application-on-vercel](https://medium.com/@masud.pervez27/building-and-deploying-my-first-fastapi-application-on-vercel-a-complete-journey-7b010345162c)

[runtimes-python](https://vercel.com/docs/functions/runtimes/python)

```bash
vc init fastapi
```

3. Install dependencies:

```bash
uv sync
```

## Running Locally

Start the development server on <http://0.0.0.0:8000>

```bash
python main.py
# using uv:
uv run main.py
```

When you make changes to your project, the server will automatically reload.

3. Run the development server:

```bash
uvicorn main:app --reload
```

4. Access the application:

- API: <http://localhost:8000>
- Interactive docs: <http://localhost:8000/docs>
- Alternative docs: <http://localhost:8000/redoc>

## Deployment

### Deploy to Vercel

1. Install Vercel CLI:

```bash
npm install -g vercel
```

2. Deploy:

```bash
vercel
```

3. For production deployment:

```bash
vercel --prod
```

The `vercel.json` configuration file handles the deployment settings automatically.

**Build Configuration:**

Vercel uses the build command specified in `vercel.json`:
- `buildCommand: "uv sync --group cloudflare --no-dev"` installs only production dependencies
- Only includes the minimal `cloudflare` dependency group (fastapi[standard] and jinja2)
- Excludes all development, testing, and formatting packages for optimal deployment size

### Deploy to Cloudflare Workers (with Wrangler)

#### Manual Deployment

1. Install Wrangler CLI:

```bash
npm install -g wrangler
```

2. Login to Cloudflare:

```bash
wrangler login
```

3. Deploy:

```bash
uv run pywrangler dev
wrangler deploy
```

```text
🎉  SUCCESS  Application created successfully!

💻 Continue Developing
Change directories: cd api
uv self update
Deploy: npm run deploy
```

The `wrangler.jsonc` configuration file handles the deployment settings automatically.

#### Automated Deployment with GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/cloudflare-wrangler.yml`) that automatically deploys to Cloudflare Workers on push to `master` or `main` branches.

**Required Secrets:**

Configure the following secrets in your GitHub repository settings:

- `CLOUDFLARE_API_TOKEN` - Your Cloudflare API token with Workers deployment permissions
- `CLOUDFLARE_ACCOUNT_ID` - Your Cloudflare account ID

**How to get these values:**

1. **CLOUDFLARE_API_TOKEN**: Go to Cloudflare Dashboard → My Profile → API Tokens → Create Token → Edit Cloudflare Workers template
2. **CLOUDFLARE_ACCOUNT_ID**: Found in Cloudflare Dashboard → Workers & Pages → Overview (right sidebar)

**Features:**

- Uses Python 3.12 (as required)
- Ultra-minimal dependency installation for Cloudflare's free tier size limits
- Uses `uv sync --group cloudflare --no-dev` with only 2 packages:
  - `fastapi[standard]` - Core framework with essential dependencies
  - `jinja2` - Template rendering
- Excludes ALL unnecessary packages:
  - ❌ redis, python-gitlab, python-json-logger, python-keycloak
  - ❌ plotly, polars, PyMuPDF, pyarrow (data processing/PDF tools)
  - ❌ slowapi, sse-starlette, structlog, tqdm (unused features)
  - ❌ 125+ development/test/format/ci packages
- Dry-run deployment on pull requests for validation
- Full deployment on pushes to main/master branches
- Cloudflare's Python Workers runtime provides the `workers` module automatically (no need to install `workers-py`)

**Note:** Cloudflare Workers with Python support is currently in beta. You may need to use Cloudflare Pages with Python or adjust the configuration based on the latest Cloudflare documentation.

## Project Structure

```text
.
├── main.py           # FastAPI application
├── pyproject.toml    # Python project configuration and dependencies (uv)
├── uv.lock          # Lock file for reproducible installs
├── vercel.json      # Vercel deployment configuration
├── wrangler.toml    # Cloudflare Wrangler configuration
└── README.md        # This file
```

## API Endpoints

### GET /

Returns a hello world message.

**Response:**

```json
{
  "message": "Hello World"
}
```

### GET /health

Health check endpoint.

**Response:**

```json
{
  "status": "healthy"
}
```

### GET /api/info

API information endpoint.

**Response:**

```json
{
  "name": "nabla-site-python",
  "version": "1.0.0",
  "description": "Sample FastAPI Hello World for Vercel and Cloudflare deployment"
}
```

### Initialize opencommit and oco

1. Install opencommit:

```bash
npm install -D opencommit
npm install -D @commitlint/cli @commitlint/config-conventional @commitlint/prompt-cli commitizen cz-emoji-conventional

git add .opencommit-commitlint
oco commitlint get

oco config set OCO_PROMPT_MODULE=@commitlint
```
