const AjaxCall = (url, data, method="GET", async=false) => {
  let returnValue = false;
  $.ajax({
    url: url,
    type: method,
    async: async,
    data: data,
    success: function(data) {
        if(data === "True") {
          returnValue = true;
        }
    }
  })
  return returnValue;
}