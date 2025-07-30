# AI-Career-Counseling-System-Multi-Agent-Overview!

Problem Statement
Young professionals and students often struggle with career guidance due to limited access to personalized counseling. This system aims to provide end-to-end AI-driven support for resume analysis, skill matching, and job opportunity discovery — powered by multiple collaborating AI agents. Many students and early professionals struggle to identify suitable job roles based on their resumes and skills. Manual counseling is time-consuming, expensive, and lacks personalization.


📁 AI-Career-Counseling-System
├── AI_Career_Counselor.ipynb       ← Colab Notebook (main project)
├── README.md                       ← Project description for GitHub
├── requirements.txt                ← Python libraries used
├── resume_sample.txt               ← Optional sample resume
└── .zip                            ← Final zip file for submission (we’ll create at the end)

## 🚀 Solution Overview

We built an **AI Career Counseling System** using **multi-agent architecture** to automate career advice. The system consists of 3 AI agents:

- 📄 **Resume Analyzer Agent** – extracts user’s qualifications, experience, and skills.
- 🧠 **Skill-Job Matcher Agent** – maps resume content to ideal job titles.
- 🌐 **Job Finder Agent** – suggests trending job roles from real-time or predefined databases.

Each agent operates independently and collaborates to provide actionable career guidance.

---

## 🧠 Why Multi-Agent AI?

A single monolithic model might miss the contextual nuances of resume screening, skill evaluation, and job mapping. Multi-agent AI enables:
- Task delegation
- Clear division of responsibilities
- Modular design
- Scalability and adaptability

---

## 🛠️ Tools, Libraries, and Frameworks

- **LLM**: Gemini 1.5 Pro (via Google Generative AI)
- **Platform**: Google Colab (free, interactive)
- **Languages**: Python
- **APIs**: `google-generativeai` library
- **Orchestration**: Custom agent logic (can be scaled to CrewAI or LangChain in future)

---

## 💡 LLM Selection

| Model | Usage | Tier |
|-------|-------|------|
| Gemini 1.5 Pro | Resume understanding, career suggestions | ✅ Free |
| Others Considered | OpenAI GPT-4, Claude 3 | ❌ Paid |

Gemini 1.5 Pro was selected for:
- High-quality natural language understanding
- Free access via Google AI Studio
- No credit card required

---

## ⚙️ How to Run

1. Open the Colab file: https://colab.research.google.com/drive/1tkX49bHnJcwa5C7Z4PITeZ90Mnx_4sYF?usp=sharing
2. Add your **Google Gemini API Key**.
3. Upload your resume (or paste content).
4. Run the cells and get:
   - Top 3 job roles
   - Career advice
   - Skill-job alignment

---

## 📁 Folder Contents

| File | Description |
|------|-------------|
| `AI_Career_Counselor.ipynb` | Colab project code |
| `requirements.txt` | Required libraries |
| `README.md` | This file |

---

## 🔚 Conclusion

This AI Career Counseling System empowers users to get job advice instantly with personalized suggestions. Multi-agent design ensures modularity, clarity, and effectiveness.


