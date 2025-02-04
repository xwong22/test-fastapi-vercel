# FastAPI Vercel Template

A modern FastAPI template configured for Vercel deployment, featuring a beautiful landing page and RESTful endpoints.

## 🚀 Features

- Beautiful HTML landing page
- RESTful API endpoints
- Automatic API documentation (Swagger UI and ReDoc)
- Logging configuration
- Vercel deployment ready
- Health check endpoint

## 📋 Prerequisites

- Python 3.12    # vercel uses the latest python version by default

## 🛠️ How to deploy your FastAPI app on Vercel

1. Create a FastAPI app with these files at the root of your project:

```
├── main.py               # Entry point for your FastAPI application
├── requirements.txt      # Project dependencies
└── vercel.json          # Vercel deployment configuration
```


2. vercel.json structure:

```
{
    "builds": [
      {
        "src": "main.py",   # can be changed to the name of your main file
        "use": "@vercel/python"    # uses the latest python version by default
      }
    ],
    "routes": [
      {
        "src": "/(.*)",
        "dest": "main.py"  # can be changed to the name of your main file
      }
    ]
  }
```

3. Deploy your FastAPI app on Vercel:

- Log in to Vercel on the website (or you can use the Vercel CLI)
- Framework Preset: Other
- Set environment variables PORT=8000
- Leave the rest of the settings as they are
- Deploy
