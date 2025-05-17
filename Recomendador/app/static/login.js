document.addEventListener("DOMContentLoaded", function () {
    const goRight = document.getElementById("goRight");
    const goLeft = document.getElementById("goLeft");
    const slideBox = document.getElementById("slideBox");
    const topLayer = document.querySelector(".topLayer");
  
    goRight.addEventListener("click", function () {
      slideBox.style.transition = "margin-left 0.5s ease"; // Puedes ajustar la duración
      topLayer.style.transition = "margin-left 0.5s ease";
      slideBox.style.marginLeft = "0";
      topLayer.style.marginLeft = "100%";
    });
  
    goLeft.addEventListener("click", function () {
      slideBox.style.transition = "margin-left 0.5s ease";
      topLayer.style.transition = "margin-left 0.5s ease";
      slideBox.style.marginLeft = "50%";
      topLayer.style.marginLeft = "0";
    });
  });
  