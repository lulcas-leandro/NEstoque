from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
from app.models.stock import Product

class ProductForm(FlaskForm):
    sku = StringField('SKU (Código Único)', validators=[DataRequired()])
    name = StringField('Nome do Produto', validators=[DataRequired()])
    description =TextAreaField('Descrição')
    submit = SubmitField('Salvar')
    
    def __init__(self, original_sku=None, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.original_sku = original_sku
    
    def validate_sku(self, sku):
        if sku.data != self.original_sku:
            product = Product.query.filter_by(sku=sku.data).first()
            if product is not None:
                raise ValidationError('Este SKU já está em uso. Por favor, escolha outro.')
