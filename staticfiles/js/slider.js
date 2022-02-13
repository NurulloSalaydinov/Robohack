const slide = new Splide( '.splide', {
  type   : 'loop',
  perPage: 3,
  perMove: 1,
  easing:'cubic-bezier(0.25, 1, 0.5, 1)',
  wheel:true,
  autoplay:true,
  breakpoints: {
  640: {

    perPage: 2,
    perMove: 1,
  },
  1024: {
    perPage: 3,
    perMove: 1,
    padding:'1rem'
  },
  1200: {
    perPage: 4,
    perMove: 1,
    padding:'1rem'
  },
},
} ).mount();
