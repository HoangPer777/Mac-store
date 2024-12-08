const birthDay = document.querySelector('#day');
const birthMonth = document.querySelector('#month');
const birthYear = document.querySelector('#year');


for (let i = 1; i <= 31; i++) {
    birthDay.innerHTML += `<option value=${i}">${i}</option>`;
}

for (let i = 1; i <= 12; i++) {
    birthMonth.innerHTML += `<option value=${i}">${i}</option>`;
}


for (let i = 1900; i <= 2024; i++) {
    birthYear.innerHTML += `<option value=${i}">${i}</option>`;
}