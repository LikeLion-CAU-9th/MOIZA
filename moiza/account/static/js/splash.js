window.onload = () => {
  setTimeout(() => {
    document.querySelector('.splash-container').style.opacity = '0';
  }, 1600)
  setTimeout(()=> {
    document.querySelector('.splash-container').style.display = 'none';
  },3000)
}