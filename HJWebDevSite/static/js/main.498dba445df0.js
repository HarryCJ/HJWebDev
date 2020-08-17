    // left: -230%;

var halfPoint = 0;
var speed = 70000;

function continueAnimation(){
	var myDiv = $('.django_recent_media_wall_inner');
  myDiv.show( "slow" );
  myDiv.animate({
    left: halfPoint*-1,
  }, speed, "linear", function() {
    // Animation complete.
  });

  myDiv.queue(function() {
    var that = $( this );
    // that.addClass( "newcolor" );
    that.css('left', '0px');
  	continueAnimation();
    that.dequeue();
  });

 
  // myDiv.animate({
  //   left:"-=200"
  // }, 1500 );
  // myDiv.queue(function() {
  //   var that = $( this );
  //   that.removeClass( "newcolor" );
  //   that.dequeue();
  // });
  // myDiv.slideUp();
}

function stopAnimation(){
	var myDiv = $('.django_recent_media_wall_inner');
  myDiv.clearQueue();
  myDiv.stop();
}

$(function(){

	split = 6;
	windowWidth = $(window).width();
	if (windowWidth < 350){
		split = 2;
		speed = 10000
	} else if (windowWidth < 650){
		split = 4;
		speed = 40000
	}

	var tileWidth = $('.django_recent_media_wall').width()/split;
	halfPoint = $('.django_recent_media_wall').width()/2;
	// var val = parseInt($('.django_recent_media_wall_inner .django_instagram_media_wall_item img').width());
	// var newval = 5 * Math.round(val/5);

	$('.django_recent_media_wall_inner .django_instagram_media_wall_item img').css('width', tileWidth);
	$('.django_recent_media_wall_inner .django_instagram_media_wall_item img').css('height', tileWidth);

	// $('.django_recent_media_wall_inner').css('width', tileWidth*$('.django_instagram_media_wall_item').length);
	$('.django_recent_media_wall_inner').css('width', tileWidth*$('.django_instagram_media_wall_item').length);

	// $('.django_recent_media_wall').css('width', tileWidth*$('.django_instagram_media_wall_item').length);
	$('.django_recent_media_wall').css('padding-top', tileWidth);


    continueAnimation();

	$( ".django_instagram_media_wall_item a" ).hover(
  function() {
    // $( this ).addClass( "hover" );
    stopAnimation();
  }, function() {
    // $( this ).removeClass( "hover" );
    continueAnimation();
  }
);

	// var currentLeft = 0;

	// function tryScrollInstagram() {
	// 	console.log("tryScrollInstagram");
	//  // $j("#right_scroll img").click();
	//  	// var currentLeft = parseInt($('.django_recent_media_wall_inner').css('left'));
	//  	currentLeft = currentLeft - 0.01;
	// 	console.log(currentLeft);
	//  	$('.django_recent_media_wall_inner').css('left', currentLeft+'%')
	// }

	// window.setInterval(tryScrollInstagram, 10);

	// $('.django_recent_media_wall_inner').animate({
 //    left: "-229%",
 //  }, 50000, "linear", function() {
 //    // Animation complete.
 //  });
})