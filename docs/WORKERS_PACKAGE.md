# Workers Package Documentation

## Overview

The `workers-py` package provides the `WorkerEntrypoint` class and other essential components for building Cloudflare Workers with Python.

## Installation

The package is now included in both Poetry and UV dependency configurations:

### UV (recommended for Cloudflare deployments)
```bash
uv sync --group cloudflare --no-dev
```

### Poetry
```bash
poetry install
```

## Usage in the Project

The package is used in `api/main.py`:

```python
from workers import WorkerEntrypoint

class Default(WorkerEntrypoint):
    async def fetch(self, request):
        import asgi
        return await asgi.fetch(app, request.js_object, self.env)
```

## Important Notes

### Runtime vs. Development

1. **Cloudflare Workers Runtime**: When deployed to Cloudflare Workers, the `workers` module is provided automatically by the Pyodide runtime. The package doesn't need to be included in the deployment bundle.

2. **Local Development**: The `workers-py` package is needed for:
   - Type checking and IDE autocompletion
   - Syntax validation
   - Local testing with `wrangler dev`

### Expected Behavior

- ✅ Package is installed and discoverable
- ✅ Syntax checking works for files that import from `workers`
- ⚠️ Direct import may fail outside Cloudflare runtime with `ModuleNotFoundError: No module named '_pyodide_entrypoint_helper'`
- ✅ Works correctly when deployed to Cloudflare Workers

This is **expected behavior** because the package depends on Pyodide's internal modules that are only available in the Cloudflare Workers runtime environment.

## Package Size Considerations

The `workers-py` package is minimal and adds minimal overhead:
- Version: 1.7.0
- Purpose: Provides type stubs and development tooling
- Impact: Does not significantly increase deployment size as it's a lightweight package

Total package count for `cloudflare` dependency group: 53 packages (including workers-py)

## Deployment

When deploying to Cloudflare Workers:

1. The GitHub Actions workflow (`.github/workflows/cloudflare-wrangler.yml`) uses:
   ```bash
   uv sync --group cloudflare --no-dev
   ```

2. This installs the minimal set of dependencies including:
   - `fastapi[standard]>=0.121.0`
   - `jinja2>=3.1.6`
   - `workers-py>=1.7.0`

3. The Cloudflare runtime provides the actual `workers` module implementation

## Troubleshooting

### Import Error in Local Environment

If you see this error:
```
ModuleNotFoundError: No module named '_pyodide_entrypoint_helper'
```

This is **expected** and **normal** when running outside the Cloudflare Workers runtime. The package is correctly installed but requires the Pyodide runtime to fully function.

### Package Not Found

If `workers-py` is not installed:

```bash
# Using UV
uv sync --group cloudflare

# Using Poetry
poetry install --with api
```

## References

- [Cloudflare Python Workers Documentation](https://developers.cloudflare.com/workers/languages/python/)
- [workers-py GitHub Repository](https://github.com/cloudflare/workers-py)
- [Python Workers Examples](https://github.com/cloudflare/python-workers-examples)
