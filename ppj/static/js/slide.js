 $( document ).ready(function() {
 	$("#executar_ws").click(function(){

	
	   $.ajax({url: "/produto/"+$("#codigo_produto").val()
	   	, success: function(result){   	   
        	$("#resultado_ws").html(result);
       }});	  

 	});

});