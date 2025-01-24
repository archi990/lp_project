from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Модель для товара
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    photo = db.Column(db.String(200))  # Ссылка на фото
    material = db.Column(db.String(100))
    dimensions = db.Column(db.String(100)) 
    availability = db.Column(db.Boolean, default=True)
    quantity = db.Column(db.Integer, default=0)
    production_time = db.Column(db.String(50))  
    author = db.Column(db.String(100))  
    price = db.Column(db.Float, nullable=False)

# Модель для пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, nullable=True)  # ID корзины
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(200), nullable=False)

# Модель для администратора
class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(200), nullable=False)

# Модель для заказа
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Связь с пользователем
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)  # Связь с продуктом
    product_quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    payment_method = db.Column(db.String(50))  
    delivery_method = db.Column(db.String(50)) 
    order_date = db.Column(db.DateTime, nullable=False) 
    update_date = db.Column(db.DateTime, nullable=True) 
    status = db.Column(db.String(50), nullable=False, default="создан")
