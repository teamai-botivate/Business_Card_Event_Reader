# 🚀 Deploying to Render — Business Card Reader

This guide explains how to host your **Business Card Reader** on [Render](https://render.com) for free (or on their paid tier).

---

## 📋 Prerequisites

1.  **GitHub Repository:** Ensure your latest code (with the `backend/` and `frontend/` folders) is pushed to GitHub.
2.  **Render Account:** Sign up at [dashboard.render.com](https://dashboard.render.com).
3.  **Python Version:** We will use **Python 3.10** as requested.

---

## 🛠️ Deployment Steps

### 1. Create a New Web Service
- Go to your Render Dashboard and click **"New +"** → **"Web Service"**.
- Connect your GitHub account and select your `Bussiness_Card_Reader` repository.

### 2. Basic Configuration
Fill in the following details:

| Field | Value |
|-------|-------|
| **Name** | `business-card-ocr` (or anything you like) |
| **Region** | Select the one closest to you (e.g., Singapore or US East) |
| **Branch** | `main` |
| **Language** | `Python 3` |

### 3. Build & Start Commands
This is crucial because of our modular folder structure:

- **Build Command:**
  ```bash
  pip install -r backend/requirements.txt
  ```
- **Start Command:**
  ```bash
  python -m uvicorn backend.main:app --host 0.0.0.0 --port $PORT
  ```

### 4. Setting the Python Version
Render uses a default Python version unless told otherwise. To use **3.10**:
- Scroll down to **"Advanced"**.
- Click **"Add Environment Variable"**.
- Key: `PYTHON_VERSION`
- Value: `3.10.12` (or `3.10.x`)

---

## 🔑 5. Environment Variables (Required)
You MUST add your API keys in the **Environment** section of Render. Do not skip this!

| Key | Value |
|-----|-------|
| `OPENAI_API_KEY` | *Your sk-proj-... key* |
| `GOOGLE_API_KEY` | *Your Google Search Key* |
| `GOOGLE_CSE_ID` | *Your Search Engine ID* |
| `APPS_SCRIPT_URL` | *Your Google Sheets Script URL* |
| `PYTHONPATH` | `.` (This helps Python find the `backend` package) |

---

## 🔄 6. Handling the Frontend
Since the Python backend serves the `index.html` from the `frontend/` folder, once the API is live, your website will be available at:
`https://your-service-name.onrender.com/`

### ⚠️ Important Note for Frontend
In your `frontend/index.html`, ensure your API URL is relative:
```javascript
const api = '/ocr'; // ✅ This is correct for deployment
```
*(We already did this in our previous steps, so it should be fine!)*

---

## 📊 Monitoring & Logs
- Once you click **"Create Web Service"**, Render will start the build.
- You can watch the **Logs** tab in Render to see if there are any errors during `pip install`.
- If you see `Application startup complete`, your app is live!

---

## 🛠️ Troubleshooting on Render

### 1. "ModuleNotFoundError: No module named 'backend'"
If you get this error, ensure you have added the environment variable `PYTHONPATH` with value `.`. This tells Python to look in the root folder for the `backend` folder.

### 2. Port Issues
Render automatically assigns a port. Using `--port $PORT` in the start command handles this automatically.

### 3. Slow Start (Free Tier)
Render's free tier puts your app to sleep after 15 minutes of inactivity. The first request after a long time might take 30-50 seconds to "wake up" the server.

---

**Everything is ready!** Just follow these steps on Render and your AI Business Card Reader will be accessible from anywhere in the world. 🌍
