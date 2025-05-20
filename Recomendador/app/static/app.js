document.addEventListener("DOMContentLoaded", function () {
    const swiper1 = new Swiper(".mySwiper1", {
        effect: 'coverflow',
        wrapperClass: "swiper-wrapper",
        grabCursor: true,
        centeredSlides: true,
        loop: true,
        speed: 600,
        lazy: true,
        preloadImages: false,
        slidesPerView: "auto",
        coverflowEffect: {
            rotate: 10,
            stretch: 50,
            depth: 200,
            modifier: 1,
            slideShadows: false,
        },
        on: {
            click(event) {
                swiper1.slideTo(this.clickedIndex);
            },
        },
        pagination: {
            el: ".swiper-pagination",
        },
    });

    const swiper2 = new Swiper('.mySwiper2', {
        scrollbar: {
            el: '.swiper-scrollbar',
            draggable: true,
        },
        slidesPerView: 3,
        spaceBetween: 20,
    });
});
