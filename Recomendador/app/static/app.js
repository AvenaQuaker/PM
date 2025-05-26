var swiper1, swiper2, swiper3, swiper4, swiper5, swiper6;


document.addEventListener("DOMContentLoaded", function () {
    btnImagen.classList.remove("animate-spin");

    swiper1 = new Swiper(".mySwiper1", {
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

    swiper2 = new Swiper('.mySwiper2', {
        scrollbar: {
            el: '.swiper-scrollbar',
            draggable: true,
        },
        slidesPerView: 6,
        spaceBetween: 20,
    });

    swiper3 = new Swiper(".mySwiper3", {
        spaceBetween: 10,
        slidesPerView: 3,
        freeMode: true,
        watchSlidesProgress: true,
    });
    swiper4 = new Swiper(".mySwiper4", {
        spaceBetween: 10,
        thumbs: {
            swiper: swiper3,
        },
    });

    swiper5 = new Swiper(".mySwiper5", {
        effect: "cards",
        perSlideOffset: 0,
        grabCursor: true,
        slideShadows: true,
        rotate: true
    });

    swiper6 = new Swiper(".mySwiper6", {
        effect: "cards",
        perSlideOffset: 0,
        grabCursor: true,
        slideShadows: true,
        rotate: true,
    });
});

let btnImagen = document.getElementById("imgCancion");
let btnPlay = document.getElementById("btnPlay")
let imgCancion = document.getElementById("imgCancion");
let gpCancion = document.getElementById("gpCancion");
let searchInput = document.getElementById("searchInput");
let user = document.getElementById("user");

btnPlay.addEventListener("click", () => {
    console.log("click");
    if (btnPlay.children[0].classList.contains("fa-play")) {
        btnImagen.classList.add("animate-spin");
        btnPlay.innerHTML = '<i class="fa fa-pause bg-cover bg-center bg-no-repeat rounded-full"></i>';
    } else {
        btnImagen.classList.remove("animate-spin");
        btnPlay.innerHTML = '<i class="fa fa-play bg-cover bg-center bg-no-repeat rounded-full"></i>';
    }
});

let searchSongs = document.getElementById("searchSongs");

searchInput.addEventListener('keydown', async (event) => {
    if (event.key === 'Enter') {
        const keyword = searchInput.value.trim();
        if (!keyword) return;

        console.log('Buscando:', keyword);
        try {
            const response = await fetch(`/songs/search/${keyword}`,);
            if (!response.ok) {
                searchSongs.innerHTML = `<div class="text-center font-fredoka mb-4">No se encontraron resultados para "${keyword}"</div>`;
            }

            const results = await response.json();
            renderSongs(results);
            console.log('Resultados:', results);

        } catch (err) {
            console.error('Error buscando:', err);
        }
    }
});

function renderSongs(songs) {
    searchSongs.innerHTML = "";

    songs.forEach(song => {
        const songDiv = document.createElement("div");
        songDiv.setAttribute("data-name", song.name);
        songDiv.setAttribute("onclick", "playSong(event)");
        songDiv.className = "border border-slate-300 flex flex-row justify-between items-center w-full h-fit mb-5 bg-[#1b074b6e] rounded-xl p-3";

        songDiv.innerHTML = `
        <div class="pointer-events-none flex flex-row justify-start items-center">
        <img class="pointer-events-none w-12 h-12 rounded-xl" src="${song.img}" alt="song">
        <div class="pointer-events-none flex flex-col justify-start items-start ml-3">
            <h1 class="pointer-events-none font-fredoka text-[1] text-lg">${song.name}</h1>
            <h3 class="pointer-events-none font-montserrat text-sm">${song.artist}</h3>
        </div>
        </div>
        <i class="pointer-events-none fa fa-play mx-2 h-5 not-md:text-center not-md:translate-y-0.5"></i>
    `;

        searchSongs.appendChild(songDiv);
    });
}

function playSong(e) {
    songName = e.target.getAttribute("data-name");
    userName = user.textContent;

    const Result = fetch(`/songs/name/${songName}`)
        .then(response => response.json())
        .then(data => {
            if (data) {
                gpCancion.children[0].style.backgroundImage = `url(${data.img})`;
                gpCancion.children[1].textContent = data.name;
                gpCancion.children[2].textContent = data.artist;
                btnImagen.classList.add("animate-spin");
                btnPlay.innerHTML = '<i class="fa fa-pause bg-cover bg-center bg-no-repeat rounded-full"></i>';
            } else {
                console.error("Error playing song:", data.message);
            }
        })
        .catch(error => {
            console.error("Error fetching play request:", error);
        });

    const userResponse = fetch('/user/addsong', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: userName, song_name: songName })
    }
    ).then(response => {
        if (response.ok) {
            console.log("Song added to last listened");
        } else {
            console.error("Error adding song to last listened");
        }
    }).catch(error => {
        console.error("Error adding song to last listened:", error);
    });

    //OBtener otra vez toda la informacion
    const refresh = fetch(`songs/refresh/${user.textContent}`).then(response => {
        if (response.ok) {
            return response.json();
        } else {
            throw new Error("Error refreshing songs");
        }
    }
    ).then(data => {
        if (data) {
            console.log("Songs refreshed:", data.songs);
            swiper1.destroy(true, true);
            swiper2.destroy(true, true);
            const wrapper1 = document.querySelector(".mySwiper1 .swiper-wrapper");
            const wrapper2 = document.querySelector(".mySwiper2 .swiper-wrapper");
            wrapper1.innerHTML = "";
            wrapper2.innerHTML = "";

            data.songs.forEach(song => {
                const slide = document.createElement("div");
                slide.className = "swiper-slide slider bg-cover bg-center bg-no-repeat";
                slide.style.backgroundImage = `url('${song.img}')`;
                slide.setAttribute("data-name", song.name);
                slide.setAttribute("onclick", "playSong(event)");

                slide.innerHTML = `
        <h1 class="pointer-events-none font-fredoka text-2xl">${song.name}</h1>
        <h3 class="pointer-events-none font-montserrat text-xl">${song.artist}</h3>
    `;
                wrapper1.appendChild(slide);
            });

            data.artists.forEach(artist => {
                const slide = document.createElement("div");
                slide.className = "swiper-ball swiper-slide";
                slide.setAttribute("data-name", artist.name);
                slide.setAttribute("onclick", "playSong(event)");

                slide.innerHTML = `
        <div class="pointer-events-none! bg-cover bg-center bg-no-repeat swiperbar border border-slate-300"
        style="background-image: url('${artist.img}')"></div>
        <h1 class="pointer-events-none! font-montserrat text-xl flex text-center">${artist.artist}</h1>
    `;
                wrapper2.appendChild(slide);
            });

            document.querySelector(".mySwiper4 .swiper-wrapper").innerHTML = "";
            document.querySelector("#thumbSlider").innerHTML = "";
            document.getElementById("FVA").innerText = "More of " + data.MRArtist;

            data.artistSongs.forEach(artist => {
                const mainSlide = document.createElement("div");
                mainSlide.className = "imgThumb swiper-slide";
                mainSlide.innerHTML = `
    <div onclick="playSong(event)" data-name="${artist.name}" class="py-10 flex justify-center items-end w-full h-full rounded-2xl bg-center bg-cover"
    style="background-image: url('${artist.img}')">
    <h3 class="pointer-events-none relative z-10 font-fredoka text-5xl text-shadow-lg">${artist.name}</h3>
    </div>
`;
                const thumbSlide = document.createElement("div");
                thumbSlide.className = "swiper-slide";
                thumbSlide.innerHTML = `
    <div class="imgSlide w-full h-full rounded-2xl bg-center bg-cover"
    style="background-image: url('${artist.img}')"></div>
`;

                document.querySelector(".mySwiper4 .swiper-wrapper").appendChild(mainSlide);
                document.querySelector("#thumbSlider").appendChild(thumbSlide);
            });

            swiper5.destroy(true, true);
            document.querySelector(".mySwiper5 .swiper-wrapper").innerHTML = "";
            document.getElementById("FVG").innerText = "For " + data.MRGenre + " Enyojers";
            data.genreSongs.forEach(song => {
                const slide = document.createElement("div");
                slide.className = "GESlider swiper-slide";
                slide.innerHTML = `
    <div onclick="playSong(event)" data-name="${song.name}" 
    class="w-[60%] h-full rounded-2xl bg-center bg-cover"
    style="background-image: url('${song.img}')"></div>
`;
                document.querySelector(".mySwiper5 .swiper-wrapper").appendChild(slide);
            });

            swiper6.destroy(true, true);
            document.querySelector(".mySwiper6 .swiper-wrapper").innerHTML = "";
            document.getElementById("FVE").innerText = "Feeling " + data.MREmotion;
            data.emotionSongs.forEach(song => {
                const slide = document.createElement("div");
                slide.className = "GESlider swiper-slide";
                slide.innerHTML = `
    <div onclick="playSong(event)" data-name="${song.name}" 
    class="w-[60%] h-full rounded-2xl bg-center bg-cover"
    style="background-image: url('${song.img}')"></div>
`;
                document.querySelector(".mySwiper6 .swiper-wrapper").appendChild(slide);
            })

            swiper1 = new Swiper(".mySwiper1", {
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

            swiper2 = new Swiper('.mySwiper2', {
                scrollbar: {
                    el: '.swiper-scrollbar',
                    draggable: true,
                },
                slidesPerView: 6,
                spaceBetween: 20,
            });

            swiper3 = new Swiper(".mySwiper3", {
                spaceBetween: 10,
                slidesPerView: 3,
                freeMode: true,
                watchSlidesProgress: true,
            });
            swiper4 = new Swiper(".mySwiper4", {
                spaceBetween: 10,
                thumbs: {
                    swiper: swiper3,
                },
            });
            swiper5 = new Swiper(".mySwiper5", {
                effect: "cards",
                perSlideOffset: 0,
                grabCursor: true,
                slideShadows: true,
                rotate: true
            });

            swiper6 = new Swiper(".mySwiper6", {
                effect: "cards",
                perSlideOffset: 0,
                grabCursor: true,
                slideShadows: true,
                rotate: true,
            });
        } else {
            console.error("Error refreshing songs:", data.message);
        }
    }).catch(error => {
        console.error("Error fetching refresh request:", error);
    });


}