console.log("addrecipes.js");

$(function() {
	
	$('#submitSimulator').on('click', submitSimulator);	
	$('#submitStep').on('click', submitStep);	
	$('#inputStep').on('keyup', function(e) {	
		if(e.keyCode === 13) {
			submitSimulator();
		}
	});
});



var list_of_step = [];

function addStepToList() {


	var currnet_step =  $('#addstepToList').val();
	var need_timer =  $('#inputTime').val();
	
	
	
	var i;
	if (user_name == "")
	{
		swal("Missing User!", "please enter the user you want to add to the group", "info");
		return;
	}
	for (i=0; i<users.length; i++)
		if (user_name == users[i])
		{
			swal("User Exists!", "user is already exists in group", "info");
			return;
		}
	users.push(user_name);
	var dom = document.getElementById('users_list');
	i = users.length-1;
	dom.insertAdjacentHTML('beforeend','<td>'+ users[i] + '</td>'
		+'<td><img src="../static/images/deleteButton.png" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	$( "#selectUser" ).val("")


	var user_name = $('#drop_usersList').val();
	var user_permit = $('#userPermit').val();
	
	if (user_name == "")
	{
		swal("Missing User!", "please enter the user you want to add to the list", "info");
		return;
	}
	
	nameAndPermit = [];
	for(i=0;i<list.length;i++)
	{
		if(list[i][0]==user_name)
		{
			swal("User Exists!", user_name + " is already exists in list", "info");
			return;
		}
	}
	nameAndPermit.push(user_name);
	nameAndPermit.push(user_permit);
	list.push(nameAndPermit);
	var dom = document.getElementById('box');
	var i = list.length-1;
	dom.insertAdjacentHTML('beforeend','<td>'+ list[i][0] + '</td>' + '<td>' +list[i][1] + '</td>'
	+'<td><img src="../static/images/deleteButton.png" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	
	$( "#drop_usersList" ).val("");
	$( "#userPermit" ).val("Viewer");
	//$('#box').val($('#box').val()+user_name +"\t" +user_permit + "\n");
	
}
	
	
	
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
		pic_url = "http://www.designofsignage.com/application/symbol/building/image/600x600/no-photo.jpg"
	
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



