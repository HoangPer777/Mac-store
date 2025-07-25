/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './static/css/component-css/*.{html,js,jsx,ts,tsx}'
      , "./node_modules/flowbite/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('flowbite/plugin')
  ],
}

