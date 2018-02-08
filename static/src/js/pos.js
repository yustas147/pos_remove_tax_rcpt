odoo.define('pos_remove_tax_rcpt.mypos', function (require) {
    var models = require('point_of_sale.models');
    models.load_fields("product.product", ['displayed_price']);
});