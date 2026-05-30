# ⚡ RENDER FIX - DO THIS NOW

## 🎯 The Problem:
Render is trying to run `gunicorn` (Django command) instead of `uvicorn` (FastAPI command).

## ✅ The Solution (2 Minutes):

### STEP 1: Open Render Dashboard
Go to: https://dashboard.render.com/

### STEP 2: Click Your Service
Click on **"naamveda-backend"** (or whatever you named it)

### STEP 3: Go to Settings
Click **"Settings"** in the left sidebar

### STEP 4: Find "Start Command"
Scroll down to the **"Build & Deploy"** section

You'll see a field called **"Start Command"**

### STEP 5: Enter This EXACT Command
**DELETE** whatever is there and **PASTE** this:

```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

⚠️ **IMPORTANT:** 
- Use `$PORT` (with dollar sign) - NOT 6005, NOT 8000
- Render automatically sets the PORT variable
- Don't change `$PORT` to any number!

### STEP 6: Save
Click **"Save Changes"** button at the bottom

### STEP 7: Redeploy
1. Scroll to top of page
2. Click **"Manual Deploy"** dropdown (top right)
3. Click **"Clear build cache & deploy"**
4. Wait 2-3 minutes

---

## 🎉 Success Looks Like This:

In the deployment logs, you should see:

```
==> Build successful 🎉
==> Deploying...
==> Running 'uvicorn app.main:app --host 0.0.0.0 --port $PORT'
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000
==> Your service is live 🎉
```

---

## 🧪 Test Your Backend:

After deployment succeeds:

1. Copy your URL from Render (looks like: `https://naamveda-backend.onrender.com`)
2. Open in browser: `https://your-url.onrender.com/docs`
3. You should see **FastAPI Swagger UI** with all your endpoints! 🎉

---

## ❌ If You Still See "gunicorn: command not found":

It means the Start Command field is still empty or wrong.

**Double-check:**
1. Go to Settings
2. Scroll to "Build & Deploy"
3. Make sure "Start Command" has: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Click "Save Changes"
5. Redeploy again

---

## 📝 Quick Copy-Paste:

**Start Command (COPY THIS):**
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Build Command (should already be set):**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Root Directory (should already be set):**
```
backend
```

---

## 🚀 After Backend Works:

1. ✅ Copy backend URL
2. ✅ Go to Vercel dashboard
3. ✅ Update `NEXT_PUBLIC_API_URL` environment variable
4. ✅ Redeploy frontend
5. ✅ Test: https://naamveda.vercel.app
6. ✅ Generate names! 🎉

---

**You're almost there!** Just need to set that start command in the dashboard! 💪
