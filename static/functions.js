  $('document').ready(function() {  
    // This code will allow for two things:
    // submitting a post request to one of two Django controllers (either adding a favorite or deleting one),
    // thus adding the favorite to the database, as well as 
    // toggling the favorites star
  
    //REPLACE WITH LINKS TO YOUR FAVORITES BUTTON IMAGES (src1 is not favorited, src2 is favorited)
    var imgSRC={'src1':'/static/images/star_off.png','src2':'/static/images/star_on.png'};
    //Controller for button of something that is not favorited
    $('.favorites').live('click', function() {
        var img=$(this);
        //Note: id represents the id of the element you want to be favorited
        //replace with the proper selector 
        id=$(this).parent().parent().attr('id');
        $.post('/favorite/', {"id": id}, function(data) {
          //functionality for an unsuccessful request can easily be added by checking for data.length = 0
          img.attr('src', imgSRC.src2);
          img.attr('class', 'favorites_on');
        });
    });

    $('.favorites_on').live('click', function() {
        var img=$(this);
        id=$(this).parent().parent().attr('id');
        console.log(id);
        $.post('/delete_favorite/', {"id": id}, function(data) {
          img.attr('src', imgSRC.src1);
          img.attr('class', 'favorites');
        });
	});
