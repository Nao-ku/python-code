const btncart = document.querySelector(".container-car-icon")

const containercartproducts = document.querySelector(".container-cart-products")


btncart.addEventListener("click",() =>{
    containercartproducts.classList.toggle("hiden-cart")
})


const cartInfo = document.querySelector(".cart-product")
const rowprodruct = document.querySelector(".row-product")


const productslist = document.querySelector(".container-items")


let allproducts =[];


const valortotal= document.querySelector(".total-pagar")

const countproducts = document.querySelector("#contador-productos")



productslist.addEventListener("click", e =>{

    if(e.target.classList.contains("btn-add-cart")){
       const product = e.target.parentElement
       
       const infoproduct ={
         quantity: 1,
         title: product.querySelector("h2").textContent,
         price: product.querySelector("p").textContent,
       };
        
       const exits = allproducts.some(product => product.title === infoproduct.title) 
       if(exits){
         const products = allproducts.map(product => {
            if(product.title = infoproduct.title){
                product.quantity++;
                return product
            }else{
                return product
            }
         })
         allproducts = [...products]
       }else{
          allproducts = [...allproducts, infoproduct]
       }
      
         showHTML();
    }
      
})

rowprodruct.addEventListener("click",(e) => {
    if(e.target.classList.contains("icon-close")){
        const product = e.target.parentElement
        const title = product.querySelector("p").textContent

        allproducts = allproducts.filter(
            product => product.title !== title
        );

        showHTML()

    }
})






const showHTML =() => {

    rowprodruct.innerHTML='';

    let total = 0;
    let totalofProducts = 0;

    
    allproducts.forEach(product => {
    const containerProduct = document.createElement("div")
    containerProduct.classList.add("cart-profuct")

    containerProduct.innerHTML = `
           <div class="info-cart-product">
                <span class="cantidad-producto-carrito">${product.quantity}</span>
                     <p class="titulo-carrito-producto">${product.title}</p>
                <span class="precio-carrito-producto">${product.price}</span>
            </div>
                 <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="icon-close">
                     <path stroke-linecap="round" stroke-linejoin="round" d="m9.75 9.75 4.5 4.5m0-4.5-4.5 4.5M21 12a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" />
                 </svg>   
        `

        rowprodruct.append(containerProduct)

        total = 
            total + parseInt(product.quantity * product.price.slice(1))
        totalofProducts = totalofProducts+ product.quantity;

    })

    valortotal.innerText = `$${total}`
    countproducts.innerText = totalofProducts; 

}




