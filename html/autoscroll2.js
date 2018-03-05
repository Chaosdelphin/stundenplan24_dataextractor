function upscroll(){
				$('body,html').animate({scrollTop: 0}, 40);
        downscroll();
	}
function downscroll(){
				$('html,body').animate({scrollTop: document.body.scrollHeight*8},320000);
	}

