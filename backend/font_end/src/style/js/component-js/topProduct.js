
const products = [
    { id: 1, name: 'Product 1', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 2, name: 'Product 2', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 3, name: 'Product 3', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 4, name: 'Product 4', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 5, name: 'Product 5', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 6, name: 'Product 6', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 7, name: 'Product 7', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
    { id: 8, name: 'Product 8', image: '../../../resource/Image/mba13-m3-midnight-gallery1-202402.jpeg' },
];

const productsPerPage = 4;
let currentPage = 1;

function displayProducts() {
    const start = (currentPage - 1) * productsPerPage;
    const end = start + productsPerPage;
    const paginatedProducts = products.slice(start, end);

    const productContainer = document.getElementById('productContainer');
    productContainer.innerHTML = '';

    paginatedProducts.forEach(product => {
        const productDiv = document.createElement('div');
        productDiv.className = 'product';
        productDiv.innerHTML = `
            <img src="${product.image}" alt="${product.name}">
            <h3>${product.name}</h3>
        `;
        productContainer.appendChild(productDiv);
    });

    setupPagination();
}

function setupPagination() {
    const paginationContainer = document.getElementById('pagination');
    paginationContainer.innerHTML = '';

    const pageCount = Math.ceil(products.length / productsPerPage);

    for (let i = 1; i <= pageCount; i++) {
        const button = document.createElement('button');
        button.innerText = i;
        button.className = currentPage === i ? 'active' : '';
        button.addEventListener('click', () => {
            currentPage = i;
            displayProducts();
        });
        paginationContainer.appendChild(button);
    }
}

displayProducts();
