const modal_on = (modalId) => {
  const ModalSelector = "#" + modalId;
  const ModalContainer = document.querySelector(ModalSelector);
  ModalContainer.style.display = "inline-block";
}

const modal_off = (modalID) => {
  const ModalSelector = "#" + modalID;
  const ModalContainer = document.querySelector(ModalSelector);
  ModalContainer.style.display = "none";
}