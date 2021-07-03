const bottomSheetSwitch = () => {
  const sheet = document.querySelectorAll('.bottom-sheet')[0];
  const container = document.querySelectorAll('.bottom-sheet-container')[0];
  let classList = sheet.classList;
  for(let i = 0; i < classList.length; i++){
    if(classList[i] === "sheet-up"){
      removeClass('.bottom-sheet', 0, 'sheet-up');
      removeClass('.bottom-sheet-container', 0, 'container-up');
      return 0;
    }
  }
  
  sheet.className += " sheet-up";
  container.className += " container-up";
  return 1;
}

const bottomChoice = (num) => {
  const choice = document.querySelectorAll('.bottom-choice');
  const select = choice[num];
  for(let i = 0; i < choice.length; i++) {
    removeClass('.bottom-choice', i, 'selected');
    removeClass('.opinion-container', i, 'hide');
  }
  select.className += " selected"
  for(let i = 0; i < choice.length; i++) {
    if(i === num) {
      continue;
    }
    document.querySelectorAll('.opinion-container')[i].className += " hide";
  }
}

const removeClass = (JSpath, index, className) => {
  const target = document.querySelectorAll(JSpath)[index];
  console.log("remove" + index)
  const classList = target.className.split(' ');
  let newClassName = "";
  for(let i = 0; i < classList.length; i++) {
    if(classList[i] != className) {
      newClassName += (classList[i] + " ");
    }
  }
  newClassName = newClassName.trimEnd();
  target.className = newClassName;
}

const choiceClickHandler0 = () => {
  bottomChoice(0);
}

const choiceClickHandler1 = () => {
  bottomChoice(1);
}

const choiceClickHandler2 = () => {
  bottomChoice(2);
}

const choiceClickHandler3 = () => {
  bottomChoice(3);
}

const choiceClickHandler4 = () => {
  bottomChoice(4);
}


window.onload = () => {
  // Need to be refactor when the data is given
  let gage = document.querySelectorAll('.gage');
  percent = (1*160)/6; // Need Saciling!!
  gage[0].style.width = String(percent) + "%";
  percent = (2*160)/6; // Need Saciling!!
  gage[1].style.width = String(percent) + "%";
  percent = (1*160)/6; // Need Saciling!!
  gage[2].style.width = String(percent) + "%";
  percent = (1*160)/6; // Need Saciling!!
  gage[3].style.width = String(percent) + "%";
  percent = (1*160)/6; // Need Saciling!!
  gage[4].style.width = String(percent) + "%";

  let choice = document.querySelectorAll('.bottom-choice');
  choice[0].addEventListener("click", choiceClickHandler0, false);
  choice[1].addEventListener("click", choiceClickHandler1, false);
  choice[2].addEventListener("click", choiceClickHandler2, false);
  choice[3].addEventListener("click", choiceClickHandler3, false);
  choice[4].addEventListener("click", choiceClickHandler4, false);
}