import os

from dotenv import load_dotenv
from flask import Flask, render_template_string, request
from openai import OpenAI

load_dotenv()

app = Flask(__name__)



HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>SmartWrite AI</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
        }

        textarea {
            width: 100%;
            height: 180px;
            padding: 12px;
            font-size: 16px;
            box-sizing: border-box;
        }

        select, button {
            margin-top: 15px;
            padding: 10px;
            font-size: 16px;
        }

        button {
            cursor: pointer;
        }

        .result {
            margin-top: 30px;
            padding: 20px;
            background: #f3f3f3;
            white-space: pre-wrap;
        }
    </style>
</head>

<body>
    <h1>SmartWrite AI</h1>
    <p>Improve your writing instantly with AI.</p>

    <form method="POST">
        <textarea name="text"
                  placeholder="Enter your text here..."
                  required>{{ text }}</textarea>

        <br>

        <select name="style">
            <option value="Professional">Professional</option>
            <option value="Friendly">Friendly</option>
            <option value="Shorter">Shorter</option>
        </select>

        <br>

        <button type="submit">Improve Text</button>
    </form>

    {% if result %}
    <div class="result">
        <strong>Improved Text:</strong>
        <p>{{ result }}</p>
    </div>
    {% endif %}
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    text = ""

    if request.method == "POST":
        text = request.form["text"]
        style = request.form["style"]
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
Improve the following text.

Style: {style}

Original text:
{text}

Return only the improved version.
"""

        response = client.responses.create(
            model="gpt-4o-mini",
            input=prompt
        )

        result = response.output_text

    return render_template_string(
        HTML,
        result=result,
        text=text
    )


if __name__ == "__main__":
    app.run(debug=True)