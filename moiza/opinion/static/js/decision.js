const preserveDecision = () => {
  let choice = document.querySelector('.selected');
  const result = AjaxCall('../decision-preserve/', {'choice': choice.id});
  if(result) {
    location.href = "../decision-reason/";
  }
}

const decisionSubmit = () => {
  let reason = document.querySelector('textarea').value;
  if (reason.trim().length > 0) {
    const result = AjaxCall('../decision-submit/', {'reason': reason});
    if(result) {
      location.href = "../decision-complete/";
    } else {
      alert("의견 선택에 실패하였습니다. 잠시후 다시 시도해주세요!")
    }
  }
}