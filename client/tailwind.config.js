/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        beige: {
          DEFAULT: '#a1450b',
        },
        purple: {
          DEFAULT: '#b9b1cb',
        }
      },
      fontFamily: {
        sans: ['Georgia', 'system-ui', 'Avenir', 'Helvetica', 'Arial', 'sans-serif'],
      },
      backgroundImage: {
        'hero': "url('/bg2.jpg')",
      },
      minHeight: {
        'custom': 'calc(100vh - 8rem)', // Subtracting 3rem (48px)
      },
    },
  },
  plugins: [],
}