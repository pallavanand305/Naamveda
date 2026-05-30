# 🔧 FIX: CORS Issue - Frontend Can't Connect to Backend

## 🎯 THE PROBLEM:
Your backend is working, but the frontend can't connect due to CORS (Cross-Origin Resource Sharing) restrictions.

---

## ✅ SOLUTION: Add Vercel URL to CORS Allowed Origins

### **STEP 1: Go to Render Dashboard**
1. Open: https://dashboard.render.com/
2. Click on **"naamveda-backend"** service

### **STEP 2: Go to Environment Tab**
1. Click **"Environment"** in the left sidebar
2. Look for `ALLOWED_ORIGINS` variable

### **STEP 3: Update ALLOWED_ORIGINS**

**If the variable EXISTS:**
1. Click **"Edit"** (pencil icon) next to `ALLOWED_ORIGINS`
2. Update the value to:
   ```
   https://naamveda.vercel.app,http://localhost:3001,http://localhost:3000
   ```
3. Click **"Save Changes"**

**If the variable DOESN'T EXIST:**
1. Click **"Add Environment Variable"** button
2. **Key:** `ALLOWED_ORIGINS`
3. **Value:** `https://naamveda.vercel.app,http://localhost:3001,http://localhost:3000`
4. Click **"Save"**

### **STEP 4: Also Add FRONTEND_URL**

Add another environment variable:
1. Click **"Add Environment Variable"**
2. **Key:** `FRONTEND_URL`
3. **Value:** `https://naamveda.vercel.app`
4. Click **"Save"**

### **STEP 5: Wait for Auto-Redeploy**
- Render will automatically redeploy when you save environment variables
- Wait 2-3 minutes for the service to restart
- Watch the **"Events"** tab for deployment status

---

## 🧪 TEST AFTER REDEPLOY:

### **Test 1: Check CORS Headers**
1. Open: https://naamveda.vercel.app
2. Press **F12** (Developer Tools)
3. Go to **"Network"** tab
4. Try generating names again
5. Click on the request to `naamveda-backend.onrender.com`
6. Check **"Response Headers"** - should see:
   ```
   access-control-allow-origin: https://naamveda.vercel.app
   ```

### **Test 2: Generate Names**
1. Fill in the form on https://naamveda.vercel.app
2. Click **"Generate Names"**
3. Should see 3 names with numerology scores! 🎉

---

## 🐛 IF STILL NOT WORKING:

### **Check Browser Console:**
1. Press **F12**
2. Go to **"Console"** tab
3. Look for errors
4. Share the error message

### **Common Errors:**

**Error 1: "CORS policy: No 'Access-Control-Allow-Origin'"**
- **Fix:** Make sure `ALLOWED_ORIGINS` includes `https://naamveda.vercel.app`
- **Fix:** Make sure there are NO spaces after commas in the value

**Error 2: "Failed to fetch"**
- **Fix:** Check if backend is awake (visit /health endpoint)
- **Fix:** Wait 60 seconds for cold start

**Error 3: "500 Internal Server Error"**
- **Fix:** Check Render logs for Python errors
- **Fix:** May need to check AI generator service

---

## 📝 COMPLETE ENVIRONMENT VARIABLES LIST:

Here's what you should have in Render:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `your-super-secret-key-change-this-in-production-min-32-chars` |
| `ALGORITHM` | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` |
| `DATABASE_URL` | `sqlite:///./naamveda.db` |
| `OPENAI_API_KEY` | `sk-dummy-key-for-testing` |
| `RAZORPAY_KEY_ID` | `rzp_test_dummy` |
| `RAZORPAY_KEY_SECRET` | `dummy_secret` |
| `FRONTEND_URL` | `https://naamveda.vercel.app` |
| `BACKEND_URL` | `https://naamveda-backend.onrender.com` |
| `ENVIRONMENT` | `production` |
| `ALLOWED_ORIGINS` | `https://naamveda.vercel.app,http://localhost:3001,http://localhost:3000` |
| `PYTHON_VERSION` | `3.11.9` |

---

## 🎯 QUICK FIX SUMMARY:

1. ✅ Go to Render → Environment
2. ✅ Add/Update `ALLOWED_ORIGINS` = `https://naamveda.vercel.app,http://localhost:3001,http://localhost:3000`
3. ✅ Add/Update `FRONTEND_URL` = `https://naamveda.vercel.app`
4. ✅ Save and wait 2-3 minutes
5. ✅ Test on https://naamveda.vercel.app

---

**This should fix the CORS issue!** Let me know once you've updated the environment variables! 🚀
