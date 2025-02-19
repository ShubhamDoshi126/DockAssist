# 🚀 DockAssist: AI-Powered Dockerfile Generator  

DockAssist is an AI-powered tool designed to make **Docker** and **containerization** more accessible for developers—especially beginners! By simply uploading your project details, DockAssist generates a **ready-to-use Dockerfile**, ensuring your application is containerized with best practices.  

Whether you're new to **Docker** or want to automate your containerization workflow, DockAssist makes it effortless!  

## 🌟 Why Use DockAssist?  

- **Simplifies Containerization** 🐳: No need to manually write Dockerfiles—just provide details, and let AI handle the rest!  
- **Perfect for Beginners** 🎓: Encourages best practices and makes it easy to learn Docker without struggling with syntax.  
- **AI-Powered Optimization** 🤖: Uses **Google’s Gemini AI** to generate an efficient Dockerfile tailored to your project.  
- **Supports Various Dependencies** 📂: Upload your `requirements.txt`, `package.json`, or other dependency files.  
- **Streamlined Deployment** 🚀: Makes it easy to ship your applications in a containerized environment.  

---

## 🛠 Installation & Setup  

### 📌 Prerequisites  
- Python 3.10+  
- Docker Installed 🐳  
- Google Gemini API Key (for AI-powered generation)  

### 📥 Clone the Repository  
```sh
git clone https://github.com/yourusername/DockAssist.git
cd DockAssist
```

### 📦 Install Dependencies  
```sh
pip install -r requirements.txt
```

### 🔑 Set Up Google Gemini API Key  
Create a `config.py` file in the project root and add:  
```python
GENAI_API_KEY = "your-gemini-api-key"
```

---

## 🚀 Running DockAssist  

### 🖥 Run Locally  
```sh
python app.py
```
Visit `http://127.0.0.1:5000/` in your browser to start generating Dockerfiles!  

### 🐳 Run with Docker  
**Want to Dockerize DockAssist itself?** You can!  
```sh
docker build -t dockassist .
docker run -p 5000:5000 dockassist
```

---

## 🔥 How It Works  

1. **Open DockAssist** in your browser.  
2. **Enter project details** (language, dependencies, entry point, etc.).  
3. **Upload a dependency file** (e.g., `requirements.txt`).  
4. **Click "Generate Dockerfile"**, and the AI creates an optimized Dockerfile for you.  
5. **Use the generated Dockerfile** to containerize your project effortlessly!  

---

## 💡 Why Docker?  

Docker makes application deployment **faster, scalable, and platform-independent**! With DockAssist, even beginners can:  
✅ **Create portable applications** that run anywhere.  
✅ **Eliminate "works on my machine" issues** by using containers.  
✅ **Deploy with confidence** knowing the best practices are followed.  

---

### 📢 Join the Containerization Revolution!  

If you're a beginner, DockAssist is your gateway to mastering **Docker** and **containerized development**. Start today and take your projects to the next level! 🚀🐳  
