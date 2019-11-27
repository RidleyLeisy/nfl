$(document).ready(function(){
    $("#kitchen_color").change(function(){
      $("img[name=image-swap]").attr("src",$(this).val());
 
    });
 
 });