# 📊 GitHub Analyzer

A simple web application that analyzes a GitHub profile and provides insights into repositories, languages, and developer activity.

Built as a student project at the **University of Applied Sciences Burgenland**.

---

## ✨ Features

- 🔐 GitHub OAuth login
- 📁 Repository overview
- ⭐ Top starred repositories
- 📊 Language distribution analysis
- 👤 GitHub profile summary
- 📈 Developer activity insights
- 🌐 Clean, responsive UI (Bootstrap)

---


## Setup

```bash
git clone https://github.com/andreas-wien/github_analyzer.git
cd github_analyzer
python -m venv .venv
source .venv/bin/activate  # or .\.venv\bin\Activate.ps1 on Windows
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

- Flask
- requests
- python-dotenv
- gunicorn
- Bootstrap
- plotly


## 🔐 Security Notes

- Never commit your .env file
- Keep your FLASK_SECRET_KEY secret and random
- OAuth credentials are required for authentication
- Access tokens are stored in session cookies


## 📌 Project Purpose

This project was created to:

- Learn Flask web development
- Work with REST APIs
- Implement OAuth authentication
- Analyze real-world GitHub data
- Build a full-stack Python web application


## 📄 License

This project is licensed under the MIT License.