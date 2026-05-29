# 🚀 DEPLOYMENT GUIDE - STEP BY STEP

## 📋 OVERVIEW

**Time:** 20 minutes  
**Cost:** FREE (₹0)  
**Result:** Live website accessible to anyone

**Stack:**
- Backend → Railway (FREE tier)
- Frontend → Vercel (FREE forever)
- Database → Railway PostgreSQL (FREE tier)

---

## 🎯 STEP 1: DEPLOY BACKEND TO RAILWAY (10 mins)

### 1.1 Create Railway Account

1. Go to: **https://railway.app**
2. Click **"Login with GitHub"**
3. Authorize Railway to access your GitHub
4. You'll get **$5 FREE credit** (good for 2 months)

### 1.2 Create New Project

1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Search and select: **"Naamveda"**
4. Click on your repository

### 1.3 Configure Backend Service

1. Railway will scan your repo
2. Click **"Add a service"**
3. Select **"GitHub Repo"**
4. Choose **"Naamveda"** repo again
5. **IMPORTANT:** Click **"Settings"** → **"Root Directory"**
6. Enter: `backend`
7. Click **"Save"**

Railway will auto-detect:
- ✅ Python
- ✅ FastAPI
- ✅ requirements.txt

### 1.4 Add PostgreSQL Database

1. In the same project, click **"New"**
2. Select **"Database"**
3. Choose **"Add PostgreSQL"**
4. Railway creates database automatically
5. Wait 1 minute for database to be ready

### 1.5 Add Environment Variables

1. Click on your **backend service** (not database)
2. Go to **"Variables"** tab
3. Click **"+ New Variable"**
4. Add these one by one:

```env
DATABASE_URL=${{Postgres.DATABASE_URL}}
SECRET_KEY=naamveda-production-secret-key-2026-change-this-to-random-string
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4-turbo-preview
RAZORPAY_KEY_ID=rzp_test_your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
ENVIRONMENT=production
LOG_LEVEL=INFO
ALLOWED_ORIGINS=*
FRONTEND_URL=https://naamveda.vercel.app
FREE_NAMES_COUNT=3
PREMIUM_NAMES_COUNT=10
PREMIUM_REPORT_PRICE=29900
```

**IMPORTANT NOTES:**
- `DATABASE_URL=${{Postgres.DATABASE_URL}}` - Railway auto-fills this!
- `ALLOWED_ORIGINS=*` - We'll update this after Vercel deployment
- `FRONTEND_URL` - We'll update this after Vercel deployment
- OpenAI and Razorpay keys are optional for now (mock data works!)

### 1.6 Generate Domain

1. Click on your backend service
2. Go to **"Settings"** tab
3. Scroll to **"Networking"** section
4. Click **"Generate Domain"**
5. Railway creates a public URL

**COPY THIS URL!** Example: `https://naamveda-production.up.railway.app`

### 1.7 Deploy!

1. Railway automatically deploys
2. Go to **"Deployments"** tab
3. Wait 2-3 minutes
4. Status should show: ✅ **Success**

### 1.8 Test Backend

Open in browser: `https://YOUR-BACKEND-URL.railway.app/docs`

You should see: **FastAPI Swagger documentation**

✅ **Backend is LIVE!**

---

## 🎯 STEP 2: DEPLOY FRONTEND TO VERCEL (10 mins)

### 2.1 Create Vercel Account

1. Go to: **https://vercel.com/signup**
2. Click **"Continue with GitHub"**
3. Authorize Vercel
4. Complete signup (FREE forever)

### 2.2 Import Project

1. Click **"Add New..."** → **"Project"**
2. Find **"Naamveda"** in your repos
3. Click **"Import"**

### 2.3 Configure Project

**Framework Preset:** Next.js ✅ (auto-detected)

**Root Directory:**
1. Click **"Edit"** next to Root Directory
2. Enter: `frontend`
3. Click **"Continue"**

**Build Settings:** (Leave as default)
- Build Command: `npm run build`
- Output Directory: `.next`
- Install Command: `npm install`

### 2.4 Add Environment Variables

Click **"Environment Variables"** section

**Add Variable 1:**
- Name: `NEXT_PUBLIC_API_URL`
- Value: `https://YOUR-RAILWAY-BACKEND-URL.railway.app`
- (Use YOUR actual Railway URL from Step 1.6!)

**Add Variable 2:**
- Name: `NEXT_PUBLIC_RAZORPAY_KEY_ID`
- Value: `rzp_test_your_key_id`
- (Optional for now)

### 2.5 Deploy!

1. Click **"Deploy"**
2. Vercel starts building
3. Wait 2-3 minutes
4. You'll see: **"Congratulations!"** 🎉

### 2.6 Get Your Frontend URL

Vercel shows your live URL:
- Example: `https://naamveda.vercel.app`
- Or: `https://naamveda-git-main-pallavanand305.vercel.app`

**COPY THIS URL!**

### 2.7 Test Frontend

1. Open your Vercel URL in browser
2. You should see: Beautiful landing page! ✅
3. Click **"Generate Names"**
4. Fill the form and test

✅ **Frontend is LIVE!**

---

## 🎯 STEP 3: UPDATE BACKEND CORS (2 mins)

Now we need to connect frontend to backend properly.

### 3.1 Go Back to Railway

1. Open Railway dashboard
2. Click your **backend service**
3. Go to **"Variables"** tab

### 3.2 Update Variables

Find and update these:

**ALLOWED_ORIGINS:**
```
https://naamveda.vercel.app,https://naamveda-git-main-pallavanand305.vercel.app
```
(Use YOUR actual Vercel URLs - include both!)

**FRONTEND_URL:**
```
https://naamveda.vercel.app
```
(Use YOUR main Vercel URL)

### 3.3 Redeploy Backend

1. Go to **"Deployments"** tab
2. Click **"..."** on latest deployment
3. Click **"Redeploy"**
4. Wait 1 minute

✅ **CORS Updated!**

---

## 🎉 STEP 4: TEST YOUR LIVE WEBSITE!

### 4.1 Open Your Website

Go to: `https://naamveda.vercel.app` (your actual URL)

### 4.2 Test Everything

**Landing Page:**
- [ ] Page loads beautifully
- [ ] All sections visible
- [ ] Mobile responsive
- [ ] Images load

**Name Generator:**
- [ ] Click "Generate Names" button
- [ ] Fill the form:
  - Gender: Boy
  - Date of Birth: 15-08-2024
  - Starting Letter: A
  - Religion: Hindu
  - Style: Modern
  - Intention: Success
- [ ] Click "Generate Names"
- [ ] Wait 2-3 seconds
- [ ] Names appear! ✅

**Check Results:**
- [ ] 3 names shown (free preview)
- [ ] Each name has meaning
- [ ] Numerology numbers shown
- [ ] "Why this name" explanation
- [ ] Spiritual blessing

### 4.3 Test API Directly

Go to: `https://YOUR-BACKEND-URL.railway.app/docs`

- [ ] API documentation loads
- [ ] Try `/api/v1/names/generate` endpoint
- [ ] Test with sample data

✅ **Everything Working!**

---

## 📱 STEP 5: SHARE WITH FRIENDS!

### 5.1 Your Live URLs

**Frontend (Share this!):**
```
https://naamveda.vercel.app
```

**Backend API:**
```
https://naamveda-production.up.railway.app
```

**API Docs:**
```
https://naamveda-production.up.railway.app/docs
```

### 5.2 Message to Send Friends

```
Hey! 👋

I built an AI-powered baby naming platform called Naamveda!

It generates spiritually meaningful Indian baby names using:
✨ Numerology (Chaldean system)
✨ Sanskrit meanings
✨ Vedic astrology
✨ AI personalization

Try it here: https://naamveda.vercel.app

Just fill the form and get 3 FREE name suggestions!

I'd love your honest feedback:
1. Would you pay ₹299 for a full report with 10 names?
2. What do you like most?
3. What's missing or confusing?

Thanks! 🙏
```

### 5.3 Track Responses

| # | Name | Would Pay? | Liked | Concerns | Date |
|---|------|------------|-------|----------|------|
| 1 | | ☐ YES ☐ NO | | | |
| 2 | | ☐ YES ☐ NO | | | |
| 3 | | ☐ YES ☐ NO | | | |
| 4 | | ☐ YES ☐ NO | | | |
| 5 | | ☐ YES ☐ NO | | | |
| 6 | | ☐ YES ☐ NO | | | |
| 7 | | ☐ YES ☐ NO | | | |
| 8 | | ☐ YES ☐ NO | | | |
| 9 | | ☐ YES ☐ NO | | | |
| 10 | | ☐ YES ☐ NO | | | |

**Target:** 5+ YES responses

---

## 💰 COST BREAKDOWN

### Current (First 2 Months):
- Railway: **FREE** ($5 credit)
- Vercel: **FREE** (forever)
- GitHub: **FREE**
- **Total: ₹0**

### After 2 Months:
- Railway: **$5/month** (₹420/month)
- Vercel: **FREE** (forever)
- **Total: ₹420/month**

### When to Add Costs:
- Domain: ₹800/year (after 5+ YES)
- OpenAI API: ₹1,000 (after first customer)

---

## 🔄 AUTO-DEPLOYMENT

### Now Enabled!

When you make changes:

```bash
cd naamveda-mvp
git add .
git commit -m "Updated feature"
git push origin main
```

**Automatic:**
- ✅ Vercel redeploys frontend (30 seconds)
- ✅ Railway redeploys backend (2 minutes)

No manual work needed! 🎉

---

## 🆘 TROUBLESHOOTING

### Frontend Not Loading?
1. Check Vercel deployment logs
2. Verify `NEXT_PUBLIC_API_URL` is correct
3. Check browser console (F12)

### Backend Not Connecting?
1. Check Railway deployment logs
2. Verify environment variables
3. Test API docs endpoint

### CORS Errors?
1. Update `ALLOWED_ORIGINS` in Railway
2. Include all Vercel URLs
3. Redeploy backend

### Names Not Generating?
1. Check Railway logs for errors
2. Mock data should work without OpenAI
3. Try different form inputs

### Database Errors?
1. Check if PostgreSQL is running in Railway
2. Verify `DATABASE_URL` variable
3. Check Railway logs

---

## 📊 DEPLOYMENT CHECKLIST

- [ ] Railway account created
- [ ] Backend deployed to Railway
- [ ] PostgreSQL database added
- [ ] Backend environment variables set
- [ ] Backend domain generated
- [ ] Backend tested (API docs load)
- [ ] Vercel account created
- [ ] Frontend deployed to Vercel
- [ ] Frontend environment variables set
- [ ] Frontend URL copied
- [ ] Backend CORS updated
- [ ] Backend redeployed
- [ ] Website tested (names generate)
- [ ] URLs shared with friends
- [ ] Feedback tracking started

---

## 🎯 SUCCESS CRITERIA

### Technical:
- ✅ Website loads in < 3 seconds
- ✅ Names generate successfully
- ✅ Mobile responsive
- ✅ No console errors
- ✅ API responds correctly

### Business:
- ✅ 10+ people tested
- ✅ 5+ said "YES, would pay"
- ✅ Positive feedback
- ✅ Clear value proposition

---

## 🚀 NEXT STEPS AFTER DEPLOYMENT

### Immediate (Today):
1. Test website yourself
2. Share with 3-5 close friends
3. Get initial feedback
4. Fix any bugs

### This Week:
1. Share with 10-20 people
2. Collect detailed feedback
3. Track "would pay" responses
4. Identify common patterns

### If 5+ Say YES:
1. Buy domain (₹800)
2. Add custom domain to Vercel
3. Add OpenAI API key (₹1,000)
4. Complete payment integration
5. Launch to 100+ people!

---

## 💡 PRO TIPS

### Railway:
- Check logs regularly for errors
- Monitor usage (free tier limits)
- Upgrade when needed

### Vercel:
- Use preview deployments for testing
- Check analytics for traffic
- Free tier is generous

### GitHub:
- Commit often with clear messages
- Use branches for big changes
- Keep main branch stable

---

## 📞 SUPPORT

### Railway:
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway

### Vercel:
- Docs: https://vercel.com/docs
- Support: https://vercel.com/support

### Your Project:
- GitHub: https://github.com/pallavanand305/Naamveda.git
- Backend: https://YOUR-URL.railway.app
- Frontend: https://YOUR-URL.vercel.app

---

## ✅ READY TO DEPLOY?

**Start with Step 1: Railway Backend**

Go to: **https://railway.app**

You're 20 minutes away from being LIVE! 🚀

---

**Last Updated:** May 29, 2026  
**Status:** Ready for deployment  
**Estimated Time:** 20 minutes  
**Cost:** FREE
