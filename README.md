🧠 AI-Powered SMS Marketing Dashboard

A full-stack web application that enables e-commerce brands to generate, schedule, and analyze AI-personalized SMS campaigns. Built with React, FastAPI, and OpenAI.
🚀 Features

    📝 AI SMS Generator: GPT-powered message generator tailored to customer and product data

    📊 Analytics Dashboard: Real-time charts to measure performance (CTR, open rate, etc.)

    🎯 Campaign Scheduling: Schedule and preview SMS messages

    🧪 A/B Testing: Compare different message variations

    🛍 Shopify Mock Integration: Simulated e-commerce data for campaigns

🛠️ Tech Stack
Layer	Stack
Frontend	React.js, TypeScript, Tailwind CSS
Backend	FastAPI (Python), PostgreSQL
Auth	JWT (token-based), bcrypt
AI	OpenAI GPT-4 (via API)
Data Viz	Chart.js / Recharts
Deployment	Render / Railway / Vercel
📁 Project Structure
```
📦 sms-ai-dashboard/
├── frontend/             # React + TypeScript UI
├── backend/              # FastAPI server & AI logic
│   ├── app/
│   │   ├── main.py       # Entry point
│   │   ├── auth/         # JWT-based auth
│   │   ├── ai/           # OpenAI integration
│   │   ├── routes/       # API routes
│   │   └── models/       # DB models (SQLAlchemy)
├── scripts/              # Mock data generators
├── README.md
```
🧪 Local Development
Backend (FastAPI)

cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

Frontend (React)

cd frontend
npm install
npm run dev

🔐 Authentication

    Custom user registration & login using bcrypt-hashed passwords

    JWT tokens stored in HTTP-only cookies for secure sessions

🤖 OpenAI Integration

    Uses GPT-4 via the OpenAI API

    Prompts include product names, customer segments, tone/style

    Optional: add RAG to enhance context (e.g., using Pinecone or local vector DB)

📦 Future Enhancements

    ✅ Real Shopify API integration

    ✅ Multi-user team support

    ✅ SMS gateway integration (e.g., Twilio)

--

This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.
