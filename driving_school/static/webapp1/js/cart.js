// find out the cart Item from localStorage
console.log('working');
if (localStorage.getItem('product_cart') == null) {
    var product_cart = {};
    console.log('none')
} else {
    product_cart = JSON.parse(localStorage.getItem('product_cart'));
    console.log(product_cart)
    updateCart(product_cart)
}

//update the cart
function updateCart(product_cart) {
    var sum = 0;
    for (var item in product_cart) {
        sum = sum + product_cart[item][0]

    }
    localStorage.setItem('product_cart', JSON.stringify(product_cart))
    document.getElementById('product_cart').innerHTML = sum;
    document.getElementById('product_cart2').innerHTML = sum;
    updatesideshow(product_cart);


}

//add sideshow to cart

updatesideshow(product_cart);

function updatesideshow(product_cart) {
    console.log('we are in updatesideshow');
    var popStr = "";
    popStr = popStr + "<div class='mx-2 my-2'>";

    var i = 1;
    var single_price_qty = 0;
    var total_price = 0;

    for (var item in product_cart) {
        // popStr = popStr + "<b>" + i + "</b>. ";
        popStr = popStr + `<div class="row"><div class="col-md-4"><div class="header-cart-item-img">
                    <img src="${product_cart[item][3]}" alt="IMG">
                </div></div><div class="col-md-8">`;

        single_price_qty = product_cart[item][0] * product_cart[item][2];
        // console.log('hi..'+single_price_qty)

        total_price = total_price + single_price_qty;

        popStr = popStr + product_cart[item][1] + '<br>Price: £' + product_cart[item][2] + "<br>" +
            "</div></div><br><br><br>";
        i = i + 1;

    }
    popStr = popStr + "</div><b>Total: £" + total_price +
        "</b><br><br><div class='row'><div class='col-md-6'><a href='{% url 'cart' %}'><button class='flex-c-m stext-100 cl0 size-106 bg3 bor2 hov-btn3 p-lr-15 trans-04 m-r-8 m-b-10' id='checkout'>View Cart</button></a></div><div class='col-md-6'><a href='/'><button class='flex-c-m stext-100 cl0 size-106 bg3 bor2 hov-btn3 p-lr-15 trans-04 m-b-10' id='clearCart' onclick='clearCart()'>Clear Cart</button></a></div></div> "

    console.log(popStr);
    document.getElementById('sideshow').innerHTML = popStr;


}

//clear cart
function clearCart(product_cart) {
    // product_cart = JSON.parse(localStorage.getItem('product_cart'));
    // for (var item in product_cart){
    // 	document.getElementById('div'+item).innerHTML = '<a id="' + item + '" class="tooltip-1 product_cart" data-toggle="tooltip" data-placement="left"><i class="ti-shopping-cart"></i><span>Add to cart</span></a>'
    // }
    localStorage.clear();
    product_cart = {};
    updateCart(product_cart);
}