# 🚀 DEPLOYMENT GUIDE - GITHUB → RAILWAY → VERCEL

## 📋 OVERVIEW

**Strategy:** GitHub → Railway (Backend) → Vercel (Frontend)

**Time:** 20 minutes  
**Cost:** FREE (₹0)  
**Result:** Live website with permanent URLs

---

## ✅ PRE-DEPLOYMENT CHECKLIST

- [x] Code complete
- [x] .gitignore configured
- [x] No real API keys in code
- [x] Backend running locally
- [x] Frontend running locally
- [ ] GitHub account created
- [ ] Railway account created
- [ ] Vercel account created

---

## 🎯 STEP 1: PUSH TO GITHUB (5 minutes)

### 1.1 Create GitHub Account
- Go to: https://github.com/signup
- Sign up (FREE)

### 1.2 Create New Repository
1. Click "+" → "New repository"
2. Name: `naamveda-mvp`
3. Description: "AI-powered Indian baby naming platform"
4. Visibility: **Private** (recommended for now)
5. DON'T initialize with README
6. Click "Create repository"

### 1.3 Push Your Code

**Open terminal in project folder:**

```bash
cd naamveda-mvp

# Initialize git
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - Naamveda MVP ready for deployment"

# Add remote (replace YOUR-USERNAME)
git remote add origin https://github.com/YOUR-USERNAME/naamveda-mvp.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**✅ Done! Your code is on GitHub!**

---

## 🎯 STEP 2: DEPLOY BACKEND TO RAILWAY (7 minutes)

### 2.1 Create Railway Account
- Go to: https://railway.app
- Click "Login with GitHub"
- Authorize Railway

### 2.2 Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Select `naamveda-mvp` repo
4. Railway will detect both frontend and backend

### 2.3 Configure Backend Service
1. Click "Add Service" → "GitHub Repo"
2. Select your repo
3. **Root Directory:** `backend`
4. Railway auto-detects Python/FastAPI

### 2.4 Add Environment Variables
Click "Variables" tab, add these:

```env
DATABASE_URL=postgresql://postgres:password@postgres:5432/naamveda
SECRET_KEY=your-super-secret-key-change-this-12345678
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
OPENAI_API_KEY=sk-your-key-here
OPENAI_MODEL=gpt-4-turbo-preview
RAZORPAY_KEY_ID=rzp_test_your_key_id
RAZORPAY_KEY_SECRET=your_key_secret
ENVIRONMENT=production
LOG_LEVEL=INFO
ALLOWED_ORIGINS=https://naamveda.vercel.app
FRONTEND_URL=https://naamveda.vercel.app
```

**Note:** We'll update FRONTEND_URL after Vercel deployment

### 2.5 Add PostgreSQL Database
1. Click "New" → "Database" → "Add PostgreSQL"
2. Railway creates database automatically
3. DATABASE_URL is auto-configured

### 2.6 Deploy!
1. Click "Deploy"
2. Wait 2-3 minutes
3. Click "Settings" → "Generate Domain"
4. **Copy your backend URL:** `https://naamveda-api.railway.app`

**✅ Backend is live!**

Test it: `https://naamveda-api.railway.app/docs`

---

## 🎯 STEP 3: DEPLOY FRONTEND TO VERCEL (5 minutes)

### 3.1 Create Vercel Account
- Go to: https://vercel.com/signup
- Click "Continue with GitHub"
- Authorize Vercel

### 3.2 Import Project
1. Click "Add New..." → "Project"
2. Import `naamveda-mvp` repo
3. Vercel detects Next.js automatically

### 3.3 Configure Project
**Framework Preset:** Next.js (auto-detected)  
**Root Directory:** `frontend`  
**Build Command:** `npm run build` (auto-filled)  
**Output Directory:** `.next` (auto-filled)

### 3.4 Add Environment Variables
Click "Environment Variables", add:

```env
NEXT_PUBLIC_API_URL=https://naamveda-api.railway.app
NEXT_PUBLIC_RAZORPAY_KEY_ID=rzp_test_your_key_id
```

**Replace with YOUR Railway backend URL!**

### 3.5 Deploy!
1. Click "Deploy"
2. Wait 2-3 minutes
3. **Copy your frontend URL:** `https://naamveda.vercel.app`

**✅ Frontend is live!**

---

## 🎯 STEP 4: UPDATE BACKEND CORS (2 minutes)

### 4.1 Update Railway Environment Variables
1. Go back to Railway
2. Click your backend service
3. Click "Variables"
4. Update these:

```env
ALLOWED_ORIGINS=https://naamveda.vercel.app
FRONTEND_URL=https://naamveda.vercel.app
```

**Use YOUR actual Vercel URL!**

### 4.2 Redeploy Backend
1. Click "Deployments"
2. Click "Redeploy" on latest deployment
3. Wait 1 minute

**✅ CORS configured!**

---

## 🎯 STEP 5: TEST YOUR LIVE WEBSITE (3 minutes)

### 5.1 Open Your Website
Go to: `https://naamveda.vercel.app` (your actual URL)

### 5.2 Test Features
- [ ] Landing page loads
- [ ] All sections visible
- [ ] Click "Generate Names"
- [ ] Fill the form
- [ ] Submit
- [ ] Names generated!

### 5.3 Test API
Go to: `https://naamveda-api.railway.app/docs`
- [ ] API docs load
- [ ] Try `/api/v1/names/generate` endpoint

**✅ Everything working!**

---

## 🎉 YOU'RE LIVE!

### Your URLs:
- **Frontend:** `https://naamveda.vercel.app`
- **Backend:** `https://naamveda-api.railway.app`
- **API Docs:** `https://naamveda-api.railway.app/docs`

### Share with Friends:
Send them: `https://naamveda.vercel.app`

Ask: **"Would you pay ₹299 for this?"**

---

## 📊 WHAT YOU GET

### ✅ Features:
- Permanent URLs (don't change)
- Automatic HTTPS
- Global CDN (fast worldwide)
- Auto-deploy on git push
- Free SSL certificates
- Professional domains
- Unlimited bandwidth (Vercel)
- 500 hours/month (Railway free tier)

### 💰 Costs:
- **Month 1-2:** FREE ($5 Railway credit)
- **Month 3+:** $5/month (₹420/month)
- **Vercel:** FREE forever
- **GitHub:** FREE forever

---

## 🔄 AUTO-DEPLOYMENT

### Now when you make changes:

```bash
# Make changes to code
git add .
git commit -m "Updated feature X"
git push

# Vercel auto-deploys frontend (30 seconds)
# Railway auto-deploys backend (2 minutes)
```

**No manual deployment needed!** 🎉

---

## 🆘 TROUBLESHOOTING

### Frontend not loading?
- Check Vercel deployment logs
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check browser console for errors

### Backend not connecting?
- Check Railway deployment logs
- Verify environment variables
- Test API docs endpoint

### CORS errors?
- Update `ALLOWED_ORIGINS` in Railway
- Include your Vercel URL
- Redeploy backend

### Names not generating?
- Check if OpenAI key is added
- Mock data should still work
- Check Railway logs for errors

---

## 🎯 NEXT STEPS AFTER DEPLOYMENT

### Immediate (Today):
1. Test website yourself
2. Share with 3-5 close friends
3. Get initial feedback

### This Week:
1. Share with 10-20 people
2. Track "would pay" responses
3. Collect feedback

### If 5+ say YES:
1. Buy domain (₹800)
   - namkaran.ai
   - shubhnaam.in
2. Add custom domain to Vercel
3. Add OpenAI API key (₹1,000)
4. Launch to 100+ people!

---

## 💡 PRO TIPS

### Custom Domain (After validation):
1. Buy domain from Namecheap/GoDaddy
2. Add to Vercel: Settings → Domains
3. Update DNS records
4. Done! `https://naamveda.com`

### Environment Variables:
- Never commit real API keys
- Use Railway/Vercel dashboards
- Update via web interface

### Monitoring:
- Railway: Check logs for errors
- Vercel: Check analytics
- Both have free monitoring

### Scaling:
- Vercel: Auto-scales (FREE)
- Railway: Upgrade plan when needed
- Database: Railway handles it

---

## 📞 SUPPORT

### Railway:
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway

### Vercel:
- Docs: https://vercel.com/docs
- Support: https://vercel.com/support

### GitHub:
- Docs: https://docs.github.com
- Support: https://support.github.com

---

## ✅ DEPLOYMENT CHECKLIST

- [ ] GitHub account created
- [ ] Repository created
- [ ] Code pushed to GitHub
- [ ] Railway account created
- [ ] Backend deployed to Railway
- [ ] PostgreSQL database added
- [ ] Backend environment variables set
- [ ] Backend domain generated
- [ ] Vercel account created
- [ ] Frontend deployed to Vercel
- [ ] Frontend environment variables set
- [ ] Backend CORS updated
- [ ] Website tested
- [ ] API tested
- [ ] URL shared with friends

---

## 🚀 READY TO DEPLOY?

**Start with Step 1: Push to GitHub**

Run these commands:
```bash
cd naamveda-mvp
git init
git add .
git commit -m "Initial commit - Naamveda MVP"
```

Then create GitHub repo and push!

**I'll help you with each step!** 🎉

---

**Last Updated:** May 29, 2026  
**Status:** Ready to deploy  
**Estimated Time:** 20 minutes  
**Cost:** FREE
