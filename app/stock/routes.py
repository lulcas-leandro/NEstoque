from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.stock import stock_bp
from app.stock.forms import ProductForm, StockMovementForm
from app.models.stock import Product, StockMovement
from app.extensions import db

@stock_bp.route('/')
@stock_bp.route('/products')
@login_required
def list_products():
    products = Product.query.all()
    return render_template('stock/list_products.html', products=products, title='Estoque de Produtos')

@stock_bp.route('/product/new', methods=['GET', 'POST'])
@login_required
def create_product():
    form = ProductForm()
    if form.validate_on_submit():
        product = Product(sku=form.sku.data, name=form.name.data, description=form.description.data)
        db.session.add(product)
        db.session.commit()
        flash('Produto cadastrado com sucesso!')
        return redirect(url_for('stock.list_products'))
    return render_template('stock/create_edit_product.html', title='Novo Produto', form=form)

@stock_bp.route('/product/<int:product_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(original_sku=product.sku)
    if form.validate_on_submit():
        product.sku = form.sku.data
        product.name = form.name.data
        product.description = form.description.data
        db.session.commit()
        flash('Produto atualizado com sucesso!')
        return redirect(url_for('stock.list_products'))
    elif request.method == 'GET':
        form.sku.data = product.sku
        form.name.data = product.name
        form.description.data = product.description
    return render_template('stock/create_edit_product.html', title='Editar Produto', form=form)

@stock_bp.route('/product/<int:product_id>/delete', methods=['POST'])
@login_required
def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    flash('Produto deletado com sucesso!')
    return redirect(url_for('stock.list_products'))

@stock_bp.route('/product/<int:product_id>', methods=['GET', 'POST'])
@login_required
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    form = StockMovementForm()
    
    movements = product.movements.order_by(StockMovement.timestamp.desc()).all()
    return render_template('stock/product_detail.html', title=product.name, 
                           product=product, form=form, movements=movements)
    
@stock_bp.route('/product/<int:product_id>/move', methods=['POST'])
@login_required
def move_stock(product_id):
    product = Product.query.get_or_404(product_id)
    form = StockMovementForm()

    if form.validate_on_submit():
        quantity = form.quantity.data
        notes = form.notes.data
        movement_type = 'ENTRADA' if form.submit_in.data else 'SAIDA'

        if movement_type == 'SAIDA' and product.quantity < quantity:
            flash('Erro: Quantidade de saída excede o estoque disponível.')
            return redirect(url_for('stock.product_detail', product_id=product.id))
        if movement_type == 'ENTRADA':
            product.quantity += quantity
        else:
            product.quantity -= quantity

        movement = StockMovement(product_id=product.id, 
                                 user_id=current_user.id, 
                                 movement_type=movement_type, 
                                 quantity=quantity, 
                                 notes=notes)
        
        db.session.add(movement)
        db.session.add(product)
        db.session.commit()
        flash(f'{movement_type.capitalize()} registrada com sucesso!')

    return redirect(url_for('stock.product_detail', product_id=product.id))