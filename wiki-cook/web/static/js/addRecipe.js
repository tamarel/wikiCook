console.log("addRecipe.js");

$(function() {
	$('#submitSimulator').on('click', submitStep);	//bind the guessSubmit function to the guess_submit event
	$('#inputStep').on('keyup', function(e) {		//submitting on enter also
		if(e.keyCode === 13) {
			submitStep();
		}
	});
});

function submitStep() {
	var nameRecipe = $('#inputNameRecipe').val(); 
	var ingredients = $('#inputIngredients').val(); 
	var type =  $('#inputType').val(); 
	var step =  $('#inputStep').val(); 
	
	if (nameRecipe.length == 0 || ingredients.length == 0 || step.length == 0 )
	{
		alert("must enter all the field\n");
		return;
	}
	
	alert("must enter all the field\n");
	
	 $.ajax({
		url:'/addRecipe',
		type:'GET',
		dataType:'json',
        data:{nameRecipe:nameRecipe, ingredients:ingredients, step:step, type:type },
		success:function(data, status, xhr) {
			alert("susses to add simulator ");
			location.reload();
			return;
		},
		error:function(xhr, status, error) {
            alert("the add simulator to the list failed!\n");
			document.getElementById("descriptionadd").value = "";
			return;
		}
	});
	
	
}