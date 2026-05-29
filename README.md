# 🕉️ Naamveda - AI-Powered Indian Baby Naming Platform

[![License](https://img.shields.io/badge/license-Proprietary-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/next.js-14-black.svg)](https://nextjs.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)

Naamveda is an AI-powered platform that generates spiritually meaningful Indian baby names using numerology, Nakshatra/Rashi, and Sanskrit meanings. Combining ancient Vedic wisdom with modern AI technology.

## ✨ Features

- 🤖 **AI-Powered Generation** - GPT-4 powered personalized name suggestions
- 🔢 **Numerology Engine** - Chaldean system calculations for auspicious names
- ⭐ **Vedic Astrology** - Nakshatra and Rashi compatibility
- 📜 **Sanskrit Meanings** - Deep cultural and spiritual significance
- 📄 **PDF Reports** - Beautiful downloadable reports with detailed analysis
- 💳 **Secure Payments** - Razorpay integration for seamless transactions
- 📱 **Responsive Design** - Beautiful UI optimized for all devices

## 🛠️ Tech Stack

**Frontend:**
- Next.js 14 (React)
- TypeScript
- Tailwind CSS
- Vercel (Deployment)

**Backend:**
- FastAPI (Python)
- PostgreSQL
- OpenAI GPT-4
- Razorpay
- Railway (Deployment)

## 📁 Project Structure

```
naamveda-mvp/
├── backend/
│   ├── app/
│   │   ├── api/v1/endpoints/    # API routes
│   │   ├── core/                # Configuration & database
│   │   └── services/            # Business logic
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── app/                     # Next.js pages
│   ├── components/              # React components
│   └── package.json
└── docker-compose.yml
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Node.js 18+
- PostgreSQL (or SQLite for local development)

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# Configure your .env file
uvicorn app.main:app --reload --port 6005
```

### Frontend Setup

```bash
cd frontend
npm install
cp .env.example .env.local
# Configure your .env.local file
npm run dev
```

### Access the Application

- **Frontend:** http://localhost:3000
- **Backend API:** http://localhost:6005
- **API Documentation:** http://localhost:6005/docs

## 🔧 Environment Variables

### Backend (.env)

```env
DATABASE_URL=postgresql://user:pass@localhost/naamveda
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=sk-your-openai-key
RAZORPAY_KEY_ID=rzp_test_your_key
RAZORPAY_KEY_SECRET=your_razorpay_secret
ALLOWED_ORIGINS=http://localhost:3000
```

### Frontend (.env.local)

```env
NEXT_PUBLIC_API_URL=http://localhost:6005
NEXT_PUBLIC_RAZORPAY_KEY_ID=rzp_test_your_key
```

## 📚 API Documentation

### Main Endpoints

- `POST /api/v1/names/generate` - Generate personalized baby names
- `POST /api/v1/payments/create-order` - Create payment order
- `GET /api/v1/reports/download/{report_id}` - Download PDF report
- `POST /api/v1/auth/register` - User registration
- `POST /api/v1/auth/login` - User login

**Interactive API Docs:** http://localhost:6005/docs

## 🐳 Docker Deployment

```bash
docker-compose up -d
```

## 📦 Production Deployment

See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) for detailed deployment instructions.

**Recommended Stack:**
- Frontend: Vercel (Free)
- Backend: Railway (Free tier available)
- Database: Railway PostgreSQL

## 🗺️ Roadmap

- [x] MVP with core features
- [x] Numerology engine
- [x] AI name generation
- [x] Payment integration
- [ ] Production deployment
- [ ] Custom domain
- [ ] WhatsApp delivery
- [ ] Email notifications
- [ ] Mobile apps (iOS/Android)
- [ ] Multi-language support

## 💰 Pricing

- **Free Preview:** 3 name suggestions
- **Premium Report:** ₹299 - Full report with 10 personalized names, meanings, and numerology analysis

## 🤝 Contributing

This is a proprietary project. For collaboration inquiries, please contact the developer.

## 📄 License

Proprietary - All rights reserved

## 📞 Contact

**Developer:** Pallav Anand  
**Location:** Noida, India  
**GitHub:** [@pallavanand305](https://github.com/pallavanand305)

---

**Built with ❤️ in India** 🇮🇳
