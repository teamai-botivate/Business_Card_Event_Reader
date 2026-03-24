# 📘 Full System Documentation & Setup Guide (Hindi + English)

Ye document is system ko fully setup krne aur uska working flow smjhne ke liye banaya gya hai. Isme system ka har ek part (Backend, Frontend, Apps Script, Database) detail me explain kiya gya hai.

---

## 🏗️ 1. System Overview (Pura System Kaise Kaam Krta Hai)

Ye ek **AI-Powered Business Card Reader** hai. Iska kaam hai business card se data extract krna aur usko enrich (extra info nikalna) krke Google Sheets me save krna.

**Working Flow:**

```mermaid
graph TD
    A[User Uploads Card] -->|Frontend/Scanner| B[FastAPI Backend /ocr]
    B -->|OCR Image| C[OpenAI GPT-4o Vision]
    C -->|Extracted Data| D[Waterfall Enrichment Pipeline]
    D -->|Get Domain| E[Jina Reader Scraper]
    D -->|Fallback Search| F[Google Custom Search]
    E -->|Scrapy Metadata| G[Social Link Extraction]
    G -->|Final Payload| H[Google Apps Script]
    H -->|Save Images| I[Google Drive]
    H -->|Save Data| J[Google Sheets]
```

1. **Frontend:** User apni business card ki image upload krta hai.
2. **Backend (FastAPI):** Image ko OpenAI (GPT-4o Vision) ke paas bhejta hai text extract krne ke liye.
3. **Enrichment:** extracted email se company ki website pata krta hai, fir website scrape krke (Jina API) social media links aur company details nikalta hai.
4. **Google Apps Script:** Sara data (along with images) Google Sheets me save ho jata hai.
5. **Dashboard:** `leads.html` page pr sara saved data table format me dikhta hai.

---

## 🛠️ 2. Prerequisites (Zaroori Chije)

Setup shuru krne se pehle ye chije honi chahiye:

- **Python 3.10+** (Install kr lein)
- **Node.js** (Sirf agr React wala scanner build krna ho)
- **OpenAI API Key** (GPT-4o ke liye)
- **Google Cloud API Key & CSE ID** (Search fallback ke liye)
- **Google Account** (Google Sheets aur Apps Script ke liye)

---

## 🚀 3. Installation & Setup (Step-by-Step)

### Step 3.1: Project Clone Kaise Krein (GitHub Se)

1. **Terminal Open Krein:** Apne computer me `PowerShell`, `CMD` ya `Terminal` open krein.
2. **Command Type Krein:** Niche di gayi command ko copy krke terminal me paste krein:
   ```bash
   git clone https://github.com/teamai-botivate/Business_Card_Event_Reader.git
   ```
3. **Folder Ke Andar Jayein:** Clone hone ke baad folder me jaane ke liye ye command likhein:
   ```bash
   cd Business_Card_Event_Reader
   ```
4. **Setup Shuru Krein:** Ab aap niche diye gaye `Virtual Environment` aur `Dependencies` ke steps follow kr skte hain.

### Step 3.2: Python Setup & Backend Run
1. **Virtual Environment Banayein:**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows ke liye
   ```
2. **Dependencies Install Krein:**
   ```bash
   pip install -r requirements.txt
   pip install -r backend/requirements.txt
   ```
3. **Backend Run Krein:**
   Backend start krne ke liye root folder se ye command chalayein:
   ```bash
   python run.py
   ```
   Server `http://127.0.0.1:8000` pr start ho jayega.

### Step 3.3: NPM & Frontend Setup (Scanner Build)
Agr aap live camera scanner (React app) use krna chahte hain, to use build krna hoga:

1. **Scanner Folder me Jayein:**
   ```bash
   cd BotivateScanner
   ```
2. **NPM Dependencies Install Krein:**
   ```bash
   npm install
   ```
3. **Build Banayein:**
   ```bash
   npm run build
   ```
   Ye command `dist` folder banayegi jise Backend use krta hai. Build hone ke baad wapas root folder me aa jayein (`cd ..`).

### Step 3.4: Environment Variables (.env)

`backend/` folder ke andar ek `.env` file banayein aur ye keys dalein:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=AIzaSyCxHj_EhVfi-p4DPNCZmTlcF8Uq3T1E-N0
GOOGLE_CSE_ID=0441dbb7ce6ee45b9
APPS_SCRIPT_URL=your_google_apps_script_url
```

---

## 🔑 4. Google API & CSE ID Detail (A-to-Z Guide)

Ye keys isliye zaroori hain taki agr website na mile, to system Google pr search krke company ka data nikal sake.

### 4.1 — Google API Key Kaise Banayein?
1. **Google Cloud Console** ([console.cloud.google.com](https://console.cloud.google.com/)) pr jayein.
2. Ek naya **Project** banayein.
3. Sidebar me **"APIs & Services" > "Library"** pr jayein.
4. Search krein **"Custom Search API"** aur use **Enable** kr dein.
5. Fir **"APIs & Services" > "Credentials"** pr jayein.
6. **"+ CREATE CREDENTIALS" > "API Key"** pr click krein.
7. Aapki key (AIzaSy...) ready ho jayegi.

### 4.2 — Google CSE ID (Custom Search Engine) Kaise Banayein?
1. **Programmable Search Engine** ([programmablesearchengine.google.com](https://programmablesearchengine.google.com/)) pr jayein.
2. **"Add"** button pr click krein.
3. Search engine ka naam rakhein: `Business Card Reader`.
4. "What to search?" me koi bhi dummy site (jaise `www.google.com`) dal dein.
5. Create hone ke baad, **Settings** me jayein aur **"Search the entire web"** option ko **ON** kr dein. (Ye sabse zaroori step hai).
6. Wahi pr aapko **"Search engine ID"** milegi, use copy krke `.env` me dalein.

---

## 📊 5. Google Sheets & Apps Script Setup (Database)

Is system ka database **Google Sheet** hai.

### Step 4.1: Sheet Taiyar Krein

1. Ek nayi Google Sheet banayein.
2. Sheet me niche likhe tabs (pages) banayein (Casing ka dhyan rakhein):
   - `Ai Card` (Main leads ke liye)
   - `Event Details` (Events save krne ke liye)
   - `Event Ai Card` (Event specific leads ke liye)
   - `Visitor Details` (Form se aaye leads ke liye)
   - `Company Profile` (Apni company details ke liye)

### Step 4.2: Apps Script Code Dalein

1. Sheet me **Extensions > Apps Script** pr jayein.
2. Wahan `FINAL_APPS_SCRIPT.js` ka pura code paste kr dein.
3. Code me top pr `SHEET_ID` aur `FOLDER_ID` ko apni sheet aur Google Drive folder ki ID se replace krein.
4. **Deploy** button pr click krein -> **New Deployment**.
5. Select type: **Web App**.
6. Access: **Anyone**.
7. Deploy krne ke baad jo (Web app) **URL** mile, usko `.env` file me `APPS_SCRIPT_URL` me dal dein.

---

## 📡 5. Data Fetching & Enrichment Logic

System data kaise lata hai?

1. **GPT-4o OCR:** Pehle image se plain text extract hota hai (Name, Email, Phone).
2. **Waterfall Enrichment:**
   - Email ka domain (e.g. `@botivate.ai`) nikal kr `botivate.ai` website search krta hai.
   - **Jina Reader API** (`r.jina.ai/url`) ka use krke website ka content fetch krta hai.
   - Fetch hue content se Social Media (Instagram, FB, LinkedIn) links regex se extract hote hain.
   - Agr website nhi milti, to **Google Search** API se company ka data dhunda jata hai.
3. **Confidence Score:** Data ki reliability ke basis pr 0-100 ka score calculate hota hai.

---

## 🖥️ 6. Frontend Structure

Project me 2 tarah ke frontend hain:

1. **Vanilla Frontend (`frontend/` folder):**
   - `index.html`: Main scanner aur upload page.
   - `leads.html`: Dashboard jahan sara data tabular form me dikhta hai.
2. **React Scanner (`BotivateScanner/` folder):**
   - Ye ek advanced React + Vite app hai jisme live camera scanner hai.
   - Isko use krne ke liye `BotivateScanner` me `npm install` aur `npm run build` krna pdta hai.

---

## ❓ 7. Troubleshooting (Common Issues)

- **"No item with the given ID"**: Check krein ki `SHEET_ID` aur `FOLDER_ID` Apps Script me sahi hain ya nhi.
- **OCR Failed**: Check krein OpenAI key active hai aur usme credits hain.
- **CORS Error**: Backend running hai ya nhi (port 8000).

---

## 📝 Folder Structure Summary

```
Bussiness_Card_Reader/
├── backend/                # FastAPI Logic (Python)
├── frontend/               # UI Files (HTML/JS)
├── BotivateScanner/        # React Camera UI (Vite)
├── .env                    # Secret Keys (OpenAI, Google)
├── FINAL_APPS_SCRIPT.js    # Google Sheets Ka Dimag
└── DOCUMENTATION_AND_SETUP_GUIDE.md  # Ye wala File
```

Ab koi bhi naya person in steps ko follow krke 10-15 minutes me system ready kr skta hai. 🚀
