from flask import Flask, render_template, request, redirect, url_for
from src.shop import SweetShop
from src.sweet import Sweet

def create_app():
    app = Flask(__name__)
    shop = SweetShop()

    @app.route('/')
    def index():
        sweets = shop.view_sweets()
        return render_template('index.html', sweets=sweets)

    @app.route('/add', methods=['POST'])
    def add_sweet():
        try:
            sweet = Sweet(
                id=int(request.form['id']),
                name=request.form['name'],
                category=request.form['category'],
                price=float(request.form['price']),
                quantity=int(request.form['quantity'])
            )
            shop.add_sweet(sweet)
        except Exception as e:
            print(f"Error adding sweet: {e}")
        return redirect(url_for('index'))

    return app

# Run only when executed directly
if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
