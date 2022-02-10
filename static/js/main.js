let menu = document.querySelector("#menu");
let burgerBtn = document.querySelector(".mobile-menu");
let menuOpen = document.querySelector("#open");


function openMenu() {

    if (menuOpen.children[0].classList.contains("fa-ellipsis-h")) {
        menuOpen.children[0].classList.remove("fa-ellipsis-h")
        menuOpen.children[0].classList.add("fa-ellipsis-v")
    } else {
        menuOpen.children[0].classList.remove("fa-ellipsis-v")
        menuOpen.children[0].classList.add("fa-ellipsis-h")
    }

    menu.classList.toggle("close");

}

function closeMenu() {
    let menuClose = document.querySelector(".close");
    menuClose.style.top = '0'
}

// MODAL
let modal = document.querySelector(".modal");

function openCloseModal() {
    modal.classList.toggle("active-modal")
}
