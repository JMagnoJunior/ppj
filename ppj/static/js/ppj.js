var app = angular.module('ppj', []);

app.config(['$interpolateProvider', function($interpolateProvider) {
  $interpolateProvider.startSymbol('{[');
  $interpolateProvider.endSymbol(']}');
}]);

app.controller('clienteCtrl',  function($scope) {  
    
    
});

// ------------------------ JQUERY ------------------
 $( document ).ready(function() {

	$( "#procurar" ).click(function() {
		
	   $.ajax({url: "/clientes"
	   	+"?nome="+$("#nome_cliente").val()
	   	+"&data_nascimento="+$("#data_nascimento_cliente").val()
	   	+"&sexo="+$("#sexo_cliente").val()
	   	+"&estado_civil="+$("#estado_civil_cliente").val()
	   	, success: function(result){   	   
        	$("#result").html(result);
       }});	  
	});  

	$( "#incluir" ).click(function() {
		$(location).attr('href','incluir/cliente');	  
	});   

	$( "#limpar" ).click(function() {    		
		$("#nome_cliente").val("")
		$("#data_nascimento_cliente").val("")
		$("#sexo_cliente").val("")
		$("#estado_civil_cliente").val("")
	});

   $("#add_dependente").click(function(){

	   $.ajax({url: "/add_dependente"
	   	, success: function(result){  
        	$("#dependentes").append(result+"<br />");
       }});	

   });

   $("#gravar").click(function(){

	   	dependentes  = []

	   	$(".dependente").each(function() {  
	   		dependente = {nome:$(this).find(".nome_dependente").val(), sexo:$(this).find(".sexo_dependente").val() }
	    	dependentes.push(dependente);
		});
		 

		$.ajax({
		   	type:'POST',
		   	url: "/inclui/cliente",
		   	contentType: 'application/json; charset=utf-8',
		   	data: JSON.stringify({ nome: $("#nome_cliente").val(), data_nascimento: $("#data_nascimento_cliente").val(),sexo:$("#sexo_cliente").val(),estado_civil:$("#estado_civil_cliente").val(),dependentes:dependentes }),
		   	success: function(result){  
		   		$("#nome_cliente").val("")
				$("#data_nascimento_cliente").val("")
				$("#sexo_cliente").val("")
				$("#estado_civil_cliente").val("")
				$(".dependente").each(function() {  
		   			$(this).find(".nome_dependente").val("");
		   			$(this).find(".sexo_dependente").val("")
				});
		 
	        	$("#resultado").html(result)
	       },
		   error: function (xhr, ajaxOptions, thrownError) {		   		
        		$("#resultado").html("<span class='erro'>Nao foi possivel incluir o registro</span>")	
      	   },

	   });

    });


	$( "#procurar_dependentes" ).click(function() {
	   $.ajax({url: "/dependentes"
	   	+"?nome="+$(".nome_dependente").val()
	   	+"&sexo="+$(".sexo_dependente").val()

	   	, success: function(result){   	   
        	$("#result").html(result);
       }});	  
	});  

});
