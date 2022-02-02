(function(){
    const list = document.querySelector('.menu__enlaces');
    const menu = document.querySelector('.menu__hamburguesa');

    window.addEventListener('resize', ()=> {
        if(window.innerWidth > 800){

            if(list.classList.contains('menu__enlaces--mostrado'))
            list.classList.remove('menu__enlaces--mostrado');

        }
    })
    menu.addEventListener('click', ()=> list.classList.toggle('menu__enlaces--mostrado'));
})();

window.addEventListener("scroll", function(){
    var nav = document.querySelector("nav");
    var logo = document.querySelector('.menu__logo');
    // var logo = document.querySelector('.menu__enlace');
    
    //menú
    nav.classList.toggle("abajo", window.scrollY>0);
    //Logo
    logo.classList.toggle("abajo__logo--color", window.scrollY>0);
    //Enlaces
    // logo.classList.toggle("abajo__enlace--hover", window.scrollY>0);

})

//Carrusel
var splide = new Splide( '.splide', {
    type   : 'loop',
    perPage: 3,
    start  : 0,
    gap    : '7rem',
    focus  : 'center',
    arrows : false,
    padding: { left: '3rem', right: '3rem' },
    breakpoints: {
        1000:{
            perPage: 2,
        },
        600:{
            perPage: 1,
        },
    },
} );

splide.mount();
