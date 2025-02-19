import os
from flask import Flask, request, render_template, send_file
import google.generativeai as genai
from werkzeug.utils import secure_filename
from config import GENAI_API_KEY

# Set API Key
genai.configure(api_key=GENAI_API_KEY)

# Flask App Setup
app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = "uploads"
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)


# HTML Form with CSS
HTML_FORM = """
<!DOCTYPE html>
<html lang="en">
<head>
    <title>DockAssist AI Dockerfile Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            width: 400px;
        }
        h1 {
            margin-top: 0;
            color: #333;
            align-self: center;
        }
        h2 {
            margin-top: 0;
            color: #333;
        }
        form {
            display: flex;
            flex-direction: column;
        }
        input[type="text"], input[type="file"] {
            margin-bottom: 10px;
            padding: 8px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        input[type="submit"] {
            padding: 10px;
            background-color: #007bff;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        input[type="submit"]:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>DockAssist AI Dockerfile Generator</h1>
        <h2>Upload Project Files & Provide Details</h2>
        <form action="/" method="post" enctype="multipart/form-data">
            Programming Language: <input type="text" name="language" required><br>
            Dependencies (File or List): <input type="file" name="file"><br>
            Build Steps: <input type="text" name="build_steps"><br>
            Entry Point: <input type="text" name="entry_point"><br>
            Port: <input type="text" name="port"><br>
            Additional Configurations: <input type="text" name="additional_configs"><br>
            <input type="submit" value="Generate Dockerfile">
        </form>
    </div>
</body>
</html>
"""


# Function to generate Dockerfile using Gemini API
def generate_dockerfile(details):
    prompt = f"""
    Generate an optimized Dockerfile for the following project:

    Programming Language: {details['language']}
    Dependencies: {details['dependencies']}
    Build Steps: {details['build_steps']}
    Entry Point: {details['entry_point']}
    Port: {details['port']}
    Additional Configurations: {details['additional_configs']}

    Ensure best practices, security, and multi-stage builds where applicable. For each section write a small comment explaining the purpose of the step.
    """

    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)

    return response.text

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        details = {
            "language": request.form["language"],
            "dependencies": "",
            "build_steps": request.form.get("build_steps", ""),
            "entry_point": request.form.get("entry_point", ""),
            "port": request.form.get("port", ""),
            "additional_configs": request.form.get("additional_configs", ""),
        }

        # Handle file upload
        if "file" in request.files and request.files["file"].filename:
            file = request.files["file"]
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(file_path)

            # Read file content (if it's a text-based dependency file)
            if filename.endswith((".txt", ".json", ".yml", ".yaml")):
                with open(file_path, "r") as f:
                    details["dependencies"] = f.read()

        # Generate Dockerfile
        dockerfile_content = generate_dockerfile(details)

        # Save to file
        dockerfile_path = os.path.join(app.config["UPLOAD_FOLDER"], "Dockerfile")
        with open(dockerfile_path, "w") as f:
            f.write(dockerfile_content)

        return send_file(dockerfile_path, as_attachment=True)

    return HTML_FORM

if __name__ == "__main__":
    app.run(debug=True)
