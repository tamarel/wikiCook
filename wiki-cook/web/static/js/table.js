$(function() {
	$('#pressFeatured').on('click', pressFeatured);	
	
	});

function pressFeatured() {

	var nameRecipe = this.textContent; 
	 $.ajax({
		url:'/featured',
		type:'GET',
		dataType:'json',
        data:{nameRecipe:this.textContent },
		success:function(data, status, xhr) {
			alert("susses to add simulator ");
			location.reload();
			return;
		},
		error:function(data, status, error) {
            alert(data);
			window.location.replace("/featured");
			return;
		}
	});
	
	
}