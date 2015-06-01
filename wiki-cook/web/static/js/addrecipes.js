console.log("addrecipes.js");

$(function() {
	$('#submitSimulator').on('click', submitStep);	
	$('#inputStep').on('keyup', function(e) {	
		if(e.keyCode === 13) {
			submitStep();
		}
	});
});

function submitStep() {
	var nameRecipe = $('#inputNameRecipe').val(); 
	var ingredients = $('#inputIngredients').val(); 
	var typeRecipe =  $('#inputType').val(); 
	var step =  $('#inputStep').val(); 
	
	if (nameRecipe.length == 0 || ingredients.length == 0 || step.length == 0 )
	{
		alert("must enter all the field\n");
		return;
	}
	
	 $.ajax({
		url:'/addrecipes',
		type:'GET',
		dataType:'json',
        data:{nameRecipe:nameRecipe, ingredients:ingredients, typeRecipe:typeRecipe , step:step },
		success:function(data, status, xhr) {
			alert("susses to add simulator ");
			location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("added the recipe successfully!\n");
			return;
		}
	});
	
	
}



