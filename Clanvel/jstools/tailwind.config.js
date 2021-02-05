module.exports = {
  future: {
      removeDeprecatedGapUtilities: true,
      purgeLayersByDefault: true,
  },
  purge: {
      enabled: false, //true for production build
      content: [
          '../**/templates/*.html',
          '../**/templates/**/*.html'
      ]
  },
  theme: {
      extend: {
        backgroundImage: theme => ({
            'hero-pattern': "url('static/img/rare-fest_t20_7lJolN.jpg')",
           })
      },
  variants: {},
  plugins: [],
    }
}