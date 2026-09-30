from flask import Flask, render_template, jsonify, abort, url_for, request
app = Flask(__name__)



BOOKS = [
    {
        "id": 1,
        "title": "Lập trình Python",
        "author": "Nguyễn Văn A",
        "year": 2024,
        "category": "Lập trình",
        "available": True
    },
    {
        "id": 2,
        "title": "Lập trình C++",
        "author": "Trần Văn B",
        "year": 2023,
        "category": "Lập trình",
        "available": True
    },
    {
        "id": 3,
        "title": "Cơ sở dữ liệu",
        "author": "Lê Văn C",
        "year": 2022,
        "category": "Cơ sở dữ liệu",
        "available": False
    },
    {
        "id": 4,
        "title": "Mạng máy tính",
        "author": "Phạm Văn D",
        "year": 2024,
        "category": "Mạng",
        "available": True
    },
    {
        "id": 5,
        "title": "Trí tuệ nhân tạo",
        "author": "Nguyễn Văn E",
        "year": 2025,
        "category": "Trí tuệ nhân tạo",
        "available": False
    },
    {
        "id": 6,
        "title": "Lập trình Web Flask",
        "author": "Trần Văn F",
        "year": 2025,
        "category": "Lập trình",
        "available": True
    }
]



@app.route("/")
def index():
    total = len(BOOKS)
    available = sum(1 for book in BOOKS if book["available"])

    return render_template(
        "base.html",
        total=total,
        available=available
    )


@app.route("/books")
def books():
    category = request.args.get("category")

    if category:
        filtered_books = [
            book for book in BOOKS
            if book["category"] == category
        ]
    else:
        filtered_books = BOOKS

    categories = sorted(set(book["category"] for book in BOOKS))

    return render_template(
        "books.html",
        books=filtered_books,
        categories=categories,
        selected_category=category
    )


@app.route("/books/<int:book_id>")
def book_detail(book_id):
    book = next(
        (book for book in BOOKS if book["id"] == book_id),
        None
    )

    if book is None:
        abort(404)

    return render_template(
        "detail.html",
        book=book
    )



@app.route("/api/books")
def api_books():
    return jsonify(BOOKS)

@app.route("/api/books/<int:book_id>")
def api_book_detail(book_id):
    book = next(
        (book for book in BOOKS if book["id"] == book_id),
        None
    )

    if book is None:
        return jsonify({
            "error": "Không có sách"
        }), 404

    return jsonify(book)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)