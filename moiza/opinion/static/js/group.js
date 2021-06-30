const spreadBoard = (style) => {
  style.width = "100%";
  style.maxWidth = "100%";
  style.left = "0";
  style.transform = "translate(0, -50%)";
}

const openBoard = () => {
  const container = document.querySelector('.container');
  const containerStyle = container.style;
  spreadBoard(containerStyle);
  let elem = document.querySelectorAll('.container *');
  let elem_dash = document.querySelectorAll('.dashBoard *');
  for(let i = 1; i < elem.length; i++) {
    target = true;
    for(let k = 0; k <elem_dash.length; k++) {
      if(elem[i] == elem_dash[k]){
        target = false;
      }
    }
    if(target) {
      elem[i].style.display = 'none';
    }
  }
  document.querySelector('.dashBoard').style.display = 'block';
}