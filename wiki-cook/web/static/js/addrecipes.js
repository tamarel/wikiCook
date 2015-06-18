console.log("addrecipes.js");

$(function() {
	
	$('#submitSimulator').on('click', submitRcipeTRY);	
	$('#submitStep').on('click', addStepToList);	
	$('#inputStep').on('keyup', function(e) {	
		if(e.keyCode === 13) {
			submitSimulator();
		}
	});
});



var list_of_step = [];

function addStepToList() {


	var currnet_step =  $('#inputStep').val();
	var need_timer =  $('#inputTime').val();
	
	if (currnet_step == "")
	{
		swal("Missing User!", "please enter the step you want to add to the recipe", "info");
		return;
	}
	
	stepANDtimer = [];
	
	stepANDtimer.push(currnet_step);
	stepANDtimer.push(need_timer);
	list_of_step.push(stepANDtimer);
	
	var dom = document.getElementById('box');
	var i = list_of_step.length-1;
	if ( list_of_step[i][1] !=""){
	dom.insertAdjacentHTML('beforeend','<td>'+ list_of_step[i][0] + '</td>' + '<td>' +list_of_step[i][1] +'(min)' + '</td>'
	+'<td><img src="/static/img/deleteButton.jpg" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	}
	else {
	dom.insertAdjacentHTML('beforeend','<td>'+ list_of_step[i][0] + '</td>' + '<td>' +list_of_step[i][1] + '</td>'
	+'<td><img src="/static/img/deleteButton.jpg" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	}
	
	$( "#inputStep" ).val("");
	$( "#inputTime" ).val("");
	
	
}

function deleteFromList(index) {
	list_of_step.splice(index,1);
	var dom = document.getElementById('box');
	$("#box").empty();
	dom.insertAdjacentHTML('beforeend','<col width="300px" /><col width="130px" /><col width="30px" /><tr><td><h3>Step</h3></td><td><h3>timer</h3></td> </tr>');
	for (i = 0; i < list_of_step.length; ++i)
	{
		if ( list_of_step[i][1]!=""){
	dom.insertAdjacentHTML('beforeend','<td>'+ list_of_step[i][0] + '</td>' + '<td>' +list_of_step[i][1] +'(min)' + '</td>'
	+'<td><img src="/static/img/deleteButton.jpg" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	}
	else {
	dom.insertAdjacentHTML('beforeend','<td>'+ list_of_step[i][0] + '</td>' + '<td>' +list_of_step[i][1] + '</td>'
	+'<td><img src="/static/img/deleteButton.jpg" onclick=deleteFromList('+i+') valign="bottom"></td></p>')
	}
	}
}

function submitRcipeTRY() {
	var nameRecipe = $('#inputNameRecipe').val(); 
	var ingredients = $('#inputIngredients').val(); 
	var typeRecipe =  $('#inputType').val(); 
	
	var pic_url =  $('#inputpic_url').val();
	
	if (nameRecipe.length == 0 || ingredients.length == 0  )
	{
		alert("must enter all the field\n");
		return;
	}
	
	if (pic_url.length == 0)
		pic_url = "http://www.designofsignage.com/application/symbol/building/image/600x600/no-photo.jpg"
	
	list_of_step = JSON.stringify(list_of_step);
	$('#inputNameRecipe').val("");
	 $('#inputIngredients').val(""); 
	$.ajax({
		url:'/addrecipes',
		type:'GET',
		dataType:'json',
		data:{nameRecipe:nameRecipe, ingredients:ingredients, typeRecipe:typeRecipe , list_of_step:list_of_step , pic_url:pic_url},
		success:function(data, status, xhr) {
			alert("susses to add simulator ");
			location.reload();
			
		},
		error:function(xhr, status, error) {
		alert(" added the recipe successfully!\n");
		return;
		}
			
	});					
							
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



