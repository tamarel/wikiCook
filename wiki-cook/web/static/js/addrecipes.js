console.log("addrecipes.js");

$(function() {
	
	$('#submitSimulator').on('click', submitSimulator);	
	$('#inputStep').on('keyup', function(e) {	
		if(e.keyCode === 13) {
			submitSimulator();
		}
	});
});



	
	
	
function submitSimulator() {
	var nameRecipe = $('#inputNameRecipe').val(); 
	var ingredients = $('#inputIngredients').val(); 
	var typeRecipe =  $('#inputType').val(); 
	var step =  $('#outputtext').val(); 
	var pic_url =  $('#inputpic_url').val();
	
	if (nameRecipe.length == 0 || ingredients.length == 0 || step.length == 0 )
	{
		alert("must enter all the field\n");
		return;
	}
	
	if (pic_url.length == 0)
		pic_url = "http://crossfit-marietta.com/wp-content/plugins/nertworks-all-in-one-social-share-tools/images/no_image.png"
	
	 $.ajax({
		url:'/addrecipes',
		type:'GET',
		dataType:'json',
        data:{nameRecipe:nameRecipe, ingredients:ingredients, typeRecipe:typeRecipe , step:step , pic_url:pic_url},
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



