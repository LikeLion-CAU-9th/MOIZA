window.onload = () => {
  // Need to be refactor when the data is given
  let gage = document.querySelectorAll('.gage');
  percent = (3*160)/7; // Need Saciling!!
  gage[0].style.width = String(percent) + "%";
  percent = (1*160)/7; // Need Saciling!!
  gage[1].style.width = String(percent) + "%";
  percent = (1*160)/7; // Need Saciling!!
  gage[2].style.width = String(percent) + "%";
  percent = (2*160)/7; // Need Saciling!!
  gage[3].style.width = String(percent) + "%";

}

const bottomSheetSwitch = () => {
  const sheet = document.querySelectorAll('.bottom-sheet')[0];
  const container = document.querySelectorAll('.bottom-sheet-container')[0];
  let sheetHeight = sheet.style.height;
  if(sheetHeight === '18vh') {
    sheet.style.height = '40vh';
    container.style.height = '30vh';
    return 0;
  }
  sheet.style.height = '18vh';
  container.style.height = '8vh';
  return 0;
}

const bottomChoice = () => {

}