const createSuggestion = () => {
  const title = document.querySelector("#content").value;
  const inputOptions = document.querySelectorAll('.options');
  let data = {};
  data['title'] = title;
  optionNum = 0
  for(let i = 0; i < inputOptions.length; i++) {
    if(inputOptions[i].value.trim().length > 0) {
      let keyName = "selection" + i;
      data[keyName] = inputOptions[i].value;
      optionNum += 1;
      console.log(optionNum)
    }
  }
  if (title.trim().length < 1 || optionNum == 0) {
    alert("논의 생성을 실패하였습니다.");
    console.log(optionNum)
    return false;
  }
  const result = AjaxCall('../create-suggestion/', data)
  if(result) {
    location.href="../topic-complete/"
    return true
  }
  alert("논의 생성을 실패하였습니다.");
  return false
}