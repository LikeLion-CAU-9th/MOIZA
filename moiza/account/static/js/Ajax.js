let script = document.createElement('script');
script.src = 'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

const AjaxCall = (url, method="GET", async=false, data) => {
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