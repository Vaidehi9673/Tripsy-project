function sliding() {
    $(".container-fluid").hide().fadeIn(2000);
    $(".navbar-brand").hide().show("slide", { direction: 'left' }, 1000);
    $(".info-desc").hide();
    $(".info-btn").click(function() {
        $(".info-desc").fadeToggle();
    });
    $(".message").innerTEXT = "";

    
}

var checkpwd = document.querySelector(".pwd")
var checkconfirmPwd = document.querySelector(".confirmPwd")
var checkCaptcha = document.querySelector(".showCaptchaCode")
var checkReCaptcha = document.querySelector(".Captcha")
var msg = document.querySelector(".message")
var emailMessage = document.querySelector(".emailMsg")
var pwdMessage = document.querySelector(".pwdMsg")
var captchaMessage = document.querySelector(".captchaMsg")




function createCaptcha(){

        var result           = '';
        var characters       = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
        var charactersLength = characters.length;
        for ( var i = 0; i < 6; i++ ) {
          result += characters.charAt(Math.floor(Math.random() * 
     charactersLength));
       }
    //    return result;
    checkCaptcha.value = result;
       checkCaptcha.innerHTML = result;
}


// ----------------------------------------------------------


function checkInputs(){

          
            
    if(checkpwd.value.length<8)
    {
         pwdMessage.innerHTML = "Password should not be less than 8 characters."
        return false
    }
    else if(checkpwd.value != checkconfirmPwd.value){
         pwdMessage.innerHTML = "Password and confirm Password do not match."
        return false
    }
    else if(checkCaptcha != checkReCaptcha){
     captchaMessage.innerHTML = "Captcha & Re-Captcha do not match";

    }
    else if (checkReCaptcha == "")
     {
         captchaMessage.innerHTML = "Re-Captcha must be filled";
         return false
     } 
     else if (validateCaptcha > 0 || recaptcha.length > 6) {
         captchaMessage.innerHTML = "Wrong captcha";
         return false
     } 
    else{
        return true
    }
  }