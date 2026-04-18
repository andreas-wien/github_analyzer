## Setup

```bash
git clone <repo>
cd github_analyzer
python -m venv venv
source venv/bin/activate  # or .\venv\bin\Activate.ps1 on Windows
pip install -r requirements.txt
python app.py
```

Create the OAUTH App: https://github.com/settings/developers
-> Add client id and secret to .env variables "GITHUB_CLIENT_ID" and "GITHUB_CLIENT_SECRET"

Generate a secret key for Flask to use:
```python
import secrets
print(secrets.token_urlsafe(32))
```
-> Add output to .env variable "FLASK_SECRET_KEY"

See .env.example for all env variables used in this project.

## Dependencies
Flask
requests
python-dotenv
gunicorn