/** @odoo-module */

import PublicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";


PublicWidget.registry.websiteCartDelete = PublicWidget.Widget.extend({
    selector:'.clear_cart_div',
    events: {
        'click .js_clear_cart': '_onClickClearCart',
    },
    _onClickClearCart:function(ev){
        jsonrpc('/shop/cart/clear').then(function(){
            location.reload(true);
        });
    },
});