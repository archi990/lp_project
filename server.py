from flask import Flask, render_template
app = Flask(__name__)

#home page
@app.route('/')
def home():
    return render_template('home.html')

#product list
@app.route('/products')
def product_list():
    return render_template('product_list.html')


#product detail
@app.route('/products/product_details')
def product_details():
    return render_template('product_details.html')

if __name__ == "__main__":
    app.run(debug=True)