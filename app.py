from flask import Flask, render_template_string, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "shopping123"

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 15000},
    {"id": 3, "name": "Headphones", "price": 2000},
]

html = """
<!DOCTYPE html>
<html>
<head>
<title>My Shopping Store</title>
<style>
body{font-family:Arial;background:#f2f2f2;text-align:center;}
.card{background:white;padding:15px;margin:20px auto;width:250px;
border-radius:10px;box-shadow:0 0 10px gray;}
button{background:green;color:white;padding:10px;border:none;border-radius:5px;}
a{font-size:20px;text-decoration:none;}
</style>
</head>
<body>

<h1>🛒 My Shopping Store</h1>

<p><a href="/cart">View Cart ({{cart_count}})</a></p>

{% for p in products %}
<div class="card">
<h2>{{p.name}}</h2>
<h3>₹{{p.price}}</h3>
<a href="/add/{{p.id}}"><button>Add to Cart</button></a>
</div>
{% endfor %}

</body>
</html>
"""

cart_html = """
<h1>Your Cart</h1>
{% for item in items %}
<p>{{item.name}} - ₹{{item.price}}</p>
{% endfor %}
<a href="/">⬅ Back to Shop</a>
"""

@app.route("/")
def home():
    cart = session.get("cart", [])
    return render_template_string(html, products=products, cart_count=len(cart))

@app.route("/add/<int:id>")
def add(id):
    cart = session.get("cart", [])
    cart.append(id)
    session["cart"] = cart
    return redirect(url_for("home"))

@app.route("/cart")
def cart():
    cart = session.get("cart", [])
    items = [p for p in products if p["id"] in cart]
    return render_template_string(cart_html, items=items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)