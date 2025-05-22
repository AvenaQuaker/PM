const loginForm = document.getElementById("loginForm");
const signUpBtn = document.getElementById("register");
const goLeft = document.getElementById("goLeft");


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

document.querySelector('form[action="/auth/login"]')?.addEventListener("submit", async function (e) {
  e.preventDefault();

  const form = e.target;
  const formData = new FormData(form);

  Swal.fire({
    title: "Iniciando sesión",
    text: "Por favor, espera...",
    allowOutsideClick: false,
    didOpen: () => {
      Swal.showLoading();
    }
  });

  setTimeout(async () => {
    try {
      const response = await fetch("/auth/login", {
        method: "POST",
        body: formData,
      });

      if (response.redirected) {
        window.location.href = response.url;
        return;
      }

      const data = await response.json();
      if (data.message) {
        Swal.fire("Error", data.message, "error");
      }
    } catch (err) {
      console.error("Error:", err);
      Swal.fire("Error", "Hubo un problema en el servidor.", "error");
    }
  }, 2000);
});


signUpBtn?.addEventListener("click", async () => {
  const inputs = document.querySelectorAll(".left input");
  const username = inputs[0].value.trim();
  const password = inputs[1].value.trim();
  const confirmPassword = inputs[2].value.trim();

  if (!username || !password || !confirmPassword) {
    return Swal.fire("Error", "Rellena todos los campos", "error");
  }

  if (password !== confirmPassword) {
    return Swal.fire("Error", "Las contraseñas no coinciden", "error");
  }

  const response = await fetch("/auth/register", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password })
  });

  const data = await response.json();

  if (response.ok) {
    Swal.fire("¡Registrado!", data.message, "success").then(() => {
      setTimeout(() => {
        goLeft.click();
      }, 2000);
    });
  } else {
    Swal.fire("Error", data.message, "error");
  }
});
