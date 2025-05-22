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
        slidesPerView: 6,
        spaceBetween: 20,
    });

    var swiper3 = new Swiper(".mySwiper3", {
        spaceBetween: 10,
        slidesPerView: 3,
        freeMode: true,
        watchSlidesProgress: true,
    });
    var swiper4 = new Swiper(".mySwiper4", {
        spaceBetween: 10,
        thumbs: {
            swiper: swiper3,
        },
    });

    var swiper5 = new Swiper(".mySwiper5", {
        effect: "cards",
        perSlideOffset:0,
        grabCursor: true,
        slideShadows: true,
        rotate:true
    });

    var swiper6 = new Swiper(".mySwiper6", {
        effect: "cards",
        perSlideOffset:0,
        grabCursor: true,
        slideShadows: true,
        rotate:true,
    });
});