function upscroll(){
		$('body,html').animate({scrollTop: 0}, 40);
  	downscroll();
	}
function downscroll(){
		$('html,body').animate({scrollTop: document.body.scrollHeight*2},40000);
	}
window.onload = function () {
    console.log('Dokument geladen');
    upscroll();
    }
