/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./templates/**/*.html", "./**/templates/**/*.html"],
  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
      colors: {
        brand: {
          primary: "#1E40AF",
          secondary: "#38BDF8",
        },
        chinuch: "#7C3AED",
      },
    },
  },
  plugins: [],
};
