// function to send request to server
function loadimages() {
  // creating a http request object
  var req = new XMLHttpRequest();
  // accessing the dom element
  var result = document.getElementById("result");
  // function which executes when the state of the http request is resolved
  req.onreadystatechange = function() {
    // checking if the request has been successfull
    if (this.readyState == 4 && this.status == 200) {
      // populatin the result to the dom.
      result.innerHTML += this.responseText;
    }
  };
  // opening the request
  req.open("POST", "/loadmore", true);
  // setting the header and content type of the request
  req.setRequestHeader(
    "content-type",
    "application/x-www-form-urlencoded;charset=UTF-8"
  );
  // sending request
  req.send();
}
// jquery function to hide the error dom element when page loads
$(document).ready(function() {
  $("#encryptMessage").focus(function() {
    $("#error").hide("slow");
  });
});

// function to handle submission of encryption.
function startEncryption() {
  //accessing dom element
  var image = document.getElementsByName("encryptImg");
  // getting the id of the image which is selected
  for (var i = 0, length = image.length; i < length; i++) {
    if (image[i].checked) {
      var imageValue = image[i].value;
      break;
    }
  }
  // accessing dom element
  var message = document.getElementById("encryptMessage").value;
  // stripping the message which is entered
  var message = message.trim();
  // validating the user input
  if (message !== "" && typeof imageValue !== "undefined") {
    // creating dom element and appending the dom tree.
    var cardbody = document.getElementById("cardbody");
    cardbody.innerHTML = "";
    var h4 = document.createElement("p");
    h4.style = "text-align:center";
    var t = document.createTextNode("Your Message : " + message);
    h4.appendChild(t);
    cardbody.appendChild(h4);
    var h4 = document.createElement("p");
    h4.style = "text-align:center";
    var t = document.createTextNode("Selected Image: ");
    var img = document.createElement("img");
    img.src = "https://source.unsplash.com/" + imageValue + "/250x250";
    img.className = "img-thumbnail";
    img.style = "max-widht:250px";
    h4.appendChild(t);
    h4.appendChild(img);
    cardbody.appendChild(h4);
    var button = document.createElement("button");
    var loading = document.createElement("i");
    loading.className = "fa fa-spinner fa-spin";
    var t = document.createTextNode(" Encryption in Process ...");
    button.append(loading);
    button.appendChild(t);
    button.disabled = true;
    button.className = "btn btn-light btn-block";
    cardbody.appendChild(button);

    // creating http request object
    var req = new XMLHttpRequest();
    // function which executes when the state of the http request is resolved
    req.onreadystatechange = function() {
      // checking if the request has been successfull
      if (this.readyState == 4 && this.status == 200) {
        // manupulating dom
        button.id = this.responseText;
        button.disabled = false;
        loading.className = "fa fa-download";
        t.textContent = " Download Image";
      }
    };
    // opening request with proper data
    req.open(
      "POST",
      "/encrypt?message=" + message + "&image=" + imageValue,
      true
    );
    // setting request header and data type
    req.setRequestHeader(
      "content-type",
      "application/x-www-form-urlencoded;charset=UTF-8"
    );
    req.send(); // sending request
    // function to handle button click
    button.onclick = function() {
      // creating dom element and appending the dom tree.
      cardbody.innerHTML = "";
      h2 = document.createElement("h2");
      text = document.createTextNode("Thank You !");
      h2.appendChild(text);
      h2.style = "text-align:center;";
      cardbody.appendChild(h2);
      p = document.createElement("p");
      text = document.createTextNode("Decrypt Your Message Here");
      p.appendChild(text);
      p.style = "text-align:center;";
      cardbody.appendChild(p);
      p = document.createElement("p");
      p.style = "text-align:center;";
      a = document.createElement("a");
      a.className = "btn btn-light";
      a.href = "/decrypt";
      text = document.createTextNode("Decryption");
      a.appendChild(text);
      p.appendChild(a);
      cardbody.appendChild(p);

      // creating http request
      var req = new XMLHttpRequest();
      // opening the request
      req.open("GET", "/downloadimage?id=" + button.id, true);
      // setting the response type
      req.responseType = "blob";
      req.send(); // sending the request
      // function to handle the response from the request
      req.onload = function(e) {
        // checking if the request is success
        if (this.status == 200) {
          // accessing the response
          var blob = new Blob([this.response], { type: "image/png" });
          // creating dom element and appending to dom tree
          var a = document.createElement("a");
          a.style = "display:none;";
          cardbody.appendChild(a);
          let url = window.URL.createObjectURL(blob);
          a.href = url;
          a.download = "Encrypted_Image" + new Date().getTime() + ".png";
          button.onclick = function() {};
          a.click();
          window.URL.revokeObjectURL(url);
        } else {
          console.log(e);
        }
      };
    };
  } else {
    document.getElementById("error").style.display = "block";
  }
}
