const navBtn = document.querySelector('.nav-btn')
const signUp = document.querySelector('.sign__up')
const removeBtn = document.querySelector('.bx-x')

navBtn.onclick = ()=> {
    signUp.style.display = 'block'
    setTimeout(()=> {
        signUp.style.opacity = '1'
    }, 200)
}

removeBtn.onclick = ()=> {
    signUp.style.display = 'none'
}