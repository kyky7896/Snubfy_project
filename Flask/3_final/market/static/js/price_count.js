function add(value){

    let product_price = document.getElementById("product_price").innerText
    let value1=value
    let multiple=product_price*value1
    let tot_price = document.getElementById("tot_price")
    tot_price.innerText=multiple

}