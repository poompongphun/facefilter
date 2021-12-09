const navja = document.getElementById('navbarnaja')

// function if u scroll mouse down on website navbar will have shadow
function shadow(){
    navja.style.boxShadow = `0 10px 10px -2px rgba(163, 163, 163, ${window.scrollY > 0 ? 0.2 : 0})`;
}