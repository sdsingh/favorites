  $('document').ready(function() {  
    // This code will allow for two things:
    // submitting a post request to one of two Django controllers (either adding a favorite or deleting one),
    // thus adding the favorite to the database, as well as 
    // toggling the favorites star
  
    //REPLACE WITH LINKS TO YOUR FAVORITES BUTTON IMAGES (src1 is not favorited, src2 is favorited)
    var imgSRC={'src1':'/static/images/not_favorited.png','src2':'/static/images/favorited.png'};
    //Controller for button of something that is not favorited
      $('.favorites').live('click', function() {
        if(USER_STATUS == 'true'){
           //user is logged in, let's go!
           var img=$(this);
           //Note: id represents the id of the element you want to be favorited
           //replace with the proper selector 
           id=$(this).parent().parent().attr('id');
           console.log(id);
           $.post('/favorite/', {"id": id}, function(data) {
               img.attr('src', imgSRC.src2);
               img.attr('class', 'favorites_on');
           });
        } else {
           //not logged in, redirect to login page!
           window.location = '/login/';
        }
      });
      $('.favorites_on').live('click', function() {
        if(USER_STATUS == 'true'){
           //user is logged in, let's go!
           var img=$(this);
           id=$(this).parent().parent().attr('id');
           console.log(id);
           $.post('/favorite/', {"id": id}, function(data) {
               img.attr('src', imgSRC.src1);
               img.attr('class', 'favorites');
           });
        } else {
           //not logged in, redirect to login page!
           window.location = '/login/';
        }
      });
