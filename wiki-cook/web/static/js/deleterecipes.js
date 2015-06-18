
$(function() {
	
	$('#deleteRecipe').on('click', deleteRecipe);	

});


function deleteRecipe(recipename , flag) {
   
   var nameRecipe = recipename
   if (flag)
   {
       	 $.ajax({
			url:'/deleterecipes',
			type:'GET',
			dataType:'json',
			data:{nameRecipe:nameRecipe},
			success:function(data, status, xhr) {
				alert("susses to add simulator ");
				location.reload();
				return;
			},
			error:function(xhr, status, error) {
				alert("delete the recipe successfully!\n");
				location.reload();
				return;
			}
		});
	}

}