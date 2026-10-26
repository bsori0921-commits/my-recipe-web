
from flask import Flask, render_template, request
import json
from pathlib import Path

app = Flask(__name__)

# JSON 파일에서 레시피 불러오기
def load_recipes():
    path = Path(__file__).parent / "recipes.json"

    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


@app.route("/")
def home():
    recipes = load_recipes()

    # 사용자가 검색한 음식 이름
    keyword = request.args.get("search", "").strip()

    # 음식 이름에 검색어가 포함되는지 확인
    if keyword:
        results = {
            name: recipe
            for name, recipe in recipes.items()
            if keyword.lower() in name.lower()
        }
    else:
        results = recipes

    return render_template(
        "index.html",
        recipes=results,
        keyword=keyword
    )


if __name__ == "__main__":
    app.run(debug=True)
