# 🚀 Render Backend Deployment - Step by Step

## ✅ STEP 1: Go to Render Dashboard
1. Open: https://dashboard.render.com/
2. Click **"New +"** button (top right)
3. Select **"Web Service"**

---

## ✅ STEP 2: Connect GitHub Repository
1. Click **"Build and deploy from a Git repository"**
2. Click **"Connect account"** if not connected
3. Find and select: **pallavanand305/Naamveda**
4. Click **"Connect"**

---

## ✅ STEP 3: Configure Basic Settings

### Fill these fields EXACTLY:

**Name:** `naamveda-backend`

**Region:** `Singapore (Southeast Asia)` *(closest to India)*

**Branch:** `main`

**Root Directory:** `backend` ⚠️ **IMPORTANT!**

**Runtime:** Should auto-detect as **Python 3**

---

## ✅ STEP 4: Configure Build & Start Commands

**Build Command:**
```
pip install --upgrade pip && pip install -r requirements.txt
```

**Start Command:**
```
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## ✅ STEP 5: Select Instance Type

**Instance Type:** Select **"Free"** ($0/month)

⚠️ **Note:** Free instances spin down after 15 minutes of inactivity. First request after spin-down takes 30-60 seconds.

---

## ✅ STEP 6: Add Environment Variables

Click **"Add Environment Variable"** and add these **15 variables**:

| Key | Value |
|-----|-------|
| `SECRET_KEY` | `your-super-secret-key-change-this-in-production-min-32-chars` |
| `ALGORITHM` | `HS256` |
| `ACCESS_TOKEN_EXPIRE_MINUTES` | `30` |
| `DATABASE_URL` | `sqlite:///./naamveda.db` |
| `OPENAI_API_KEY` | `sk-dummy-key-for-testing` |
| `RAZORPAY_KEY_ID` | `rzp_test_your_key_id` |
| `RAZORPAY_KEY_SECRET` | `your_razorpay_secret` |
| `FRONTEND_URL` | `https://naamveda.vercel.app` |
| `BACKEND_URL` | `https://naamveda-backend.onrender.com` |
| `ENVIRONMENT` | `production` |
| `CORS_ORIGINS` | `https://naamveda.vercel.app,http://localhost:3001` |
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | `your-email@gmail.com` |
| `SMTP_PASSWORD` | `your-app-password` |

⚠️ **Note:** After deployment, you'll get the actual Render URL. Come back and update `BACKEND_URL` with it.

---

## ✅ STEP 7: Advanced Settings (Optional but Recommended)

Scroll down to **"Advanced"** section:

**Python Version:** 
- If you see a field for Python version, enter: `3.11.9`
- If not visible, skip (we've configured it in files)

**Auto-Deploy:** Keep **"Yes"** (deploys automatically on git push)

---

## ✅ STEP 8: Deploy!

1. Click **"Create Web Service"** button at the bottom
2. Wait 3-5 minutes for deployment
3. Watch the logs - should see:
   - ✅ Using Python version 3.11.9
   - ✅ Installing dependencies
   - ✅ Starting uvicorn server

---

## ✅ STEP 9: Get Your Backend URL

After successful deployment:
1. Copy the URL from top of page (looks like: `https://naamveda-backend.onrender.com`)
2. Test it by visiting: `https://naamveda-backend.onrender.com/docs`
3. You should see FastAPI Swagger documentation

---

## ✅ STEP 10: Update Backend URL in Render

1. Go to **"Environment"** tab in Render dashboard
2. Find `BACKEND_URL` variable
3. Update it with your actual Render URL
4. Click **"Save Changes"**
5. Service will auto-redeploy

---

## ✅ STEP 11: Update Frontend on Vercel

1. Go to: https://vercel.com/dashboard
2. Click on **"naamveda"** project
3. Go to **"Settings"** → **"Environment Variables"**
4. Find `NEXT_PUBLIC_API_URL`
5. Update value to: `https://naamveda-backend.onrender.com` (your actual URL)
6. Click **"Save"**
7. Go to **"Deployments"** tab
8. Click **"..."** on latest deployment → **"Redeploy"**

---

## ✅ STEP 12: Test Complete Flow

1. Visit: https://naamveda.vercel.app
2. Click **"Generate Name"** button
3. Fill the form:
   - Father's Name: `Rajesh Kumar`
   - Mother's Name: `Priya Sharma`
   - Date of Birth: `2024-01-15`
   - Gender: `Male`
   - Religion: `Hindu`
4. Click **"Generate Names"**
5. Should see 10 names with numerology scores! 🎉

---

## 🎯 Expected Results

✅ Backend URL: `https://naamveda-backend.onrender.com`
✅ Frontend URL: `https://naamveda.vercel.app`
✅ API Docs: `https://naamveda-backend.onrender.com/docs`
✅ Name generation works with mock data (no OpenAI key needed)

---

## 🐛 Troubleshooting

### If deployment fails with Python 3.14 error:
1. Go to Render dashboard → Your service
2. Click **"Environment"** tab
3. Add new variable: `PYTHON_VERSION` = `3.11.9`
4. Click **"Manual Deploy"** → **"Clear build cache & deploy"**

### If "Failed to fetch" error on frontend:
1. Check backend URL is correct in Vercel env variables
2. Check CORS_ORIGINS includes your Vercel URL
3. Wait 60 seconds after first request (free tier cold start)

### If names don't generate:
1. Check backend logs in Render dashboard
2. Verify mock data is working (no OpenAI key needed)
3. Check browser console for errors

---

## 💰 Cost Breakdown

**Current Setup (FREE):**
- Vercel: FREE (Hobby plan)
- Render: FREE (512 MB RAM, spins down after 15 min)
- **Total: ₹0/month** ✅

**After 5+ YES responses (₹1,800 investment):**
- Domain (.in): ₹800/year
- OpenAI API: ₹1,000 initial credit
- Vercel: Still FREE
- Render: Still FREE
- **Total: ₹1,800 one-time**

**Monthly costs after initial investment:**
- Domain: ₹67/month (₹800/12)
- OpenAI: ~₹100-300/month (usage-based)
- Vercel: FREE
- Render: FREE (or upgrade to $7/month for no spin-down)
- **Total: ₹167-367/month**

---

## 🎉 Next Steps After Deployment

1. ✅ Test with 10-20 friends
2. ✅ Get 5+ YES responses for ₹299 payment
3. ✅ Buy domain from GoDaddy/Hostinger (₹800)
4. ✅ Add OpenAI API key (₹1,000 credit)
5. ✅ Add Razorpay payment integration
6. ✅ Launch! 🚀

---

**Need Help?** Check logs in Render dashboard or contact support.
