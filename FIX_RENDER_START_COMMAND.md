# 🔧 FIX: Render Start Command Error

## ❌ Current Error:
```
bash: line 1: gunicorn: command not found
==> Exited with status 127
```

**Cause:** Render is using default Django start command instead of our FastAPI uvicorn command.

---

## ✅ SOLUTION: Update Start Command in Render Dashboard

### **STEP 1: Go to Your Service Settings**
1. Open: https://dashboard.render.com/
2. Click on your **"naamveda-backend"** service
3. Click **"Settings"** tab (left sidebar)

---

### **STEP 2: Update Start Command**
1. Scroll down to **"Build & Deploy"** section
2. Find **"Start Command"** field
3. **DELETE** the current command (it's probably empty or has gunicorn)
4. **PASTE** this exact command:
   ```
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```
5. Click **"Save Changes"** button

---

### **STEP 3: Verify Build Command (Optional)**
While you're in Settings, also verify:

**Build Command** should be:
```
pip install --upgrade pip && pip install -r requirements.txt
```

If it's different, update it and click **"Save Changes"**

---

### **STEP 4: Trigger Manual Deploy**
1. Go to **"Manual Deploy"** section (top right)
2. Click **"Clear build cache & deploy"** button
3. Wait 2-3 minutes for deployment
4. Watch the logs - should see:
   ```
   ✅ Build successful 🎉
   ✅ Deploying...
   ✅ INFO:     Started server process
   ✅ INFO:     Uvicorn running on http://0.0.0.0:10000
   ```

---

### **STEP 5: Test Your Backend**
After successful deployment:

1. Copy your backend URL (top of page)
2. Visit: `https://your-backend-url.onrender.com/docs`
3. You should see **FastAPI Swagger UI** 🎉

---

## 🎯 Expected Success Output:
```
==> Build successful 🎉
==> Deploying...
==> Setting WEB_CONCURRENCY=1 by default
==> Running 'uvicorn app.main:app --host 0.0.0.0 --port $PORT'
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:10000 (Press CTRL+C to quit)
==> Your service is live 🎉
```

---

## 🐛 If Still Fails:

### Option A: Check Root Directory
1. In Settings, verify **"Root Directory"** = `backend`
2. If empty or wrong, update it
3. Save and redeploy

### Option B: Check Environment Variables
Make sure these are set in **"Environment"** tab:
- `PYTHON_VERSION` = `3.11.9`
- All other 15 variables from deployment guide

### Option C: Use Blueprint (render.yaml)
If manual setup keeps failing, try Blueprint deployment:
1. Delete current service
2. Click **"New +"** → **"Blueprint"**
3. Connect GitHub repo
4. Render will auto-read `render.yaml`
5. Click **"Apply"**

---

## 📝 Quick Reference:

**Start Command (COPY THIS):**
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

**Build Command (COPY THIS):**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Root Directory:**
```
backend
```

---

**Need Help?** The build succeeded (Python 3.11 worked!), so we're 90% there. Just need to fix the start command! 🚀
