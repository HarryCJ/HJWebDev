 var currentPage = window.location.pathname;
// $( "#toggle" ).toggle( "slide" );
var siteURL = window.location.protocol+"//"+window.location.hostname+":8000";
var pageURL = siteURL + window.location.pathname;
var ajaxURL = pageURL + "ajax/"

var could_not_connect_message = '<div class="error-message message bad-connection-message">Could not connect.</div>';

function rotateLogo(x, y, x_direction, y_direction){

	// var x = -15;
	// var y = -15;
	$('.hj-logo').css("box-shadow", "rgb(180, 97, 58) "+x+"px  "+y+"px 0px 30px");
	
	console.log("start");
	console.log(x_direction);
	console.log(y_direction);
	if (y_direction == "up") {
		y= y+ 1;
		console.log(y);
		y = y * 1.1;
		y = y.toFixed(5)
		console.log(y);
		if (y > 15){

		return 0;	
		}
		if (y >= 15){
			y =15;
			y_direction = "down";	
		}
	} else if (y_direction == "down") {
		y -= 1;
		// y = y * -1.5;
		if (y <= -15){
			y_direction = "up";	
		}
	}
	console.log(x_direction);
	console.log(y_direction);
	console.log("finish");

	 if (x_direction == "right"){
		x = x + 1;
		// x = x * 1.5;
		if (x >= 15){
			x_direction = "left";
		}
	} else if (x_direction == "left") {
		x -= 1;
		// x = x * -1.5;
		if (x <= -15){
			x_direction = "right";	
		}
	}

	setTimeout(function(){
		// x+=1; y+=1;
		rotateLogo(x, y, x_direction, y_direction);
	}, 10);
}

// rotateLogo(15, 0, "right", "up");

function setGlobalClickHandler(){

	var handler = function(e){

		if (isLoading == true){
			e.preventDefault(); //Stops link from working
			return;
		}

		var target = e.target || e.srcElement;

		if ($(target).hasClass("ajax-link")) {

			var ajax_options = {"href": target.getAttribute('href'),
				"ajax-page-id": target.getAttribute('ajax-page-id'),
				"ajax-page-title": target.getAttribute('ajax-page-title')};

				//Check if page already exists
				if ($(".content-container-ajax.page-id-"+ajax_options["ajax-page-id"]).length){

					//Switch existing page
					$(".content-container-ajax").css("opacity", 0).hide();
					$(".content-container-ajax.page-id-"+ajax_options["ajax-page-id"]).show().css("opacity", 1);

					toggleActivePage(ajax_options, target);
					pushState(ajax_options);

					
				} else {

					//Load new page
					loadPage(ajax_options);

				}

				// window.scrollTo(0, 0);
			$("html, body").animate({ scrollTop: 0 }, "fast");
			e.preventDefault(); //Stops link from working
		}
	}

	for (var ls = document.links, numLinks = ls.length, i=0; i<numLinks; i++){
	    ls[i].onclick= handler;
	}
}

function pushState(ajax_options){

	window.history.pushState(ajax_options, ajax_options["ajax-page-title"], ajax_options["href"]);
	document.title = ajax_options["ajax-page-title"];
}

function toggleActivePage(ajax_options, target = null) {
	// console.log(ajax_options);

	//Change active nav menu item
	if (target != null && $(target).closest(".activatable").length > 0) {
		$(".activatable.active").removeClass("active");
		$(target).closest(".activatable").addClass("active");
	} else {
		if ($('.activatable [ajax-page-id="'+ajax_options["ajax-page-id"]+'"]').length){
			$(".activatable.active").removeClass("active");
			$('.activatable [ajax-page-id="'+ajax_options["ajax-page-id"]+'"]').closest(".activatable").addClass("active");
		}
	}
}

var isLoading = true;
function togglePageLoading(my_isLoading){
	isLoading = my_isLoading;

	if (isLoading == true){
		setTimeout(function(){
			if (isLoading == true){
				$('.loading-icon-container').css("opacity", 1);
			}
		}, 500);
	} else {
		$('.loading-icon-container').css("opacity", 0);
	}
}

function setUpInitialPage() {
	togglePageLoading(false);
	// var newHeight = $('.content-container .content-container-ajax').height();
	// $('.content-container .content-container-ajax').css("height", "0px");
	$('.content-container .content-container-ajax').animate(
		{opacity: 1, }, { queue: false, duration: 200 })
	// .animate({height: newHeight, }, { queue: false, duration: 250 });
	setTimeout(function(){
		$('.footer-container').show();
		// $("html").css("overflow-y", "visible");
	}, 250);
}

function loadPage(ajax_options, initial = false) {

	var loadURL = siteURL + ajax_options["href"] + "ajax/"
	togglePageLoading(true);

	var results = $('<div>').load(loadURL, function( response, status, xhr ) {
		if(status == "success"){

			if (initial == true){// && window.location.pathname == "/"){
				$('.content-container-ajax').append($(this).children().html());

				$(this).remove();

				if(document.readyState === 'ready' || document.readyState === 'complete') {

					setUpInitialPage();

				} else {
					$(window).bind("load", function() {

						setUpInitialPage();

					});
				}

				// $(window).bind("load", function() {

				// 	togglePageLoading(false);
				// 	var newHeight = $('.content-container .content-container-ajax').height();
				// 	$('.content-container .content-container-ajax').css("height", "0px");
				// 	$('.content-container .content-container-ajax').animate(
				// 		{opacity: 1, }, { queue: false, duration: 200 })
				// 	.animate({height: newHeight, }, { queue: false, duration: 250 });
				// 	setTimeout(function(){
				// 		$('.footer-container').show();
				// 		$("html").css("overflow-y", "scroll");
				// 	}, 250);

				// });
			} else {
				togglePageLoading(false);
				$(".content-container-ajax").css("opacity", 0).hide();
				$('.content-container').append($(this).html());

				$(this).remove();

        				$(".content-container-ajax.page-id-"+ajax_options["ajax-page-id"]).show().css("opacity", 1);
			}

        			$('.messages-container').slideUp();
        			toggleActivePage(ajax_options);
        			pushState(ajax_options);
			setGlobalClickHandler();

		} else {

			togglePageLoading(false);
			addMessage(could_not_connect_message);
			clearMessagesSoon();
		}


	})
}

function addMessage(message){

	$('.messages-container').append(message);
	if ($('.messages-container').is(":hidden")){
		$('.messages-container').slideDown( "fast", function() {});
	}
}

var clearMessagesSoonID = 0;
function clearMessagesSoon(){
	clearMessagesSoonID = clearMessagesSoonID + 1;
	var my_clearMessagesSoonID = clearMessagesSoonID;

	setTimeout(function(){
		if (my_clearMessagesSoonID == clearMessagesSoonID){
			$('.messages-container').slideUp( "fast", function() {
				if ($('.messages-container').is(":hidden")){
					$('.messages-container').empty();
				}
			});
		}
	}, 3000);
}


window.onpopstate = function(e) {
	// console.log(e.state);
	var ajax_options = e.state;
	$(".content-container-ajax").hide().css("opacity", 0);
	$(".content-container-ajax.page-id-"+ajax_options["ajax-page-id"]).show().css("opacity", 1);
	toggleActivePage(ajax_options);
};

$(function(){


	setGlobalClickHandler();

            // alert(pageURL);
    	var ajax_options = {"href": window.location.pathname,
    		"ajax-page-id": $('.content-container-ajax')[0].getAttribute('ajax-page-id'),
    		"ajax-page-title": $('.content-container-ajax')[0].getAttribute('ajax-page-title')};
	loadPage(ajax_options, true);
	// var results = $('<div>').load(ajaxURL, function( response, status, xhr ) {

	// 	if(status == "success"){
	// 		// $(this).find('ajax-container')
	// 		$('.content-container').append($(this).html());
	// 		$(this).remove();
	// 		var newHeight = $('.content-container .content-container-ajax').height();
	// 		 $('.content-container .content-container-ajax').css("height", "0px");
	// 		$('.content-container .content-container-ajax').animate({
	// 		    opacity: 1, height: newHeight,
	// 		  }, 250, "linear", function() {
	// 		    // Animation complete.
	// 		  });;
	// 	}

	// })

});
	// var results = $('<div>').load(url, function( response, status, xhr ) {

	// 	if(status == "success"){
	// 		loadingNewPage[type] = false;
	// 		page[type] = page[type] + 1;
	// 		if (cID == loadingID[type]){
	// 			$(this).insertBefore( '.'+type+' .load-more-button-container' );
	// 		}
	// 	}
	// 	$('.'+type+' .load-more-button').toggleClass('load-more-button-loading');
	// 	$('.'+type+' .load-more-button > .pagination-nav').hide();
	// 	$('.'+type+' .load-more-button > span').show();

	// 	if ($(this).find('.ajax-end-of-results').length > 0){
	// 		$('.'+type+' .load-more-button').hide();
	// 	} else {
	// 		$('.'+type+' .load-more-button').show();
	// 	}

	// 	if (appendList[type] == true) {
	// 		$('.'+type+' .ajax-content:first').append($(this).children().html());
	// 		$(this).remove();
	// 	}

	// })


//     // left: -230%;

// var halfPoint = 0;
// var speed = 70000;

// function continueAnimation(){
// 	var myDiv = $('.django_recent_media_wall_inner');
//   myDiv.show( "slow" );
//   myDiv.animate({
//     left: halfPoint*-1,
//   }, speed, "linear", function() {
//     // Animation complete.
//   });

//   myDiv.queue(function() {
//     var that = $( this );
//     // that.addClass( "newcolor" );
//     that.css('left', '0px');
//   	continueAnimation();
//     that.dequeue();
//   });

 
//   // myDiv.animate({
//   //   left:"-=200"
//   // }, 1500 );
//   // myDiv.queue(function() {
//   //   var that = $( this );
//   //   that.removeClass( "newcolor" );
//   //   that.dequeue();
//   // });
//   // myDiv.slideUp();
// }

// function stopAnimation(){
// 	var myDiv = $('.django_recent_media_wall_inner');
//   myDiv.clearQueue();
//   myDiv.stop();
// }

// $(function(){

// 	split = 6;
// 	windowWidth = $(window).width();
// 	if (windowWidth < 350){
// 		split = 2;
// 		speed = 10000
// 	} else if (windowWidth < 650){
// 		split = 4;
// 		speed = 40000
// 	}

// 	var tileWidth = $('.django_recent_media_wall').width()/split;
// 	halfPoint = $('.django_recent_media_wall').width()/2;
// 	// var val = parseInt($('.django_recent_media_wall_inner .django_instagram_media_wall_item img').width());
// 	// var newval = 5 * Math.round(val/5);

// 	$('.django_recent_media_wall_inner .django_instagram_media_wall_item img').css('width', tileWidth);
// 	$('.django_recent_media_wall_inner .django_instagram_media_wall_item img').css('height', tileWidth);

// 	// $('.django_recent_media_wall_inner').css('width', tileWidth*$('.django_instagram_media_wall_item').length);
// 	$('.django_recent_media_wall_inner').css('width', tileWidth*$('.django_instagram_media_wall_item').length);

// 	// $('.django_recent_media_wall').css('width', tileWidth*$('.django_instagram_media_wall_item').length);
// 	$('.django_recent_media_wall').css('padding-top', tileWidth);


//     continueAnimation();

// 	$( ".django_instagram_media_wall_item a" ).hover(
//   function() {
//     // $( this ).addClass( "hover" );
//     stopAnimation();
//   }, function() {
//     // $( this ).removeClass( "hover" );
//     continueAnimation();
//   }
// );

// 	// var currentLeft = 0;

// 	// function tryScrollInstagram() {
// 	// 	console.log("tryScrollInstagram");
// 	//  // $j("#right_scroll img").click();
// 	//  	// var currentLeft = parseInt($('.django_recent_media_wall_inner').css('left'));
// 	//  	currentLeft = currentLeft - 0.01;
// 	// 	console.log(currentLeft);
// 	//  	$('.django_recent_media_wall_inner').css('left', currentLeft+'%')
// 	// }

// 	// window.setInterval(tryScrollInstagram, 10);

// 	// $('.django_recent_media_wall_inner').animate({
//  //    left: "-229%",
//  //  }, 50000, "linear", function() {
//  //    // Animation complete.
//  //  });
// })